#!/usr/bin/env python
"""The Python half of the reliability layer: same policy, same answers, plus the CLI.

Why two implementations and not one: the live guard has to run inside `pi`, which is a
Node process, so it is TypeScript (`pi-extensions/reliability-core.ts`). Everything else -
MCP servers, the launchers, the tests, the diagnostics - is Python. Both read
`mcp/reliability.json`, and `tests/reliability_parity.mjs` runs the TypeScript one under
plain node and asserts the two produce identical classifications and identical loop
verdicts for the same fixture. A threshold changed in the policy file therefore changes
both, and a change to one implementation that the other does not follow fails the test.

What the state tracker is, and what it deliberately is not
---------------------------------------------------------
There is no separate state file. The extension already writes one JSONL line per tool
call with the tool, the outcome, the error code and the verification result; a second
file saying the same thing would be a second thing to fall out of sync. `state` reads
that log back and renders it as a per-run step list - the minimum needed to answer "did
this already succeed?" and "what actually failed?" without trusting the model's summary.

Usage
-----
    python tools/reliability.py status                 # policy + last run summary
    python tools/reliability.py state [--run ID]       # step list for one run
    python tools/reliability.py log --tail 40          # the raw events, newest last
    python tools/reliability.py log --code FILE_NOT_FOUND
    python tools/reliability.py verify <path>          # postcondition check on one file
    python tools/reliability.py classify "No such file or directory: foo.ts"
    python tools/reliability.py prune                  # enforce the retention policy
    python tools/reliability.py selftest               # the policy's own regression suite

Every command takes `--json` and prints machine-readable output instead of a table.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY_FILE = ROOT / "mcp" / "reliability.json"

#: Fallback copied from mcp/reliability.json. tests/test_reliability.py asserts equality,
#: so this can never quietly become a second policy.
DEFAULT_POLICY: dict = {
    "loop_guard": {
        "enabled": True,
        "max_identical_failures": 1,
        "max_identical_failures_transient": 3,
        "cycle_length": 4,
        "cycle_repeats": 2,
        "max_tracked_fingerprints": 256,
    },
    "duplicate_success": {
        "enabled": True,
        "tools": ["write", "edit"],
        "generation_tools": ["write", "edit", "bash", "powershell"],
        "max_duplicates": 1,
    },
    "write_guard": {"enabled": True, "max_bytes": 12000, "max_lines": 320, "max_rewrites": 3},
    "progress_guard": {
        "enabled": True,
        "block_after_inspections": 20,
        "require_zero_mutations": True,
        "inspection_tools": ["read", "ls", "grep", "find"],
        "inspection_bash_prefixes": [
            "ls", "cat", "sed", "head", "tail", "grep", "rg", "find", "wc", "type", "which",
            "pwd", "echo", "cd", "git status", "git log", "git diff", "dir", "stat", "file", "du",
        ],
    },
    "write_verification": {"enabled": True, "mtime_freshness_ms": 120000, "tools": ["write", "edit"]},
    "path_guard": {"enabled": True, "block_outside_repo": True, "warn_outside_project": True},
    "logging": {"enabled": True, "dir": "logs/reliability", "max_files": 14, "max_bytes_per_file": 2097152},
    "state": {"enabled": True, "dir": "data/reliability", "max_runs_kept": 40},
    "errors": {
        "codes": {
            "REPEATED_TOOL_CALL": {"retryable": False, "next_action": "Do not repeat this call. Inspect the parent directory, verify the active project, search for the name, or change the arguments."},
            "TOOL_CYCLE_DETECTED": {"retryable": False, "next_action": "Two calls are alternating without progress. Stop both, re-read the last error, and change strategy - a different tool or a different argument."},
            "DUPLICATE_SUCCESS": {"retryable": False, "next_action": "This exact call already succeeded in the current state. Read the earlier result or move to the next step."},
            "NO_PROGRESS": {"retryable": False, "next_action": "Stop inspecting. Nothing has been written yet: create the first file with `write` (a small one, then extend it with `edit`). Further reads will be refused until something is on disk."},
            "FILE_NOT_FOUND": {"retryable": False, "next_action": "List the parent directory or search for the filename; do not retry this path unchanged."},
            "PATH_OUTSIDE_SANDBOX": {"retryable": False, "next_action": "Write inside the repository (and inside the active project when there is one). Use an absolute path only when the repository itself is the target."},
            "PERMISSION_DENIED": {"retryable": False, "next_action": "Report the permission boundary and ask for an authorized alternative; repeating the same call will fail identically."},
            "INVALID_ARGUMENT": {"retryable": False, "next_action": "Correct the arguments against the tool schema. Do not resend the same payload."},
            "TIMEOUT": {"retryable": True, "next_action": "Check whether the server is healthy before retrying; retry once only if the operation is idempotent."},
            "SERVER_UNAVAILABLE": {"retryable": True, "next_action": "The MCP server or model endpoint is down. Start or restart it, then retry at most once."},
            "OUTPUT_TOO_LARGE": {"retryable": False, "next_action": "Reduce the payload: ranged read, narrower grep, or split the write into a first chunk plus edits."},
            "VALIDATION_FAILED": {"retryable": False, "next_action": "Read the validator's actual message and patch the cause; do not resend the same code."},
            "WRITE_NOT_VERIFIED": {"retryable": False, "next_action": "The tool claimed success but the file on disk did not change. Re-read the file and retry the write with correct content."},
            "UNKNOWN": {"retryable": False, "next_action": "Read the error text and change something before calling again."},
        },
        "patterns": [
            ["REPEATED_TOOL_CALL", ["repeated tool call", "already failed identically"]],
            ["TOOL_CYCLE_DETECTED", ["tool cycle"]],
            ["DUPLICATE_SUCCESS", ["already succeeded in this state"]],
            ["NO_PROGRESS", ["nothing has been written yet", "no progress"]],
            ["WRITE_NOT_VERIFIED", ["write not verified"]],
            ["PATH_OUTSIDE_SANDBOX", ["outside the repository", "outside the project", "path escapes", "sandbox"]],
            ["FILE_NOT_FOUND", ["no such file", "cannot find the file", "file not found", "does not exist", "enoent", "not found"]],
            ["PERMISSION_DENIED", ["permission denied", "eacces", "eperm", "access is denied", "access denied", "unauthorized", "forbidden"]],
            ["OUTPUT_TOO_LARGE", ["output token limit", "maximum context", "context length", "too large", "truncated", "exceeds the maximum", "response was cut"]],
            ["TIMEOUT", ["timed out", "timeout", "etimedout", "deadline exceeded"]],
            ["SERVER_UNAVAILABLE", ["econnrefused", "connection refused", "connection reset", "server unavailable", "not connected", "no studios connected", "failed to start", "epipe"]],
            ["VALIDATION_FAILED", ["error ts", "syntax error", "validation failed", "lint error", "failed to parse", "unexpected token", "is not valid json", "exit code 1"]],
            ["INVALID_ARGUMENT", ["invalid argument", "invalid params", "invalid type", "expected string", "must be a", "eisdir", "is a directory", "missing required"]],
        ],
    },
}


# ---------------------------------------------------------------------------
# Policy
# ---------------------------------------------------------------------------

def load_policy(root: Path | None = None) -> dict:
    """`mcp/reliability.json`, merged over the defaults section by section."""
    root = Path(root or ROOT)
    file = root / "mcp" / "reliability.json"
    try:
        raw = json.loads(file.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return json.loads(json.dumps(DEFAULT_POLICY))  # deep copy
    out = json.loads(json.dumps(DEFAULT_POLICY))
    for key, value in raw.items():
        if key.startswith("$"):
            continue
        if key == "errors" and isinstance(value, dict):
            out["errors"]["codes"].update(value.get("codes") or {})
            if value.get("patterns"):
                out["errors"]["patterns"] = value["patterns"]
        elif isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key].update({k: v for k, v in value.items() if not k.startswith("$")})
        else:
            out[key] = value
    return out


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------

def classify(message: str, policy: dict | None = None, hint: str | None = None) -> dict:
    policy = policy or DEFAULT_POLICY
    text = (message or "").lower()
    code = hint
    if code is None:
        code = "UNKNOWN"
        for candidate, needles in policy["errors"]["patterns"]:
            if any(needle in text for needle in needles):
                code = candidate
                break
    entry = policy["errors"]["codes"].get(code) or policy["errors"]["codes"]["UNKNOWN"]
    return {"code": code, "retryable": bool(entry["retryable"]), "next_action": entry["next_action"]}


def error_payload(code: str, operation: str, policy: dict | None = None, **fields) -> str:
    """The model-facing contract of section 4.8, as the JSON string both clients read."""
    policy = policy or DEFAULT_POLICY
    cls = classify("", policy, hint=code)
    body = {
        "ok": False,
        "error_code": code,
        "retryable": cls["retryable"],
        "operation": operation,
        "message": fields.pop("message", None) or cls["next_action"],
        "next_action": cls["next_action"],
    }
    body.update({k: v for k, v in fields.items() if v is not None})
    return json.dumps(body, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Fingerprints
# ---------------------------------------------------------------------------

def stable_stringify(value) -> str:
    if value is None or not isinstance(value, (dict, list, str, int, float, bool)):
        return "null" if value is None else json.dumps(value)
    if isinstance(value, list):
        return "[" + ",".join(stable_stringify(v) for v in value) + "]"
    if isinstance(value, dict):
        return "{" + ",".join(
            f"{json.dumps(k)}:{stable_stringify(value[k])}" for k in sorted(value)
        ) + "}"
    return json.dumps(value, ensure_ascii=False)


def server_of(tool_name: str) -> str:
    idx = tool_name.find("__")
    return tool_name[:idx] if idx > 0 else "builtin"


def fingerprint(tool_name: str, args: dict, context: str = "") -> str:
    material = stable_stringify(
        {"server": server_of(tool_name), "tool": tool_name, "args": args or {}, "ctx": context}
    )
    return hashlib.sha1(material.encode("utf-8")).hexdigest()[:16]


# ---------------------------------------------------------------------------
# Loop guard (mirror of the TypeScript one)
# ---------------------------------------------------------------------------

class LoopGuard:
    """Same rules as `LoopGuard` in pi-extensions/reliability-core.ts."""

    TRANSIENT = ("TIMEOUT", "SERVER_UNAVAILABLE", "OUTPUT_TOO_LARGE")

    def __init__(self, policy: dict | None = None):
        self.policy = policy or DEFAULT_POLICY
        self.failures: dict[str, dict] = {}
        self.order: list[str] = []
        self.history: list[tuple[str, str]] = []
        self.blocked = 0

    def reset(self) -> None:
        self.failures.clear()
        self.order.clear()
        self.history.clear()
        self.blocked = 0

    def before(self, tool_name: str, args: dict, context: str = "") -> dict:
        cfg = self.policy["loop_guard"]
        if not cfg["enabled"]:
            return {"decision": "allow"}
        fp = fingerprint(tool_name, args, context)
        # Cycle first, repeat second - same ordering and same reason as the TypeScript
        # guard: A -> B -> A -> B is a failure of the PAIR, and with
        # max_identical_failures=1 the repeat check would always shadow it.
        cycle = self._detect_cycle(fp)
        if cycle:
            self.blocked += 1
            cls = classify("", self.policy, hint="TOOL_CYCLE_DETECTED")
            return {
                "decision": "block",
                "code": "TOOL_CYCLE_DETECTED",
                "attempts": cycle,
                "retryable": False,
                "message": (
                    f"{cycle} calls have been alternating between two tools and failing each "
                    f"time - neither one is making progress."
                ),
                "next_action": cls["next_action"],
            }
        record = self.failures.get(fp)
        if record:
            transient = record["code"] in self.TRANSIENT
            limit = cfg["max_identical_failures_transient"] if transient else cfg["max_identical_failures"]
            if record["count"] >= limit:
                self.blocked += 1
                cls = classify("", self.policy, hint="REPEATED_TOOL_CALL")
                return {
                    "decision": "block",
                    "code": "REPEATED_TOOL_CALL",
                    "attempts": record["count"],
                    "retryable": False,
                    "message": (
                        f"this exact call to {record['tool']} has already failed "
                        f"{record['count']}x with {record['code']}, and nothing changed in between."
                    ),
                    "next_action": cls["next_action"],
                }
        return {"decision": "allow"}

    def after(self, tool_name: str, args: dict, is_error: bool, code: str | None = None, context: str = "") -> None:
        cfg = self.policy["loop_guard"]
        if not cfg["enabled"]:
            return
        fp = fingerprint(tool_name, args, context)
        if not is_error:
            self.failures.pop(fp, None)
            if fp in self.order:
                self.order.remove(fp)
            return
        code = code or "UNKNOWN"
        record = self.failures.get(fp)
        if record and record["code"] == code:
            record["count"] += 1
        else:
            if fp not in self.failures:
                self.order.append(fp)
                cap = cfg["max_tracked_fingerprints"]
                while len(self.order) > cap:
                    evicted = self.order.pop(0)
                    self.failures.pop(evicted, None)
            self.failures[fp] = {"code": code, "count": 1, "tool": tool_name}
        self.history.append((fp, code))
        window = cfg["cycle_length"] * cfg["cycle_repeats"]
        if len(self.history) > window:
            del self.history[: len(self.history) - window]

    def reset_on_mutation(self) -> None:
        """Forget counted failures; KEEP the cycle window (see the TypeScript twin)."""
        self.failures.clear()
        self.order.clear()

    def _detect_cycle(self, next_fp: str) -> int | None:
        cfg = self.policy["loop_guard"]
        length, reps = cfg["cycle_length"], cfg["cycle_repeats"]
        if length < 2 or reps < 2:
            return None
        period = max(2, length // reps)
        need = period * reps
        recent = [fp for fp, _ in self.history[-(need - 1):]]
        if len(recent) < need - 1:
            return None
        seq = recent + [next_fp]
        tail = seq[-period:]
        if len(set(tail)) != period:
            return None
        for block in range(reps):
            start = len(seq) - period * (block + 1)
            if seq[start:start + period] != tail:
                return None
        return need


# ---------------------------------------------------------------------------
# Duplicate-success ledger (mirror of the TypeScript one)
# ---------------------------------------------------------------------------

class SuccessLedger:
    """Same rules as `SuccessLedger` in pi-extensions/reliability-core.ts.

    `generation` is the state version. It advances on every successful mutating call;
    a recorded success is only a duplicate while the version it was recorded at is
    still the current one. That is what makes `edit` -> `bash` -> `edit` -> `bash`
    legal while `write` -> `write` is not.
    """

    def __init__(self, policy: dict | None = None):
        self.policy = policy or DEFAULT_POLICY
        self.generation = 0
        self.seen: dict[str, dict] = {}

    def reset(self) -> None:
        self.generation = 0
        self.seen.clear()

    def _is_mutating(self, tool: str) -> bool:
        cfg = self.policy["duplicate_success"]
        return tool in cfg["tools"] or server_of(tool) in cfg["tools"]

    def _bumps(self, tool: str) -> bool:
        cfg = self.policy["duplicate_success"]
        return tool in cfg["generation_tools"] or server_of(tool) in cfg["generation_tools"]

    def before(self, tool_name: str, args: dict, context: str = "") -> dict:
        cfg = self.policy["duplicate_success"]
        if not cfg["enabled"] or not self._is_mutating(tool_name):
            return {"decision": "allow"}
        fp = fingerprint(tool_name, args, context)
        hit = self.seen.get(fp)
        if hit and hit["generation"] == self.generation and hit["count"] >= cfg["max_duplicates"]:
            cls = classify("", self.policy, hint="DUPLICATE_SUCCESS")
            return {
                "decision": "block",
                "code": "DUPLICATE_SUCCESS",
                "attempts": hit["count"],
                "retryable": False,
                "message": (
                    f"this exact {tool_name} call already succeeded in this state "
                    f"(generation {self.generation})."
                ),
                "next_action": cls["next_action"],
            }
        return {"decision": "allow"}

    def after(self, tool_name: str, args: dict, is_error: bool, context: str = "") -> None:
        if not self.policy["duplicate_success"]["enabled"] or is_error:
            return
        if self._bumps(tool_name):
            self.generation += 1
        if not self._is_mutating(tool_name):
            return
        fp = fingerprint(tool_name, args, context)
        hit = self.seen.get(fp)
        if hit and hit["generation"] == self.generation:
            hit["count"] += 1
        else:
            self.seen[fp] = {"generation": self.generation, "count": 1, "tool": tool_name}


# ---------------------------------------------------------------------------
# Progress guard (mirror of the TypeScript one)
# ---------------------------------------------------------------------------

def is_inspection(tool_name: str, args: dict, policy: dict | None = None) -> bool:
    """Mirror of `isInspection` in reliability-core.ts - see there for the reasoning."""
    policy = policy or DEFAULT_POLICY
    cfg = policy["progress_guard"]
    if tool_name in cfg["inspection_tools"]:
        return True
    if tool_name not in ("bash", "powershell"):
        return False
    command = args.get("command") if isinstance(args, dict) else ""
    if not isinstance(command, str) or not command.strip():
        return False
    import re

    segments = [s.strip() for s in re.split(r"\|\||&&|;|\|", command) if s.strip()]
    if not segments:
        return False
    for segment in segments:
        lower = segment.lower()
        if not any(lower == p or lower.startswith(p + " ") for p in cfg["inspection_bash_prefixes"]):
            return False
    return True


class ProgressGuard:
    """Same rules as `ProgressGuard` in pi-extensions/reliability-core.ts."""

    def __init__(self, policy: dict | None = None):
        self.policy = policy or DEFAULT_POLICY
        self.inspections = 0
        self.mutations = 0
        self.blocked = 0

    def reset(self) -> None:
        self.inspections = 0
        self.mutations = 0
        self.blocked = 0

    def before(self, tool_name: str, args: dict, context: str = "") -> dict:
        cfg = self.policy["progress_guard"]
        if not cfg["enabled"]:
            return {"decision": "allow"}
        if cfg["require_zero_mutations"] and self.mutations > 0:
            return {"decision": "allow"}
        if self.inspections < cfg["block_after_inspections"]:
            return {"decision": "allow"}
        if not is_inspection(tool_name, args, self.policy):
            return {"decision": "allow"}
        self.blocked += 1
        cls = classify("", self.policy, hint="NO_PROGRESS")
        return {
            "decision": "block",
            "code": "NO_PROGRESS",
            "attempts": self.inspections,
            "retryable": False,
            "message": (
                f"{self.inspections} consecutive inspection calls and nothing written yet. "
                f"More reading will not turn into a file."
            ),
            "next_action": cls["next_action"],
        }

    def after(self, tool_name: str, args: dict, is_error: bool, context: str = "") -> None:
        if not self.policy["progress_guard"]["enabled"]:
            return
        if is_inspection(tool_name, args, self.policy):
            self.inspections += 1
            return
        self.inspections = 0
        if not is_error:
            self.mutations += 1


# ---------------------------------------------------------------------------
# Write verification
# ---------------------------------------------------------------------------

def verify_write(path: str | Path, expected_bytes: int | None = None,
                 freshness_ms: int | None = None, policy: dict | None = None,
                 now: float | None = None) -> dict:
    policy = policy or DEFAULT_POLICY
    freshness = freshness_ms if freshness_ms is not None else policy["write_verification"]["mtime_freshness_ms"]
    now_ms = (now if now is not None else time.time()) * 1000.0
    p = Path(path)
    try:
        st = p.stat()
    except OSError:
        return {"ok": False, "code": "WRITE_NOT_VERIFIED", "message": f"the file does not exist after the call: {p}"}
    if not p.is_file():
        return {"ok": False, "code": "WRITE_NOT_VERIFIED", "message": f"the target is not a regular file: {p}"}
    if st.st_size == 0 and (expected_bytes or 0) > 0:
        return {"ok": False, "code": "WRITE_NOT_VERIFIED", "message": f"the file is empty after the call: {p}"}
    if expected_bytes and st.st_size != expected_bytes:
        return {"ok": False, "code": "WRITE_NOT_VERIFIED",
                "message": f"the file is {st.st_size} bytes but {expected_bytes} were written: {p}",
                "bytes": st.st_size}
    if now_ms - st.st_mtime * 1000.0 > freshness:
        return {"ok": False, "code": "WRITE_NOT_VERIFIED",
                "message": f"the file was not modified by this call (mtime is "
                           f"{round((now_ms - st.st_mtime * 1000.0) / 1000)}s old): {p}",
                "bytes": st.st_size}
    return {"ok": True, "bytes": st.st_size}


# ---------------------------------------------------------------------------
# Logs and state
# ---------------------------------------------------------------------------

def log_dir(root: Path | None = None, policy: dict | None = None) -> Path:
    policy = policy or DEFAULT_POLICY
    root = Path(root or ROOT)
    d = Path(policy["logging"]["dir"])
    return d if d.is_absolute() else root / d


def read_events(root: Path | None = None, policy: dict | None = None) -> list[dict]:
    """Every event, oldest first. A malformed line is skipped, never fatal."""
    d = log_dir(root, policy)
    if not d.is_dir():
        return []
    events: list[dict] = []
    for file in sorted(d.glob("*.jsonl")):
        try:
            for line in file.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    events.append(json.loads(line))
                except ValueError:
                    continue
        except OSError:
            continue
    return events


def runs(events: list[dict]) -> list[dict]:
    """Group events by run_id, newest run first, each with its step list."""
    grouped: dict[str, list[dict]] = {}
    for event in events:
        grouped.setdefault(event.get("run_id") or "?", []).append(event)
    out = []
    for run_id, items in grouped.items():
        steps = [e for e in items if e.get("tool") not in ("session",)]
        failures = [e for e in steps if not e.get("ok", True)]
        out.append({
            "run_id": run_id,
            "client": items[0].get("client"),
            "engine": next((e.get("engine") for e in items if e.get("engine")), None),
            "project": next((e.get("project") for e in items if e.get("project")), None),
            "started": items[0].get("ts"),
            "ended": items[-1].get("ts"),
            "steps": len(steps),
            "failures": len(failures),
            "blocked": sum(1 for e in steps if e.get("decision") == "block"),
            "error_codes": sorted({e["error_code"] for e in failures if e.get("error_code")}),
            "items": steps,
        })
    out.sort(key=lambda r: r.get("started") or "", reverse=True)
    return out


def prune(root: Path | None = None, policy: dict | None = None, dry_run: bool = False) -> list[str]:
    """Keep `logging.max_files` newest JSONL files. Never touches anything else."""
    policy = policy or DEFAULT_POLICY
    d = log_dir(root, policy)
    if not d.is_dir():
        return []
    files = sorted(d.glob("*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
    doomed = files[int(policy["logging"]["max_files"]):]
    removed = []
    for file in doomed:
        removed.append(file.name)
        if not dry_run:
            try:
                file.unlink()
            except OSError:
                pass
    return removed


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _print_status(policy: dict, events: list[dict], as_json: bool) -> int:
    grouped = runs(events)
    summary = {
        "policy": str(POLICY_FILE.relative_to(ROOT)) if POLICY_FILE.exists() else "(defaults)",
        "log_dir": str(log_dir()),
        "log_files": len(list(log_dir().glob("*.jsonl"))) if log_dir().is_dir() else 0,
        "events": len(events),
        "runs": len(grouped),
        "last_run": None,
    }
    if grouped:
        last = grouped[0]
        summary["last_run"] = {
            "run_id": last["run_id"],
            "engine": last["engine"],
            "project": last["project"],
            "steps": last["steps"],
            "failures": last["failures"],
            "blocked": last["blocked"],
            "error_codes": last["error_codes"],
            "started": last["started"],
        }
    if as_json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 0
    print(f"policy      : {summary['policy']}")
    print(f"log         : {summary['log_dir']}  ({summary['log_files']} file(s), {summary['events']} event(s))")
    print(f"runs        : {summary['runs']}")
    last = summary["last_run"]
    if last:
        print(f"last run    : {last['run_id']}")
        print(f"  engine    : {last['engine']}")
        print(f"  project   : {last['project']}")
        print(f"  steps     : {last['steps']}  failures: {last['failures']}  blocked: {last['blocked']}")
        if last["error_codes"]:
            print(f"  errors    : {', '.join(last['error_codes'])}")
    else:
        print("last run    : (none yet - start a pi session)")
    return 0


def _print_state(events: list[dict], run_id: str | None, as_json: bool) -> int:
    grouped = runs(events)
    if not grouped:
        print("no runs recorded yet", file=sys.stderr)
        return 1
    target = next((r for r in grouped if r["run_id"] == run_id), None) if run_id else grouped[0]
    if target is None:
        print(f"no run with id {run_id!r}", file=sys.stderr)
        return 1
    if as_json:
        print(json.dumps(target, indent=2, ensure_ascii=False))
        return 0
    print(f"run    : {target['run_id']}")
    print(f"engine : {target['engine']}   project: {target['project']}")
    print(f"steps  : {target['steps']}  failures: {target['failures']}  blocked: {target['blocked']}")
    print()
    for i, step in enumerate(target["items"], 1):
        mark = "ok  " if step.get("ok") else "FAIL"
        extra = f" {step.get('error_code')}" if step.get("error_code") else ""
        verify = f" [{step.get('verification')}]" if step.get("verification") else ""
        print(f"{i:3} {mark} {step.get('tool')}{extra}{verify}")
    return 0


def _print_log(events: list[dict], tail: int, code: str | None, as_json: bool) -> int:
    selected = [e for e in events if not code or e.get("error_code") == code]
    selected = selected[-tail:] if tail else selected
    if as_json:
        print(json.dumps(selected, indent=2, ensure_ascii=False))
        return 0
    for event in selected:
        flag = "ok  " if event.get("ok") else "FAIL"
        bits = [event.get("ts", ""), flag, event.get("tool", "")]
        if event.get("error_code"):
            bits.append(event["error_code"])
        if event.get("decision"):
            bits.append(f"->{event['decision']}")
        if event.get("verification"):
            bits.append(f"verify={event['verification']}")
        if event.get("note"):
            bits.append(str(event["note"]))
        print("  ".join(bits))
    return 0


def _selftest(policy: dict, as_json: bool) -> int:
    """The policy's own regression suite - what the guard must decide, asserted here."""
    cases = [
        ("No such file or directory: world.ts", "FILE_NOT_FOUND"),
        ("EACCES: permission denied, open 'x'", "PERMISSION_DENIED"),
        ("connect ECONNREFUSED 127.0.0.1:8080", "SERVER_UNAVAILABLE"),
        ("the response hit the output token limit", "OUTPUT_TOO_LARGE"),
        ("error TS2322: Type 'string' is not assignable", "VALIDATION_FAILED"),
        ("invalid argument: expected string, got number", "INVALID_ARGUMENT"),
        ("operation timed out after 300s", "TIMEOUT"),
        ("something entirely new happened", "UNKNOWN"),
    ]
    failures = []
    for text, want in cases:
        got = classify(text, policy)["code"]
        if got != want:
            failures.append({"input": text, "want": want, "got": got})

    guard = LoopGuard(policy)
    guard.after("read", {"path": "missing.ts"}, True, "FILE_NOT_FOUND")
    first_retry = guard.before("read", {"path": "missing.ts"})
    if first_retry["decision"] != "block" or first_retry["code"] != "REPEATED_TOOL_CALL":
        failures.append({"input": "identical retry after FILE_NOT_FOUND", "want": "block", "got": first_retry})

    guard2 = LoopGuard(policy)
    guard2.after("read", {"path": "missing.ts"}, True, "FILE_NOT_FOUND")
    changed = guard2.before("read", {"path": "other.ts"})
    if changed["decision"] != "allow":
        failures.append({"input": "a DIFFERENT path after a failure", "want": "allow", "got": changed})

    guard3 = LoopGuard(policy)
    guard3.after("bash", {"command": "npm run build"}, True, "TIMEOUT")
    guard3.after("bash", {"command": "npm run build"}, True, "TIMEOUT")
    transient_ok = guard3.before("bash", {"command": "npm run build"})
    if transient_ok["decision"] != "allow":
        failures.append({"input": "3rd attempt after two timeouts", "want": "allow (transient budget)", "got": transient_ok})

    # A -> B -> A -> B, all four failing. The repeat counter alone would block the 4th call
    # as a plain repeat; the cycle check runs first because the PAIR is what is stuck, and
    # naming that is the more useful message.
    guard4 = LoopGuard(policy)
    for tool, args, code in (
        ("read", {"path": "a.ts"}, "FILE_NOT_FOUND"),
        ("grep", {"pattern": "x"}, "INVALID_ARGUMENT"),
        ("read", {"path": "a.ts"}, "FILE_NOT_FOUND"),
    ):
        guard4.after(tool, args, True, code)
    cycle = guard4.before("grep", {"pattern": "x"})
    if cycle["decision"] != "block" or cycle["code"] != "TOOL_CYCLE_DETECTED":
        failures.append({"input": "A B A then B again, all failing", "want": "TOOL_CYCLE_DETECTED", "got": cycle})

    # The same shape must NOT be flagged when the calls are not identical pairs.
    guard5 = LoopGuard(policy)
    for tool, args, code in (
        ("read", {"path": "a.ts"}, "FILE_NOT_FOUND"),
        ("grep", {"pattern": "x"}, "INVALID_ARGUMENT"),
        ("read", {"path": "b.ts"}, "FILE_NOT_FOUND"),
    ):
        guard5.after(tool, args, True, code)
    not_cycle = guard5.before("grep", {"pattern": "y"})
    if not_cycle["decision"] != "allow":
        failures.append({"input": "three DIFFERENT failing calls", "want": "allow", "got": not_cycle})

    result = {"ok": not failures, "cases": len(cases) + 4, "failures": failures}
    if as_json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        for f in failures:
            print(f"FAIL {f['input']!r}: want {f['want']!r}, got {f['got']!r}")
        print(f"{result['cases'] - len(failures)}/{result['cases']} reliability self-tests passed")
    return 0 if not failures else 1


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Reliability layer: policy, logs, state, checks.")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    sub = ap.add_subparsers(dest="cmd")

    sub.add_parser("status", help="policy path, log stats and the last run")
    p_state = sub.add_parser("state", help="step list of one run")
    p_state.add_argument("--run", default=None, help="run id (default: the newest)")
    p_log = sub.add_parser("log", help="raw events, newest last")
    p_log.add_argument("--tail", type=int, default=40)
    p_log.add_argument("--code", default=None)
    p_verify = sub.add_parser("verify", help="postcondition check on a file")
    p_verify.add_argument("path")
    p_verify.add_argument("--bytes", type=int, default=None)
    p_class = sub.add_parser("classify", help="what the guard would call this error")
    p_class.add_argument("text")
    sub.add_parser("prune", help="enforce the log retention policy")
    sub.add_parser("selftest", help="run the policy's regression suite")

    a = ap.parse_args(argv[1:])
    policy = load_policy()

    if a.cmd == "selftest":
        return _selftest(policy, a.json)
    if a.cmd == "classify":
        print(json.dumps(classify(a.text, policy), indent=2, ensure_ascii=False))
        return 0
    if a.cmd == "verify":
        print(json.dumps(verify_write(a.path, expected_bytes=a.bytes, policy=policy), indent=2, ensure_ascii=False))
        return 0
    if a.cmd == "prune":
        removed = prune(policy=policy)
        print(f"removed {len(removed)} old log file(s)" + (f": {', '.join(removed)}" if removed else ""))
        return 0

    events = read_events(policy=policy)
    if a.cmd == "log":
        return _print_log(events, a.tail, a.code, a.json)
    if a.cmd == "state":
        return _print_state(events, a.run, a.json)
    return _print_status(policy, events, a.json)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
