#!/usr/bin/env python
"""Resolve the active project - one CLI, one set of rules, for the launchers.

`agent.cmd` re-reads `data/active_project.txt` when it is given no argument and then writes
it straight back, so a project deleted since the last run would be resurrected on every
launch. The launcher needs to know that BEFORE it writes.

The check lives here rather than in batch on purpose. The resolution rules (absolute path,
repo-relative path, bare name under `projects/games/`, stale pointer -> error) are already
owned by the three stacks via `resolve_project`; re-implementing them in `cmd` would drift
from them, and drift is exactly how the stacks came to disagree about the pointer file.

    python tools/active_project.py            # validate the pointer file
    python tools/active_project.py <name|path>  # validate an explicit argument

Exit codes:  0 = resolves to a live directory (the path goes to stdout)
             1 = the pointer is stale or absent, or the argument resolves nowhere
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from threejs import config  # noqa: E402


def main(argv: list[str]) -> int:
    explicit = argv[1] if len(argv) > 1 else ""
    try:
        root = config.resolve_project(explicit)
    except ValueError as exc:
        # The resolver already words this well and names the dead path; pass it through.
        print(exc, file=sys.stderr)
        return 1

    # Reaching here with a missing directory means the caller named something that is not
    # there. For the POINTER that is the stale case, and the resolver has already rejected
    # it above; this branch catches an explicit argument that resolves nowhere.
    if not root.is_dir():
        print(
            "the active project does not exist: %s - the project was deleted or renamed. "
            "Point the system at a live project with `dev.cmd <name>`." % root,
            file=sys.stderr,
        )
        return 1

    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
