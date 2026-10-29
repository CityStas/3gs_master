#!/usr/bin/env python
"""Compare local GGUF models on the 2D-level autotest - one server at a time.

Why a separate script. `level_autotest.py --live` scores whatever is already on
`:8080`; this drives the *swap*: start llama-server with model A, run the harness, stop
it, repeat for B and C. The three candidates are the project's Qwen3.5 9B (33 blocks with
an MTP head) and two 32-block Qwen3.5 derivations that live outside the repo.

The comparison is deliberately mechanical: the same tasks, the same linter, the same
scoring as the harness. It reports pass rate, per-task seconds and the exact linter
errors, so "which model is better" is a diff, not an opinion.

    python tools/compare_models.py                       # all three, 1 run each
    python tools/compare_models.py --runs 2              # repeat for stability
    python tools/compare_models.py --only ornith         # substring match on the name
    python tools/compare_models.py --thinking            # leave thinking ON (default: OFF)
    python tools/compare_models.py --port 8080

It OWNS the server lifecycle: it starts and stops `llama-server.exe` itself and never
leaves one behind. Requires the same 8 GB card, so it refuses to run if `:8080` is
already answering (that server is someone else's - stop it first).
"""
from __future__ import annotations

import argparse
import json
import os
import signal
import subprocess
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


@dataclass
class Candidate:
    key: str
    label: str
    gguf: Path


CANDIDATES: tuple[Candidate, ...] = (
    Candidate(
        "qwen35-9b",
        "Qwen3.5 9B Q4_K_M (project, 33 blocks + MTP)",
        ROOT / "models" / "Qwen_Qwen3.5-9B-Q4_K_M.gguf",
    ),
    Candidate(
        "deepseek-v4-flash",
        "Qwen3.5 9B DeepSeek-V4-Flash Q4_K_M (32 blocks, no MTP)",
        Path(r"E:\Programs\LocalLLM\Models\deepseek"
             r"\Qwen3.5-9B-DeepSeek-V4-Flash-Q4_K_M"
             r"\Qwen3.5-9B-DeepSeek-V4-Flash-Q4_K_M.gguf"),
    ),
    Candidate(
        "ornith",
        "Ornith 1.5 9B CRACK Q4_K_M (32 blocks, no MTP)",
        Path(r"E:\Programs\LocalLLM\Models\deq"
             r"\Ornith-1.5-9B-CRACK-Q4_K_M"
             r"\Ornith-1.5-9B-CRACK-Q4_K_M.gguf"),
    ),
)

LLAMA = ROOT / "bin" / "llama" / "llama-server.exe"


def health(port: int, timeout: float = 1.5) -> bool:
    try:
        req = urllib.request.Request(f"http://127.0.0.1:{port}/health",
                                     headers={"User-Agent": "cmp"})
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open(req, timeout=timeout):
            return True
    except (urllib.error.URLError, OSError):
        return False


def start_server(model: Path, alias: str, port: int, ctx: int) -> subprocess.Popen:
    log = ROOT / "logs" / f"cmp-{alias}.log"
    log.parent.mkdir(parents=True, exist_ok=True)
    fh = open(log, "w", encoding="utf-8")
    cmd = [
        str(LLAMA), "-m", str(model), "--alias", alias,
        "--host", "127.0.0.1", "--port", str(port),
        "--jinja", "-c", str(ctx), "-ngl", "999", "-fa", "on", "-np", "1", "--no-webui",
        "--cache-type-k", "q8_0", "--cache-type-v", "q8_0",
        "--temp", "0.6", "--top-p", "0.95", "--top-k", "20",
    ]
    env = dict(os.environ)
    env["NO_PROXY"] = "127.0.0.1,localhost,::1"
    return subprocess.Popen(cmd, stdout=fh, stderr=subprocess.STDOUT, env=env,
                            cwd=str(ROOT))


def wait_up(port: int, seconds: float = 120.0) -> bool:
    t0 = time.time()
    while time.time() - t0 < seconds:
        if health(port):
            return True
        time.sleep(1.0)
    return False


def stop_server(proc: subprocess.Popen) -> None:
    try:
        proc.send_signal(signal.SIGINT)
    except Exception:
        pass
    try:
        proc.wait(timeout=15)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait(timeout=5)


def run_harness(alias: str, thinking: bool) -> list[dict]:
    """Call the already-running server through the harness, capture per-task results."""
    sys.argv = ["level_autotest", "--live", "--model", alias,
                "--save", str(ROOT / "logs" / "level_autotest" / f"_live_{alias}")]
    if not thinking:
        sys.argv.append("--no-thinking")
    from tools import level_autotest as la

    results = []
    scratch = la.SCRATCH / f"_cmp_{alias}"
    for task in la.TASKS:
        try:
            answer, finish, used = la.chat(alias, task.prompt, thinking=thinking)
        except Exception as exc:  # noqa: BLE001
            results.append({"task": task.name, "ok": False, "seconds": 0.0,
                            "errors": [f"request failed: {exc}"]})
            continue
        level = la.extract_json(answer)
        if level is None:
            note = f"no JSON in answer (finish={finish}, tokens={used})"
            if not answer.strip() and finish == "length":
                note += " - budget spent in reasoning; use thinking OFF"
            results.append({"task": task.name, "ok": False, "seconds": 0.0, "errors": [note]})
            continue
        sc = la.score_level(level, task, scratch)
        results.append({"task": task.name, "ok": sc.ok, "seconds": 0.0, "errors": sc.errors})
    return results


def main() -> int:
    p = argparse.ArgumentParser(description="Compare local GGUF models on the 2D autotest.")
    p.add_argument("--port", type=int, default=8080)
    p.add_argument("--ctx", type=int, default=16384,
                   help="context for the comparison run (keep it small: swap loop)")
    p.add_argument("--runs", type=int, default=1, help="repeat each model N times")
    p.add_argument("--only", default="", help="substring match on candidate key")
    p.add_argument("--thinking", action="store_true",
                   help="leave thinking ON (default is OFF: the known-good setting)")
    p.add_argument("--out", type=Path, default=ROOT / "logs" / "model_comparison.json")
    a = p.parse_args()

    if not LLAMA.exists():
        print(f"llama-server not found: {LLAMA}", file=sys.stderr)
        return 2
    if health(a.port):
        print(f"a server is already answering on :{a.port}. Stop it first "
              f"(Ctrl+C in its window) - this script owns the port.", file=sys.stderr)
        return 2

    todo = [c for c in CANDIDATES if a.only in c.key] if a.only else list(CANDIDATES)
    todo = [c for c in todo if c.gguf.exists()]
    if not todo:
        print("no candidate GGUF found", file=sys.stderr)
        return 2
    for c in CANDIDATES:
        if not c.gguf.exists():
            print(f"[skip] missing: {c.gguf}")

    summary: list[dict] = []
    for cand in todo:
        print(f"\n=== {cand.label} ===")
        runs: list[list[dict]] = []
        for r in range(a.runs):
            proc = start_server(cand.gguf, cand.key, a.port, a.ctx)
            try:
                if not wait_up(a.port):
                    print("  server did not come up; see logs\\cmp-*.log")
                    runs.append([{"task": "-", "ok": False, "seconds": 0.0,
                                  "errors": ["server failed to start"]}])
                    continue
                res = run_harness(cand.key, a.thinking)
                runs.append(res)
                ok = sum(1 for x in res if x["ok"])
                print(f"  run {r + 1}: {ok}/{len(res)} passed")
            finally:
                stop_server(proc)
                time.sleep(2.0)  # let VRAM free before the next model

        flat = [x for run in runs for x in run]
        passed = sum(1 for x in flat if x["ok"])
        summary.append({
            "model": cand.key,
            "label": cand.label,
            "gguf": str(cand.gguf),
            "passed": passed,
            "total": len(flat),
            "runs": runs,
        })

    print("\n================ SUMMARY ================")
    for s in summary:
        print(f"  {s['model']:20s} {s['passed']:2d}/{s['total']:<2d}  {s['label']}")
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nwritten: {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
