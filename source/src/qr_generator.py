import os
import io
from src.config import GITHUBMIRROR_DIR, QRCODES_DIR, LAST_FILE_INDEX, build_raw_file_url
from src.logger import log

# -------------------- QR-КОДЫ ПОДПИСОК --------------------
# Каждый QR содержит прямую ссылку на файл подписки (githubmirror/N.txt),
# поэтому импорт в клиент всегда тянет свежие конфиги.

def _make_qr_png(url: str) -> bytes:
    import qrcode
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def generate_qr_codes() -> list[int]:
    """Генерирует qr-codes/N.png для всех файлов подписок 1..LAST_FILE_INDEX.
    Возвращает список индексов, для которых PNG изменился."""
    os.makedirs(QRCODES_DIR, exist_ok=True)
    changed: list[int] = []
    for file_index in range(1, LAST_FILE_INDEX + 1):
        txt_path = os.path.join(GITHUBMIRROR_DIR, f"{file_index}.txt")
        if not os.path.exists(txt_path):
            log(f"ℹ️ QR: пропуск {file_index}.png — файла подписки ещё нет")
            continue
        url = build_raw_file_url(file_index)
        png_path = os.path.join(QRCODES_DIR, f"{file_index}.png")
        try:
            data = _make_qr_png(url)
        except Exception as e:
            log(f"⚠️ Ошибка генерации QR {file_index}.png: {e}")
            continue
        old = None
        if os.path.exists(png_path):
            try:
                with open(png_path, "rb") as f:
                    old = f.read()
            except Exception:
                old = None
        if old == data:
            continue
        with open(png_path, "wb") as f:
            f.write(data)
        changed.append(file_index)
    if changed:
        log(f"🔳 Обновлены QR-коды: {', '.join(f'{i}.png' for i in changed)}")
    else:
        log(f"🔳 QR-коды 1..{LAST_FILE_INDEX} без изменений")
    return changed
