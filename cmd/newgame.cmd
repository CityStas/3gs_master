@echo off
setlocal
rem --- this launcher lives in cmd\; the repo root is one level up ---
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"
set "PY=%GS_ROOT%.venv\Scripts\python.exe"
if not exist "%PY%" (
  echo [ERROR] Python venv not found: "%PY%"
  echo Create it with:  python -m venv .venv
  exit /b 1
)

cd /d "%GS_ROOT%"

rem --- Scaffold a new project in projects\games\. The stack it needs is six
rem --- entries across web3d\ and tools\; copying them by hand means finding out
rem --- which one you forgot from a browser console. The source is the REPOSITORY
rem --- (STACK_SRC in tools/new_game.py), never a neighbouring project - deleting
rem --- one project must not stop the others from being created.
rem --- Projects live ONLY in projects\games\ - that is the only directory
rem --- check.cmd, the gates, gen.cmd and --sync look at, so the argument is a
rem --- NAME, not a path.
rem ---
rem ---   newgame.cmd my_game
rem ---   newgame.cmd my_game --sync            (refresh only the stack)
rem ---   newgame.cmd my_game --force           (overwrite levels too)
rem ---   newgame.cmd my_game --cli             (only what the CLI agent needs)
if "%~1"=="" (
  echo Usage: newgame.cmd ^<name^> [--sync] [--force] [--cli]
  echo.
  echo   newgame.cmd my_game
  echo   newgame.cmd my_game --sync
  echo.
  echo Games are created in projects\games\ only. See STUDIO.md.
  exit /b 2
)

"%PY%" "%GS_ROOT%tools\new_game.py" %*
exit /b %errorlevel%
