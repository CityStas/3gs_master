"""Path sandboxing and Roblox project discovery.

Every file tool of this stack goes through `safe_path`: a tool call must never be able to
write outside the project the agent was pointed at, and "the project" is the single
definition in `config.resolve_project` - not whatever `cwd` happens to be.
"""
from __future__ import annotations

import re
from pathlib import Path

from .. import config

# Directories that decide which side of the client-server boundary a script runs on.
SERVER_ROOTS = ("serverscriptservice", "serverstorage", "workspace", "serverpackages")
CLIENT_ROOTS = ("starterplayerscripts", "startercharacterscripts", "startergui",
                "replicatedfirst", "starterpack")
SHARED_ROOTS = ("replicatedstorage", "shared", "common", "packages", "src/shared")


class OutsideProject(ValueError):
    pass


def project_root(explicit: str = "") -> Path:
    return config.resolve_project(explicit)


def safe_path(root: Path, rel: str) -> Path:
    """`root / rel`, refusing anything that escapes `root`.

    Both sides are resolved first, so `..`, a symlink and an absolute path all end up in
    the same comparison. The check is `is_relative_to`, not a string prefix: `/proj` and
    `/proj2` share a prefix and nothing else.
    """
    root = Path(root).resolve()
    raw = (rel or "").strip().strip('"')
    p = Path(raw)
    target = (p if p.is_absolute() else root / p)
    try:
        resolved = target.resolve()
    except OSError as e:
        raise OutsideProject(f"cannot resolve {rel!r}: {e}") from e
    if resolved != root and not resolved.is_relative_to(root):
        raise OutsideProject(
            f"{rel!r} resolves outside the project root {root} - refused. "
            f"All paths are relative to the project.")
    return resolved


def script_context(rel_path: str, text: str = "") -> str:
    """server / client / shared, from the Rojo path first and the file name second.

    A `.client.luau` / `.server.luau` suffix is authoritative (Rojo maps it to
    LocalScript / Script); otherwise the service folder decides; otherwise it is shared.
    """
    parts = [p.lower() for p in Path(rel_path).parts]
    name = parts[-1] if parts else ""
    if name.endswith(".client.luau") or name.endswith(".client.lua"):
        return "client"
    if name.endswith(".server.luau") or name.endswith(".server.lua"):
        return "server"
    for part in parts[:-1]:
        if part in CLIENT_ROOTS:
            return "client"
        if part in SERVER_ROOTS:
            return "server"
        if part in SHARED_ROOTS:
            return "shared"
    return "shared"


def rojo_project(root: Path) -> Path | None:
    """The Rojo project file, if this tree is file-based.

    `default.project.json` is the convention, so it wins outright; any other
    `*.project.json` is accepted as a fallback, shortest name first. Sorting by name alone
    is not enough: `alt.project.json` and `default.project.json` are the same length, and
    the alphabetical winner would be the wrong file.
    """
    try:
        hits = sorted(root.glob("*.project.json"), key=lambda p: (p.name != "default.project.json",
                                                                 len(p.name), p.name))
    except OSError:
        return None
    return hits[0] if hits else None


def place_files(root: Path) -> list[Path]:
    """`.rbxlx` / `.rbxl` / `.rbxm` under the project (binary `.rbxl` is listed, not parsed)."""
    out: list[Path] = []
    for ext in ("*.rbxlx", "*.rbxl", "*.rbxm", "*.rbxmx"):
        try:
            out.extend(p for p in root.rglob(ext) if p.is_file())
        except OSError:
            continue
    return sorted(set(out))


def source_files(root: Path) -> list[Path]:
    """Luau sources of the project, skip-list applied (same rules as the indexer)."""
    out: list[Path] = []
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in {".luau", ".lua"}:
            continue
        try:
            rel_parts = p.relative_to(root).parts
        except ValueError:
            continue
        if any(part in config.PROJECT_SKIP_DIRS for part in rel_parts[:-1]):
            continue
        out.append(p)
    return sorted(out)


RE_ENGINE = re.compile(r'"engine"\s*:\s*"([\w.-]+)"')


def project_engine(root: Path) -> str:
    """`engine.json` when present; otherwise "roblox" - this stack is the Roblox one."""
    try:
        import json
        return json.loads((root / "engine.json").read_text(encoding="utf-8")).get("engine", "roblox")
    except (OSError, ValueError):
        return "roblox"
