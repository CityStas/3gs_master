#!/usr/bin/env python
"""Read pi session logs: what the agent actually did, and where it went wrong.

pi writes one JSONL file per session to `<agent-dir>/sessions/<slugified-cwd>/<ts>_<id>.jsonl`,
where `<agent-dir>` is whatever `PI_CODING_AGENT_DIR` named - `agent.cmd` picks
`pi-home-three` / `pi-home-godot` / `pi-home-unity` per engine, so all four profiles are
searched (see `SESSIONS_DIRS`).
That file is the whole truth about a run - every thinking block, every tool call, every
tool result - and it is the only place where a failure that pi recovered from silently
is still visible. A `write` rejected by the output token limit, a scaffolder answered
"Operation cancelled", an `npm` run in the wrong directory: none of that reaches the
chat window, but all of it is in here.

Record types
------------
    {"type": "session",              ... "cwd", "id", "version"}      once, at the top
    {"type": "model_change",         ... "provider", "modelId"}
    {"type": "thinking_level_change"}
    {"type": "message", "message": {...}}

`message.role` is `user`, `assistant` or `toolResult`. Assistant content parts are
`text`, `thinking` and `toolCall` (camelCase - note the capital C); a `toolResult`
carries `toolName`, `toolCallId` and `isError`.

Usage
-----
    python tools/pi_log.py                     # list this project's sessions
    python tools/pi_log.py --last              # summarise the newest one
    python tools/pi_log.py --last --errors     # only the problems
    python tools/pi_log.py --last --tail 6     # ... plus the last few messages
    python tools/pi_log.py --session 01a116ba  # by id prefix, or a full path
    python tools/pi_log.py --last --json
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from threejs import config  # noqa: E402

#: pi writes one JSONL per session into the *agent dir it was launched with*, i.e.
#: `PI_CODING_AGENT_DIR/sessions/<slugified-cwd>/`. `agent.cmd` picks that dir per engine
#: (`pi-home-three` / `pi-home-godot` / `pi-home-unity`), so since the per-engine profile
#: split a session from any real run lands OUTSIDE `pi-home/` and this tool reported
#: "no sessions" while sessions existed. Look in every profile.
PROFILE_HOMES = tuple(
    d for d in (
        config.THREE_RAG_HOME / "pi-home",
        config.THREE_RAG_HOME / "pi-home-three",
        config.THREE_RAG_HOME / "pi-home-godot",
        config.THREE_RAG_HOME / "pi-home-unity",
    ) if d.is_dir()
)
SESSIONS_DIRS = [d / "sessions" for d in PROFILE_HOMES]
#: Kept for the messages and for the "nothing at all" case.
SESSIONS_DIR = SESSIONS_DIRS[0] if SESSIONS_DIRS else config.THREE_RAG_HOME / "pi-home" / "sessions"

#: Text that means "this did not work", with why it matters. `isError` catches most of
#: it, but the harness-level rejections (a tool call the model never got to make) come
#: back as ordinary text with `isError` unset.
PATTERNS = (
    ("not executed", "tool call rejected by the harness before it ran"),
    ("Operation cancelled", "an interactive prompt was answered 'cancel'"),
    ("error TS", "TypeScript error"),
    ("npm error", "npm failed"),
    ("ENOENT", "path not found"),
    ("Command failed", "shell command failed"),
    ("Traceback (most recent call last)", "python exception"),
    ("EADDRINUSE", "port already in use"),
    ("ENOSPC", "out of disk"),
)


def _header(path: Path) -> dict:
    """The `session` record, read without parsing the whole file."""
    try:
        with path.open(encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if line.strip():
                    return json.loads(line)
    except (OSError, json.JSONDecodeError):
        pass
    return {}


def _records(path: Path) -> list[dict]:
    out = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue          # a session killed mid-write leaves a truncated last line
    return out


def find_sessions(cwd: str | Path | None = None) -> list[dict]:
    rows = []
    seen: set[Path] = set()
    for sessions_dir in SESSIONS_DIRS:
        if not sessions_dir.exists():
            continue
        for path in sessions_dir.glob("*/*.jsonl"):
            if path in seen:          # a profile symlinked into another must not double-count
                continue
            seen.add(path)
            header = _header(path)
            if cwd and header.get("cwd"):
                try:
                    if Path(header["cwd"]).resolve() != Path(cwd).resolve():
                        continue
                except OSError:
                    pass
            stat = path.stat()
            rows.append({"path": path, "id": header.get("id", "?"), "cwd": header.get("cwd", "?"),
                         "started": header.get("timestamp", "?"), "mtime": stat.st_mtime,
                         "bytes": stat.st_size})
    rows.sort(key=lambda r: r["mtime"], reverse=True)
    return rows


def count_records(path: Path) -> int:
    """Cheap line count - the listing must not parse every session in full."""
    try:
        with path.open(encoding="utf-8", errors="replace") as fh:
            return sum(1 for line in fh if line.strip())
    except OSError:
        return 0


def pick(spec: str, cwd: str | Path | None) -> Path:
    candidate = Path(spec)
    if candidate.exists():
        return candidate
    for row in find_sessions(cwd):
        if str(row["id"]).startswith(spec):
            return row["path"]
    raise SystemExit(f"no session matching {spec!r} for cwd {cwd}")


def summarise(path: Path) -> dict:
    records = _records(path)
    header = records[0] if records and records[0].get("type") == "session" else {}
    model = next((r for r in records if r.get("type") == "model_change"), {})

    calls: list[dict] = []          # every toolCall, in order
    results: dict[str, dict] = {}   # toolCallId -> what came back
    problems: list[dict] = []
    texts: list[dict] = []
    roles = Counter()

    for record in records:
        message = record.get("message") or {}
        role = message.get("role")
        if role:
            roles[role] += 1
        parts = message.get("content")
        if not isinstance(parts, list):
            continue
        blob = "\n".join(p.get("text", "") for p in parts if isinstance(p, dict))

        if role == "toolResult":
            # Note the shape: the *message* role is `toolResult`, the content part is an
            # ordinary `text`. Branching on the part type here silently finds nothing and
            # reports a clean run.
            results[message.get("toolCallId")] = {
                "isError": bool(message.get("isError")), "tool": message.get("toolName"),
                "t": record.get("timestamp"), "text": blob,
            }
            reasons = [why for needle, why in PATTERNS if needle in blob]
            if message.get("isError") and not reasons:
                reasons = ["tool reported an error"]
            if reasons:
                problems.append({"tool": message.get("toolName"), "why": "; ".join(reasons),
                                 "t": record.get("timestamp"), "text": blob[:600]})
            continue

        for part in parts:
            if not isinstance(part, dict):
                continue
            kind = part.get("type")
            if kind == "toolCall":
                calls.append({"name": part.get("name"), "id": part.get("id"),
                              "args": part.get("arguments") or {}, "t": record.get("timestamp")})
            elif kind == "text" and role == "assistant":
                texts.append({"t": record.get("timestamp"), "text": part.get("text", "")})

    # A toolCall with no matching toolResult never ran - the model hit the response
    # budget mid-call, which is a hard failure that produces no error record at all.
    dangling = [c for c in calls if c["id"] and c["id"] not in results]

    # "Files written" must mean *landed on disk*. Counting toolCall arguments instead
    # would have listed world/World.ts, whose 28 KB write was rejected outright.
    written: list[str] = []
    rejected: list[dict] = []
    for call in calls:
        if call["name"] not in ("write", "edit"):
            continue
        target = call["args"].get("path") or call["args"].get("file_path")
        if not target:
            continue
        outcome = results.get(call["id"])
        if outcome is None:
            rejected.append({"path": str(target), "t": call["t"],
                             "why": "no result recorded - the call never completed"})
        elif outcome["isError"]:
            rejected.append({"path": str(target), "t": call["t"],
                             "why": outcome["text"].strip().splitlines()[0][:200]})
        else:
            written.append(str(target))

    first, last = (records[0].get("timestamp"), records[-1].get("timestamp")) if records else ("?", "?")
    return {
        "path": str(path), "id": header.get("id"), "cwd": header.get("cwd"),
        "provider": model.get("provider"), "model": model.get("modelId"),
        "started": first, "ended": last, "records": len(records),
        "roles": dict(roles),
        "tools": dict(Counter(c["name"] for c in calls).most_common()),
        "calls": len(calls), "written": written, "rejected": rejected, "problems": problems,
        "dangling": [{"name": c["name"], "args": str(c["args"])[:120], "t": c["t"]} for c in dangling],
        "last_text": texts[-1]["text"] if texts else "",
    }


def render(report: dict, tail: int = 0, errors_only: bool = False) -> None:
    print(f"session : {report['id']}  ({report['path']})")
    print(f"cwd     : {report['cwd']}")
    print(f"model   : {report['provider']}/{report['model']}")
    print(f"window  : {report['started']} -> {report['ended']}   {report['records']} records")
    print(f"roles   : {report['roles']}")
    print(f"tools   : {report['calls']} calls  {report['tools']}")

    written = report["written"]
    if written and not errors_only:
        print(f"\nfiles written ({len(written)}):")
        for name, n in Counter(written).most_common():
            print(f"  {n}x  {name}")

    if report["rejected"]:
        print(f"\nwrites that did NOT land ({len(report['rejected'])}):")
        for r in report["rejected"]:
            print(f"  [{r['t']}] {r['path']}")
            print(f"      {r['why']}")

    problems = report["problems"]
    print(f"\nproblems ({len(problems)}):" if problems else "\nproblems: none")
    for p in problems:
        head = p["text"].strip().splitlines()[0][:150] if p["text"].strip() else "(empty)"
        print(f"  [{p['t']}] {p['tool']}: {p['why']}")
        print(f"      {head}")

    if report["dangling"]:
        print(f"\nunanswered tool calls ({len(report['dangling'])}) - the model never got to run these:")
        for d in report["dangling"]:
            print(f"  [{d['t']}] {d['name']}  {d['args']}")

    if tail:
        print(f"\nlast assistant message:\n  {report['last_text'][:1200]}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Read pi session logs.")
    ap.add_argument("--last", action="store_true", help="summarise the newest session")
    ap.add_argument("--session", "-s", default="", help="session id prefix or a full path")
    ap.add_argument("--project", "-p", default=str(ROOT),
                    help="only sessions whose cwd is this directory (default: the repo root)")
    ap.add_argument("--all-projects", action="store_true", help="ignore the cwd filter")
    ap.add_argument("--errors", action="store_true", help="problems only")
    ap.add_argument("--tail", type=int, default=0, help="also print the last assistant message")
    ap.add_argument("--json", action="store_true", help="raw report")
    a = ap.parse_args()

    cwd = None if a.all_projects else a.project

    if not a.last and not a.session:
        rows = find_sessions(cwd)
        if not rows:
            print(f"no sessions under {', '.join(str(d) for d in SESSIONS_DIRS)} for {cwd}")
            return 1
        print(f"{'started':<26} {'records':>8}  {'size':>9}  id")
        for row in rows[:25]:
            print(f"{row['started']:<26} {count_records(row['path']):>8}  "
                  f"{row['bytes'] / 1024:>8.1f}K  {row['id']}")
        print(f"\n{len(rows)} session(s). Summarise one with:  python tools/pi_log.py --last")
        return 0

    path = pick(a.session, cwd) if a.session else find_sessions(cwd)[0]["path"]
    report = summarise(path)
    if a.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        render(report, tail=a.tail, errors_only=a.errors)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
