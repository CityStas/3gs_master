@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"

set "PY=%GS_ROOT%.venv\Scripts\python.exe"
if not exist "%PY%" (
  echo [ERROR] Python venv not found: "%PY%"
  exit /b 1
)

set "PI_CODING_AGENT_DIR=%GS_ROOT%pi-home-three"
set "PI_SKIP_VERSION_CHECK=1"
set "PI_TELEMETRY=0"

if "%~1"=="" (
  echo Usage: ask.cmd "your task for the Three.js agent"
  echo        The project is taken from data\active_project.txt
  echo        ^(set it once with: agent.cmd C:/path/to/threejs-project^)
  exit /b 2
)

if exist "%GS_ROOT%data\active_project.txt" (
  set /p PROJ=<"%GS_ROOT%data\active_project.txt"
) else (
  set "PROJ="
)

cd /d "%GS_ROOT%"
if not "%PROJ%"=="" (
  echo Active Three.js project: %PROJ%
  set "THREE_PROJECT=%PROJ%"
) else (
  echo [WARN] No active project. Run agent.cmd ^<project^> first.
)

echo.
pi -p --no-session %* < nul
