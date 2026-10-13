import base64
import ipaddress
import json
import re
import urllib.parse

# -------------------- СТРУКТУРНАЯ ВАЛИДАЦИЯ КОНФИГОВ --------------------
# Ловим битые URI, из-за которых V2rayNG зависает при проверке задержек
# (склеенные query-параметры, кривые UUID/порты, сломанный base64 и т.п.).

MAX_CONFIG_LEN = 4096

_UUID_RE = re.compile(
    r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
)
_HEX32_RE = re.compile(r"^[0-9a-fA-F]{32}$")
_HOST_RE = re.compile(r"^[A-Za-z0-9]([A-Za-z0-9.-]*[A-Za-z0-9])?$")
_CTRL_RE = re.compile(r"[\x00-\x1f\x7f]")

# Известные query-ключи: если они встречаются В ЗНАЧЕНИИ параметра —
# значит два параметра склеились (например «path=/fp=chromesecurity=tls»).
_QUERY_KEYS = (
    "path", "fp", "security", "sni", "type", "host", "pbk", "sid", "flow",
    "alpn", "mode", "headerType", "packetEncoding", "encryption", "insecure",
    "allowInsecure", "allow_insecure", "servicename", "obfs", "obfsparam",
    "method", "plugin", "peer", "servername", "tls", "publicKey",
    "shortid", "congestioncontrol", "udprelaymode", "password", "auth",
    "protocol", "obfs-password",
)
_KEY_IN_VALUE_RE = re.compile(
    r"(?:" + "|".join(re.escape(k) for k in _QUERY_KEYS) + r")=",
    re.IGNORECASE,
)
_KEY_RE = re.compile(r"[A-Za-z0-9_\-]{1,40}")


def _is_ip(host: str) -> bool:
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False


def _b64_ok(data: str) -> bytes | None:
    try:
        clean = data.strip()
        rem = len(clean) % 4
        if rem:
            clean += "=" * (4 - rem)
        return base64.b64decode(clean, validate=False)
    except Exception:
        return None


def _valid_uuid(value: str) -> bool:
    value = value.strip()
    return bool(_UUID_RE.match(value) or _HEX32_RE.match(value))


def _check_common(scheme: str, parsed: urllib.parse.SplitResult) -> str | None:
    host = parsed.hostname
    if not host:
        return "нет адреса сервера"
    if not _is_ip(host) and not _HOST_RE.match(host):
        return f"некорректный адрес: {host[:40]}"
    try:
        port = parsed.port
    except ValueError:
        return "некорректный порт"
    if port is None:
        if scheme in ("hysteria", "hysteria2", "hy2", "tuic", "trojan"):
            return "нет порта"
        return None
    if not (0 < port < 65536):
        return f"порт вне диапазона: {port}"
    return None


def _check_query_glue(query: str) -> str | None:
    if not query:
        return None
    for pair in query.split("&"):
        if not pair:
            continue
        key, sep, value = pair.partition("=")
        if not _KEY_RE.fullmatch(key or ""):
            return f"битый ключ параметра: {key[:30]}"
        if sep and _KEY_IN_VALUE_RE.search(value):
            return "склеенные параметры query"
    return None


def _check_vless(parsed: urllib.parse.SplitResult) -> str | None:
    uid = (parsed.username or "").strip()
    if not uid:
        return "нет UUID"
    if not _valid_uuid(uid):
        return "UUID не валиден"
    params = dict(urllib.parse.parse_qsl(parsed.query, keep_blank_values=True))
    if (params.get("security", "").lower() == "reality"
            and not params.get("pbk", "").strip()):
        return "reality без pbk"
    return None


def _check_trojan(parsed: urllib.parse.SplitResult) -> str | None:
    if not (parsed.username or "").strip() and not (parsed.password or "").strip():
        return "нет пароля"
    return None


def _check_hysteria2(parsed: urllib.parse.SplitResult) -> str | None:
    if not (parsed.username or "").strip() and not (parsed.password or "").strip():
        params = dict(urllib.parse.parse_qsl(parsed.query, keep_blank_values=True))
        if not (params.get("password") or params.get("auth") or "").strip():
            return "нет пароля"
    return None


def _check_tuic(parsed: urllib.parse.SplitResult) -> str | None:
    if not _valid_uuid(parsed.username or ""):
        return "нет UUID"
    if not (parsed.password or "").strip():
        return "нет пароля"
    return None


def _check_ss(line: str, parsed: urllib.parse.SplitResult) -> str | None:
    if parsed.hostname:
        return None
    payload = line[len("ss://"):]
    payload = payload.split("#", 1)[0].split("?", 1)[0]
    decoded = _b64_ok(payload)
    if decoded is None:
        return "сломанный base64"
    text = decoded.decode("utf-8", errors="ignore")
    if "@" not in text or ":" not in text:
        return "нет адреса сервера"
    return None


def _check_vmess(line: str) -> str | None:
    payload = line[len("vmess://"):]
    payload = payload.split("#", 1)[0]
    decoded = _b64_ok(payload)
    if decoded is None:
        return "сломанный base64"
    text = decoded.decode("utf-8", errors="ignore").strip()
    if text.startswith("{"):
        try:
            j = json.loads(text)
        except Exception:
            return "сломанный JSON"
        if not str(j.get("add") or j.get("ip") or "").strip():
            return "нет адреса сервера"
        try:
            port = int(j.get("port"))
        except (TypeError, ValueError):
            return "некорректный порт"
        if not (0 < port < 65536):
            return f"порт вне диапазона: {port}"
        if not str(j.get("id") or "").strip():
            return "нет UUID"
        return None
    m = re.search(r"@([\w\.\-]+):(\d{1,5})", text)
    if not m or not (0 < int(m.group(2)) < 65536):
        return "нет адреса сервера"
    return None


def validate_config(line: str) -> str | None:
    """Возвращает причину, почему конфиг битый, или None, если всё ок."""
    line = (line or "").strip()
    if not line:
        return "пустая строка"
    if len(line) > MAX_CONFIG_LEN:
        return f"слишком длинный ({len(line)} символов)"
    if _CTRL_RE.search(line):
        return "управляющие символы"

    scheme, sep, rest = line.partition("://")
    if not sep:
        return "нет ://"
    scheme = scheme.lower()
    if not rest:
        return "пустой URI"

    body, _, fragment = rest.partition("#")
    # Пробелы допустимы только в названии профиля (фрагменте)
    if " " in body:
        return "пробел вне названия профиля"
    if fragment and _CTRL_RE.search(fragment):
        return "битое название профиля"

    if scheme == "vmess":
        return _check_vmess(line)

    try:
        parsed = urllib.parse.urlsplit(f"{scheme}://{body}")
    except Exception:
        return "URI не разбирается"
    if parsed.scheme != scheme:
        return "битая схема"

    common = _check_common(scheme, parsed)
    if common:
        return common
    glue = _check_query_glue(parsed.query)
    if glue:
        return glue

    if scheme == "vless":
        return _check_vless(parsed)
    if scheme == "trojan":
        return _check_trojan(parsed)
    if scheme in ("hysteria2", "hy2", "hysteria"):
        return _check_hysteria2(parsed)
    if scheme == "tuic":
        return _check_tuic(parsed)
    if scheme in ("ss", "ssr"):
        return _check_ss(line, parsed)
    return None


def validate_configs(lines: list[str]) -> tuple[list[str], dict[str, int]]:
    """Фильтрует список конфигов. Возвращает (валидные, {причина: сколько})."""
    good: list[str] = []
    reasons: dict[str, int] = {}
    for line in lines:
        reason = validate_config(line)
        if reason is None:
            good.append(line)
        else:
            reasons[reason] = reasons.get(reason, 0) + 1
    return good, reasons
