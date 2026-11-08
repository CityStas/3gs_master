#!/usr/bin/env python
"""The ONE place that knows where projects live and which engine one belongs to.

Layout since 2026-11-08::

    projects/<engine>/<project>/engine.json

    projects/three/<name>      engine=threejs
    projects/godot/<name>      engine=godot
    projects/unity/<name>      engine=unity
    projects/roblox/<name>     engine=roblox

Each `<engine>` folder carries its own `engine.json`, so a project that forgets
one still inherits the right engine from its parent. There is exactly ONE layout:
`projects/<engine>/<name>`. Nothing else is searched - a second, "legacy" parent
would be a second source of truth, and the one thing worse than a wrong path is a
path that resolves in two places and disagrees between the launcher and the stack.

Four stacks need this (threejs, gdmaster, unimaster, rbxmaster) and they all
used to hardcode `projects/games`. Keeping the rules here means a layout change
is one edit, and every caller - launchers, MCP servers, `pi` shim - agrees.

Import from a stack config with the repo root on `sys.path`:

    import sys; sys.path.insert(0, str(REPO_ROOT))
    from project_layout import engine_project_parents, find_project, profile_for

Nothing in here imports a stack, so there is no cycle.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

#: Repo root, derived from this file. Never from cwd - `pi` runs inside a project.
REPO = Path(__file__).resolve().parent

#: Folders under `projects/` that hold projects of one engine.
ENGINE_FOLDERS = ("three", "godot", "unity", "roblox")

#: `engine` value -> pi profile directory (agent dir, holds SYSTEM.md/skills/mcp.json).
PROFILE_BY_ENGINE = {
    "threejs": "pi-home-three",
    "godot": "pi-home-godot",
    "unity": "pi-home-unity",
    "roblox": "pi-home-roblox",
}

#: `three` is an alias for `threejs` (folder name vs engine name).
ENGINE_ALIASES = {"three": "threejs", "threejs": "threejs"}

#: Default when a project declares nothing and no parent declares anything.
DEFAULT_ENGINE = "threejs"


def projects_dir(root: Path | None = None) -> Path:
    return (root or REPO) / "projects"


def normalise_engine(value: str | None) -> str:
    """`three` -> `threejs`; anything unknown -> threejs (the historical default)."""
    if not value:
        return DEFAULT_ENGINE
    raw = str(value).strip().lower()
    return ENGINE_ALIASES.get(raw, raw if raw in PROFILE_BY_ENGINE else DEFAULT_ENGINE)


def engine_of_dir(path: Path) -> str | None:
    """`engine` from `<path>/engine.json`, or None when the marker is absent/broken.

    utf-8-sig: PowerShell 5.1 `Set-Content -Encoding utf8` writes a BOM and plain
    json.load rejects it - the engine would silently fall back to threejs.
    """
    marker = Path(path) / "engine.json"
    if not marker.is_file():
        return None
    try:
        data = json.loads(marker.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError):
        return None
    if not isinstance(data, dict):
        return None
    value = data.get("engine")
    return normalise_engine(value) if value else None


def nearest_engine(start: Path | str | None = None,
                   root: Path | None = None) -> tuple[Path | None, str | None]:
    """Walk UP from `start` to the repo root and return `(marker_dir, engine)`.

    This is what makes `pi` inside `projects/three/my_game/src/` still pick the
    threejs profile: `my_game/engine.json` is optional, `projects/three/engine.json`
    is the folder-level default.

    The walk stops at the repo root on purpose. A stray `engine.json` above the
    repository (or in another checkout) must never steer a session.
    """
    root = (root or REPO).resolve()
    here = Path(start or os.getcwd()).resolve()
    try:
        here.relative_to(root)
    except ValueError:
        return None, None
    while True:
        engine = engine_of_dir(here)
        if engine:
            return here, engine
        if here == root:
            return None, None
        parent = here.parent
        if parent == here:  # drive root, defensive
            return None, None
        here = parent


def engine_project_parents(root: Path | None = None,
                           prefer: str | None = None) -> list[Path]:
    """Existing `projects/<engine>` folders - the parents a bare name is searched in.

    A folder counts when it exists and its name is a known engine folder, whether
    or not it carries `engine.json` (a fresh `projects/roblox` without the marker
    is still the right parent for a roblox project).

    `prefer` (an engine name) puts that folder first, so `unimaster` resolves
    `my_game` to `projects/unity/my_game` even when a same-named folder exists
    under `projects/three`. Without it the order is alphabetical, which is
    stable but arbitrary.
    """
    base = projects_dir(root)
    out: list[Path] = []
    if not base.is_dir():
        return out
    for entry in sorted(base.iterdir()):
        if entry.is_dir() and entry.name.lower() in ENGINE_FOLDERS:
            out.append(entry)
    if prefer:
        want = engine_folder(prefer)
        out.sort(key=lambda d: d.name.lower() != want)
    return out


def project_search_dirs(root: Path | None = None) -> list[Path]:
    """Parents tried for a bare project name, in order: `projects/<engine>/` only."""
    return engine_project_parents(root)


def find_project(name: str | Path, root: Path | None = None) -> Path | None:
    """Resolve a bare name or a relative path to an existing project directory.

    Order: absolute path -> cwd -> repo root -> `projects/<engine>/<name>`.
    `is_dir`, not `exists`: a file carrying the project's name must not be mistaken
    for the project.
    """
    raw = str(name or "").strip().strip('"')
    if not raw:
        return None
    p = Path(raw).expanduser()
    if p.is_absolute():
        return p.resolve() if p.is_dir() else None
    base = (root or REPO).resolve()
    # `projects/three/x` written from the repo root, and `three/x` written as a
    # shorthand for it - both mean the same folder.
    for candidate in (Path.cwd() / p, base / p, base / "projects" / p,
                      *(d / p for d in project_search_dirs(root))):
        if candidate.is_dir():
            return candidate.resolve()
    return None


def default_project_parent(cwd: Path | str | None = None,
                           root: Path | None = None,
                           engine: str | None = None,
                           fallback: Path | None = None) -> Path:
    """Where a NEW project of an explicit bare name should be created.

    Inside `projects/<engine>/` that folder wins - create the project where the user
    is standing. Anywhere else the folder of the caller's own engine does, so
    `dev.cmd my_game` from the repo root lands in `projects/three/my_game`, not in
    some shared `projects/games` that no engine owns.

    `engine` is the caller's stack (threejs/godot/unity/roblox). `fallback` exists
    for a `THREE_GAMES_DIR`-style override and for tests that redirect the tree.
    """
    root = (root or REPO).resolve()
    here = Path(cwd or os.getcwd()).resolve()
    default = root / "projects" / engine_folder(engine)
    fallback_path = Path(fallback) if fallback is not None else default
    try:
        rel = here.relative_to(root)
    except ValueError:
        return fallback_path
    parts = rel.parts
    if len(parts) >= 2 and parts[0] == "projects" and parts[1].lower() in ENGINE_FOLDERS:
        return root / "projects" / parts[1]
    return fallback_path


def profile_for(engine: str | None) -> Path:
    """Absolute pi agent dir for an engine (`pi-home-three`, ...)."""
    return REPO / PROFILE_BY_ENGINE[normalise_engine(engine)]


def repo_rel(path: Path | str) -> str:
    """Path as the pointer file stores it: relative to the repo root, POSIX slashes."""
    p = Path(path).resolve()
    try:
        return p.relative_to(REPO).as_posix()
    except ValueError:
        return p.as_posix()


def engine_folder(engine: str | None) -> str:
    """`threejs` -> `three` (folder name under `projects/`)."""
    eng = normalise_engine(engine)
    return "three" if eng == "threejs" else eng
