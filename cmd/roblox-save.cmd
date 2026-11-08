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

rem --- Snapshot the place that is open in Studio into the project folder.
rem ---
rem --- There is NO scriptable save for a local .rbxl: DataModel:SavePlace wants a
rem --- PlaceId, AssetService:SavePlaceAsync wants a published place, StudioService
rem --- has no save member, and the MCP keyboard tool types into the running game,
rem --- not into Studio's File menu. What Studio does write by itself is the
rem --- AutoRecovery dump; this copies the newest one over the place file.
rem ---
rem ---   roblox-save.cmd                  active project, wait for a fresh dump
rem ---   roblox-save.cmd test_1 --now     accept the newest dump, however old
rem ---   roblox-save.cmd test_1 --wait 0  fail instead of waiting
rem ---   roblox-save.cmd --list           what is in AutoSaves right now
"%PY%" "%GS_ROOT%roblox\tools\save.py" %*
exit /b %errorlevel%
