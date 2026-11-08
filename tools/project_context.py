#!/usr/bin/env python
"""The authoritative answer to "which project, which engine, and is that real?".

`project_layout.py` owns the LAYOUT (where projects live). This module owns the DECISION
that every caller needs before it touches a file: the repository root, the active project
as a normalized absolute path, the engine, and *where the engine answer came from*. It
adds the two things the layout resolver deliberately does not do:

1. **It refuses to guess an engine.** `project_layout.normalise_engine()` maps anything
   unknown to `threejs`, because that is the historical default for a folder with no
   marker at all. For a folder that HAS a marker with `{"engine": "godot4"}` that default
   is wrong, and silently wrong: the session gets the Three.js tool surface and the model
   is told nothing. Here an unreadable or unknown marker is an `engine_ambiguous` error
   with the offending file named, not a fallback.

2. **It re-reads the pointer on every call and says whether it is stale.** A pointer is a
   hint, never a fact (tests/test_project_paths.py). `data/active_project.txt` is written
   by the launchers and outlives the project it names.

Nothing here is a second layout: every path comes from `project_layout`.

Usage
-----
    python tools/project_context.py                  # JSON for the active project
    python tools/project_context.py --json           # same, explicit
    python tools/project_context.py my_game          # a bare name or a path
    python tools/project_context.py --shell          # `set` lines for cmd, empty = no project
    python tools/project_context.py --require        # exit 1 when there is no live project

Exit codes: 0 = a live project (or no pointer at all), 1 = stale pointer / ambiguous engine
/ the explicit argument resolves nowhere, 2 = the repository root itself is unusable.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import project_layout  # noqa: E402

KNOWN_ENGINES = tuple(project_layout.PROFILE_BY_ENGINE)


def _pointer_text() -> str:
    try:
        return (ROOT / "data" / "active_project.txt").read_text(encoding="utf-8").strip()
    except OSError:
        return ""


def _read_marker(marker: Path) -> tuple[str | None, str | None]:
    """`(engine, error)` from one engine.json. utf-8-sig: PowerShell writes a BOM."""
    import json as _json

    try:
        data = _json.loads(marker.read_text(encoding="utf-8-sig"))
    except OSError as exc:
        return None, f"cannot read {marker}: {exc}"
    except ValueError as exc:
        return None, f"{marker} is not valid JSON: {exc}"
    if not isinstance(data, dict):
        return None, f"{marker} must contain a JSON object"
    raw = data.get("engine")
    if not isinstance(raw, str) or not raw.strip():
        return None, f"{marker} has no \"engine\" string"
    value = raw.strip().lower()
    value = project_layout.ENGINE_ALIASES.get(value, value)
    if value not in KNOWN_ENGINES:
        return None, (
            f"{marker} declares engine={raw!r}, which is not one of "
            f"{', '.join(KNOWN_ENGINES)}. Fix the marker or move the project under "
            f"projects/<engine>/ - the session will not be given a Three.js tool surface "
            f"for a project that says otherwise."
        )
    return value, None


def resolve(name: str | Path | None = None) -> dict:
    """Full resolution as a plain dict - the one shape every caller and test reads."""
    out: dict = {
        "repo": str(ROOT),
        "requested": "" if name is None else str(name),
        "source": "argument" if name else ("pointer" if _pointer_text() else "none"),
        "project": None,
        "project_rel": None,
        "engine": None,
        "engine_source": None,
        "project_exists": False,
        "pointer_stale": False,
        "engine_ambiguous": None,
        "error": None,
    }

    if name is None:
        raw = _pointer_text()
        if not raw:
            # No pointer is a legitimate state: a plain `pi` session at the repo root.
            out["engine"] = project_layout.DEFAULT_ENGINE
            out["engine_source"] = "default (no pointer)"
            return out
        candidate = Path(raw)
        if not candidate.is_absolute():
            candidate = ROOT / candidate
    else:
        found = project_layout.find_project(name, ROOT)
        if found is None:
            out["error"] = (
                f"no project matches {str(name)!r}: tried the absolute path, the cwd, the "
                f"repo root, and projects/<engine>/<name>. Create it with `dev.cmd {name}`."
            )
            return out
        candidate = found

    candidate = candidate.resolve()
    out["project"] = str(candidate)
    out["project_exists"] = candidate.is_dir()

    if not out["project_exists"]:
        # The pointer names something that is gone. Reported, never resolved into a path
        # that is not on disk - that is the bug tests/test_project_paths.py locks down.
        out["pointer_stale"] = out["source"] == "pointer"
        out["error"] = (
            f"the active project does not exist: {candidate} - it was deleted or renamed. "
            f"Point the system at a live project with `dev.cmd <name>`."
        )
        out["engine"] = None
        return out

    # Nearest marker, walking up to the repo root: projects/<engine>/engine.json is the
    # folder-level default, <project>/engine.json overrides it. Same rule as
    # project_layout.nearest_engine, but that one swallows a broken marker into the
    # threejs default, which is the silent misroute this function exists to prevent.
    here = candidate
    while True:
        marker = here / "engine.json"
        if marker.is_file():
            engine, err = _read_marker(marker)
            if err:
                out["engine_ambiguous"] = err
                out["error"] = err
                return out
            out["engine"] = engine
            out["engine_source"] = project_layout.repo_rel(marker)
            break
        if here == ROOT or here.parent == here:
            break
        here = here.parent

    if out["engine"] is None:
        out["engine"] = project_layout.DEFAULT_ENGINE
        out["engine_source"] = "default (no engine.json up to the repo root)"
    out["project_rel"] = project_layout.repo_rel(candidate)
    out["profile"] = str(project_layout.profile_for(out["engine"]))
    return out


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Resolve the active project and engine.")
    ap.add_argument("name", nargs="?", default=None, help="bare project name or path")
    ap.add_argument("--json", action="store_true", help="machine-readable output (default)")
    ap.add_argument("--shell", action="store_true", help="`set` lines for cmd.exe")
    ap.add_argument("--require", action="store_true", help="fail when there is no live project")
    a = ap.parse_args(argv[1:])

    info = resolve(a.name)

    if a.shell:
        if info["project"] and info["project_exists"] and not info["engine_ambiguous"]:
            print(f'set "GS_PROJECT={info["project"]}"')
            print(f'set "GS_ENGINE={info["engine"]}"')
            print(f'set "GS_ENGINE_SOURCE={info["engine_source"]}"')
        else:
            print('set "GS_PROJECT="')
            print('set "GS_ENGINE="')
            print('set "GS_ENGINE_SOURCE="')
    else:
        # JSON is the default, not an opt-in: the callers that need a shell snippet are
        # the exception, and a resolver that prints nothing unless asked is a trap.
        print(json.dumps(info, indent=2, ensure_ascii=False))

    if info["error"]:
        print(info["error"], file=sys.stderr)
        return 1
    if a.require and not info["project"]:
        print("no live project: data/active_project.txt is empty or absent", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
