"""Taking the GPU away from the language model - and giving it back.

Why this module exists
----------------------
One card, two models that each want all of it. Measured on this box
(RTX 2060 Super 8 GB, i3-12100, 16 GB RAM):

    Qwen3.5-9B resident at -c 65536     ~6.4 GiB VRAM  +  ~6.4 GB RAM
    Qwen-Image 2.1 text encoder          8.9 GiB, streamed by --lowvram

With both up, a 512x512 / 4-step text-to-image took **725 s** and
`QwenImage21TEModel_` staged 8916 MB while only 426 MiB of VRAM was free - the
card was paging the 9B out to system RAM on every denoise step. With the 9B
stopped the same class of run has the whole card, and ~6.4 GB of system RAM
comes back too.

So the answer is not a faster workflow, it is scheduling. This module owns the
two halves of that:

* `LlamaServer` - stop / start / wait for the :8080 llama.cpp server. The model
  is restarted through the same `serve-llm.cmd` that a human uses, so the
  context size, KV quantisation and sampling flags have exactly one definition.
* `GenLock` - one generation at a time across processes. The agent (over MCP)
  and a hand-run `gen.cmd` both take it, because two overlapping runs would
  each kill the other's LLM and neither would finish.
* `vram()` - real numbers from nvidia-smi, so "the model is off" is verified
  rather than assumed.

Nothing here writes to stdout: this code also runs inside stdio MCP servers,
where anything printed corrupts the JSON-RPC stream.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from .. import config

CREATE_NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)
# Detached + new process group: the server outlives whoever spawned it. A plain
# child dies with its parent's process tree, which is how two ComfyUI starts were
# lost earlier in this project.
DETACHED = getattr(subprocess, "DETACHED_PROCESS", 0) | getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)


class SchedulerError(RuntimeError):
    pass


def _find_launcher(name: str, repo_root: Path | None = None) -> Path:
    """Locate a launcher by name, wherever it currently lives.

    Launchers are split between the repo root (day-to-day: `agent`, `studio`,
    `serve-all`, `resume`) and `cmd\\` (service: `serve-llm`, `gen`, ...). Hardcoding
    one directory broke `llm_restored` the moment `serve-llm.cmd` moved to `cmd\\`,
    so search both and fall back to the root so the error message names a path the
    user recognises. `THREE_LAUNCHER_DIR` pins an explicit directory if ever needed.
    """
    root = Path(repo_root) if repo_root else config.THREE_RAG_HOME
    candidates = []
    pinned = os.environ.get("THREE_LAUNCHER_DIR", "")
    if pinned:
        candidates.append(Path(pinned) / name)
    candidates += [root / name, root / "cmd" / name]
    for cand in candidates:
        if cand.exists():
            return cand
    return candidates[0]


def run_text(args, timeout: float = 25.0) -> str:
    """Run a console tool and decode its output without guessing the encoding.

    `PYTHONUTF8=1` is set on this machine, so `text=True` decodes every child's stdout
    as UTF-8 - but `netstat` writes CP866 on a Russian Windows ("Активные подключения").
    The UnicodeDecodeError happens in a reader thread, so `stdout` comes back as `None`
    and the failure surfaces much later as
    `AttributeError: 'NoneType' object has no attribute 'splitlines'`, nowhere near the
    cause. Decode the bytes here instead: UTF-8 first, then CP866, then CP1251.
    """
    proc = subprocess.run(args, capture_output=True, timeout=timeout,
                          creationflags=CREATE_NO_WINDOW)
    raw = proc.stdout or b""
    for enc in ("utf-8", "cp866", "cp1251"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", "replace")


# --------------------------------------------------------------------- probes
def vram() -> dict:
    """`{"total_mb", "used_mb", "free_mb"}` or `{}` when nvidia-smi is unavailable."""
    try:
        out = run_text(["nvidia-smi", "--query-gpu=memory.total,memory.used,memory.free",
                        "--format=csv,noheader,nounits"])
        total, used, free = (int(x.strip()) for x in out.strip().splitlines()[0].split(","))
        return {"total_mb": total, "used_mb": used, "free_mb": free}
    except Exception:  # noqa: BLE001 - a missing GPU tool must not break generation
        return {}


def http_up(url: str, timeout: float = 2.0) -> bool:
    """HTTP 200 means the server answers. Proxy bypassed: 127.0.0.1 never goes out.

    On this machine `HTTP_PROXY` is set globally and `urllib.proxy_bypass('127.0.0.1')`
    returns False, so without the empty ProxyHandler a local probe is routed through the
    proxy and reports 502 instead of "refused".
    """
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(url, timeout=timeout) as r:
            return r.status == 200
    except Exception:  # noqa: BLE001
        return False


def port_pid(port: int) -> int:
    """PID of whatever is LISTENING on `port`, or 0."""
    if sys.platform != "win32":
        return 0
    try:
        out = run_text(["netstat", "-ano", "-p", "TCP"])
    except Exception:  # noqa: BLE001
        return 0
    for line in out.splitlines():
        parts = line.split()
        # Every field that matters - local address, state, PID - is ASCII, so the
        # localised column headers can be mojibake without hurting the match.
        if len(parts) >= 5 and parts[0].upper() == "TCP" and parts[1].endswith(f":{port}") \
                and parts[3].upper() == "LISTENING":
            try:
                return int(parts[4])
            except ValueError:
                return 0
    return 0


def process_path(pid: int) -> str:
    """Executable behind a PID. `wmic` is blocked by policy on this box, so PowerShell."""
    if sys.platform != "win32" or not pid:
        return ""
    try:
        return run_text(
            ["powershell", "-NoProfile", "-NonInteractive", "-Command",
             f"(Get-Process -Id {pid} -ErrorAction SilentlyContinue).Path"]).strip()
    except Exception:  # noqa: BLE001
        return ""


def kill_tree(pid: int) -> bool:
    if not pid:
        return False
    try:
        if sys.platform == "win32":
            subprocess.run(["taskkill", "/PID", str(pid), "/F", "/T"],
                           capture_output=True, timeout=40, creationflags=CREATE_NO_WINDOW)
        else:
            os.kill(pid, 9)
        return True
    except Exception:  # noqa: BLE001
        return False


def wait_port_free(port: int, timeout: float = 30.0) -> bool:
    t0 = time.monotonic()
    while time.monotonic() - t0 < timeout:
        if not port_pid(port):
            return True
        time.sleep(0.5)
    return False


def wait_free_vram(min_free_mb: int, timeout: float = 45.0) -> dict:
    """Block until the card has room again. Returns the last reading either way."""
    t0 = time.monotonic()
    last = vram()
    while last and last.get("free_mb", 0) < min_free_mb and time.monotonic() - t0 < timeout:
        time.sleep(1.0)
        last = vram()
    return last


# ------------------------------------------------------------------ llama.cpp
class LlamaServer:
    """The :8080 llama.cpp server, seen as something that can be switched off.

    Restart goes through `serve-llm.cmd` rather than re-deriving the command line
    here: context size, `-ngl`, KV quantisation and `reserveTokens` are a matched
    triple, and a second copy of them in Python would drift silently.
    """

    def __init__(self, port: int | None = None, host: str | None = None,
                 launcher: Path | str | None = None, log: Path | str | None = None):
        self.host = host or config.LLM_HOST
        self.port = int(port or config.LLM_PORT)
        self.base = f"http://{self.host}:{self.port}"
        self.launcher = Path(launcher) if launcher else _find_launcher("serve-llm.cmd")
        self.log = Path(log) if log else (config.LOGS_DIR / "llm-sidecar.log")
        # A detached process has no console: without a redirect its output is lost, and
        # the llama.cpp load banner is the first thing anyone wants when a start fails.
        self.window = os.environ.get("THREE_LLM_WINDOW", "") not in ("", "0", "false", "no")

    # -------------------------------------------------------------- state
    def alive(self) -> bool:
        return http_up(f"{self.base}/v1/models")

    def pid(self) -> int:
        return port_pid(self.port)

    def info(self) -> dict:
        return {
            "alive": self.alive(), "port": self.port, "pid": self.pid(),
            "launcher": str(self.launcher), "window": self.window, "log": str(self.log),
            "vram": vram(),
        }

    # ---------------------------------------------------------- lifecycle
    def stop(self, wait: float = 30.0) -> dict:
        pid = self.pid()
        if not pid:
            return {"stopped": False, "reason": f"nothing listening on :{self.port}",
                    "vram": vram()}
        before = vram()
        kill_tree(pid)
        freed = wait_port_free(self.port, wait)
        # VRAM release is asynchronous: the process is gone the moment taskkill returns,
        # but WDDM can take a moment to hand the pages back. Waiting here is what makes
        # "the model is off" a fact instead of a hope.
        after = wait_free_vram(min_free_mb=max(0, (before.get("total_mb") or 8192) - 2000),
                               timeout=45.0)
        return {"stopped": True, "pid": pid, "port_free": freed,
                "vram_before": before, "vram_after": after}

    def start(self) -> dict:
        if self.alive():
            return {"started": False, "reason": "already running", "pid": self.pid()}
        if not self.launcher.exists():
            raise SchedulerError(f"launcher not found: {self.launcher}")
        self.log.parent.mkdir(parents=True, exist_ok=True)
        handle = self.log.open("ab")
        handle.write(f"\n=== start {time.strftime('%Y-%m-%d %H:%M:%S')}\n".encode())
        handle.flush()
        if self.window:
            # Opt-in: `set THREE_LLM_WINDOW=1` restores the visible console that
            # serve-all.cmd opens. Detached is the default because it also works when
            # the caller has no window station - an MCP server spawned by pi may not.
            subprocess.Popen(f'start "3gs-llm" cmd /c ""{self.launcher}""', shell=True,
                             cwd=str(config.THREE_RAG_HOME))
            handle.close()
            return {"started": True, "mode": "window", "log": str(self.log)}
        proc = subprocess.Popen(
            ["cmd", "/c", str(self.launcher)], cwd=str(config.THREE_RAG_HOME),
            stdout=handle, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
            creationflags=DETACHED, close_fds=True,
        )
        handle.close()
        return {"started": True, "mode": "detached", "pid": proc.pid, "log": str(self.log)}

    def wait(self, timeout: float = 240.0) -> bool:
        t0 = time.monotonic()
        while time.monotonic() - t0 < timeout:
            if self.alive():
                return True
            time.sleep(1.5)
        return False

    def ensure(self, timeout: float = 240.0) -> dict:
        if self.alive():
            return {"started": False, "reason": "already running"}
        res = self.start()
        if not self.wait(timeout):
            raise SchedulerError(
                f"llama-server did not answer on {self.base}/v1/models within {timeout:.0f}s. "
                f"See {self.log}."
            )
        return res


# ---------------------------------------------------------------------- lock
class GenLock:
    """One generation at a time, across processes.

    The agent calls the pack tool over MCP while a human may be running `gen.cmd` by
    hand. Two overlapping runs would both stop the LLM and both start ComfyUI on the
    same port; the second would adopt the first's server and then kill it on the way
    out, losing the first run's outputs. Hence the lock.

    Stale locks are reclaimed: the holder's PID is written into the file, and a lock
    whose PID no longer exists is ignored.
    """

    def __init__(self, path: Path | str | None = None, stale_s: float = 6 * 3600):
        self.path = Path(path) if path else config.GEN_LOCK_FILE
        self.stale_s = stale_s
        self.held = False

    def _holder(self) -> dict:
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            return {}

    def _holder_alive(self, holder: dict) -> bool:
        pid = int(holder.get("pid") or 0)
        if not pid:
            return False
        try:
            if sys.platform == "win32":
                out = run_text(["tasklist", "/FI", f"PID eq {pid}", "/NH"], timeout=20)
                return str(pid) in out
            os.kill(pid, 0)
            return True
        except Exception:  # noqa: BLE001
            return False

    def acquire(self, timeout: float = 30.0) -> dict:
        deadline = time.monotonic() + timeout
        self.path.parent.mkdir(parents=True, exist_ok=True)
        while True:
            holder = self._holder()
            stale = holder and (not self._holder_alive(holder)
                                or (time.time() - float(holder.get("t") or 0)) > self.stale_s)
            if holder and not stale:
                if time.monotonic() >= deadline:
                    raise SchedulerError(
                        f"another generation is already running (pid {holder.get('pid')}, "
                        f"started {time.strftime('%H:%M:%S', time.localtime(holder.get('t') or 0))}). "
                        f"Wait for it, or delete {self.path} if you are sure it is dead."
                    )
                time.sleep(1.5)
                continue
            if stale:
                self.path.unlink(missing_ok=True)
            try:
                fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            except FileExistsError:
                time.sleep(0.5)
                continue
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                json.dump({"pid": os.getpid(), "t": time.time()}, fh)
            self.held = True
            return holder

    def release(self) -> None:
        if self.held:
            self.path.unlink(missing_ok=True)
            self.held = False

    def __enter__(self) -> "GenLock":
        self.acquire()
        return self

    def __exit__(self, *exc) -> None:
        self.release()
