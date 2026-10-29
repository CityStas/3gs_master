#!/usr/bin/env python
"""Unity gate for one project: static lint, then an optional real compile.

Two layers, one verdict - the same shape as the Three.js `check.cmd`
(`tscheck.py` + `pagecheck.py`) and for the same reason: the cheap layer catches what a
regex can see, the expensive layer catches what only the engine can.

  lint      (always, seconds)   `unimaster.unity.lint` over every `.cs` in `Assets/`.
                                Catches Unity 5/6 API traps that *compile fine* and fail
                                at runtime - `Rigidbody.velocity` renamed to
                                `linearVelocity`, `GameObject.FindObjectsOfType`,
                                `Component.rigidbody`, `WWW`, UnityScript-era
                                `GetComponent("Name")`. A compiler is blind to all of
                                them, and a 9B model writes them from memory constantly.

  compile   (--compile, minutes) `Unity.exe -batchmode -nographics -quit` and then the
                                `error CS####:` lines from the log. This is the only
                                thing that actually proves the C# is valid: the editor
                                *is* the compiler, and there is no standalone `csc`
                                invocation that sees the project's assemblies.

The exit code is 1 when either layer finds an **error**. Warnings alone exit 0 - the
lint deliberately separates them (see `lint.py`) so that `linearVelocity` advice does not
redden a build that is in fact fine.

    python unity/tools/check.py                       # lint the active project
    python unity/tools/check.py my_game               # lint a named project
    python unity/tools/check.py --compile             # lint + batch compile
    python unity/tools/check.py --json                # machine-readable
    python unity/tools/check.py --only Assets/Scripts
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "unity"))

from unimaster import config  # noqa: E402
from unimaster.unity import batch, lint, paths  # noqa: E402


def _lint_project(root: Path, subdir: str, limit: int) -> tuple[list, list, int]:
    """Lint every `.cs` under `subdir`. Returns (errors, warnings, files_scanned).

    `root` is passed down as `project` so the project-aware rule fires: when
    `ProjectSettings.asset` says `activeInputHandler: 1` (new Input System only), every
    `UnityEngine.Input.*` call is an error rather than an advisory.
    """
    base = paths.safe_path(root, subdir) if subdir else root
    if not base.exists():
        return [], [], 0
    errs, warns, n = [], [], 0
    for f in sorted(base.rglob("*.cs")):
        parts = f.relative_to(root).parts[:-1]
        if any(p in config.PROJECT_SKIP_DIRS for p in parts):
            continue
        n += 1
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        rel = paths.rel_to(root, f)
        for finding in lint.lint_csharp(text, rel, root):
            (errs if finding.severity == "error" else warns).append(finding)
    return errs[:limit], warns[:limit], n


def main() -> int:
    ap = argparse.ArgumentParser(description="Lint (and optionally compile) a Unity project.")
    ap.add_argument("project", nargs="?", default="",
                    help="project name under projects/games/, or a path "
                         "(default: the active project from <repo>/data/active_project.txt)")
    ap.add_argument("--only", default="Assets", help="subdirectory to lint (default Assets)")
    ap.add_argument("--compile", action="store_true",
                    help="also run a batch-mode Unity compile (editor must be closed)")
    ap.add_argument("--timeout", type=int, default=900, help="compile timeout, seconds")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--limit", type=int, default=200, help="max findings to print per class")
    a = ap.parse_args()

    try:
        root = config.resolve_project(a.project)
    except ValueError as e:
        print(f"[check] {e}", file=sys.stderr)
        return 2

    payload: dict = {"project": str(root)}

    if not paths.is_unity_project(root):
        print(f"[check] {root} is not a Unity project "
              f"(no ProjectSettings/ProjectVersion.txt and no Assets/)", file=sys.stderr)
        return 2

    errs, warns, scanned = _lint_project(root, a.only, a.limit)
    payload["lint"] = {
        "files": scanned,
        "error_count": len(errs),
        "warning_count": len(warns),
        "errors": [f.to_dict() for f in errs],
        "warnings": [f.to_dict() for f in warns],
    }

    if a.compile:
        res = batch.compile_project(root, timeout=a.timeout)
        payload["compile"] = res.to_dict()

    # Verdict: lint errors, or a compile that did not pass. Warnings never fail.
    lint_failed = bool(errs)
    compile_failed = bool(a.compile and not payload["compile"]["ok"])
    rc = 1 if (lint_failed or compile_failed) else 0
    payload["ok"] = rc == 0
    payload["engine"] = "unity"
    payload["unity_version"] = paths.unity_version_of(root)

    if a.json:
        print(json.dumps(payload, ensure_ascii=False, indent=1))
        return rc

    print(f"[check] project {root}")
    ver = payload["unity_version"] or "(version unknown)"
    print(f"[check] unity   {ver}")
    print(f"[check] lint    {scanned} .cs files scanned, "
          f"{len(errs)} error(s), {len(warns)} warning(s)")
    for f in errs:
        print(f"  [ERR ] {f.script}:{f.line}  {f.code}  {f.message}")
        if f.fix:
            print(f"          fix: {f.fix}")
    for f in warns:
        print(f"  [WARN] {f.script}:{f.line}  {f.code}  {f.message}")

    if a.compile:
        c = payload["compile"]
        print(f"[check] compile exit={c['exit_code']} in {c['seconds']}s - "
              f"{c['error_count']} error(s), {c['warning_count']} warning(s)")
        if c.get("reason"):
            print(f"  reason: {c['reason']}")
        for e in c["errors"][:40]:
            print(f"  [ERR ] {e['file']}({e['line']}): {e['code']} {e['message']}")
        if not c["ok"] and c.get("log"):
            print(f"  log: {c['log']}")

    print()
    print("== ОК ==" if rc == 0 else "== ЕСТЬ ОШИБКИ ==")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
