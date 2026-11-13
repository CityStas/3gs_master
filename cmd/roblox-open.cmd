@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_PROJECTS, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"

set "PY=%GS_ROOT%.venv\Scripts\python.exe"
if not exist "%PY%" (
  echo [ERROR] Python venv not found: "%PY%"
  echo Create it with:  python -m venv .venv
  exit /b 1
)

cd /d "%GS_ROOT%"

rem --- Opens Roblox Studio, detached, on the active project's place file.
rem --- The MCP bridge needs no manual step: the launcher strips http(s)_proxy from
rem --- Studio's environment. Studio dials ws://127.0.0.1:13469 and a system proxy
rem --- swallows that loopback handshake, leaving the agent with no studios while
rem --- Studio's own Assistant setting still says "enabled".
rem ---
rem ---   roblox-open.cmd                 active project's first .rbxlx/.rbxl
rem ---   roblox-open.cmd my_game         by name under projects\roblox\
rem ---   roblox-open.cmd my_game --empty Studio without a place
"%PY%" "%GS_ROOT%roblox\tools\open.py" %*
exit /b %errorlevel%
