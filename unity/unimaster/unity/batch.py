"""Run the Unity editor in batch mode and read back what it said.

`-batchmode -quit` is the only way a headless agent can make Unity *compile* and
*execute* something: the editor is the compiler, and there is no separate `csc`
invocation that would see the project's assemblies.

Two hard constraints, both handled here:

* **One editor per project.** Unity refuses to open a project that is already open, so
  a run against a project whose editor is live fails with a lock error rather than
  reporting a compile failure. `compile()` checks `Temp/UnityLockfile` first and says so.
* **The exit code lies.** With `-quit`, compile errors do not always change the exit
  code; the authoritative signal is the `error CS####:` lines in the log. Everything is
  parsed from the log file, never from the return code alone.
"""
from __future__ import annotations

import re
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path

from .. import config
from . import paths

RE_CS_ERROR = re.compile(r"^(?P<file>[^(\n]+)\((?P<line>\d+),\d+\):\s*error\s+(?P<code>CS\d+):\s*(?P<msg>.+)$", re.M)
RE_CS_WARNING = re.compile(r"^(?P<file>[^(\n]+)\((?P<line>\d+),\d+\):\s*warning\s+(?P<code>CS\d+):\s*(?P<msg>.+)$", re.M)
RE_UNITY_ERROR = re.compile(r"^(?:Error|error)\s*:?\s*(?P<msg>.+)$", re.M)


@dataclass
class BatchResult:
    ok: bool = False
    exit_code: int | None = None
    seconds: float = 0.0
    errors: list[dict] = field(default_factory=list)
    warnings: list[dict] = field(default_factory=list)
    log_path: str = ""
    log_tail: str = ""
    reason: str = ""
    timed_out: bool = False

    def to_dict(self, tail_chars: int = 2500) -> dict:
        return {
            "ok": self.ok,
            "exit_code": self.exit_code,
            "seconds": round(self.seconds, 1),
            "error_count": len(self.errors),
            "warning_count": len(self.warnings),
            "errors": self.errors[:40],
            "warnings": self.warnings[:20],
            "reason": self.reason,
            "timed_out": self.timed_out,
            "log": self.log_path,
            "log_tail": self.log_tail[-tail_chars:],
        }


def parse_log(text: str) -> tuple[list[dict], list[dict]]:
    errors, warnings = [], []
    for m in RE_CS_ERROR.finditer(text):
        errors.append({"file": m.group("file").strip(), "line": int(m.group("line")),
                       "code": m.group("code"), "message": m.group("msg").strip()})
    for m in RE_CS_WARNING.finditer(text):
        warnings.append({"file": m.group("file").strip(), "line": int(m.group("line")),
                         "code": m.group("code"), "message": m.group("msg").strip()})
    # Non-compiler errors Unity prints itself (missing package, license, import failure).
    if not errors:
        for m in RE_UNITY_ERROR.finditer(text):
            msg = m.group("msg").strip()
            if msg and "0 error" not in msg.lower():
                errors.append({"file": "", "line": 0, "code": "UNITY", "message": msg})
    return errors, warnings


def run_batch(project: Path, extra: list[str], timeout: int = 900,
              accept_apiupdate: bool = True) -> BatchResult:
    """Run `Unity.exe -batchmode -nographics -quit -projectPath <project> <extra>`."""
    res = BatchResult()
    try:
        exe = paths.editor_exe()
    except paths.UnityPathError as e:
        res.reason = str(e)
        return res

    if not paths.is_unity_project(project):
        res.reason = (f"{project} is not a Unity project "
                      f"(no ProjectSettings/ProjectVersion.txt and no Assets/)")
        return res

    if paths.editor_running(project):
        res.reason = (f"the Unity editor is already open on {project} "
                      f"(Temp/UnityLockfile exists). Close it, or use the live-editor tools "
                      f"instead of batch mode.")
        return res

    log_dir = config.LOGS_DIR
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"unity-batch-{time.strftime('%Y%m%d-%H%M%S')}.log"

    args = [str(exe), "-batchmode", "-nographics", "-quit",
            "-projectPath", str(project), "-logFile", str(log_path)]
    if accept_apiupdate:
        args.append("-accept-apiupdate")
    args.extend(extra)

    t0 = time.time()
    try:
        proc = subprocess.run(args, capture_output=True, text=True, timeout=timeout,
                              encoding="utf-8", errors="replace")
        res.exit_code = proc.returncode
    except subprocess.TimeoutExpired:
        res.timed_out = True
        res.reason = f"Unity did not finish within {timeout}s"
    except OSError as e:
        res.reason = f"could not start Unity: {e}"
        return res
    res.seconds = time.time() - t0

    text = ""
    try:
        text = log_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        pass
    res.log_path = str(log_path)
    res.log_tail = text
    res.errors, res.warnings = parse_log(text)
    res.ok = not res.errors and not res.timed_out
    if not res.ok and not res.reason:
        res.reason = (f"{len(res.errors)} compile/import error(s)"
                      if res.errors else "Unity reported a failure")
    return res


def compile_project(project: Path, timeout: int = 900) -> BatchResult:
    """Force a full script compile. No `-executeMethod` - opening the project compiles."""
    return run_batch(project, [], timeout=timeout)


def create_project(project: Path, timeout: int = 900) -> BatchResult:
    """Create a Unity project at `project` with `-createProject`.

    Unity has no "new project" file format you can write by hand that the editor will
    accept: `ProjectSettings/ProjectVersion.txt` alone is not enough, and a
    hand-written `Packages/manifest.json` with the wrong schema makes the editor refuse
    the folder. The editor itself must generate the skeleton - exactly the gap
    `godot_project_init` closes on the Godot side.

    Idempotent: an existing project (ProjectSettings/ProjectVersion.txt present) is
    reported as `created: false` and left untouched, so a re-run is safe.
    """
    res = BatchResult()
    if paths.is_unity_project(project):
        res.ok = True
        res.reason = "project already exists; left untouched"
        return res
    try:
        exe = paths.editor_exe()
    except paths.UnityPathError as e:
        res.reason = str(e)
        return res

    project.mkdir(parents=True, exist_ok=True)
    log_dir = config.LOGS_DIR
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"unity-create-{time.strftime('%Y%m%d-%H%M%S')}.log"

    args = [str(exe), "-batchmode", "-nographics", "-quit",
            "-createProject", str(project), "-logFile", str(log_path)]

    t0 = time.time()
    try:
        proc = subprocess.run(args, capture_output=True, text=True, timeout=timeout,
                              encoding="utf-8", errors="replace")
        res.exit_code = proc.returncode
    except subprocess.TimeoutExpired:
        res.timed_out = True
        res.reason = f"Unity did not finish creating the project within {timeout}s"
    except OSError as e:
        res.reason = f"could not start Unity: {e}"
        return res
    res.seconds = time.time() - t0

    text = ""
    try:
        text = log_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        pass
    res.log_path = str(log_path)
    res.log_tail = text
    res.errors, res.warnings = parse_log(text)
    # The authoritative signal is the folder, not the exit code: Unity's return code
    # on `-createProject` is unreliable (it can be non-zero after a successful create).
    res.ok = paths.is_unity_project(project) and not res.timed_out
    if not res.ok and not res.reason:
        res.reason = "Unity did not produce ProjectSettings/ProjectVersion.txt"
    return res


def execute_method(project: Path, method: str, method_args: str = "",
                   timeout: int = 900) -> BatchResult:
    if not re.match(r"^[A-Za-z_]\w*(\.[A-Za-z_]\w*)+$", method):
        res = BatchResult()
        res.reason = (f"'{method}' is not a fully qualified method name "
                      f"(expected Namespace.Class.Method)")
        return res
    extra = ["-executeMethod", method]
    if method_args:
        extra += ["-executeMethodArgs", method_args]
    return run_batch(project, extra, timeout=timeout)


def console_errors(project: Path, limit: int = 40) -> dict:
    """Compile/import errors from the live editor log and the project import logs."""
    chunks: list[tuple[str, str]] = []
    editor_log = paths.editor_log_path()
    if editor_log:
        try:
            chunks.append((str(editor_log),
                           editor_log.read_text(encoding="utf-8", errors="replace")[-400_000:]))
        except OSError:
            pass
    for p in paths.project_log_paths(project):
        try:
            chunks.append((str(p), p.read_text(encoding="utf-8", errors="replace")[-200_000:]))
        except OSError:
            pass

    errors, warnings = [], []
    for _src, text in chunks:
        e, w = parse_log(text)
        errors.extend(e)
        warnings.extend(w)
    # Deduplicate, newest wins.
    seen: dict[tuple, dict] = {}
    for e in errors:
        seen[(e["file"], e["line"], e["code"], e["message"])] = e
    errors = list(seen.values())[-limit:]
    return {"errors": errors, "error_count": len(errors),
            "warnings": warnings[-limit:], "sources": [s for s, _ in chunks]}
