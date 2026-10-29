"""Unity project paths, sandboxing and toolchain discovery.

Two rules that everything else depends on:

* every path handed to a tool is normalised and must resolve **inside** the project
  root - absolute paths, `..`, drive letters and UNC are rejected before any I/O;
* the editor and the CLI are discovered once here, so a missing install is a single
  clear message instead of a `FileNotFoundError` in the middle of a task.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

from .. import config


class UnityPathError(ValueError):
    pass


def project_root(project: str | Path = "") -> Path:
    root = config.resolve_project(project)
    if not root.exists():
        raise UnityPathError(f"project directory does not exist: {root}")
    return root


def is_unity_project(root: Path) -> bool:
    return (root / "ProjectSettings" / "ProjectVersion.txt").is_file() or \
           (root / "Assets").is_dir()


def safe_path(project: Path, rel: str) -> Path:
    """Resolve `rel` under `project`, refusing anything that escapes the root."""
    if not rel or not str(rel).strip():
        raise UnityPathError("empty path")
    raw = str(rel).strip().strip('"').replace("\\", "/")
    if re.match(r"^[A-Za-z]:", raw) or raw.startswith("//") or raw.startswith("\\\\"):
        raise UnityPathError(f"absolute paths are not allowed: {rel}")
    p = (project / raw).resolve()
    try:
        p.relative_to(project.resolve())
    except ValueError as e:
        raise UnityPathError(f"path escapes the project root: {rel}") from e
    return p


def rel_to(project: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(project.resolve()).as_posix()
    except ValueError:
        return str(path)


def unity_version_of(root: Path) -> str:
    """`m_EditorVersion` from ProjectSettings/ProjectVersion.txt, or ''."""
    f = root / "ProjectSettings" / "ProjectVersion.txt"
    if not f.is_file():
        return ""
    try:
        m = re.search(r"m_EditorVersion:\s*(\S+)", f.read_text(encoding="utf-8", errors="replace"))
        return m.group(1) if m else ""
    except OSError:
        return ""


def manifest(root: Path) -> dict:
    """Parsed Packages/manifest.json (dependencies map), or {}."""
    import json
    f = root / "Packages" / "manifest.json"
    if not f.is_file():
        return {}
    try:
        return json.loads(f.read_text(encoding="utf-8", errors="replace"))
    except (OSError, ValueError):
        return {}


def editor_log_path() -> Path | None:
    """The live editor log (`%LOCALAPPDATA%\\Unity\\Editor\\Editor.log`).

    On this machine `%LOCALAPPDATA%\\Unity` is a junction to `E:`, so the env path is
    correct even though the bytes live elsewhere.
    """
    local = os.environ.get("LOCALAPPDATA")
    if not local:
        return None
    p = Path(local) / "Unity" / "Editor" / "Editor.log"
    return p if p.is_file() else None


def project_log_paths(root: Path) -> list[Path]:
    out = []
    for rel in ("Logs/AssetImportWorker0.log", "Logs/shadercompiler-UnityShaderCompiler0.log"):
        p = root / rel
        if p.is_file():
            out.append(p)
    return out


def editor_running(root: Path) -> bool:
    """True when an editor instance holds this project (lock file in Temp/)."""
    return (root / "Temp" / "UnityLockfile").exists()


def editor_exe() -> Path:
    exe = config.resolve_unity_editor()
    if not exe:
        raise UnityPathError(
            "Unity.exe not found. Set UNITY_EDITOR, or install an editor under "
            f"{config.UNITY_EDITORS_INSTALL_ROOT}")
    return exe


def cli_exe() -> Path | None:
    return config.resolve_unity_cli()


def list_files(root: Path, subdir: str = "Assets", pattern: str = "*", limit: int = 400) -> list[str]:
    base = safe_path(root, subdir) if subdir else root
    if not base.exists():
        return []
    out: list[str] = []
    for p in sorted(base.rglob(pattern)):
        if p.is_dir():
            continue
        rel_parts = p.relative_to(base).parts[:-1]
        if any(part in config.PROJECT_SKIP_DIRS for part in rel_parts):
            continue
        out.append(rel_to(root, p))
        if len(out) >= limit:
            break
    return out
