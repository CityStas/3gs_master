"""Запуск Godot headless: валидация скриптов, прогон сцен, разбор ошибок.

Никакого shell-доступа наружу — только прямой subprocess на бинарник Godot
с фиксированным набором флагов.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path

from .. import config
from .paths import resolve, res_path

_ERROR_LINE = re.compile(
    r"(SCRIPT ERROR|Parse Error|Parser Error|"
    r"^ERROR: (?!.*(?:leaked at exit|still in use at exit|ObjectDB instances))|"
    r"Invalid|Cannot|Can't|Failed to|Condition .* is true|"
    r"Attempt to call|Nil|null instance|Identifier not found|Expected)",
    re.M,
)

# Godot печатает это при штатном завершении SceneTree-скрипта, который
# инстанцировал и сохранил сцену. Это не ошибки задачи.
_BENIGN = re.compile(
    r"(RID allocations? of type .* were leaked|RIDs of type .* were leaked|"
    r"resources? still in use at exit|ObjectDB instances were leaked|"
    r"Leaked instance|cleanup|_free_rids|resource\.cpp|object\.cpp|"
    r"servers/rendering)",
    re.I,
)
_GD_ERROR_STRUCT = re.compile(r"^(?P<file>[^\s:][^:]*\.gd):(?P<line>\d+)\s*-\s*(?P<msg>.+)$", re.M)


@dataclass
class RunResult:
    ok: bool
    exit_code: int
    stdout: str = ""
    stderr: str = ""
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    seconds: float = 0.0
    timed_out: bool = False
    command: str = ""

    def to_dict(self, max_output: int = 6000) -> dict:
        return {
            "ok": self.ok,
            "exit_code": self.exit_code,
            "errors": self.errors[:40],
            "error_count": len(self.errors),
            "warnings": self.warnings[:20],
            "timed_out": self.timed_out,
            "seconds": round(self.seconds, 2),
            "stdout": self.stdout[-max_output:],
            "stderr": self.stderr[-max_output:],
        }


def _env() -> dict:
    env = dict(os.environ)
    # в Git Bash APPDATA пустой -> Godot создаёт ./Godot в корне проекта
    if not env.get("APPDATA"):
        env["APPDATA"] = os.path.expandvars(r"%USERPROFILE%\AppData\Roaming")
    env.setdefault("GODOT_SILENCE_ROOT_WARNING", "1")
    return env


def _parse_output(text: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    for line in text.splitlines():
        s = line.strip()
        if not s or _BENIGN.search(s):
            continue
        if "WARNING" in s or s.startswith("W "):
            warnings.append(s)
        elif _ERROR_LINE.search(s):
            errors.append(s)
    # дедуп с сохранением порядка
    seen = set()
    errors = [e for e in errors if not (e in seen or seen.add(e))]
    warnings = [w for w in warnings if not (w in seen or seen.add(w))]
    return errors, warnings


class GodotRunner:
    def __init__(self, godot_exe: Path | None = None, project_root: Path | None = None,
                 default_timeout: float = 90.0):
        self.godot_exe = Path(godot_exe or config.GODOT_EXE)
        self.project_root = Path(project_root or config.godot_project_root() or ".")
        self.default_timeout = default_timeout

    # ------------------------------------------------------------------
    def _run(self, args: list[str], timeout: float) -> RunResult:
        cmd = [str(self.godot_exe), "--path", str(self.project_root), *args]
        t0 = time.time()
        try:
            proc = subprocess.run(
                cmd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                timeout=timeout, env=_env(), cwd=str(self.project_root),
            )
            out, err, code, timed_out = proc.stdout or "", proc.stderr or "", proc.returncode, False
        except subprocess.TimeoutExpired as e:
            out = (e.stdout or b"").decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
            err = (e.stderr or b"").decode("utf-8", "replace") if isinstance(e.stderr, bytes) else (e.stderr or "")
            code, timed_out = -1, True
        except OSError as e:
            return RunResult(ok=False, exit_code=-2, stderr=str(e),
                             errors=[f"не удалось запустить Godot: {e}"],
                             command=" ".join(cmd))
        errors, warnings = _parse_output(out + "\n" + err)
        ok = (code == 0) and not timed_out and not errors
        return RunResult(ok=ok, exit_code=code, stdout=out, stderr=err,
                         errors=errors, warnings=warnings,
                         seconds=time.time() - t0, timed_out=timed_out,
                         command=" ".join(cmd))

    # ------------------------------------------------------------------
    def check_script(self, script_path: str, timeout: float = 45.0) -> RunResult:
        """Парсинг .gd без запуска: godot --check-only --script."""
        rel = res_path(script_path, self.project_root)
        return self._run(["--headless", "--check-only", "--script", rel], timeout)

    def run_scene(self, scene_path: str | None = None, quit_after_frames: int = 180,
                  timeout: float | None = None) -> RunResult:
        """Прогон сцены headless. quit_after_frames ограничивает время."""
        args = ["--headless"]
        if quit_after_frames > 0:
            args += ["--quit-after", str(quit_after_frames)]
        if scene_path:
            args.append(res_path(scene_path, self.project_root))
        return self._run(args, timeout or self.default_timeout)

    def import_assets(self, timeout: float = 300.0) -> RunResult:
        """Переимпорт ресурсов + проверка проекта (--editor --quit)."""
        return self._run(["--headless", "--editor", "--quit"], timeout)

    def run_script_file(self, script_path: str, timeout: float = 90.0) -> RunResult:
        """Запуск SceneTree-скрипта (для мутаций сцен и проб)."""
        rel = res_path(script_path, self.project_root)
        return self._run(["--headless", "--script", rel], timeout)

    # ------------------------------------------------------------------
    def exec_tree_script(self, body: str, tmp_rel_dir: str = ".gdmaster_tmp",
                         timeout: float = 90.0) -> tuple[RunResult, dict]:
        """Сгенерировать SceneTree-скрипт, выполнить, вернуть (result, json_payload).

        Тело операции живёт в отдельной функции `__run()`, а не инлайнится в
        `_initialize()`. Это принципиально: в теле есть ранние `return` (узел не
        найден, свойство не существует, ...), а `return` из `_initialize()`
        пропустил бы и запись результата, и `quit()` — Godot остался бы висеть
        до таймаута, и наружу ушло бы бесполезное «код -1, результат не записан».
        Из `__run()` ранний `return` возвращает управление в `_initialize()`,
        которая всё равно сбрасывает `__res` и вызывает `quit(0)`.
        """
        root = self.project_root
        tmp_dir = root / tmp_rel_dir
        tmp_dir.mkdir(parents=True, exist_ok=True)
        (tmp_dir / ".gdignore").write_text("", encoding="utf-8")

        # Уборка: удаление временных файлов может быть перехвачено (Windows-песочница
        # отдаёт PermissionError, который мы глотаем как OSError), поэтому каталог
        # время от времени подметаем принудительно.
        cutoff = time.time() - 600
        for stale in tmp_dir.glob("_op_*"):
            try:
                if stale.stat().st_mtime < cutoff:
                    stale.unlink()
            except OSError:
                pass

        stamp = f"{int(time.time() * 1000)}"
        script = tmp_dir / f"_op_{stamp}.gd"
        result_file = tmp_dir / f"_op_{stamp}.json"
        result_res = f"res://{tmp_rel_dir}/_op_{stamp}.json"

        script.write_text(
            "extends SceneTree\n\n"
            "var __res: Dictionary = {}\n"
            f"var __out: String = {json.dumps(result_res)}\n\n"
            "func _initialize() -> void:\n"
            "\t__run()\n"
            "\tvar __f := FileAccess.open(__out, FileAccess.WRITE)\n"
            "\tif __f:\n"
            "\t\t__f.store_string(JSON.stringify(__res))\n"
            "\t\t__f.close()\n"
            "\tquit(0)\n\n"
            "func __run() -> void:\n"
            "\t# --- generated body ---\n"
            + "\n".join("\t" + ln if ln.strip() else "" for ln in body.splitlines())
            + "\n\t# --- end body ---\n",
            encoding="utf-8",
        )

        res = self.run_script_file(f"{tmp_rel_dir}/_op_{stamp}.gd", timeout=timeout)
        payload: dict = {}
        if result_file.exists():
            try:
                payload = json.loads(result_file.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                payload = {}
            try:
                result_file.unlink()
            except OSError:
                pass
        try:
            script.unlink()
        except OSError:
            pass
        return res, payload
