"""Проверка живости конфигов реальным GET-запросом через сам прокси (xray-core).

Стадия B гибридного healthcheck: конвертируется в outbound xray, поднимается
локальный http-inbound на 127.0.0.1:<port>, через него делается GET.
Если схема не поддерживается конвертером — возвращается None (вызывающая
сторона оставляет вердикт стадии A / конфиг).
"""

import base64
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile

from src.config import PROXY_GET_TIMEOUT, PROXY_TEST_URL, XRAY_AUTOINSTALL, XRAY_PATH
from src.healthcheck import ProbeResult, _b64decode, _is_ip
from src.logger import log

_XRAY_LOCK = threading.Lock()
_XRAY_READY: bool | None = None  # None — ещё не пробовали, True — есть, False — нет


# -------------------- XRAY-БИНАРЬ --------------------

def _asset_name() -> str | None:
    system = platform.system().lower()
    machine = platform.machine().lower()
    arm = machine in ("aarch64", "arm64")
    if system == "linux":
        return "Xray-linux-arm64-v8a.zip" if arm else "Xray-linux-64.zip"
    if system == "windows":
        return "Xray-windows-64.zip"
    if system == "darwin":
        return "Xray-macos-arm64-64.zip" if arm else "Xray-macos-64.zip"
    return None


def ensure_xray() -> bool:
    """Скачивает xray в source/bin при необходимости. Возвращает доступность бинаря."""
    global _XRAY_READY
    if _XRAY_READY is not None:
        return _XRAY_READY
    with _XRAY_LOCK:
        if _XRAY_READY is not None:
            return _XRAY_READY

        def _ok(path: str) -> bool:
            if not (path and os.path.isfile(path)):
                return False
            try:
                r = subprocess.run(
                    [path, "version"],
                    capture_output=True,
                    timeout=10,
                    creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0,
                )
                return r.returncode == 0
            except Exception:
                return False

        if _ok(XRAY_PATH):
            _XRAY_READY = True
            return True

        if not XRAY_AUTOINSTALL:
            log("⚠️ proxy-GET: xray не найден и автоустановка отключена")
            _XRAY_READY = False
            return False

        asset = _asset_name()
        if not asset:
            log(f"⚠️ proxy-GET: неизвестная платформа для xray ({platform.system()})")
            _XRAY_READY = False
            return False

        url = f"https://github.com/XTLS/Xray-core/releases/latest/download/{asset}"
        tmp_dir = tempfile.mkdtemp(prefix="xray_dl_")
        zip_path = os.path.join(tmp_dir, asset)
        try:
            log(f"⬇️ proxy-GET: скачиваю {asset} …")
            urllib.request.urlretrieve(url, zip_path)
            os.makedirs(os.path.dirname(XRAY_PATH), exist_ok=True)
            member = "xray.exe" if os.name == "nt" else "xray"
            with zipfile.ZipFile(zip_path) as zf:
                data = zf.read(member)
            tmp_bin = XRAY_PATH + ".tmp"
            with open(tmp_bin, "wb") as f:
                f.write(data)
            if os.name != "nt":
                os.chmod(tmp_bin, 0o755)
            os.replace(tmp_bin, XRAY_PATH)
            log(f"✅ proxy-GET: xray установлен в {XRAY_PATH}")
            _XRAY_READY = _ok(XRAY_PATH)
        except Exception as e:
            log(f"⚠️ proxy-GET: не удалось скачать xray ({type(e).__name__}: {e})")
            _XRAY_READY = False
        finally:
            shutil.rmtree(tmp_dir, ignore_errors=True)
        return bool(_XRAY_READY)


# -------------------- КОНВЕРТАЦИЯ КОНФИГОВ --------------------

def _params(query: str) -> dict:
    return {k.lower(): v[0] for k, v in urllib.parse.parse_qs(query, keep_blank_values=True).items()}


def _stream_settings(params: dict, network: str, security: str) -> dict:
    ss: dict = {"network": network}
    if security in ("tls", "reality"):
        ss["security"] = security

    sni = (params.get("sni") or params.get("peer") or params.get("servername") or "").strip()
    fp = (params.get("fp") or params.get("fingerprint") or "").strip()

    if security == "tls":
        ts: dict = {}
        if sni:
            ts["serverName"] = sni
        if fp:
            ts["fingerprint"] = fp
        alpn = (params.get("alpn") or "").strip()
        if alpn:
            ts["alpn"] = [a.strip() for a in urllib.parse.unquote(alpn).split(",") if a.strip()]
        ss["tlsSettings"] = ts
    elif security == "reality":
        rs: dict = {}
        if sni:
            rs["serverName"] = sni
        rs["fingerprint"] = fp or "chrome"
        if params.get("pbk"):
            rs["publicKey"] = params["pbk"]
        if params.get("sid"):
            rs["shortId"] = params["sid"]
        if params.get("spx"):
            rs["spiderX"] = urllib.parse.unquote(params["spx"])
        ss["realitySettings"] = rs

    if network == "ws":
        ws: dict = {}
        if params.get("path"):
            ws["path"] = params["path"]
        if params.get("host"):
            ws["headers"] = {"Host": urllib.parse.unquote(params["host"])}
        ss["wsSettings"] = ws
    elif network == "grpc":
        g: dict = {}
        if params.get("servicename"):
            g["serviceName"] = params["servicename"]
        if params.get("host"):
            g["authority"] = urllib.parse.unquote(params["host"])
        if (params.get("mode") or "").lower() == "multi":
            g["multiMode"] = True
        ss["grpcSettings"] = g
    elif network == "xhttp":
        x: dict = {}
        if params.get("path"):
            x["path"] = params["path"]
        if params.get("host"):
            x["host"] = urllib.parse.unquote(params["host"])
        if params.get("mode"):
            x["mode"] = params["mode"]
        ss["xhttpSettings"] = x
    return ss


_NETWORK_ALIASES = {"tcp": "tcp", "ws": "ws", "grpc": "grpc", "gun": "grpc", "xhttp": "xhttp", "splithttp": "xhttp", "h2": "http", "http": "http"}


def to_xray_config(line: str) -> dict | None:
    """Конвертирует URI-конфиг в xray-outbound. None — схема не поддерживается."""
    line = (line or "").strip()
    try:
        if line.startswith("vless://"):
            return _vless_outbound(line)
        if line.startswith("vmess://"):
            return _vmess_outbound(line)
        if line.startswith("trojan://"):
            return _trojan_outbound(line)
        if line.startswith("ss://"):
            return _ss_outbound(line)
    except Exception:
        return None
    return None


def _vless_outbound(line: str) -> dict | None:
    parsed = urllib.parse.urlsplit(line)
    uuid = urllib.parse.unquote(parsed.username or "")
    host = parsed.hostname
    if not uuid or not host:
        return None
    port = parsed.port or 443
    params = _params(parsed.query)
    network = _NETWORK_ALIASES.get((params.get("type") or "tcp").lower(), "tcp")
    security = (params.get("security") or "none").lower()
    user: dict = {"id": uuid, "encryption": params.get("encryption") or "none"}
    if params.get("flow"):
        user["flow"] = params["flow"]
    return {
        "protocol": "vless",
        "settings": {"vnext": [{"address": host, "port": port, "users": [user]}]},
        "streamSettings": _stream_settings(params, network, security),
    }


def _vmess_outbound(line: str) -> dict | None:
    payload = _b64decode(line[len("vmess://"):]).decode("utf-8", errors="ignore")
    j = json.loads(payload)
    host = str(j.get("add") or "").strip()
    uuid = str(j.get("id") or "").strip()
    if not host or not uuid:
        return None
    port = int(j.get("port") or 443)
    params = {
        "sni": str(j.get("sni") or ""),
        "host": str(j.get("host") or ""),
        "path": str(j.get("path") or ""),
        "fp": str(j.get("fp") or ""),
        "alpn": str(j.get("alpn") or ""),
    }
    network = _NETWORK_ALIASES.get(str(j.get("net") or "tcp").lower(), "tcp")
    security = "tls" if str(j.get("tls") or "").lower() in ("tls", "reality") else "none"
    user = {"id": uuid, "alterId": int(j.get("aid") or 0), "security": str(j.get("scy") or "auto")}
    return {
        "protocol": "vmess",
        "settings": {"vnext": [{"address": host, "port": port, "users": [user]}]},
        "streamSettings": _stream_settings(params, network, security),
    }


def _trojan_outbound(line: str) -> dict | None:
    parsed = urllib.parse.urlsplit(line)
    password = urllib.parse.unquote(parsed.username or "")
    host = parsed.hostname
    if not password or not host:
        return None
    port = parsed.port or 443
    params = _params(parsed.query)
    network = _NETWORK_ALIASES.get((params.get("type") or "tcp").lower(), "tcp")
    security = (params.get("security") or "tls").lower()
    if security not in ("tls", "reality", "none"):
        security = "tls"
    return {
        "protocol": "trojan",
        "settings": {"servers": [{"address": host, "port": port, "password": password}]},
        "streamSettings": _stream_settings(params, network, security),
    }


_SS_PLAIN = re.compile(r"^(?P<method>[^:@/]+):(?P<password>.+)@(?P<host>[^:/@]+):(?P<port>\d{1,5})$")


def _ss_outbound(line: str) -> dict | None:
    payload = line[len("ss://"):]
    payload = payload.split("#", 1)[0].split("?", 1)[0]
    host = port = method = password = None
    if "@" in payload:
        userinfo, hostpart = payload.rsplit("@", 1)
        try:
            decoded = _b64decode(userinfo).decode("utf-8", errors="ignore")
        except Exception:
            decoded = urllib.parse.unquote(userinfo)
        if ":" in decoded:
            method, password = decoded.split(":", 1)
        if ":" in hostpart:
            host, port_s = hostpart.rsplit(":", 1)
            port = int(port_s)
    else:
        try:
            decoded = _b64decode(payload).decode("utf-8", errors="ignore")
        except Exception:
            return None
        m = _SS_PLAIN.match(decoded)
        if not m:
            return None
        method, password, host = m.group("method"), m.group("password"), m.group("host")
        port = int(m.group("port"))
    if not (method and password and host and port):
        return None
    return {
        "protocol": "shadowsocks",
        "settings": {"servers": [{"address": host, "port": port, "method": method, "password": password}]},
    }


# -------------------- PROXY-GET ПРОВЕРКА --------------------

def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _kill(proc: subprocess.Popen):
    try:
        proc.terminate()
        try:
            proc.wait(timeout=2)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=2)
    except Exception:
        pass


def proxy_get(line: str, timeout: float | None = None) -> ProbeResult | None:
    """GET через реальный прокси по конфигу.

    Возвращает ProbeResult; None — схема не конвертируется (fallback на стадию A).
    """
    outbound = to_xray_config(line)
    if outbound is None:
        return None
    if not ensure_xray():
        return ProbeResult(False, None, "proxy-GET (нет xray)")

    timeout = timeout or PROXY_GET_TIMEOUT
    port = _free_port()
    xray_config = {
        "log": {"loglevel": "none"},
        "inbounds": [{
            "listen": "127.0.0.1",
            "port": port,
            "protocol": "http",
            "settings": {},
        }],
        "outbounds": [outbound],
    }

    tmp_dir = tempfile.mkdtemp(prefix="pp_xray_")
    cfg_path = os.path.join(tmp_dir, "config.json")
    proc: subprocess.Popen | None = None
    try:
        with open(cfg_path, "w", encoding="utf-8") as f:
            json.dump(xray_config, f)
        proc = subprocess.Popen(
            [XRAY_PATH, "run", "-c", cfg_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0,
        )
        t0 = time.monotonic()

        # Ждём, пока xray поднимет inbound (макс. 30% таймаута).
        inbound_up = False
        port_deadline = t0 + max(0.5, timeout * 0.3)
        while time.monotonic() < port_deadline:
            if proc.poll() is not None:
                return ProbeResult(False, None, "proxy-GET (xray упал)")
            try:
                with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                    inbound_up = True
                    break
            except OSError:
                time.sleep(0.05)
        if not inbound_up:
            return ProbeResult(False, None, "proxy-GET (старт xray)")

        # GET через прокси.
        remaining = max(1.0, timeout - (time.monotonic() - t0))
        proxy_handler = urllib.request.ProxyHandler({
            "http": f"http://127.0.0.1:{port}",
        })
        opener = urllib.request.build_opener(proxy_handler)
        req = urllib.request.Request(PROXY_TEST_URL, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with opener.open(req, timeout=remaining) as resp:
                resp.read(64)
                status = getattr(resp, "status", 200)
            return ProbeResult(True, None, "") if 200 <= status < 400 else ProbeResult(False, None, f"proxy-GET (статус {status})")
        except urllib.error.HTTPError as e:
            # Ответ получен — туннель работает, даже если статус 4xx/5xx.
            return ProbeResult(True, None, "")
        except Exception as e:
            return ProbeResult(False, None, f"proxy-GET ({type(e).__name__})")
    except Exception as e:
        return ProbeResult(False, None, f"proxy-GET (ошибка: {type(e).__name__})")
    finally:
        if proc is not None:
            _kill(proc)
        shutil.rmtree(tmp_dir, ignore_errors=True)
