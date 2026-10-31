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

rem --- Opens Roblox Studio, detached, on the active project's place file.
rem --- The Studio MCP server is NOT started by this: it is a toggle inside Studio
rem --- (Assistant -> ... -> Manage MCP Servers -> Enable Studio as MCP server).
rem ---
rem ---   roblox-open.cmd                 active project's first .rbxlx/.rbxl
rem ---   roblox-open.cmd my_game         by name under projects\games\
rem ---   roblox-open.cmd my_game --empty Studio without a place
"%PY%" "%GS_ROOT%roblox\tools\open.py" %*
exit /b %errorlevel%
