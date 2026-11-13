@echo off
setlocal
rem --- this launcher lives in cmd\; the repo root is one level up ---
rem --- shared paths (GS_ROOT, GS_PROJECTS, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"
set "PY=%GS_ROOT%.venv\Scripts\python.exe"
if not exist "%PY%" (
  echo [ERROR] Python venv not found: "%PY%"
  echo Create it with:  python -m venv .venv
  exit /b 1
)

cd /d "%GS_ROOT%"

rem --- Initialise a project FROM ITS engine.json. The marker is the input, the
rem --- stack is the output: engine=threejs gets web3d\ + level.json + studio,
rem --- engine=roblox/unity/godot gets nothing (their own tooling owns the
rem --- skeleton). There is no universal "new game" step any more - that name
rem --- made models call the Three.js scaffolder for Roblox projects.
rem ---
rem ---   init.cmd                          current directory, engine from engine.json
rem ---   init.cmd projects\three\my_game --engine threejs  full path + stack
rem ---   init.cmd my_game --engine threejs             resolves against CWD
rem ---   init.cmd my_game --sync           refresh only the stack
rem ---   init.cmd my_game --force          overwrite levels too
rem ---   init.cmd my_game --cli            only what the CLI agent needs
if "%~1"=="" (
  "%PY%" "%GS_ROOT%tools\project_init.py"
  exit /b %errorlevel%
)

"%PY%" "%GS_ROOT%tools\project_init.py" %*
exit /b %errorlevel%
