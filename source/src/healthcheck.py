import base64
import ipaddress
import json
import re
import socket
import ssl
import urllib.parse
from dataclasses import dataclass

# -------------------- РАЗБОР КОНФИГА --------------------

# Схемы, которые всегда ходят по TLS.
_TLS_SCHEMES = {"trojan", "hysteria", "hysteria2", "hy2", "tuic", "anytls", "juicity"}

_DEFAULT_PORTS = {
    "hysteria": 443, "hysteria2": 443, "hy2": 443,
    "tuic": 443, "anytls": 443, "juicity": 443,
}


@dataclass
class Endpoint:
    host: str
    port: int
    sni: str | None
    uses_tls: bool


def _b64decode(data: str) -> bytes:
    data = data.strip()
    rem = len(data) % 4
    if rem:
        data += "=" * (4 - rem)
    return base64.b64decode(data)


def _is_ip(host: str) -> bool:
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False


def _vmess_endpoint(line: str) -> Endpoint | None:
    try:
        payload = line[len("vmess://"):]
        # Иногда vmess-строка — base64 от "host:port?..." или JSON
        decoded = _b64decode(payload).decode("utf-8", errors="ignore")
        if decoded.startswith("{"):
            j = json.loads(decoded)
            host = str(j.get("add") or j.get("ip") or "").strip()
            try:
                port = int(j.get("port"))
            except (TypeError, ValueError):
                return None
            if not host or not (0 < port < 65536):
                return None
            tls_flag = str(j.get("tls") or "").lower()
            security = str(j.get("security") or "").lower()
            sni = str(j.get("sni") or j.get("host") or "").strip() or None
            uses_tls = tls_flag in ("tls", "reality", "xtls") or security in ("tls", "reality")
            return Endpoint(host, port, sni, uses_tls)
        # host:port?... без JSON
        return _regex_endpoint(decoded)
    except Exception:
        return None


def _uri_endpoint(line: str) -> Endpoint | None:
    try:
        parsed = urllib.parse.urlsplit(line)
        host = parsed.hostname
        if not host:
            return None
        scheme = (parsed.scheme or "").lower()
        try:
            port = parsed.port
        except ValueError:
            port = None
        if port is None:
            port = _DEFAULT_PORTS.get(scheme)
        if port is None or not (0 < port < 65536):
            return None

        params = {k.lower(): v[0] for k, v in urllib.parse.parse_qs(
            parsed.query, keep_blank_values=True).items()}
        sni = (params.get("sni") or params.get("peer") or
               params.get("servername") or params.get("host") or None)
        if sni:
            sni = sni.strip() or None

        security = (params.get("security") or "").lower()
        tls_param = (params.get("tls") or "").lower()
        uses_tls = (
            scheme in _TLS_SCHEMES
            or security in ("tls", "reality", "xtls")
            or tls_param in ("1", "true", "tls", "reality")
            or (sni is not None and security != "none")
        )
        return Endpoint(host, port, sni, uses_tls)
    except Exception:
        return None


_RE_HOSTPORT = re.compile(r"(?:@|//)([\w\.\-]+):(\d{1,5})")
_RE_SNI = re.compile(r"[?&](?:sni|peer|servername|host)=([^&#\s]+)", re.IGNORECASE)
_RE_TLS = re.compile(r"[?&]security=(tls|reality|xtls)", re.IGNORECASE)
_RE_SECURITY_NONE = re.compile(r"[?&]security=none", re.IGNORECASE)


def _regex_endpoint(line: str) -> Endpoint | None:
    m = _RE_HOSTPORT.search(line)
    if not m:
        return None
    host, port = m.group(1), int(m.group(2))
    if not (0 < port < 65536):
        return None
    sni_m = _RE_SNI.search(line)
    sni = urllib.parse.unquote(sni_m.group(1)) if sni_m else None
    scheme = line.split("://", 1)[0].lower() if "://" in line else ""
    uses_tls = (
        scheme in _TLS_SCHEMES
        or bool(_RE_TLS.search(line))
        or (sni is not None and not _RE_SECURITY_NONE.search(line))
    )
    return Endpoint(host, port, sni, uses_tls)


def extract_endpoint(line: str) -> Endpoint | None:
    """Извлекает host/port/SNI и признак TLS из строки конфига."""
    line = (line or "").strip()
    if not line:
        return None
    if line.startswith("vmess://"):
        return _vmess_endpoint(line)
    if "://" in line:
        return _uri_endpoint(line)
    return _regex_endpoint(line)


# -------------------- ПРОВЕРКИ ЖИВОСТИ --------------------

def tcp_ping(host: str, port: int, timeout: float) -> socket.socket | None:
    """TCP-тест: возвращает живой сокет или None."""
    try:
        return socket.create_connection((host, port), timeout=timeout)
    except Exception:
        return None


def tls_handshake(
    host: str,
    port: int,
    server_hostname: str | None,
    timeout: float,
    sock: socket.socket | None = None,
) -> bool:
    """Проверка живого TLS/SNI: рукопожатие (без валидации сертификата).
    Если передан открытый сокет — используется он (одно соединение вместо двух)."""
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        if sock is None:
            sock = socket.create_connection((host, port), timeout=timeout)
        with sock:
            with ctx.wrap_socket(sock, server_hostname=server_hostname) as tls:
                return tls.version() is not None
    except Exception:
        return False


@dataclass
class ProbeResult:
    alive: bool
    peer_ip: str | None = None
    reason: str = ""


def probe(line: str, timeout: float) -> ProbeResult:
    """Проверка конфига одним соединением:
    TLS-конфиги — сразу TLS/SNI-хендшейк (TCP жив по определению),
    нетLS — TCP-пинг."""
    ep = extract_endpoint(line)
    if not ep:
        return ProbeResult(False, None, "не разобран")

    if not ep.uses_tls:
        sock = tcp_ping(ep.host, ep.port, timeout)
        if sock is None:
            return ProbeResult(False, None, "TCP-пинг")
        peer_ip = None
        try:
            peer_ip = sock.getpeername()[0]
        except OSError:
            pass
        finally:
            try:
                sock.close()
            except OSError:
                pass
        return ProbeResult(True, peer_ip, "")

    # TLS: одно соединение — TCP + хендшейк
    try:
        sock = socket.create_connection((ep.host, ep.port), timeout=timeout)
    except Exception:
        return ProbeResult(False, None, "TCP-пинг")

    peer_ip = None
    try:
        peer_ip = sock.getpeername()[0]
    except OSError:
        pass

    # SNI: явный из конфига, иначе сам хост (если не IP)
    server_hostname = ep.sni or (ep.host if not _is_ip(ep.host) else None)
    if not tls_handshake(ep.host, ep.port, server_hostname, timeout, sock=sock):
        # tls_handshake закрывает сокет внутри with; на случай исключения до этого:
        try:
            sock.close()
        except OSError:
            pass
        return ProbeResult(False, peer_ip, "TLS/SNI-хендшейк")

    return ProbeResult(True, peer_ip, "")
