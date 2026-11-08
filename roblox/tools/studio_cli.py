#!/usr/bin/env python
"""Call the built-in Roblox Studio MCP server from the shell (stdio, no client UI).

    python roblox/tools/studio_cli.py list
    python roblox/tools/studio_cli.py tools
    python roblox/tools/studio_cli.py call execute_luau '{"code": "print(1)"}'

Why this exists: WorkBuddy / pi enumerate an MCP server's tool list once, when the
session starts. If Studio was closed at that moment the `roblox-studio` server advertises
zero tools for the whole session, even after Studio comes up. This CLI spawns the same
server (`%LOCALAPPDATA%\\Roblox\\mcp.bat` -> StudioMCP.exe) on demand, so the live
DataModel stays reachable without restarting the agent.

The server reports an empty list when Studio is not open, or when
Assistant -> ... -> Manage MCP Servers -> "Enable Studio as MCP server" is off.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = Path(__file__).resolve().parents[2]


def _params() -> StdioServerParameters:
    local = os.environ.get("LOCALAPPDATA", "")
    bat = Path(local) / "Roblox" / "mcp.bat"
    return StdioServerParameters(command="cmd.exe", args=["/c", str(bat)], cwd=str(ROOT))


async def _first_studio(session, wait: float) -> str:
    deadline = asyncio.get_event_loop().time() + wait
    while True:
        res = await session.call_tool("list_roblox_studios", {})
        text = "".join(getattr(b, "text", "") or "" for b in res.content)
        try:
            studios = json.loads(text).get("studios") or []
        except json.JSONDecodeError:
            studios = []
        if studios:
            return studios[0]["id"]
        if asyncio.get_event_loop().time() >= deadline:
            raise SystemExit("no Studio attached: " + text.strip())
        await asyncio.sleep(1.5)


async def _batch(session, a: argparse.Namespace) -> int:
    """Run a list of tool calls inside ONE proxy session.

    A per-call proxy means Studio has to re-attach for every single call, and it gives up
    after a few failed retries. A batch keeps one connection for a whole scenario
    (state -> play -> wait -> console -> capture -> stop).
    """
    steps = json.loads(Path(a.file).read_text(encoding="utf-8"))
    studio = a.studio or await _first_studio(session, a.wait)
    print(f"# studio {studio}")
    for index, step in enumerate(steps, 1):
        if "sleep" in step:
            await asyncio.sleep(float(step["sleep"]))
            continue
        tool = step["tool"]
        args = dict(step.get("args") or {})
        # Long Luau bodies belong in a .luau file next to the scenario, not in a JSON
        # string literal: escaping a 60-line script by hand is how scenarios rot.
        if "code_file" in step:
            base = Path(a.file).resolve().parent
            args["code"] = (base / step["code_file"]).read_text(encoding="utf-8")
        if args.pop("studio", "auto") == "auto":
            args["studio_id"] = studio
        res = await session.call_tool(tool, args)
        body = "\n".join(getattr(b, "text", "") or f"<{getattr(b, 'type', '?')}>" for b in res.content)
        if a.quiet and not res.isError:
            body = body.splitlines()[0][:200] if body else ""
        print(f"\n## {index}. {tool}{'  [ERROR]' if res.isError else ''}")
        # Image blocks (screen captures) are base64 payloads; write them out so they can be
        # opened instead of printed as "<image>".
        for block in res.content:
            data = getattr(block, "data", None)
            if getattr(block, "type", "") == "image" and data:
                import base64
                out_dir = Path(a.file).resolve().parent / "captures"
                out_dir.mkdir(exist_ok=True)
                name = f"{step.get('args', {}).get('capture_id', 'capture')}.png"
                out_path = out_dir / name
                out_path.write_bytes(base64.b64decode(data))
                print(f"saved {out_path}")
        print(body[:a.max_chars])
        if res.isError and a.stop_on_error:
            return 1
    return 0


async def _run(a: argparse.Namespace) -> int:
    async with stdio_client(_params()) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            if a.cmd == "tools":
                listed = await session.list_tools()
                for t in listed.tools:
                    print(f"{t.name}")
                    desc = (t.description or "").strip().splitlines()
                    if desc:
                        print(f"    {desc[0][:160]}")
                print(f"\n{len(listed.tools)} tool(s)")
                return 0

            if a.cmd == "schema":
                listed = await session.list_tools()
                for t in listed.tools:
                    if t.name == a.tool:
                        print(json.dumps(t.inputSchema, indent=2, ensure_ascii=False))
                        return 0
                print(f"[ERROR] no such tool: {a.tool}", file=sys.stderr)
                return 2

            args = json.loads(getattr(a, "json", "") or "{}")

            if a.cmd == "batch":
                return await _batch(session, a)

            if a.cmd == "luau":
                body = Path(a.file).read_text(encoding="utf-8")
                for old, new in a.replace:
                    if old not in body:
                        print(f"[ERROR] --replace: not found: {old!r}", file=sys.stderr)
                        return 2
                    body = body.replace(old, new, 1)
                args = {"code": body, "datamodel_type": a.datamodel}
                if a.studio:
                    args["studio_id"] = a.studio
                res = await session.call_tool("execute_luau", args)
            elif a.cmd == "list":
                # Studio re-attaches to whatever proxy is listening on its fixed local port,
                # and it retries every few seconds. A freshly spawned proxy therefore needs
                # a moment before list_roblox_studios sees anything.
                res = await session.call_tool("list_roblox_studios", {})
                deadline = asyncio.get_event_loop().time() + a.wait
                while a.wait > 0 and asyncio.get_event_loop().time() < deadline:
                    text = "".join(getattr(b, "text", "") or "" for b in res.content)
                    if '"studios":[]' not in text.replace(" ", ""):
                        break
                    await asyncio.sleep(1.5)
                    res = await session.call_tool("list_roblox_studios", {})
            else:
                res = await session.call_tool(a.tool, args)

            for block in res.content:
                text = getattr(block, "text", None)
                print(text if text is not None else block)
            if res.isError:
                return 1
            return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Roblox Studio MCP shell client.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    ls = sub.add_parser("list", help="list_roblox_studios")
    ls.add_argument("--wait", type=float, default=0.0,
                    help="seconds to keep polling while no Studio is attached")
    sub.add_parser("tools", help="tool names advertised by the server")
    s = sub.add_parser("schema", help="input schema of one tool")
    s.add_argument("tool")
    c = sub.add_parser("call", help="call any tool with JSON arguments")
    c.add_argument("tool")
    c.add_argument("json", nargs="?", default="")
    l = sub.add_parser("luau", help="execute_luau with the body of a .luau file")
    l.add_argument("file")
    l.add_argument("--datamodel", default="Edit", choices=["Edit", "Client", "Server"])
    l.add_argument("--studio", default="")
    l.add_argument("--replace", action="append", default=[], nargs=2, metavar=("OLD", "NEW"),
                   help="exact substring replacement in the file body, repeatable")
    b = sub.add_parser("batch", help="run a JSON list of tool calls in one session")
    b.add_argument("file")
    b.add_argument("--studio", default="")
    b.add_argument("--wait", type=float, default=25.0)
    b.add_argument("--quiet", action="store_true", help="first line of each result only")
    b.add_argument("--max-chars", type=int, default=4000)
    b.add_argument("--stop-on-error", action="store_true")
    a = ap.parse_args()
    return asyncio.run(_run(a))


if __name__ == "__main__":
    raise SystemExit(main())
