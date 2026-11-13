#!/usr/bin/env python
"""Render `mcp/registry.json` into every MCP client this repo uses.

Why this exists: the same servers were configured in four places by hand - three pi
profiles (`pi-home-*/mcp.json`) and WorkBuddy (`~/.workbuddy-ai/mcp.json`) - and they had
already drifted (an empty `mcp.json` in two profiles meant "no tools at all", a different
`assets` description in each). One registry, rendered, is the only version that cannot
disagree with itself.

What it does NOT do: it never deletes a server it did not write. Each target keeps a
`.generated.json` manifest of the names this tool owns; a name in the manifest that the
registry no longer defines is removed, anything else in the file is left alone.

    python tools/mcp_sync.py                 # dry run: show what would change
    python tools/mcp_sync.py --apply         # write pi profiles + WorkBuddy
    python tools/mcp_sync.py --apply --only pi
    python tools/mcp_sync.py --print roblox  # one pi profile to stdout
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "mcp" / "registry.json"
CLIENTS_FILE = ROOT / "mcp" / "clients.json"
MANIFEST = ROOT / "mcp" / ".generated.json"
WORKBUDDY_MCP = Path(os.environ.get("WORKBUDDY_MCP",
                                    Path.home() / ".workbuddy-ai" / "mcp.json"))

ENGINES = ("threejs", "godot", "unity", "roblox")
# Explicit, not `pi-home-{engine}`: the Three.js profile is `pi-home-three` (it predates
# the engine name), and deriving the path from the engine name silently created a second
# directory that pi never reads.
PI_PROFILE = {
    "threejs": ROOT / "pi-home-three" / "mcp.json",
    "godot": ROOT / "pi-home-godot" / "mcp.json",
    "unity": ROOT / "pi-home-unity" / "mcp.json",
    "roblox": ROOT / "pi-home-roblox" / "mcp.json",
}


def _load(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def _active_project() -> str:
    try:
        return (ROOT / "data" / "active_project.txt").read_text(encoding="utf-8").strip()
    except OSError:
        return ""


def _placeholders(style: str = "absolute") -> dict:
    """Expand the registry's `{...}` placeholders.

    `absolute` -> Windows paths with BACKslashes: these strings end up in `command`/`cwd`
    that the clients pass to CreateProcess, and a mixed separator is one more thing that
    can go wrong in a way that only shows as "server failed to start".

    `workspace` -> `${workspaceFolder}` variables instead, so the rendered file names no
    machine at all and can be committed (Cursor and VS Code both interpolate it in
    `command`, `args` and `env`). Program Files paths stay absolute - nothing outside the
    repo can be expressed relative to it."""
    py = ROOT / ".venv" / "Scripts" / "python.exe"
    if style == "workspace":
        return {
            "{repo}": "${workspaceFolder}",
            "{python}": "${workspaceFolder}/.venv/Scripts/python.exe",
            "{studio_mcp}": str(_studio_mcp()),
            "{active_project}": _active_project(),
        }
    return {
        "{repo}": str(ROOT),
        "{python}": str(py),
        "{studio_mcp}": _studio_mcp(),
        "{active_project}": _active_project(),
    }


def _studio_mcp() -> str:
    """The StudioMCP.exe of the installed Studio, or "" (the `mcp.bat` route is used then)."""
    try:
        sys.path.insert(0, str(ROOT / "roblox"))
        from rbxmaster import config  # noqa: PLC0415
        return (str(config.STUDIO_MCP)
                if config.STUDIO_MCP and config.STUDIO_MCP.suffix.lower() == ".exe" else "")
    except Exception:  # noqa: BLE001 - a missing stack must not break the sync
        return ""


def _expand(value, ph: dict):
    if isinstance(value, str):
        for k, v in ph.items():
            value = value.replace(k, v)
        return value
    if isinstance(value, list):
        return [_expand(v, ph) for v in value]
    if isinstance(value, dict):
        return {k: _expand(v, ph) for k, v in value.items()}
    return value


def _norm(path: str) -> str:
    """`F:/repo/roblox` -> `F:\\repo\\roblox`. Templates are written with `/` for
    readability; a `cwd` handed to CreateProcess should be a plain Windows path."""
    if len(path) > 2 and path[1] == ":":
        return path.replace("/", "\\")
    return path


def _pi_entry(cfg: dict, ph: dict) -> dict:
    out = {"command": _expand(cfg["command"], ph),
           "args": _expand(cfg.get("args", []), ph)}
    if cfg.get("cwd"):
        out["cwd"] = _norm(_expand(cfg["cwd"], ph))
    if cfg.get("env"):
        out["env"] = _expand(cfg["env"], ph)
    out["exposure"] = cfg.get("exposure", "direct")
    out["timeout"] = cfg.get("timeout", 300)
    out["description"] = cfg.get("description", "")
    return out


def _workbuddy_entry(cfg: dict, ph: dict) -> dict:
    """WorkBuddy has no `cwd` and no per-engine gating, so the module root moves into
    PYTHONPATH - otherwise `-m gdmaster.mcp...` cannot be resolved from an arbitrary cwd."""
    command = _expand(cfg["command"], ph)
    args = _expand(cfg.get("args", []), ph)
    env = _expand(cfg.get("env", {}) or {}, ph)
    cwd = _expand(cfg.get("cwd", ""), ph)
    if cwd and "python" in Path(command).name.lower():
        env["PYTHONPATH"] = _norm(cwd)
    out: dict = {"command": command, "args": args}
    if env:
        out["env"] = env
    out["type"] = "stdio"
    # Only write the key when it is true: WorkBuddy's own settings UI drops `disabled: false`
    # when you switch a server on, so emitting it made every later dry run report a diff
    # against a file that was already correct.
    if not (cfg.get("workbuddy") or {}).get("enabled", False):
        out["disabled"] = True
    return out


def _load_clients() -> dict:
    return _load(CLIENTS_FILE, {}).get("clients", {})


def _is_ambient(cfg: dict) -> bool:
    """Servers safe to load in a client that has no per-engine gating and no guaranteed
    active project - the same set WorkBuddy gets: the four RAG bases and the asset
    pipeline. The project servers answer for `data/active_project.txt` and are started by
    the 3GS launchers when a project is actually in play."""
    return bool((cfg.get("workbuddy") or {}).get("enabled", False))


def _canonical(cfg: dict, ph: dict, style: str) -> tuple[str, list, dict]:
    """Transport-neutral stdio launcher: interpreter, argv, env.

    No `cwd`. Every stack resolves its own root from `__file__` (GDM_HOME / UNIM_HOME /
    RBX_HOME / THREE_RAG_HOME) and treats cwd as only one candidate when resolving a
    project path, so the module root travels in PYTHONPATH instead. That is what lets a
    client with no `cwd` field at all (Cursor) work exactly like one that has it."""
    command = _expand(cfg["command"], ph)
    args = _expand(cfg.get("args", []), ph)
    env = dict(_expand(cfg.get("env", {}) or {}, ph))
    root = _expand(cfg.get("cwd", ""), ph)
    if root and "python" in Path(command).name.lower():
        env.setdefault("PYTHONPATH", root)
    if style != "workspace":
        command = _norm(command)
        env = {k: _norm(v) for k, v in env.items()}
    return command, list(args), env


def _shape_entry(shape: str, command: str, args: list, env: dict) -> dict:
    if shape == "command-array":
        # opencode: the executable and its arguments share ONE array, and env is
        # `environment`, and disabling is `disabled: true` (there is no `enabled`).
        entry: dict = {"type": "local", "command": [command, *args]}
        if env:
            entry["environment"] = env
        return entry
    entry = {"type": "stdio", "command": command}
    if args:
        entry["args"] = args
    if env:
        entry["env"] = env
    return entry


def render_client(registry: dict, client: dict, ph: dict) -> dict:
    style = client.get("path_style", "absolute")
    shape = client.get("shape", "argv")
    servers = {}
    for name, cfg in registry["servers"].items():
        if cfg.get("exposure", "direct") != "direct" or not _is_ambient(cfg):
            continue
        command, args, env = _canonical(cfg, ph, style)
        servers[name] = _shape_entry(shape, command, args, env)
    payload: dict = {}
    if client.get("schema"):
        payload["$schema"] = client["schema"]
    return {"payload": payload, "servers": servers,
            "root": client.get("root", ["mcpServers"])}


def _dig(doc: dict, path: list) -> dict:
    """Return (creating as needed) the nested dict a client keeps its servers under."""
    cur = doc
    for key in path:
        nxt = cur.get(key)
        if not isinstance(nxt, dict):
            nxt = {}
            cur[key] = nxt
        cur = nxt
    return cur


def render_pi(registry: dict, engine: str, ph: dict) -> dict:
    servers = {}
    for name, cfg in registry["servers"].items():
        engines = cfg.get("engines", ["any"])
        if engine not in engines and "any" not in engines:
            continue
        servers[name] = _pi_entry(cfg, ph)
    return {"autoEnableCodemode": False, "mcpServers": servers}


def render_workbuddy(registry: dict, ph: dict) -> dict:
    return {name: _workbuddy_entry(cfg, ph) for name, cfg in registry["servers"].items()}


def render_workbuddy_profile(registry: dict, engine: str, ph: dict) -> dict:
    """One engine's WorkBuddy surface, generated from the same registry.

    WorkBuddy has no per-engine gating and no way to switch profiles inside a session: it
    loads every server that is not marked `disabled` and needs a reload to see a new list.
    So the honest implementation of "a WorkBuddy profile" is this - write the file with the
    selected engine's servers enabled and everything else explicitly disabled, and tell the
    user to reload. That is derived state, not a hand-maintained second config, and it keeps
    `mcp/registry.json` the only place a server is declared.

    `engines: ["any"]` (the shared asset pipeline) is always enabled: it is the one server
    that is correct in every session.
    """
    out = {}
    for name, cfg in registry["servers"].items():
        entry = _workbuddy_entry(cfg, ph)
        engines = cfg.get("engines", ["any"])
        wanted = engine in engines or "any" in engines
        if wanted:
            entry.pop("disabled", None)
        else:
            entry["disabled"] = True
        out[name] = entry
    return out


def _merge(target: dict, generated: dict, owned: list[str], label: str,
           verbose: bool) -> tuple[dict, list[str], list[str]]:
    """Merge generated entries into `target`, reporting added/updated/dropped.

    Ownership rule: only names in `owned` (what this tool wrote last time) may be removed.
    Everything else in the file - chrome-devtools, playwright, sequential-thinking, a
    hand-added server - is preserved untouched.
    """
    out = dict(target)
    added, updated = [], []
    for name, entry in generated.items():
        if name not in out:
            added.append(name)
        elif out[name] != entry:
            updated.append(name)
        out[name] = entry
    dropped = [n for n in owned if n not in generated and n in out]
    for n in dropped:
        del out[n]
    if verbose:
        if added:
            print(f"  {label}: + {', '.join(added)}")
        if updated:
            print(f"  {label}: ~ {', '.join(updated)}")
        if dropped:
            print(f"  {label}: - {', '.join(dropped)}")
        if not (added or updated or dropped):
            print(f"  {label}: up to date")
    return out, added + updated, dropped


def _write(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Force LF: Path.write_text defaults to os.linesep (CRLF on Windows), which
    # flipped the committed LF blobs to CRLF on every sync and buried the real
    # one-line change under a whole-file diff.
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Sync mcp/registry.json into pi and WorkBuddy.")
    ap.add_argument("--apply", action="store_true", help="write the files (default: dry run)")
    ap.add_argument("--only", choices=("pi", "workbuddy"), default="",
                    help="limit to one client")
    ap.add_argument("--profile", choices=ENGINES + ("all",), default="",
                    help="WorkBuddy: enable only this engine's servers (plus the shared "
                         "`any` ones) and disable the rest. Needs a client reload.")
    ap.add_argument("--print", dest="show", choices=ENGINES, default="",
                    help="print one pi profile and exit")
    ap.add_argument("--client", action="append", default=[], metavar="NAME[,NAME]",
                    help="also render repo-local configs for these MCP clients - see "
                         "mcp/clients.json. `--client all` renders every one.")
    ap.add_argument("--print-client", metavar="NAME", default="",
                    help="print one client's config block and exit - the way to configure "
                         "a client that is not listed in mcp/clients.json")
    a = ap.parse_args(argv[1:])

    registry = _load(REGISTRY, None)
    if not registry or "servers" not in registry:
        print(f"[ERROR] cannot read {REGISTRY}", file=sys.stderr)
        return 2
    ph = _placeholders()
    clients = _load_clients()

    if a.print_client:
        cdef = clients.get(a.print_client)
        if not cdef:
            print(f"[ERROR] unknown client {a.print_client!r}; known: "
                  f"{', '.join(sorted(clients))}", file=sys.stderr)
            return 2
        r = render_client(registry, cdef,
                          _placeholders(cdef.get("path_style", "absolute")))
        out = dict(r["payload"])
        _dig(out, r["root"]).update(r["servers"])
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0

    if a.show:
        print(json.dumps(render_pi(registry, a.show, ph), ensure_ascii=False, indent=2))
        return 0

    if a.profile == "all":
        a.profile = ""
    if a.profile and a.only == "pi":
        print("[ERROR] --profile applies to WorkBuddy; pi picks its profile from engine.json",
              file=sys.stderr)
        return 2
    if a.profile:
        a.only = "workbuddy"

    manifest = _load(MANIFEST, {})
    print(f"registry: {len(registry['servers'])} servers -> {', '.join(ENGINES)} + WorkBuddy")
    print(f"mode    : {'APPLY' if a.apply else 'dry run (--apply to write)'}")
    if a.profile:
        print(f"profile : workbuddy={a.profile} (other engines' servers are disabled, not removed)")

    if a.only in ("", "pi"):
        for engine, path in PI_PROFILE.items():
            existing = _load(path, {})
            current = existing.get("mcpServers", {})
            generated = render_pi(registry, engine, ph)["mcpServers"]
            label = path.parent.name
            owned = manifest.get(label, [])
            merged, touched, dropped = _merge(current, generated, owned, label,
                                              verbose=True)
            if a.apply and (touched or dropped or not path.exists()):
                payload = dict(existing)
                payload["autoEnableCodemode"] = False
                payload["mcpServers"] = merged
                _write(path, payload)
            manifest[label] = sorted(generated)

    if a.only in ("", "workbuddy"):
        existing = _load(WORKBUDDY_MCP, {"mcpServers": {}})
        current = existing.get("mcpServers", {})
        generated = (render_workbuddy_profile(registry, a.profile, ph) if a.profile
                     else render_workbuddy(registry, ph))
        owned = manifest.get("workbuddy", [])
        merged, touched, dropped = _merge(current, generated, owned, "workbuddy", verbose=True)
        if a.apply and (touched or dropped or not WORKBUDDY_MCP.exists()):
            payload = dict(existing)
            payload["mcpServers"] = merged
            _write(WORKBUDDY_MCP, payload)
        manifest["workbuddy"] = sorted(generated)
        print(f"  target : {WORKBUDDY_MCP}")
        active = sorted(name for name, entry in generated.items() if not entry.get("disabled"))
        off = sorted(name for name, entry in generated.items() if entry.get("disabled"))
        print(f"  active : {', '.join(active) or '(none)'}")
        if off:
            print(f"  off    : {', '.join(off)}")

    wanted: list[str] = []
    for spec in a.client:
        wanted += [s.strip() for s in spec.split(",") if s.strip()]
    if "all" in wanted:
        wanted = sorted(clients)
    for cname in dict.fromkeys(wanted):
        cdef = clients.get(cname)
        if not cdef:
            print(f"[ERROR] unknown client {cname!r}; known: "
                  f"{', '.join(sorted(clients))}", file=sys.stderr)
            return 2
        style = cdef.get("path_style", "absolute")
        path = ROOT / cdef["path"]
        rendered = render_client(registry, cdef, _placeholders(style))
        payload = dict(_load(path, {}))
        for key, value in rendered["payload"].items():
            payload.setdefault(key, value)
        target = _dig(payload, rendered["root"])
        label = f"client-{cname}"
        merged, touched, dropped = _merge(target, rendered["servers"],
                                          manifest.get(label, []), label, verbose=True)
        target.clear()
        target.update(merged)
        if a.apply and (touched or dropped or not path.exists()):
            _write(path, payload)
        manifest[label] = sorted(rendered["servers"])
        print(f"  target : {path}")
        print(f"  mode   : {style} "
              f"({'committable' if cdef.get('commit') else 'local only'})")

    if a.apply:
        _write(MANIFEST, manifest)
        print("\nwritten. Restart the client(s) to pick the new server list up:")
        print("  pi       - next `agent.cmd` session")
        print("  WorkBuddy- Settings -> Connectors/MCP -> reload, or restart the app")
        print("  others   - reload the window / restart the client (see each client's docs)")
    else:
        print("\nnothing written. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
