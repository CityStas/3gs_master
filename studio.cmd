@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0cmd\_env.cmd"
set "PY=%GS_ROOT%.venv\Scripts\python.exe"
if not exist "%PY%" (
  echo [ERROR] Python venv not found: "%PY%"
  echo Create it with:  python -m venv .venv
  exit /b 1
)


rem --- The whole studio in ONE window: the models (:8080, :8081) and the game
rem --- server (:8777) run as children of this console, so a single Ctrl+C stops
rem --- everything. See tools/studio.py for the details.
rem ---
rem ---   studio.cmd                  a game from projects\games\ (the only one)
rem ---   studio.cmd test_game_1      a specific game; the folder must exist
rem ---   studio.cmd my_game 8788     another port
rem ---   studio.cmd --no-models      studio only, no models (starts instantly)
rem ---
rem --- Nothing is created: a missing folder is an error, an empty one opens an
rem --- empty scene. The standard stack is laid down by newgame.cmd, on purpose.

"%PY%" "%GS_ROOT%tools\studio.py" %*
set "RC=%errorlevel%"

rem --- Keep the window open on failure: a double click would otherwise close it
rem --- before the error could be read. A normal Ctrl+C exit closes it.
if not "%RC%"=="0" (
  echo.
  echo Exit code: %RC%
  pause
)
exit /b %RC%
