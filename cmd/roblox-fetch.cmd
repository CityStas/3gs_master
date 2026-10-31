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
echo Fetching the Roblox corpus ^(guides + Engine API + Open Cloud + starter kit^)...
echo.
"%PY%" roblox\tools\fetch_docs.py %*
echo.
echo Build the index with:  gs roblox-index
