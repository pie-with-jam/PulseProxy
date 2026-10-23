import os
import urllib.parse
import json
import re
import base64
import threading
import concurrent.futures
from src.config import (
    URLS,
    LOCAL_PATHS,
    GITHUBMIRROR_DIR,
    SNI_DOMAINS_PATH,
    EXTRA_URLS_FOR_SPECIAL,
    EXTRA_URL_TIMEOUT,
    EXTRA_URL_MAX_ATTEMPTS,
    OWN_CONFIGS,
    SOURCE_COUNT,
    SPECIAL_FILE_NAME,
    HEALTHCHECK_ENABLED,
    HEALTHCHECK_MODE,
    HEALTHCHECK_TIMEOUT,
    HEALTHCHECK_WORKERS,
    PROXY_GET_TIMEOUT,
    PROXY_GET_WORKERS,
    CHINA_FILE_INDEX,
    CHINA_FILE_NAME,
    IRAN_FILE_INDEX,
    IRAN_FILE_NAME,
    CN_CIDR_PATH,
    CN_EXEMPT_CIDR_PATHS,
    IR_CIDR_PATH,
    COUNTRY_PROBE_LIMIT,
)
from src.logger import log
from src.network import fetch_data, NotModified, _format_fetch_error
from src.parser import filter_insecure_configs
from src.cidr import (
    refresh_cidr_whitelist,
    host_in_whitelist,
    parse_cidr_lines,
    build_network_index,
    host_in_index,
)
from src.healthcheck import extract_endpoint, probe, ProbeResult, _is_ip as _is_ip_literal
from src.validator import validate_configs

# -------------------- ЛОКАЛЬНЫЕ ФАЙЛЫ --------------------

_ETAGS_PATH = os.path.join(GITHUBMIRROR_DIR, ".etags.json")
_etags_lock = threading.Lock()


def _load_etags() -> dict:
    try:
        with open(_ETAGS_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _save_etag(url: str, etag: str | None):
    if not etag:
        return
    with _etags_lock:
        etags = _load_etags()
        if etags.get(url) == etag:
            return
        etags[url] = etag
        try:
            os.makedirs(os.path.dirname(_ETAGS_PATH), exist_ok=True)
            tmp = _ETAGS_PATH + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(etags, f, ensure_ascii=False, indent=0)
            os.replace(tmp, _ETAGS_PATH)
        except Exception:
            pass

def save_to_local_file(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    config_count = len([line for line in content.splitlines() if line.strip()])
    log(f"📁 Данные сохранены локально в {os.path.basename(path)} с {config_count} конфигами")


def extract_source_name(url: str) -> str:
    """Извлекает понятное имя источника из URL."""
    try:
        parts = urllib.parse.urlparse(url).path.split("/")
        if len(parts) > 2:
            return f"{parts[1]}/{parts[2]}"
        return urllib.parse.urlparse(url).netloc
    except Exception:
        return "Источник"


def download_and_save(idx: int) -> tuple[str, int] | None:
    """Скачивает файл (с If-None-Match по ETag), фильтрует и сохраняет локально.
    Возвращает (local_path, file_index) если файл изменился, иначе None."""
    url = URLS[idx]
    local_path = LOCAL_PATHS[idx]
    file_index = idx + 1
    try:
        cached_etag = _load_etags().get(url)
        try:
            result = fetch_data(url, etag=cached_etag, return_etag=True)
        except NotModified:
            config_count = 0
            try:
                with open(local_path, "r", encoding="utf-8") as f:
                    config_count = len([line for line in f if line.strip()])
            except Exception:
                pass
            log(f"🔄 304: {file_index}.txt не изменился ({config_count} конфигов).")
            return None

        data, new_etag = result
        _save_etag(url, new_etag)
        data, _ = filter_insecure_configs(local_path, data)

        if os.path.exists(local_path):
            try:
                with open(local_path, "r", encoding="utf-8") as f:
                    if f.read() == data:
                        config_count = len([line for line in data.splitlines() if line.strip()])
                        log(f"🔄 Изменений для {file_index}.txt нет ({config_count} конфигов).")
                        return None
            except Exception:
                pass

        save_to_local_file(local_path, data)
        return local_path, file_index

    except Exception as e:
        short_msg = str(e)
        if len(short_msg) > 200:
            short_msg = short_msg[:200] + "…"
        log(f"⚠️ Ошибка при скачивании {file_index}.txt ({url}): {short_msg}")
        return None

# -------------------- СПЕЦИАЛЬНЫЙ ФАЙЛ (БЕЛЫЕ СПИСКИ) --------------------

def _load_sni_domains() -> set[str] | None:
    """Загружает белый список SNI-доменов (sni_domains.json) как множество."""
    try:
        with open(SNI_DOMAINS_PATH, "r", encoding="utf-8") as f:
            sni_domains = json.load(f)
        return {str(d).strip().lower() for d in sni_domains if str(d).strip()}
    except Exception as e:
        log(f"❌ Ошибка загрузки {SNI_DOMAINS_PATH}: {e}")
        return None


def _sni_in_whitelist(sni: str | None, domains: set[str]) -> bool:
    """SNI в белом списке: точное совпадение или поддомен белого домена.
    Проверяется РЕАЛЬНЫЙ SNI из конфига, а не вся строка."""
    if not sni or not domains:
        return False
    host = sni.strip().lower().rstrip(".")
    if not host:
        return False
    if host in domains:
        return True
    # поддомен: id.vk.com → vk.com, xxx.userapi.com → userapi.com
    parts = host.split(".")
    for i in range(1, len(parts)):
        if ".".join(parts[i:]) in domains:
            return True
    return False


def _collect_source_lines() -> list[str]:
    """Читает готовые файлы 1..N (параллельно)."""
    lines: list[str] = []
    max_workers = min(16, (os.cpu_count() or 1) + 4)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        for result in concurrent.futures.as_completed(
            [executor.submit(_read_source_file, i) for i in range(1, SOURCE_COUNT + 1)]
        ):
            lines.extend(result.result())
    return lines


def _read_source_file(file_idx: int) -> list[str]:
    local_path = os.path.join(GITHUBMIRROR_DIR, f"{file_idx}.txt")
    if not os.path.exists(local_path):
        return []
    try:
        with open(local_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except Exception:
        return []


def _fetch_extra_configs(url: str) -> tuple[list[str], int]:
    """Скачивает доп. источник для спецфайла. Возвращает (конфиги, сколько отсеяно небезопасных)."""
    count_removed = 0
    configs: list[str] = []
    try:
        data = fetch_data(
            url,
            timeout=EXTRA_URL_TIMEOUT,
            max_attempts=EXTRA_URL_MAX_ATTEMPTS,
            allow_http_downgrade=False,
        )
        data, count_removed = filter_insecure_configs(
            os.path.join(GITHUBMIRROR_DIR, SPECIAL_FILE_NAME), data, log_enabled=False
        )
        configs = [line.strip() for line in data.splitlines() if line.strip()]
    except Exception as e:
        log(f"⚠️ Ошибка при загрузке {SPECIAL_FILE_NAME} ({url}): {_format_fetch_error(e)}")
    return configs, count_removed


def create_filtered_configs() -> str:
    """Создаёт спецфайл: конфиги, прошедшие белые списки (SNI/CIDR) и healthcheck."""
    special_path = os.path.join(GITHUBMIRROR_DIR, SPECIAL_FILE_NAME)

    sni_domains = _load_sni_domains()
    if sni_domains is None:
        return special_path

    cidr_networks = refresh_cidr_whitelist()

    # ---- 1. Сбор кандидатов ----
    all_lines = _collect_source_lines()

    total_insecure_filtered = 0
    max_extra_workers = max(1, min(8, len(EXTRA_URLS_FOR_SPECIAL)))
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_extra_workers) as executor:
        for future in concurrent.futures.as_completed(
            [executor.submit(_fetch_extra_configs, u) for u in EXTRA_URLS_FOR_SPECIAL]
        ):
            configs, count_removed = future.result()
            all_lines.extend(configs)
            total_insecure_filtered += count_removed

    if total_insecure_filtered > 0:
        log(f"ℹ️ Отфильтровано {total_insecure_filtered} небезопасных конфигов для {SPECIAL_FILE_NAME}")

    # Свои конфиги из storage.json — без ограничений белого списка.
    own_lines = [str(c).strip() for c in OWN_CONFIGS if str(c).strip()]

    # ---- 2. Дедупликация (свои конфиги приоритетнее) ----
    seen_lines: set[str] = set()
    seen_hostport: set[str] = set()
    candidates: list[str] = []
    own_set: set[str] = set()

    for cfg in all_lines:
        if not cfg or cfg in seen_lines:
            continue
        seen_lines.add(cfg)
        hp = _host_port_key(cfg)
        if hp and hp in seen_hostport:
            continue
        if hp:
            seen_hostport.add(hp)
        candidates.append(cfg)

    for cfg in own_lines:
        if cfg in own_set:
            continue
        own_set.add(cfg)
        if cfg not in seen_lines:
            seen_lines.add(cfg)
            candidates.append(cfg)

    if not candidates:
        log(f"⚠️ Нет кандидатов для {SPECIAL_FILE_NAME}")
        save_to_local_file(special_path, "")
        return special_path

    # ---- 2.5 Валидация структуры (битые URI ломают проверку в V2rayNG) ----
    total_amp = sum(1 for c in candidates if "&amp;" in c)
    if total_amp:
        candidates = [c.replace("&amp;", "&") if "&amp;" in c else c for c in candidates]
        log(f"🔧 Починено HTML-экранирование &amp; → &: {total_amp} конфигов")
    candidates, invalid_reasons = validate_configs(candidates)
    if invalid_reasons:
        dropped_invalid = sum(invalid_reasons.values())
        log(f"🗑️ Отсеяно битых конфигов: {dropped_invalid}")
        for reason, count in sorted(invalid_reasons.items(), key=lambda x: -x[1]):
            log(f"   ├─ {reason}: {count}")

    # ---- 3. Белый список (реальный SNI / CIDR IP) до healthcheck ----
    def _whitelisted_static(line: str) -> bool:
        ep = extract_endpoint(line)
        if not ep:
            return False
        # Реальный SNI (или host, если SNI не задан) — белый домен
        effective_sni = ep.sni or (ep.host if not _is_ip_literal(ep.host) else None)
        if effective_sni and _sni_in_whitelist(effective_sni, sni_domains):
            return True
        # IP-хост в русских мобильных подсетях (CIDR)
        return bool(host_in_whitelist(ep.host, cidr_networks))

    dropped_not_whitelisted = 0
    to_probe: list[str] = []
    for line in candidates:
        if line in own_set or _whitelisted_static(line):
            to_probe.append(line)
        else:
            dropped_not_whitelisted += 1

    log(
        f"🔎 Белый список ({SPECIAL_FILE_NAME}): {len(to_probe)} кандидатов "
        f"из {len(candidates)} (вне белого списка: {dropped_not_whitelisted})"
    )

    # ---- 4. Healthcheck только кандидатов из белого списка ----
    dropped_dead = 0
    drop_reasons: dict[str, int] = {}
    unique_configs: list[str] = []

    def _run_stage(
        lines: list[str],
        check,
        workers: int,
        stage_label: str,
    ) -> list[str]:
        """Прогоняет check по lines; возвращает живых. Мёртвые копятся в drop_reasons."""
        nonlocal dropped_dead
        alive: list[str] = []

        def _one(line: str) -> tuple[str, object]:
            try:
                return line, check(line)
            except Exception as e:
                from src.healthcheck import ProbeResult as _PR
                return line, _PR(False, None, f"ошибка {stage_label}: {type(e).__name__}")

        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, workers)) as executor:
            for line, result in executor.map(_one, lines):
                if result is None or not result.alive:
                    dropped_dead += 1
                    reason = result.reason if result is not None else f"{stage_label}: нет вердикта"
                    drop_reasons[reason] = drop_reasons.get(reason, 0) + 1
                    continue
                alive.append(line)
        return alive

    if HEALTHCHECK_ENABLED and to_probe:
        alive = to_probe

        # Стадия A — быстрый TCP/TLS (кроме режима только-proxy).
        if HEALTHCHECK_MODE in ("hybrid", "tcp"):
            alive = _run_stage(
                alive,
                lambda line: probe(line, HEALTHCHECK_TIMEOUT),
                HEALTHCHECK_WORKERS,
                "TCP",
            )
            log(
                f"🩺 Healthcheck TCP ({SPECIAL_FILE_NAME}): живых {len(alive)} "
                f"из {len(to_probe)}"
            )
        else:
            log(f"🩺 Healthcheck TCP пропущен (режим {HEALTHCHECK_MODE})")

        # Стадия B — реальный GET через сам прокси (кроме режима только-tcp).
        if HEALTHCHECK_MODE in ("hybrid", "proxy") and alive:
            from src.proxy_probe import ensure_xray, proxy_get

            if ensure_xray():
                alive_b = _run_stage(
                    alive,
                    lambda line: proxy_get(line, PROXY_GET_TIMEOUT),
                    PROXY_GET_WORKERS,
                    "proxy-GET",
                )
                log(
                    f"🩺 Healthcheck proxy-GET ({SPECIAL_FILE_NAME}): живых "
                    f"{len(alive_b)} из {len(alive)} (после TCP: {len(alive)})"
                )
                alive = alive_b
            else:
                log(
                    f"⚠️ proxy-GET пропущен (xray недоступен) — остались "
                    f"результаты TCP: {len(alive)}"
                )

        unique_configs = alive
        for reason, count in sorted(drop_reasons.items(), key=lambda x: -x[1]):
            log(f"   ├─ мёртвые ({reason}): {count}")
    elif not HEALTHCHECK_ENABLED:
        unique_configs = to_probe
        log(f"🏥 Healthcheck отключён — в файле {len(unique_configs)} конфигов")
    else:
        log(f"⚠️ Нет кандидатов после белого списка для {SPECIAL_FILE_NAME}")

    try:
        with open(special_path, "w", encoding="utf-8") as f:
            f.write("\n".join(unique_configs))
        log(
            f"📁 Создан файл {SPECIAL_FILE_NAME}: {len(unique_configs)} конфигов "
            f"(мёртвых: {dropped_dead}, вне белого списка: {dropped_not_whitelisted}, "
            f"своих: {len(own_set)})"
        )
    except Exception as e:
        log(f"⚠️ Ошибка при сохранении {SPECIAL_FILE_NAME}: {e}")

    return special_path


def _host_port_key(line: str) -> str | None:
    """Ключ дедупликации «host:port» (существующая логика + разбор через extract_endpoint)."""
    if not line:
        return None
    if line.startswith("vmess://"):
        try:
            payload = line[8:]
            rem = len(payload) % 4
            if rem:
                payload += "=" * (4 - rem)
            decoded = base64.b64decode(payload).decode("utf-8", errors="ignore")
            if decoded.startswith("{"):
                j = json.loads(decoded)
                host = j.get("add") or j.get("host") or j.get("ip")
                port = j.get("port")
                if host and port:
                    return f"{str(host).lower()}:{port}"
        except Exception:
            pass
        return None
    m = re.search(r"(?:@|//)([\w\.\-]+):(\d{1,5})", line)
    if m:
        return f"{m.group(1).lower()}:{m.group(2)}"
    return None


# -------------------- СТРАНОВЫЕ ФАЙЛЫ (КИТАЙ / ИРАН) --------------------

def _load_country_index(cidr_path: str, label: str):
    """Загружает CIDR-список страны и строит быстрый индекс. None при ошибке."""
    try:
        with open(cidr_path, "r", encoding="utf-8") as f:
            networks = parse_cidr_lines(f.read())
        if not networks:
            log(f"⚠️ {label}: CIDR-список пуст ({os.path.basename(cidr_path)})")
            return None
        index = build_network_index(networks)
        log(f"📍 {label}: загружено {len(networks)} подсетей ({os.path.basename(cidr_path)})")
        return index
    except FileNotFoundError:
        log(f"⚠️ {label}: не найден {cidr_path} — файл пропущен")
        return None
    except Exception as e:
        log(f"⚠️ {label}: ошибка чтения {cidr_path}: {e}")
        return None


def _collect_country_candidates() -> tuple[list[str], list[str]]:
    """Кандидаты для страновых файлов: storage.json + готовые файлы 1..N
    в детерминированном порядке источников. Возвращает (свои, общий пул)."""
    own_lines = [str(c).strip() for c in OWN_CONFIGS if str(c).strip()]
    pool: list[str] = []
    for i in range(1, SOURCE_COUNT + 1):
        pool.extend(_read_source_file(i))
    return own_lines, pool


def _dedupe_pool(own_lines: list[str], pool: list[str]) -> tuple[list[str], set[str]]:
    """Дедупликация пула: свои конфиги (список №1) приоритетнее по host:port."""
    seen_lines: set[str] = set()
    seen_hostport: set[str] = set()
    candidates: list[str] = []

    def _add(cfg: str):
        if not cfg or cfg in seen_lines:
            return
        hp = _host_port_key(cfg)
        if hp and hp in seen_hostport:
            return
        seen_lines.add(cfg)
        if hp:
            seen_hostport.add(hp)
        candidates.append(cfg)

    own_set = {c for c in own_lines if c}
    for cfg in own_lines:
        _add(cfg)
    for cfg in pool:
        _add(cfg)
    return candidates, own_set


def _load_exempt_index(paths: list, label: str):
    """Индексы исключений (Гонконг/Макао/Тайвань): IP в них — не «внутри страны»."""
    networks = []
    for p in paths:
        try:
            with open(p, "r", encoding="utf-8") as f:
                found = parse_cidr_lines(f.read())
            networks.extend(found)
        except FileNotFoundError:
            log(f"⚠️ {label}: не найден {os.path.basename(p)} — исключение не применено")
        except Exception as e:
            log(f"⚠️ {label}: ошибка чтения {os.path.basename(p)}: {e}")
    if not networks:
        return None
    index = build_network_index(networks)
    log(f"🛟 {label}: исключения (HK/MO/TW) — {len(networks)} подсетей")
    return index


def create_country_configs() -> list[str]:
    """Создаёт страновые файлы для пользователей из Китая (№31) и Ирана (№32).

    Логика: конфиги, чей сервер находится внутри самой страны (по CIDR),
    бесполезны для обхода её же фильтров — они исключаются. Для Китая
    диапазоны Гонконга/Макао/Тайваня из исключения исключены: они вне GFW
    и остаются полезными близкими выходами. Доменные эндпоинты проверяются
    по реальному IP соединения (peer_ip) на стадии healthcheck.
    Живость проверяется с серверов CI (не из КНР/Ирана) — это приближение."""
    specs = [
        (CHINA_FILE_INDEX, CHINA_FILE_NAME, CN_CIDR_PATH, "Китай", CN_EXEMPT_CIDR_PATHS),
        (IRAN_FILE_INDEX, IRAN_FILE_NAME, IR_CIDR_PATH, "Иран", []),
    ]
    written: list[str] = []

    prepared: list[str] | None = None
    own_set: set[str] = set()
    exempt_cache: dict = {}

    for file_index, file_name, cidr_path, label, exempt_paths in specs:
        out_path = os.path.join(GITHUBMIRROR_DIR, file_name)
        index = _load_country_index(cidr_path, label)
        if index is None:
            continue

        exempt_key = tuple(exempt_paths)
        if exempt_key not in exempt_cache:
            exempt_cache[exempt_key] = _load_exempt_index(exempt_paths, label) if exempt_paths else None
        exempt = exempt_cache[exempt_key]

        def _in_country(host: str) -> bool:
            """IP внутри страны, но не в зоне исключения (HK/MO/TW)."""
            if not host or not host_in_index(host, index):
                return False
            if exempt and host_in_index(host, exempt):
                return False
            return True

        # Общий пул кандидатов готовится один раз для обоих файлов.
        if prepared is None:
            own_lines, pool = _collect_country_candidates()
            candidates, own_set = _dedupe_pool(own_lines, pool)
            total_amp = sum(1 for c in candidates if "&amp;" in c)
            if total_amp:
                candidates = [c.replace("&amp;", "&") if "&amp;" in c else c for c in candidates]
                log(f"🔧 Починено HTML-экранирование &amp; → &: {total_amp} конфигов")
            candidates, invalid_reasons = validate_configs(candidates)
            if invalid_reasons:
                dropped_invalid = sum(invalid_reasons.values())
                log(f"🗑️ Отсеяно битых конфигов: {dropped_invalid}")
                for reason, count in sorted(invalid_reasons.items(), key=lambda x: -x[1]):
                    log(f"   ├─ {reason}: {count}")
            prepared = candidates
        candidates = prepared

        # ---- 1. Статический отсев: сервер-IP внутри страны (кроме HK/MO/TW) ----
        dropped_in_country = 0
        fresh: list[str] = []
        for line in candidates:
            ep = extract_endpoint(line)
            if ep and _in_country(ep.host):
                dropped_in_country += 1
                continue
            fresh.append(line)

        # ---- 2. Равномерная выборка под бюджет healthcheck ----
        probe_list = fresh
        if COUNTRY_PROBE_LIMIT and len(fresh) > COUNTRY_PROBE_LIMIT:
            step = len(fresh) / COUNTRY_PROBE_LIMIT
            probe_list = [fresh[int(i * step)] for i in range(COUNTRY_PROBE_LIMIT)]
            log(
                f"🔎 {file_name}: выборка {len(probe_list)} кандидатов "
                f"из {len(fresh)} (вне страны: {dropped_in_country} отсечено статически)"
            )
        else:
            log(f"🔎 {file_name}: кандидатов {len(fresh)} (отсечено статически: {dropped_in_country})")

        # ---- 3. Healthcheck TCP/TLS + отсев доменов, разрешившихся в страну ----
        alive: list[str] = []
        dropped_dead = 0
        if HEALTHCHECK_ENABLED and probe_list:
            drop_reasons: dict[str, int] = {}

            def _one(line: str) -> tuple[str, ProbeResult]:
                try:
                    return line, probe(line, HEALTHCHECK_TIMEOUT)
                except Exception as e:
                    return line, ProbeResult(False, None, f"ошибка TCP: {type(e).__name__}")

            with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, HEALTHCHECK_WORKERS)) as executor:
                for line, result in executor.map(_one, probe_list):
                    if result is None or not result.alive:
                        dropped_dead += 1
                        reason = result.reason if result is not None else "нет вердикта"
                        drop_reasons[reason] = drop_reasons.get(reason, 0) + 1
                        continue
                    # Домен мог разрешиться на сервер внутри страны (кроме HK/MO/TW) — исключаем.
                    if result.peer_ip and _in_country(result.peer_ip):
                        dropped_in_country += 1
                        continue
                    alive.append(line)
            log(
                f"🩺 Healthcheck TCP ({file_name}): живых {len(alive)} из {len(probe_list)} "
                f"(отсечено внутри страны после DNS: {dropped_in_country})"
            )
            for reason, count in sorted(drop_reasons.items(), key=lambda x: -x[1]):
                log(f"   ├─ мёртвые ({reason}): {count}")
        elif not HEALTHCHECK_ENABLED:
            alive = probe_list
            log(f"🏥 Healthcheck отключён — в {file_name} {len(alive)} конфигов")

        try:
            with open(out_path, "w", encoding="utf-8") as f:
                f.write("\n".join(alive))
            own_alive = sum(1 for c in alive if c in own_set)
            log(
                f"📁 Создан файл {file_name}: {len(alive)} конфигов "
                f"(внутри страны: {dropped_in_country}, мёртвых: {dropped_dead}, своих: {own_alive})"
            )
            written.append(out_path)
        except Exception as e:
            log(f"⚠️ Ошибка при сохранении {file_name}: {e}")

    return written
