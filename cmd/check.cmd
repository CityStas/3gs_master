@echo off
setlocal
rem --- this launcher lives in cmd\; the repo root is one level up ---
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"
set "PY=%GS_ROOT%.venv\Scripts\python.exe"
if not exist "%PY%" (
  echo [ERROR] Python venv not found: "%PY%"
  echo Create it with:  python -m venv .venv
  exit /b 1
)

cd /d "%GS_ROOT%"

rem --- Two gates, one verdict. tscheck.py is what a compiler can see; pagecheck.py is
rem --- what only a browser would otherwise discover - an import that 404s aborts the
rem --- whole module graph and leaves a BLANK page with no visible error, and a missing
rem --- asset is a sprite that silently never appears. Both exit 1 on trouble, so the
rem --- worse one decides. Pass a name under projects\games\ (default: the one named in
rem --- data\active_project.txt). Extra args pass through to tsc; pagecheck ignores the
rem --- ones that are not its own:
rem ---   check.cmd new_local_game --full
rem ---   check.cmd new_local_game --json
set "RC=0"
rem --- tscheck exits 2 when the project has no node_modules (TypeScript not installed).
rem --- That is an unfinished environment, not a code error, so it is reported as SKIP
rem --- and does not turn the verdict red. Real type errors (exit 1) still fail.
"%PY%" "%GS_ROOT%tools\tscheck.py" %*
if errorlevel 2 (
  echo [SKIP] tscheck: no node_modules in the project - TypeScript gate not run
) else if errorlevel 1 set "RC=1"
echo.
"%PY%" "%GS_ROOT%tools\pagecheck.py" %*
if errorlevel 1 set "RC=1"
exit /b %RC%
