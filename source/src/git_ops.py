import subprocess
import os
from src.config import GITHUBMIRROR_DIR, README_PATH, GIT_ROOT, QRCODES_DIR
from src.logger import log, offset

# -------------------- GIT --------------------

def _target_branch() -> str:
    """Ветка для пуша: из CI-переменных, иначе текущая ветка, иначе main."""
    for var in ("GITHUB_REF_NAME", "CI_COMMIT_BRANCH"):
        val = os.environ.get(var)
        if val:
            return val
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, cwd=GIT_ROOT,
        )
        name = out.stdout.strip()
        if out.returncode == 0 and name and name != "HEAD":
            return name
    except Exception:
        pass
    return "main"


def git_commit_and_push(dry_run: bool = False):
    """Добавляет изменённые файлы в индекс, делает коммит и пушит."""
    try:
        paths = [
            os.path.relpath(GITHUBMIRROR_DIR, GIT_ROOT),
            os.path.relpath(QRCODES_DIR, GIT_ROOT),
        ]
        if os.path.exists(README_PATH):
            paths.append(os.path.relpath(README_PATH, GIT_ROOT))
        subprocess.run(
            ["git", "add", *paths],
            check=True,
            cwd=GIT_ROOT,
        )

        diff = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=GIT_ROOT,
        )
        if diff.returncode == 0:
            log("ℹ️ Нет изменений для коммита")
            return

        subprocess.run(
            ["git", "commit", "-m", f"🚀 Автообновление репозитория: {offset}"],
            check=True,
            cwd=GIT_ROOT,
        )
        log("✅ Коммит создан")

        if dry_run:
            log("ℹ️ Dry-run: push пропущен")
            return

        subprocess.run(["git", "push", "origin", f"HEAD:{_target_branch()}"], check=True, cwd=GIT_ROOT)
        log("✅ Изменения запушены в репозиторий")

    except subprocess.CalledProcessError as e:
        log(f"❌ Ошибка git: {e}")
        raise
