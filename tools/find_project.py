#!/usr/bin/env python
"""One CLI the .cmd launchers can call: name or path -> project directory.

`agent.cmd three/test_space`, `dev.cmd skateshop`, `studio.cmd my_game` all mean
"the project called X", but only the Python stacks knew how to resolve that
(absolute -> cwd -> repo root -> `projects/<engine>/<name>`). Batch cannot
reproduce those rules without drifting from them, so it calls this instead - the
same `project_layout.find_project` the stacks use.

    python tools/find_project.py skateshop            # -> projects/roblox/skateshop
    python tools/find_project.py three/test_space     # -> projects/three/test_space
    python tools/find_project.py newgame --create     # mkdir, then print the path
    python tools/find_project.py --engine skateshop   # -> roblox (no path)

Prints the path RELATIVE to the repo root with forward slashes, which is what
`data/active_project.txt` holds and what `resolve_project` reads back.
Exit codes: 0 = found/created, 1 = not found (or creation failed).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from project_layout import (  # noqa: E402
    default_project_parent,
    engine_of_dir,
    find_project,
    nearest_engine,
    repo_rel,
)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="resolve a project name to a directory")
    ap.add_argument("name", help="bare name, relative path, or absolute path")
    ap.add_argument("--create", action="store_true",
                    help="create the directory when it does not exist yet")
    ap.add_argument("--engine", action="store_true",
                    help="print the engine of the resolved project instead of its path")
    ap.add_argument("--engine-name", metavar="NAME",
                    help="engine for --create when cwd does not say (threejs/godot/unity/roblox)")
    a = ap.parse_args(argv[1:])

    dst = find_project(a.name, REPO)

    if dst is None and a.create:
        raw = Path(a.name)
        # The engine decides the folder: `dev.cmd my_game` from the repo root lands
        # in `projects/three/my_game` unless you are standing in another engine's
        # folder (then that one wins). `--engine godot` overrides the guess.
        guessed = a.engine_name or nearest_engine(Path.cwd(), REPO)[1]
        parent = default_project_parent(Path.cwd(), REPO, guessed) \
            if raw.parent == Path(".") else (REPO / raw).parent
        dst = (parent / raw.name).resolve()
        try:
            dst.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            print(f"[find_project] cannot create {dst}: {exc}", file=sys.stderr)
            return 1

    if dst is None:
        print(f"[find_project] no project named {a.name!r}: tried cwd, the repo root "
              f"and projects/<engine>/", file=sys.stderr)
        return 1

    if a.engine:
        _, engine = nearest_engine(dst, REPO)
        if engine is None:
            engine = engine_of_dir(dst) or "threejs"
        print(engine)
        return 0

    print(repo_rel(dst))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
