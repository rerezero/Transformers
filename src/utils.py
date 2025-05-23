import sys
from pathlib import Path

def read_text(src: str | None) -> str:
    """
    src=None → stdin-оос уншина.
    src=зам   → файл уншина.
    """
    if src is None:
        return sys.stdin.read()
    p = Path(src)
    if not p.exists():
        raise FileNotFoundError(f"{p} олдсонгүй.")
    return p.read_text(encoding="utf-8")
