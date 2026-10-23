import bisect
import ipaddress
import os
from src.config import CIDR_WHITELIST_PATH, CIDR_WHITELIST_URL
from src.logger import log

# -------------------- CIDR БЕЛЫЙ СПИСОК --------------------

def parse_cidr_lines(text: str) -> list:
    """Парсит CIDR-подсети из текста (одна подсеть на строку, # — комментарий)."""
    networks: list = []
    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        try:
            networks.append(ipaddress.ip_network(line, strict=False))
        except ValueError:
            log(f"⚠️ CIDR:{lineno} — невалидная подсеть «{line}»")
    return networks


def refresh_cidr_whitelist() -> list:
    """Скачивает актуальный CIDR-белый список и обновляет локальный файл.
    При ошибке загрузки использует существующий локальный файл."""
    try:
        from src.network import fetch_data
        data = fetch_data(
            CIDR_WHITELIST_URL,
            timeout=30,
            max_attempts=2,
            allow_http_downgrade=False,
        )
        networks = parse_cidr_lines(data)
        if not networks:
            log("⚠️ CIDR-источник вернул пустой список — используем локальный файл")
            return load_cidr_whitelist()
        os.makedirs(os.path.dirname(CIDR_WHITELIST_PATH), exist_ok=True)
        with open(CIDR_WHITELIST_PATH, "w", encoding="utf-8") as f:
            f.write(
                "# Белый список CIDR для спецфайла (одна подсеть на строку).\n"
                f"# Источник: {CIDR_WHITELIST_URL}\n"
                "# Автообновляется при каждом запуске генератора.\n"
            )
            f.write(data if data.endswith("\n") else data + "\n")
        log(f"🔄 CIDR-белый список обновлён: {len(networks)} подсетей")
        return networks
    except Exception as e:
        log(f"⚠️ Не удалось обновить CIDR-белый список: {e} — используем локальный файл")
        return load_cidr_whitelist()


def load_cidr_whitelist(path: str | None = None) -> list:
    """Загружает CIDR-подсети из cidrwhitelist.txt (одна подсеть на строку, # — комментарий)."""
    path = path or CIDR_WHITELIST_PATH
    networks: list = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for lineno, raw in enumerate(f, start=1):
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                try:
                    networks.append(ipaddress.ip_network(line, strict=False))
                except ValueError:
                    log(f"⚠️ cidrwhitelist.txt:{lineno} — невалидный CIDR «{line}»")
    except FileNotFoundError:
        log(f"ℹ️ {path} не найден — CIDR-фильтр отключён")
    except Exception as e:
        log(f"⚠️ Ошибка чтения {path}: {e}")
    return networks


def ip_in_whitelist(ip: str | None, networks: list) -> bool:
    """Проверяет, входит ли IP-адрес в одну из белых CIDR-подсетей."""
    if not ip or not networks:
        return False
    try:
        addr = ipaddress.ip_address(ip)
    except ValueError:
        return False
    return any(net.version == addr.version and addr in net for net in networks)


def host_in_whitelist(host: str | None, networks: list) -> bool:
    """Проверяет хост: если это IP-литерал — проверка по CIDR, иначе False."""
    if not host:
        return False
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return False
    return ip_in_whitelist(host, networks)


# -------------------- БЫСТРЫЙ ИНДЕКС CIDR --------------------

def build_network_index(networks: list) -> dict:
    """Строит быстрый индекс по CIDR-подсетям для массовых проверок.

    Линейный перебор подсетей на каждый IP слишком медленный для сотен
    тысяч конфигов (например, 8802 подсетей Китая). Индекс объединяет
    пересекающиеся/смежные подсети через collapse_addresses и ищет
    бинарным поиском по отсортированным началам диапазонов."""
    collapsed = list(ipaddress.collapse_addresses(networks))
    index: dict[int, tuple[list[int], list[tuple[int, int]]]] = {}
    for version in (4, 6):
        ranges = sorted(
            (int(net.network_address), int(net.broadcast_address))
            for net in collapsed if net.version == version
        )
        if ranges:
            index[version] = ([s for s, _ in ranges], ranges)
    return index


def ip_in_index(ip: str | None, index: dict) -> bool:
    """Проверяет IP по быстрому индексу (O(log n) вместо O(n·m))."""
    if not ip or not index:
        return False
    try:
        addr = ipaddress.ip_address(ip)
    except ValueError:
        return False
    entry = index.get(addr.version)
    if not entry:
        return False
    starts, ranges = entry
    val = int(addr)
    pos = bisect.bisect_right(starts, val) - 1
    if pos < 0:
        return False
    start, end = ranges[pos]
    return start <= val <= end


def host_in_index(host: str | None, index: dict) -> bool:
    """Хост в индексе: IP-литерал проверяется по индексу, домен — нет (False)."""
    if not host:
        return False
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return False
    return ip_in_index(host, index)
