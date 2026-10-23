import os
import subprocess
import json

SOURCE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# -------------------- КОРЕНЬ РЕПОЗИТОРИЯ --------------------
try:
    GIT_ROOT = subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"],
        stderr=subprocess.DEVNULL,
    ).decode().strip()
except Exception:
    GIT_ROOT = os.path.abspath(os.path.join(SOURCE_ROOT, ".."))

GITHUBMIRROR_DIR = os.path.join(GIT_ROOT, "githubmirror")
README_PATH = os.path.join(GIT_ROOT, "README.md")
SNI_DOMAINS_PATH = os.path.join(SOURCE_ROOT, "config", "sni_domains.json")
URLS_PATH = os.path.join(SOURCE_ROOT, "config", "urls.json")
URLS_30_PATH = os.path.join(SOURCE_ROOT, "config", "30_urls.json")
STORAGE_PATH = os.path.join(SOURCE_ROOT, "config", "storage.json")
CIDR_WHITELIST_PATH = os.path.join(SOURCE_ROOT, "config", "cidrwhitelist.txt")
CN_CIDR_PATH = os.path.join(SOURCE_ROOT, "config", "cn_cidr.txt")
IR_CIDR_PATH = os.path.join(SOURCE_ROOT, "config", "ir_cidr.txt")
QRCODES_DIR = os.path.join(GIT_ROOT, "qr-codes")

# -------------------- ЗАГРУЗКА КОНФИГУРАЦИИ --------------------
def _load_json_list(path: str, default: list) -> list:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                # Сортируем по ключам-числам для сохранения оригинального порядка
                return [data[k] for k in sorted(data.keys(), key=lambda x: int(x))]
            return data
    except Exception:
        return default


URLS = _load_json_list(URLS_PATH, [])
# Дополнительные источники для спецфайла (белые списки) и свои конфиги из storage.json.
EXTRA_URLS_FOR_SPECIAL = _load_json_list(URLS_30_PATH, [])
OWN_CONFIGS = _load_json_list(STORAGE_PATH, [])

# Количество публичных источников (1..SOURCE_COUNT) и номер спецфайла (SOURCE_COUNT + 1).
SOURCE_COUNT = len(URLS)
SPECIAL_FILE_INDEX = SOURCE_COUNT + 1
SPECIAL_FILE_NAME = f"{SPECIAL_FILE_INDEX}.txt"

# Страновые спецфайлы: №31 — без серверов в Китае, №32 — без серверов в Иране.
CHINA_FILE_INDEX = SPECIAL_FILE_INDEX + 1
CHINA_FILE_NAME = f"{CHINA_FILE_INDEX}.txt"
IRAN_FILE_INDEX = SPECIAL_FILE_INDEX + 2
IRAN_FILE_NAME = f"{IRAN_FILE_INDEX}.txt"
# Индекс последнего файла подписки (для QR-генератора и ссылок).
LAST_FILE_INDEX = IRAN_FILE_INDEX
# Файлы без внешнего URL (собираются из 1..SOURCE_COUNT + storage.json).
SPECIAL_FILE_SOURCES = {
    SPECIAL_FILE_INDEX: "Обход SNI/CIDR белых списков",
    CHINA_FILE_INDEX: "Для Китая (без серверов в CN)",
    IRAN_FILE_INDEX: "Для Ирана (без серверов в IR)",
}

# Создаём папку зеркала, если она не существует
os.makedirs(GITHUBMIRROR_DIR, exist_ok=True)

def _looks_like_github_token(token: str | None) -> bool:
    """Проверяет, похож ли токен на GitHub PAT (чтобы не слать сторонний токен в GitHub API)."""
    if not token:
        return False
    t = token.strip()
    return t.startswith(("ghp_", "gho_", "ghu_", "ghs_", "ghr_", "github_pat_"))


_MY_TOKEN = os.environ.get("MY_TOKEN")
# Токен ТОЛЬКО для GitHub API (статистика).
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN") or (_MY_TOKEN if _looks_like_github_token(_MY_TOKEN) else None)
# Путь проекта (например pie-with-jam/PulseProxy).
# В GitHub Actions подхватывается автоматически из GITHUB_REPOSITORY.
REPO_NAME = os.environ.get("REPO_PATH") or os.environ.get("GITHUB_REPOSITORY") or "pie-with-jam/PulseProxy"
# Хост для ссылок на файлы.
GIT_HOST = os.environ.get("GIT_HOST", "github.com")


def build_raw_file_url(file_index: int) -> str:
    """Строит прямую ссылку на файл конфига с учётом хоста."""
    if "github" in GIT_HOST.lower():
        return f"https://github.com/{REPO_NAME}/raw/refs/heads/main/githubmirror/{file_index}.txt"
    return f"https://{GIT_HOST}/{REPO_NAME}/-/raw/main/githubmirror/{file_index}.txt"

EXTRA_URL_TIMEOUT = int(os.environ.get("EXTRA_URL_TIMEOUT", "6"))
EXTRA_URL_MAX_ATTEMPTS = int(os.environ.get("EXTRA_URL_MAX_ATTEMPTS", "2"))

# Актуальный CIDR-белый список (русские мобильные подсети) — автообновление при каждом запуске.
CIDR_WHITELIST_URL = os.environ.get(
    "CIDR_WHITELIST_URL",
    "https://raw.githubusercontent.com/hxehex/russia-mobile-internet-whitelist/refs/heads/main/cidrwhitelist.txt",
)

# Сколько кандидатов максимум проверять на живость в страновых файлах (31/32).
# Полный пул ~400k+ конфигов целиком healthcheck невозможен — берётся
# равномерная выборка под бюджет; 0 — без лимита.
COUNTRY_PROBE_LIMIT = int(os.environ.get("COUNTRY_PROBE_LIMIT", "4000"))

LOCAL_PATHS = [os.path.join(GITHUBMIRROR_DIR, f"{i+1}.txt") for i in range(SOURCE_COUNT)]
LOCAL_PATHS.append(os.path.join(GITHUBMIRROR_DIR, SPECIAL_FILE_NAME))

DEFAULT_MAX_WORKERS = int(os.environ.get("MAX_WORKERS", "16"))

# -------------------- HEALTHCHECK СПЕЦФАЙЛА --------------------
# Живость конфигов в спецфайле: TCP-пинг + TLS/SNI-хендшейк.
# Режимы: hybrid — TCP-предфильтр, затем GET через прокси (рекомендуется);
# tcp — только TCP/TLS; proxy — только GET через прокси (без предфильтра).
HEALTHCHECK_ENABLED = os.environ.get("HEALTHCHECK", "1") != "0"
HEALTHCHECK_MODE = os.environ.get("HEALTHCHECK_MODE", "hybrid").lower()
if HEALTHCHECK_MODE not in ("hybrid", "tcp", "proxy"):
    HEALTHCHECK_MODE = "hybrid"
HEALTHCHECK_TIMEOUT = float(os.environ.get("HEALTHCHECK_TIMEOUT", "3"))
HEALTHCHECK_WORKERS = int(os.environ.get("HEALTHCHECK_WORKERS", "150"))

# -------------------- PROXY-GET ЧЕРЕЗ XRAY --------------------
PROXY_GET_TIMEOUT = float(os.environ.get("PROXY_GET_TIMEOUT", "10"))
PROXY_GET_WORKERS = int(os.environ.get("PROXY_GET_WORKERS", "24"))
PROXY_TEST_URL = os.environ.get("PROXY_TEST_URL", "http://www.gstatic.com/generate_204")
XRAY_AUTOINSTALL = os.environ.get("XRAY_AUTOINSTALL", "1") != "0"
XRAY_PATH = os.environ.get(
    "XRAY_PATH",
    os.path.join(SOURCE_ROOT, "bin", "xray.exe" if os.name == "nt" else "xray"),
)
