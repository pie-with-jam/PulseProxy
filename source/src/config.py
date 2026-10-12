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

LOCAL_PATHS = [os.path.join(GITHUBMIRROR_DIR, f"{i+1}.txt") for i in range(SOURCE_COUNT)]
LOCAL_PATHS.append(os.path.join(GITHUBMIRROR_DIR, SPECIAL_FILE_NAME))

DEFAULT_MAX_WORKERS = int(os.environ.get("MAX_WORKERS", "16"))

# -------------------- HEALTHCHECK СПЕЦФАЙЛА --------------------
# Живость конфигов в спецфайле: TCP-пинг + TLS/SNI-хендшейк.
HEALTHCHECK_ENABLED = os.environ.get("HEALTHCHECK", "1") != "0"
HEALTHCHECK_TIMEOUT = float(os.environ.get("HEALTHCHECK_TIMEOUT", "3"))
HEALTHCHECK_WORKERS = int(os.environ.get("HEALTHCHECK_WORKERS", "150"))
