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

rem --- Static gate for Luau: unbalanced `end`, deprecated globals, Instance.new parent,
rem --- lowercase method names, numeric require, LoadLibrary, server-only services in a
rem --- client script, LocalPlayer on the server. Exit code 1 = errors.
rem ---
rem ---   roblox-check.cmd my_game
rem ---   roblox-check.cmd my_game --json
rem ---   roblox-check.cmd my_game --errors-only
rem ---
rem --- It cannot prove the script compiles: Studio's Output is the authority for that.
"%PY%" "%GS_ROOT%roblox\tools\check.py" %*
exit /b %errorlevel%
