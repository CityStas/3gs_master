"""Path policy: единственная разрешённая область — корень Godot-проекта."""
from __future__ import annotations

import os
import re
from pathlib import Path

from .. import config

_DRIVE_RE = re.compile(r"^[A-Za-z]:[\\/]")
_UNC_RE = re.compile(r"^(\\\\|//)")
_ENV_RE = re.compile(r"%(USERPROFILE|APPDATA|LOCALAPPDATA|PROGRAMDATA|TEMP|TMP|HOMEPATH)%", re.I)


class PathDenied(PermissionError):
    """Путь вне разрешённой области проекта."""


def project_root() -> Path:
    root = config.godot_project_root()
    if root is None:
        raise PathDenied(
            "GODOT-проект не задан. Установи GDM_PROJECT=<путь к папке проекта> "
            "или запусти агента из каталога проекта."
        )
    return root


def is_res_path(p: str) -> bool:
    return p.startswith("res://") or p.startswith("user://")


def normalize(p: str, root: Path | None = None) -> str:
    """Привести вход к относительному POSIX-пути внутри проекта."""
    if not p or not p.strip():
        raise PathDenied("пустой путь")
    raw = p.strip().replace("\\", "/")

    if _ENV_RE.search(raw):
        raise PathDenied(f"переменные окружения в путях запрещены: {p}")
    if _UNC_RE.match(raw):
        raise PathDenied(f"UNC/сетевые пути запрещены: {p}")

    if raw.startswith("res://"):
        raw = raw[len("res://"):]
    elif raw.startswith("user://"):
        raise PathDenied("user:// вне области проекта")

    if _DRIVE_RE.match(raw) or raw.startswith("/"):
        raise PathDenied(
            f"абсолютные пути запрещены, используй res:// или путь относительно проекта: {p}"
        )

    parts: list[str] = []
    for seg in raw.split("/"):
        if seg in ("", "."):
            continue
        if seg == "..":
            if not parts:
                raise PathDenied(f"выход за корень проекта запрещён: {p}")
            parts.pop()
            continue
        parts.append(seg)
    if not parts:
        raise PathDenied(f"некорректный путь: {p}")
    return "/".join(parts)


def resolve(p: str, root: Path | None = None, must_exist: bool = False) -> Path:
    root = (root or project_root()).resolve()
    rel = normalize(p, root)
    target = (root / rel).resolve()
    try:
        target.relative_to(root)
    except ValueError as e:
        raise PathDenied(f"путь выходит за корень проекта: {p}") from e
    if must_exist and not target.exists():
        raise PathDenied(f"файл не найден: res://{rel}")
    return target


def res_path(p: str, root: Path | None = None) -> str:
    return "res://" + normalize(p, root)


def guard_extension(p: str, allowed: set[str]) -> str:
    rel = normalize(p)
    suffix = Path(rel).suffix.lower()
    if suffix not in allowed:
        raise PathDenied(
            f"расширение {suffix or '(нет)'} не разрешено для записи. Разрешены: "
            f"{', '.join(sorted(allowed))}"
        )
    return rel


WRITABLE_EXTS = {
    ".gd", ".tscn", ".tres", ".godot", ".gdshader", ".shader",
    ".json", ".cfg", ".md", ".txt", ".gdshaderinc",
}
