# auth_permissions.py
import csv
from pathlib import Path
from typing import Dict

PERMISSIONS_FILE = Path("C:\\MCP\\auth\\user.csv")

USER_PERMISSIONS: Dict[str, dict] = {}
_LAST_MTIME: float | None = None


def _load_permissions() -> None:
    global USER_PERMISSIONS

    with PERMISSIONS_FILE.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        USER_PERMISSIONS = {
            row["username"].strip().lower(): row
            for row in reader
        }


def ensure_permissions_loaded() -> None:
    global _LAST_MTIME

    if not PERMISSIONS_FILE.exists():
        raise RuntimeError("Permissions CSV file not found")

    mtime = PERMISSIONS_FILE.stat().st_mtime

    # First load OR file changed
    if _LAST_MTIME is None or mtime != _LAST_MTIME:
        _load_permissions()
        _LAST_MTIME = mtime


def get_user_permissions(username: str) -> dict | None:
    ensure_permissions_loaded()
    return USER_PERMISSIONS.get(username.lower())


_load_permissions()
def get_user_permissions(username: str) -> dict | None:
    return USER_PERMISSIONS.get(username.lower())


permission = get_user_permissions("ali")
print(permission)