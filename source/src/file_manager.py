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
    HEALTHCHECK_TIMEOUT,
    HEALTHCHECK_WORKERS,
)
from src.logger import log
from src.network import fetch_data, NotModified, _format_fetch_error
from src.parser import filter_insecure_configs
from src.cidr import refresh_cidr_whitelist, host_in_whitelist
from src.healthcheck import extract_endpoint, probe, ProbeResult, _is_ip as _is_ip_literal

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

    if HEALTHCHECK_ENABLED and to_probe:
        max_workers = max(1, HEALTHCHECK_WORKERS)

        def _check(line: str) -> tuple[str, ProbeResult]:
            try:
                return line, probe(line, HEALTHCHECK_TIMEOUT)
            except Exception as e:
                return line, ProbeResult(False, None, f"ошибка probe: {type(e).__name__}")

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            for line, result in executor.map(_check, to_probe):
                if not result.alive:
                    dropped_dead += 1
                    drop_reasons[result.reason] = drop_reasons.get(result.reason, 0) + 1
                    continue
                unique_configs.append(line)
        log(f"🩺 Healthcheck ({SPECIAL_FILE_NAME}): живые {len(unique_configs)} из {len(to_probe)}")
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
