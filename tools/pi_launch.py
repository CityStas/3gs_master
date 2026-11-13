#!/usr/bin/env python
"""`pi` launcher that picks the engine profile from where you are standing.

The problem this solves: `agent.cmd` already selects `pi-home-<engine>` from the
active project's `engine.json`, but it lives in the repo root and wants a project
argument. A bare `pi` typed inside `projects/three/my_game` had no
`PI_CODING_AGENT_DIR`, so it silently ran the GLOBAL `~/.pi/agent` profile - the
wrong skills, no engine MCP servers, no RAG - while looking completely normal.

Now `pi` inside `projects/<engine>/<project>/` (or any subfolder of it) behaves
exactly like `agent.cmd` would:

  * walks UP for `engine.json` (project -> engine folder -> repo root);
  * `PI_CODING_AGENT_DIR` = `pi-home-<engine>`: SYSTEM.md, skills, mcp.json,
    models.json of that engine;
  * writes `data/active_project.txt` so the RAG / project MCP servers resolve the
    SAME project the session is standing in (they read the pointer, not cwd);
  * sets `GS_ROOT`, `GS_ENGINE`, `THREE_PROJECT`, `NO_PROXY`;
  * picks the model from whichever local server answers (:8080 router first);
  * appends a two-line system note naming the engine and the repo root.

`cmd\\pi.cmd` is the front door: it calls this with `--env-file`, sources the
generated `set` lines, then runs the real `pi-launcher.js` itself. Python is NOT
in front of the TUI - the console owner stays cmd.exe, exactly as before.

Three modes:

    python tools/pi_launch.py --plan        # what would happen here (JSON), no launch
    python tools/pi_launch.py --env-file F  # write `set` lines for cmd to source
    python tools/pi_launch.py --print-env   # same, to stdout (for tests/debug)

Anything after `--` is the pi command line and is only *inspected* (so a caller's
`--model` is not overridden); it is never forwarded from here.
"""
from __future__ import annotations

import json
import os
import socket
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from project_layout import (  # noqa: E402
    normalise_engine,
    engine_folder,
    nearest_engine,
    profile_for,
    repo_rel,
)

#: Real pi entry point. `pi.cmd` in the pi install is a shim (see cmd\pi-shim.cmd),
#: so the launcher script - not the .cmd - is what everything calls.
PI_LAUNCHER = Path(os.path.expanduser("~")) / ".pi" / "agent" / "bin" / "pi-launcher.js"

#: Router (:8080, `serve-all.cmd`) is preferred: it is the only mode with RAG.
ROUTER_PORT = 8080
#: The router's default, the same id agent.cmd / pi-here.cmd pass. The 9B distill sat
#: here until the 4B replaced it and then the 2B: 5512 MB on an 8 GB card left ~1 GB
#: free and pinned the GPU for the whole session. The 2B is lighter *and* the build we
#: actually fine-tune (models/FINETUNE.md), and `tools/llm_models.py` owns this choice
#: via DEFAULT_ID - keep the two in step.
ROUTER_MODEL = "3gs/qwen3.5-2b"
#: The Ollama fallback keeps the distill id deliberately: Ollama has no 2B manifest, so
#: a 2B id would 404 on the first request of this branch.
OLLAMA_MODEL = "ollama/qwen3.5-9b-distill-deepseek-v4.1-flash"


def port_open(port: int, host: str = "127.0.0.1", timeout: float = 0.4) -> bool:
    s = socket.socket()
    s.settimeout(timeout)
    try:
        return s.connect_ex((host, port)) == 0
    finally:
        s.close()


def resolve_project_dir(marker: Path | None, cwd: Path, engine: str) -> Path:
    """Which directory is "the project" - the one the pointer and the MCP servers use.

    `engine.json` can sit on the project (`projects/roblox/skateshop/engine.json`)
    or on the engine folder (`projects/roblox/engine.json`). In the second case the
    project is the FIRST folder under `projects/roblox/` on the way down to cwd -
    not the engine folder (which is a container of projects) and not cwd (which may
    be `.../ds_port/src/`). Without this the pointer named `projects/roblox` and
    every project MCP server resolved the wrong tree.
    """
    if marker is None:
        return cwd
    engine_parent = REPO / "projects" / engine_folder(engine)
    if marker.resolve() != engine_parent.resolve():
        return marker
    try:
        rel = cwd.resolve().relative_to(engine_parent)
    except ValueError:
        return marker
    return engine_parent / rel.parts[0] if rel.parts else marker


def plan(cwd: Path, passthrough_args: list[str]) -> dict:
    """Decide everything without touching the filesystem or the network."""
    info: dict = {
        "cwd": str(cwd),
        "repo": str(REPO),
        "engine": None,
        "engine_marker": None,
        "profile": None,
        "project": None,
        "project_rel": None,
        "pointer": None,
        "model": None,
        "reason": None,
        "apply": False,
    }

    # An outer launcher (agent.cmd, pi-here.cmd, run_pi.py) has already chosen a
    # profile. Re-deciding here would override an explicit choice with a guess.
    if os.environ.get("PI_CODING_AGENT_DIR"):
        info["reason"] = "PI_CODING_AGENT_DIR already set - outer launcher decides"
        info["profile"] = os.environ["PI_CODING_AGENT_DIR"]
        return info

    try:
        cwd.relative_to(REPO)
    except ValueError:
        info["reason"] = "cwd is outside the 3GS_Master repo - plain pi"
        return info

    marker, engine = nearest_engine(cwd)
    if engine is None:
        info["reason"] = "no engine.json between cwd and the repo root - plain pi"
        return info

    engine = normalise_engine(engine)
    project = resolve_project_dir(marker, cwd, engine)
    info.update({
        "engine": engine,
        "engine_marker": str(marker),
        "profile": str(profile_for(engine)),
        "project": str(project),
        "project_rel": repo_rel(project),
        "pointer": str(REPO / "data" / "active_project.txt"),
        "apply": True,
    })

    if not any(a == "--model" or a.startswith("--model=") for a in passthrough_args):
        info["model"] = ROUTER_MODEL if port_open(ROUTER_PORT) else OLLAMA_MODEL
    return info


def system_prompt(info: dict) -> str:
    """Two lines, not a rulebook: AGENTS.md already carries the rules.

    It exists because the model cannot see `PI_CODING_AGENT_DIR`, and "which
    engine am I in" is exactly the thing it otherwise guesses from the task
    wording (and then writes `.tscn` into a three.js project).
    """
    return (
        f"3GS Master session: engine={info['engine']}, repo root={info['repo']}, "
        f"project={info['project_rel']}. The tools of this engine's profile "
        f"({Path(info['profile']).name}) are authoritative - its RAG answers version "
        f"questions, other engines' APIs do not exist here. Work inside "
        f"{info['project_rel']}/; do not create another project folder unless asked by name.\n"
    )


def build_env(info: dict) -> dict[str, str]:
    env: dict[str, str] = {}

    if not info["apply"]:
        return env

    env["PI_CODING_AGENT_DIR"] = info["profile"]
    env["GS_ROOT"] = str(REPO)
    env["GS_ENGINE"] = info["engine"]
    env["THREE_PROJECT"] = info["project_rel"]
    env["PI_SKIP_VERSION_CHECK"] = "1"
    env["PI_TELEMETRY"] = "0"

    # A system proxy swallows loopback calls: pi sends HTTP_PROXY to 127.0.0.1:1234
    # and hangs. Keep localhost out of it for this process tree.
    noproxy = os.environ.get("NO_PROXY", "")
    parts = [p for p in noproxy.split(",") if p.strip()]
    for host in ("127.0.0.1", "localhost", "::1"):
        if host not in parts:
            parts.append(host)
    env["NO_PROXY"] = ",".join(parts)
    env["no_proxy"] = env["NO_PROXY"]

    if info["model"]:
        env["PI_MODEL_ARGS"] = f'--model {info["model"]}'

    sp_file = Path(tempfile.gettempdir()) / f"3gs_pi_sp_{os.getpid()}.txt"
    try:
        sp_file.write_text(system_prompt(info), encoding="utf-8")
        env["PI_SP_ARGS"] = f'--append-system-prompt "{sp_file}"'
    except OSError:
        env["PI_SP_ARGS"] = ""

    return env


def write_pointer(info: dict) -> None:
    """Keep `data/active_project.txt` in step with the session.

    The RAG and the project MCP servers (godot/unity/roblox) resolve the project
    from this file, NOT from cwd. A stale pointer means the session edits one
    folder while the tools inspect another - the failure mode that looks like
    "the model is stupid".
    """
    if not info["apply"]:
        return
    target = REPO / "data" / "active_project.txt"
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(info["project_rel"], encoding="utf-8")
    except OSError as exc:
        print(f"[pi] WARN: cannot write {target}: {exc}", file=sys.stderr)


def as_cmd(env: dict[str, str]) -> str:
    """`set` lines safe for cmd.exe: `set "K=V"` tolerates spaces, `&`, `^`."""
    lines = ["@echo off"]
    for key, value in env.items():
        lines.append(f'set "{key}={value}"')
    return "\r\n".join(lines) + "\r\n"


def split_args(argv: list[str]) -> tuple[list[str], list[str]]:
    """Split our own flags from the passthrough pi command line after `--`."""
    if "--" in argv:
        i = argv.index("--")
        return argv[:i], argv[i + 1:]
    return argv, []


def main(argv: list[str]) -> int:
    own, passthrough = split_args(argv)
    cwd = Path.cwd()

    if "--plan" in own:
        info = plan(cwd, passthrough)
        print(json.dumps(info, indent=2, ensure_ascii=False))
        return 0

    info = plan(cwd, passthrough)
    env = build_env(info)
    write_pointer(info)

    if "--print-env" in own:
        print(as_cmd(env), end="")
        return 0

    if "--env-file" in own:
        dest = own[own.index("--env-file") + 1]
        Path(dest).write_text(as_cmd(env), encoding="utf-8")
        # One line for the console: which profile the session actually got. Silent
        # when an outer launcher (agent.cmd) already chose - that one prints its own
        # banner and a second line would only look like a second decision.
        if info["apply"]:
            print(f"[pi] engine={info['engine']}  profile={Path(info['profile']).name}  "
                  f"project={info['project_rel']}")
        return 0

    # Direct mode (tests, or `python tools/pi_launch.py`): run pi ourselves.
    args = [os.environ.get("COMSPEC", "cmd.exe"), "/c", "node", str(PI_LAUNCHER)]
    if info["model"]:
        args += ["--model", info["model"]]
    if info["apply"]:
        sp = Path(tempfile.gettempdir()) / f"3gs_pi_sp_{os.getpid()}.txt"
        sp.write_text(system_prompt(info), encoding="utf-8")
        args += ["--append-system-prompt", str(sp)]
    args += passthrough

    import subprocess
    merged = dict(os.environ)
    merged.update(env)
    try:
        return subprocess.call(args, env=merged)
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
