#!/usr/bin/env python
"""Run an asset pack from the command line - the same scheduler the agent uses.

    python tools/generate.py --status
    python tools/generate.py --project projects/games/my_game --jobs plan.json
    python tools/generate.py --project projects/games/my_game --jobs plan.json --json

`cmd/gen.cmd` at the repo root is a thin wrapper around this, with the venv and the
proxy bypass already set. Both paths take the same lock, so a hand-run pack and an
agent-run pack cannot overlap.

A plan file is either a bare array of jobs or `{"jobs": [...]}`; see
`assets/pack.example.json` for every field.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from threejs import config  # noqa: E402
from threejs.assets.hardware import DETACHED  # noqa: E402
from threejs.assets.scheduler import GenerationScheduler  # noqa: E402


def _mb(value) -> str:
    return f"{value / 1048576:.1f} MB" if isinstance(value, int) else "?"


def _detach(argv: list[str], log_path: Path) -> int:
    """Re-launch this script as a detached process and return its pid.

    A pack is long - the 3D tiers run for 15-20 minutes - and a process started from a
    tool call dies with the caller's shell. That cost a full `spore-shroom` mesh once:
    the run was killed at 7/12 of the shape sampler, `generate.log` simply stopped after
    `job_begin` with no `job_end` and `error: None`. Detaching puts the pack in its own
    process group with no console, the same way `sd.py`/`comfy.py` start their servers,
    so it outlives whatever started it.
    """
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, "ab") as log:
        proc = subprocess.Popen(
            [sys.executable, str(Path(__file__).resolve()), *argv],
            stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT,
            cwd=str(ROOT), creationflags=DETACHED, close_fds=True,
        )
    return proc.pid


def _vram_line(tag: str, reading: dict) -> str:
    if not reading:
        return f"  {tag:<7}: nvidia-smi unavailable"
    return (f"  {tag:<7}: {reading.get('used_mb')} MiB used / "
            f"{reading.get('free_mb')} MiB free of {reading.get('total_mb')} MiB")


def show_status(scheduler: GenerationScheduler) -> int:
    s = scheduler.status()
    llm, comfy, sd, lock = s["llm"], s["comfy"], s["sd"], s["lock"]
    llm_pid = f"  pid {llm['pid']}" if llm.get("pid") else ""
    comfy_free = comfy.get("vram_free_mb")
    comfy_pid = f"  vram_free {comfy_free} MiB" if comfy_free is not None else ""
    sd_pid = f"  pid {sd['pid']}" if sd.get("pid") else ""
    sd_used = (sd.get("vram") or {}).get("used_mb")
    sd_extra = f"  vram {sd_used} MiB" if sd_used is not None else ""
    packs = comfy.get("custom_nodes")

    print("3GS_Master - GPU arbitration")
    print(f"  invariant  : {s['invariant']}")
    print(f"  llm  :8080 : {'UP' if llm['alive'] else 'down'}{llm_pid}")
    print(f"  zimg :8687 : {'UP' if sd.get('alive') else 'down'}{sd_pid}{sd_extra}"
          f"   (default image engine)")
    print(f"  comfy:8188 : {'UP' if comfy.get('alive') else 'down'}{comfy_pid}")
    if packs is not None:
        shown = packs if isinstance(packs, str) else (", ".join(packs) or "none")
        print(f"  packs      : {shown}")
    print(_vram_line("vram", s["vram"]))
    if lock:
        import time as _t
        since = _t.strftime("%H:%M:%S", _t.localtime(lock.get("t") or 0))
        print(f"  lock       : HELD by pid {lock.get('pid')} since {since}")
    else:
        print("  lock       : free")
    resident = [n for n, up in (("llm", llm["alive"]), ("z-image", sd.get("alive")),
                                ("comfy", comfy.get("alive"))) if up]
    if len(resident) > 1:
        print()
        print(f"  WARNING: {' and '.join(resident)} are resident at once - generation will be slow.")
        print("  Use asset_generate_pack / cmd/gen.cmd instead of starting a backend by hand.")
    print(f"  log        : {s['log']}")
    return 0


def show_report(report: dict, project: Path) -> None:
    print()
    print(f"  jobs      : {len(report['jobs'])}  in {report['total_s']}s")
    for row in report["jobs"]:
        mark = "ok  " if row["ok"] else "FAIL"
        print(f"    [{mark}] {row['name']:<24} {row['kind']:<6} {row['s']:>8.1f}s  "
              f"{len(row['files'])} file(s)")
        if row["error"]:
            print(f"           {row['error']}")

    files = report.get("files") or []
    if files:
        print()
        print("  files -> project")
        for f in files:
            url = f"   {f['url']}" if f.get("url") else ""
            print(f"    {f['rel'] or f['path']:<52} {_mb(f['bytes']):>9}"
                  f"{'  (overwrote)' if f['overwrote'] else ''}{url}")

    llm, comfy, vram = report["llm"], report["comfy"], report["vram"]
    print()
    print("  gpu")
    if not llm["was_up"]:
        print("  llm    : was not running - nothing to restore")
    elif llm.get("restored"):
        print(f"  llm    : stopped, restored{' (already up)' if not llm.get('started') else ''}")
    else:
        print(f"  llm    : NOT RESTORED - {llm.get('error')}")
        print(f"           {llm.get('hint', '')}")
    print(f"  comfy  : {(comfy.get('stopped') or {}).get('stopped') and 'stopped' or 'see log'}")
    sd = report.get("sd") or {}
    if sd:
        print(f"  z-image: {(sd.get('stopped') or {}).get('stopped') and 'stopped' or 'see log'}")
    switches = report.get("engine_switches")
    if switches is not None:
        print(f"  engines: {switches} backend switch(es) during the run")
    print(_vram_line("before", vram.get("before") or {}))
    print(_vram_line("during", vram.get("during") or {}))
    print(_vram_line("after", vram.get("after") or {}))
    if report.get("staging"):
        print(f"  staging: {report['staging']}  (kept for inspection)")
    print()
    print(f"  result : {'OK' if report['ok'] else 'FAILED'}")
    if report.get("error"):
        print(f"           {report['error']}")
    if report.get("failed"):
        print(f"           failed jobs: {', '.join(report['failed'])}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Serialised asset generation for 3GS_Master.")
    ap.add_argument("--project", "-p", default="", help="project directory, or a name under projects/games/")
    ap.add_argument("--jobs", "-j", default="", help="JSON plan file (array of jobs)")
    ap.add_argument("--status", action="store_true", help="report GPU ownership and exit")
    ap.add_argument("--keep-comfy", action="store_true",
                    help="leave ComfyUI running afterwards (it will fight the LLM for the card)")
    ap.add_argument("--no-stop-llm", action="store_true",
                    help="do not stop the language model - loses the whole speed-up")
    ap.add_argument("--json", action="store_true", help="print the raw report")
    ap.add_argument("--detach", action="store_true",
                    help="re-launch as a detached process and return immediately - "
                         "use this for any pack with a 3D job, otherwise the run dies "
                         "with the shell that started it")
    a = ap.parse_args()

    if a.detach:
        if not a.jobs:
            print("[ERROR] --detach needs --jobs (there is nothing to detach)")
            return 1
        argv = [x for x in sys.argv[1:] if x != "--detach"]
        log_path = config.LOGS_DIR / f"generate-{Path(a.jobs).stem}.log"
        pid = _detach(argv, log_path)
        print(f"3GS_Master - detached asset generation\n"
              f"  pid     : {pid}\n"
              f"  plan    : {a.jobs}\n"
              f"  log     : {log_path}\n"
              f"  status  : {config.GEN_STATUS_FILE}\n"
              f"  lock    : {config.GEN_LOCK_FILE}\n\n"
              f"Follow it with:  tools/generate.py --status   (or watch the log above)")
        return 0

    scheduler = GenerationScheduler()
    if a.status or not a.jobs:
        if not a.status and not a.jobs:
            print("No --jobs given, showing status. Use --jobs plan.json to generate.\n")
        return show_status(scheduler)

    plan_path = Path(a.jobs)
    if not plan_path.is_absolute():
        plan_path = (Path.cwd() / plan_path).resolve()
    if not plan_path.exists():
        print(f"[ERROR] plan file not found: {plan_path}")
        return 1
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    jobs = plan.get("jobs", []) if isinstance(plan, dict) else plan
    project = a.project or (plan.get("project") if isinstance(plan, dict) else "") or ""

    resolved = config.resolve_project(project)
    print("3GS_Master - serialised asset generation")
    print(f"  project : {resolved}")
    print(f"  plan    : {plan_path}  ({len(jobs)} job(s))")
    print(f"  mode    : LLM {'kept resident (slow)' if a.no_stop_llm else 'stopped for the run'}, "
          f"ComfyUI {'left running' if a.keep_comfy else 'stopped afterwards'}")

    report = scheduler.generate_pack(project, jobs, stop_llm=not a.no_stop_llm,
                                     keep_comfy=a.keep_comfy)
    if a.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        show_report(report, resolved)
    return 0 if report.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
