#!/usr/bin/env python
"""Block until the local llama.cpp servers actually answer, then exit.

`serve-all.cmd` launches both servers with `start`, which returns immediately. Anything
chained after it with `&&` therefore ran while the 9B model was still loading (~30 s on
this box), saw a dead LLM, and aborted the chain. That is how

    serve-all.cmd && doctor.cmd && ... && agent.cmd

silently did nothing: doctor exited 1, and cmd never reached agent.cmd.

This tool turns "started" into "ready":

    python tools/wait_ready.py                # wait up to 300 s for both
    python tools/wait_ready.py --timeout 600
    python tools/wait_ready.py --quiet        # only the final line
    python tools/wait_ready.py --check        # one-shot probe, no waiting
    python tools/wait_ready.py --check-rerank # is the OPTIONAL reranker up?
    python tools/wait_ready.py --status       # who is on the three ports
    python tools/wait_ready.py --stop         # kill whatever holds them

Exit codes: 0 = both up, 1 = timeout (or, with --check, at least one down).

The reranker on :8083 is deliberately NOT part of the wait. It is an accelerator,
not a dependency: every retriever degrades to plain hybrid search when it is
missing and counts the failure, so blocking a startup on it would turn a
relevance drop into a hard stop. `serve-all.cmd` still starts it when its port is
free, and `--status` / `--stop` cover it like the other two.

(:8082 is the Qwen2.5-VL vision server - `cmd\vlm.cmd` - and is not managed here.)
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from threejs import config  # noqa: E402

# Required: the agent cannot answer at all without these two.
REQUIRED = [
    ("LLM  ", f"{config.LLM_BASE_URL}/models"),
    ("EMBED", f"{config.EMBED_BASE_URL}/health"),
]

# Optional: started by serve-all, never waited on. See the module docstring.
OPTIONAL = [
    ("RERANK", f"{config.RERANK_BASE_URL}/health"),
]

TARGETS = REQUIRED + OPTIONAL


def _probe(url: str, timeout: float = 2.0) -> bool:
    """HTTP 200 means the server is up. Proxy is bypassed: 127.0.0.1 must never go out."""
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(url, timeout=timeout) as r:
            return r.status == 200
    except Exception:
        return False


def check(quiet: bool = False) -> int:
    """Single probe, no retries. Used by serve-all.cmd to avoid duplicate windows."""
    down = [label.strip() for label, url in REQUIRED if not _probe(url)]
    if down:
        if not quiet:
            print("not running: %s" % ", ".join(down))
        return 1
    if not quiet:
        print("both servers already running")
    return 0


def check_rerank(quiet: bool = False) -> int:
    """Is the optional reranker up? 0 = up, 1 = down.

    serve-all.cmd asks this before spawning, for the same reason it asks about the
    other two: a second llama-server on a busy port dies instantly while the first
    one keeps answering, which reads as success.
    """
    up = all(_probe(url) for _, url in OPTIONAL)
    if not quiet:
        print("reranker running" if up else "reranker not running")
    return 0 if up else 1


def wait(timeout: float = 300.0, quiet: bool = False, interval: float = 2.0) -> int:
    deadline = time.monotonic() + timeout
    done: set[str] = set()
    t0 = time.monotonic()

    while True:
        for label, url in REQUIRED:
            if label in done:
                continue
            if _probe(url):
                done.add(label)
                if not quiet:
                    print("  [ ready ] %s %s  (%.1fs)" % (label, url, time.monotonic() - t0))
        if len(done) == len(REQUIRED):
            print("servers ready in %.1fs" % (time.monotonic() - t0))
            if not quiet:
                for label, url in OPTIONAL:
                    print("  [ %s ] %s %s"
                          % ("ready" if _probe(url) else " down", label, url))
            return 0
        if time.monotonic() >= deadline:
            missing = [label for label, _ in REQUIRED if label not in done]
            print("TIMEOUT after %.0fs, still down: %s" % (timeout, ", ".join(missing)))
            print("Look at the two server windows: the model may still be loading, or a")
            print("port may be held by a stale process (netstat -ano | findstr :8080).")
            return 1
        time.sleep(interval)


def _port(url: str) -> int:
    return int(urlparse(url).port or 0)


def _pids_on(port: int) -> list[int]:
    """PIDs of the processes LISTENING on `port`.

    Windows only, and deliberately without psutil: the venv has no third-party
    packages, and `netstat -ano` is always there.
    """
    try:
        out = subprocess.run(["netstat", "-ano", "-p", "TCP"],
                             capture_output=True, text=True, errors="replace").stdout
    except OSError:
        return []
    pids: list[int] = []
    for line in out.splitlines():
        parts = line.split()
        # Proto  Local Address  Foreign Address  State  PID
        if len(parts) < 5 or parts[0].upper() != "TCP" or parts[3].upper() != "LISTENING":
            continue
        if parts[1].rsplit(":", 1)[-1] != str(port):
            continue
        try:
            pids.append(int(parts[4]))
        except ValueError:
            pass
    return pids


def status() -> int:
    """Who is on :8080, :8081 and :8083 - a live server or an orphaned process.

    Why this exists. Closing the two server windows does NOT always kill
    `llama-server`: it can survive as an orphan and keep the port. Then the next
    `serve-all.cmd` sees both ports answering, correctly refuses to spawn a
    second pair, and opens no windows at all. That looks exactly like "the
    launcher stopped opening terminals", so it has to SAY what it found.

    The exit code counts the REQUIRED servers only - a missing reranker is
    reported as `DOWN` but is not a failure.
    """
    print("local servers:")
    down = 0
    for label, url in TARGETS:
        port = _port(url)
        up = _probe(url)
        pids = _pids_on(port)
        who = "pid " + ", ".join(str(p) for p in pids) if pids else "no listener"
        optional = (label, url) in OPTIONAL
        tag = " (optional)" if optional else ""
        print("  %-6s :%-5d %-4s  %s%s" % (label.strip(), port, "up" if up else "DOWN", who, tag))
        if not up and not optional:
            down += 1
    return 1 if down else 0


def stop() -> int:
    """Kill whatever holds the three ports, so `--restart` can start fresh.

    Touches ONLY processes listening on our ports - nothing else. Called by
    `serve-all.cmd --restart`, which is the honest way out of the orphan case:
    the alternative is hunting the PID by hand with `netstat -ano | findstr`.
    """
    killed = 0
    for label, url in TARGETS:
        port = _port(url)
        for pid in _pids_on(port):
            r = subprocess.run(["taskkill", "/PID", str(pid), "/F"],
                               capture_output=True, text=True, errors="replace")
            if r.returncode == 0:
                print("  killed pid %d on :%d (%s)" % (pid, port, label.strip()))
                killed += 1
            else:
                msg = (r.stderr or r.stdout or "").strip().splitlines()
                print("  could not kill pid %d on :%d - %s"
                      % (pid, port, msg[-1] if msg else "unknown error"))
    if not killed:
        print("  nothing was listening on :8080 / :8081 / :8083")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Wait for the local llama.cpp servers.")
    ap.add_argument("--timeout", type=float, default=300.0,
                    help="seconds to wait for both servers (default 300)")
    ap.add_argument("--quiet", action="store_true", help="print only the final line")
    ap.add_argument("--check", action="store_true",
                    help="one-shot probe instead of waiting; exit 1 if either is down")
    ap.add_argument("--check-rerank", action="store_true",
                    help="probe only the optional reranker; exit 1 if it is down")
    ap.add_argument("--status", action="store_true",
                    help="show each server and the PID holding its port")
    ap.add_argument("--stop", action="store_true",
                    help="kill whatever is listening on the three ports")
    a = ap.parse_args()
    if a.stop:
        return stop()
    if a.status:
        return status()
    if a.check_rerank:
        return check_rerank(quiet=a.quiet)
    if a.check:
        return check(quiet=a.quiet)
    return wait(timeout=a.timeout, quiet=a.quiet)


if __name__ == "__main__":
    raise SystemExit(main())
