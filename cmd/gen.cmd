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

rem --- The scheduler always appends to logs\generate.log and writes a live snapshot
rem --- to data\gen-status.json. This only mirrors it to stderr so a manual run is not
rem --- silent; stderr rather than stdout, because the same code runs inside the stdio
rem --- MCP server where stdout is the JSON-RPC channel.
set "THREE_GEN_VERBOSE=1"

cd /d "%GS_ROOT%"
"%PY%" "%GS_ROOT%tools\generate.py" %*
exit /b %errorlevel%
