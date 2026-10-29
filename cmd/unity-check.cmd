@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"

set "PY=%GS_ROOT%.venv\Scripts\python.exe"
if not exist "%PY%" (
  echo [ERROR] Python venv not found: "%PY%"
  echo Create it with:  python -m venv .venv
  exit /b 1
)

cd /d "%GS_ROOT%"

rem --- Two layers, one verdict - same shape as check.cmd for Three.js.
rem ---   lint     : Unity 5/6 API traps the compiler cannot see (seconds)
rem ---   compile  : a real -batchmode Unity compile (minutes, editor must be closed)
rem --- Warnings alone do not fail the gate; only errors do.
rem ---   unity-check.cmd my_game
rem ---   unity-check.cmd my_game --compile
rem ---   unity-check.cmd my_game --json
"%PY%" "%GS_ROOT%unity\tools\check.py" %*
exit /b %errorlevel%
