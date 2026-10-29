#!/usr/bin/env python
"""Diagnose pi session logs for the failure modes that make a local model look "dumb".

`pi_log.py` already lists sessions and flags tool errors. This goes one level deeper into
the specific pathologies the Qwen3.5 9B runs show: a model that *does not think* despite
`reasoning: true`, that repeats the same tool call after the same error, that writes a
file and then re-writes it whole because an `edit` did not match, and that runs out of
context and gets compacted mid-task.

It is read-only: it never touches a session file and writes nothing.

    python tools/pi_diag.py                     # all sessions, table
    python tools/pi_diag.py --session 01a12f94  # one session in detail
    python tools/pi_diag.py --json              # machine-readable

The heuristics are named so a disagreement is easy to spot, not hidden in a score:
    thin_thinking   assistant turns with a thinking block whose text is < 40 chars.
                    A reasoning model that "thinks" in one short sentence is not
                    deliberating - it is pattern-matching straight into a tool call.
    no_thinking     assistant turns with NO thinking block at all.
    repeat_error    the same tool called again with arguments identical to a *failed*
                    call - the textbook "stuck" loop.
    rewrite_whole   a `bash` call using a heredoc (`cat > file << EOF`) to rewrite a file
                    the agent already wrote. Bypasses the edit/write budget and hides the
                    real diff.
    compaction      the session hit the context limit mid-task.
    write_truncated a write rejected because the answer exceeded the output token budget.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

PROFILE_HOMES = tuple(
    d for d in (ROOT / "pi-home", ROOT / "pi-home-three",
                ROOT / "pi-home-godot", ROOT / "pi-home-unity")
    if d.is_dir()
)
SESSIONS_DIRS = [d / "sessions" for d in PROFILE_HOMES]

THIN_CHARS = 40
HEREDOC_RE = re.compile(r"<<-?\s*['\"]?[A-Za-z_][A-Za-z0-9_]*['\"]?")


def session_files() -> list[Path]:
    out: list[Path] = []
    for d in SESSIONS_DIRS:
        if d.is_dir():
            out.extend(sorted(d.glob("*/*.jsonl")))
    return sorted(out, key=lambda p: p.stat().st_mtime)


def _content(msg: dict):
    c = msg.get("content")
    return c if isinstance(c, list) else []


def analyse(path: Path) -> dict:
    records = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            continue

    think_lens: list[int] = []
    no_thinking = 0
    assistant = 0
    calls: list[tuple[str, str]] = []       # (tool name, serialised args)
    failed: dict[tuple[str, str], int] = {}
    repeat_error = 0
    heredocs = 0
    compactions = 0
    truncated = 0
    tools = Counter()

    for rec in records:
        typ = rec.get("type")
        if typ == "compaction":
            compactions += 1
            continue
        msg = rec.get("message")
        if not isinstance(msg, dict):
            continue
        role = msg.get("role")

        if role == "assistant":
            assistant += 1
            blocks = _content(msg)
            th = [b for b in blocks if isinstance(b, dict) and b.get("type") == "thinking"]
            if th:
                for b in th:
                    think_lens.append(len(str(b.get("thinking") or b.get("text") or "")))
            else:
                no_thinking += 1
            for b in blocks:
                if isinstance(b, dict) and b.get("type") == "toolCall":
                    tc = b.get("toolCall") or b
                    name = tc.get("name") or "?"
                    args = json.dumps(tc.get("arguments") or {}, sort_keys=True)
                    tools[name] += 1
                    calls.append((name, args))
                    if name == "bash" and HEREDOC_RE.search(str((tc.get("arguments") or {}).get("command", ""))):
                        heredocs += 1
                    last_by_name = (name, args)
        elif role == "toolResult":
            text = " ".join(str(b.get("text", "")) for b in _content(msg) if isinstance(b, dict))
            is_err = bool(msg.get("isError")) or "error" in text.lower() or "Traceback" in text
            if is_err and calls:
                name, args = calls[-1]
                key = (name, args)
                failed[key] = failed.get(key, 0) + 1
                if failed[key] >= 2:
                    repeat_error += 1
            if "over the budget for a single call" in text or "output token limit" in text:
                truncated += 1

    thin = sum(1 for n in think_lens if n < THIN_CHARS)
    return {
        "file": str(path),
        "name": path.name,
        "assistant_turns": assistant,
        "thinking_blocks": len(think_lens),
        "avg_think_chars": round(sum(think_lens) / len(think_lens), 1) if think_lens else 0,
        "min_think_chars": min(think_lens) if think_lens else 0,
        "max_think_chars": max(think_lens) if think_lens else 0,
        "thin_thinking": thin,
        "no_thinking": no_thinking,
        "tool_calls": sum(tools.values()),
        "tools": dict(tools),
        "repeat_error": repeat_error,
        "heredoc_rewrites": heredocs,
        "compactions": compactions,
        "write_truncated": truncated,
    }


def print_table(rows: list[dict]) -> None:
    print(f"{'session':30s} {'asst':>5s} {'think':>5s} {'avg':>5s} {'thin':>5s} "
          f"{'none':>5s} {'calls':>5s} {'rep-err':>7s} {'heredoc':>7s} {'cmp':>4s}")
    print("-" * 92)
    for r in rows:
        print(f"{r['name'][:30]:30s} {r['assistant_turns']:5d} {r['thinking_blocks']:5d} "
              f"{r['avg_think_chars']:5.0f} {r['thin_thinking']:5d} {r['no_thinking']:5d} "
              f"{r['tool_calls']:5d} {r['repeat_error']:7d} {r['heredoc_rewrites']:7d} "
              f"{r['compactions']:4d}")
    tot = Counter()
    for r in rows:
        tot["thin"] += r["thin_thinking"]
        tot["none"] += r["no_thinking"]
        tot["rep"] += r["repeat_error"]
        tot["heredoc"] += r["heredoc_rewrites"]
        tot["trunc"] += r["write_truncated"]
    print("-" * 92)
    print(f"TOTAL across {len(rows)} sessions: "
          f"thin_thinking={tot['thin']}  no_thinking={tot['none']}  "
          f"repeat_error={tot['rep']}  heredoc_rewrites={tot['heredoc']}  "
          f"write_truncated={tot['trunc']}")


def print_detail(r: dict) -> None:
    print(f"session : {r['name']}")
    print(f"file    : {r['file']}")
    print(f"assistant turns      : {r['assistant_turns']}")
    print(f"thinking blocks      : {r['thinking_blocks']} "
          f"(avg {r['avg_think_chars']} chars, min {r['min_think_chars']}, "
          f"max {r['max_think_chars']})")
    print(f"thin thinking (<{THIN_CHARS}) : {r['thin_thinking']}")
    print(f"no thinking at all   : {r['no_thinking']}")
    print(f"tool calls           : {r['tool_calls']}  {r['tools']}")
    print(f"repeated-failed calls: {r['repeat_error']}")
    print(f"heredoc whole-rewrite: {r['heredoc_rewrites']}")
    print(f"compactions          : {r['compactions']}")
    print(f"write truncated      : {r['write_truncated']}")


def main() -> int:
    p = argparse.ArgumentParser(description="Diagnose pi session logs for model pathologies.")
    p.add_argument("--session", default="", help="id prefix, name, or full path")
    p.add_argument("--json", action="store_true", help="emit JSON")
    a = p.parse_args()

    files = session_files()
    if not files:
        print("no sessions found", file=sys.stderr)
        return 2

    if a.session:
        match = [f for f in files if a.session in f.name or a.session in str(f)]
        if not match:
            print(f"no session matching {a.session!r}", file=sys.stderr)
            return 2
        rows = [analyse(match[0])]
        if a.json:
            print(json.dumps(rows[0], ensure_ascii=False, indent=2))
        else:
            print_detail(rows[0])
        return 0

    rows = [analyse(f) for f in files]
    if a.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        print_table(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
