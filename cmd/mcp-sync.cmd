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

rem --- Renders mcp\registry.json into the four pi profiles and into WorkBuddy's
rem --- ~\.workbuddy-ai\mcp.json. Dry run by default; --apply writes.
rem ---
rem ---   gs mcp-sync              show what would change
rem ---   gs mcp-sync --apply      write pi profiles + WorkBuddy
rem ---   gs mcp-sync --apply --only pi
rem ---   gs mcp-sync --print roblox
"%PY%" "%GS_ROOT%tools\mcp_sync.py" %*
exit /b %errorlevel%
