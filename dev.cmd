@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0cmd\_env.cmd"

rem --- One command for the whole cycle: models, optional studio, agent.
rem ---
rem ---   dev.cmd test                 models + agent
rem ---   dev.cmd test --studio        + studio in a PARALLEL window (live view)
rem ---
rem --- Argument is a game NAME in projects\games\ (a leading path is tolerated).
rem --- The folder is created when missing, and NOTHING is put inside it: no
rem --- scene.js, no levels.json, no tools\, no serve.py. The model lays down
rem --- whatever it needs. Laying down the standard stack is a separate, explicit
rem --- act - newgame.cmd <name> - and dev.cmd never does it behind your back.
rem ---
rem --- The studio is OPTIONAL and runs in its OWN window: the agent takes over
rem --- this one (pi is interactive and blocks). It is a viewer, not part of the
rem --- agent - it can be started later (studio.cmd <game>) and closed without
rem --- touching the session; the two only share the files on disk.

set "GAMEARG="
set "STUDIO=0"
set "REMOVED="
:parse
if "%~1"=="" goto :parsed
if /i "%~1"=="--studio"    (set "STUDIO=1" & shift & goto :parse)
if /i "%~1"=="--no-studio" (set "STUDIO=0" & shift & goto :parse)
rem --- flags that used to scaffold. Recognised only to be refused by name: a
rem --- silently swallowed --force would look like it worked.
if /i "%~1"=="--cli"       (set "REMOVED=%~1" & shift & goto :parse)
if /i "%~1"=="--force"     (set "REMOVED=%~1" & shift & goto :parse)
if not defined GAMEARG (set "GAMEARG=%~1" & shift & goto :parse)
shift
goto :parse
:parsed

if defined REMOVED (
  echo [ERROR] %REMOVED% is no longer a dev.cmd flag: dev.cmd does not scaffold.
  echo         It creates the empty folder and starts the agent - that is all.
  echo         Lay down the standard stack explicitly:  newgame.cmd ^<name^>
  exit /b 2
)

if not defined GAMEARG (
  echo Usage: dev.cmd ^<game^> [--studio]
  echo.
  echo   dev.cmd my_game              models, then the agent
  echo   dev.cmd my_game --studio     + studio in a parallel window
  echo.
  echo The game is a NAME in %GS_GAMES_REL%\ - the folder is created when missing
  echo and left EMPTY. The standard stack comes from newgame.cmd only:
  echo   newgame.cmd my_game          scene.js, levels.json, tools\, serve.py
  exit /b 2
)

rem --- bare name from whatever was typed: "test", "projects\games\test" ---------
for %%I in ("%GAMEARG%") do set "GAMENAME=%%~nI"

rem --- 1. The folder, and nothing but the folder. Scaffolding used to live here:
rem ---    a missing web3d\levels.json silently triggered newgame.cmd, so a
rem ---    one-line "start the agent" also rewrote the file tree. The model does
rem ---    not need that tree - it creates its own files - and an implicit write
rem ---    of twenty files is not something a launcher should do. The only thing
rem ---    created here is the directory the agent is pointed at, because
rem ---    data\active_project.txt names it.
if exist "%GS_GAMES%\%GAMENAME%" goto :have_dir
echo Creating empty %GS_GAMES_REL%\%GAMENAME% ...
mkdir "%GS_GAMES%\%GAMENAME%"
if errorlevel 1 goto :fail_mkdir
:have_dir

rem --- 2. Models. Blocking: returns only when :8080 and :8081 answer, so the
rem ---    agent never starts against a half-loaded 9B.
call "%GS_ROOT%serve-all.cmd"
if errorlevel 1 (
  echo [ERROR] models did not come up - nothing was launched.
  exit /b 1
)

rem --- 3. Environment check. A broken venv or a missing model must be loud HERE,
rem ---    not in the middle of a session.
call "%GS_ROOT%cmd\doctor.cmd"
if errorlevel 1 (
  echo [ERROR] doctor found a problem - fix it before starting the agent.
  exit /b 1
)

rem --- 4. Studio, in a PARALLEL window, BEFORE the agent takes this one.
rem ---    --no-models: serve-all already owns :8080/:8081, and the studio does
rem ---    not use them anyway.
if "%STUDIO%"=="1" (
  echo Starting the studio in a separate window...
  start "3gs-studio" cmd /c ""%GS_ROOT%studio.cmd" %GAMENAME% --no-models"
  rem Give the window a moment to appear before pi paints the console.
  ping -n 3 127.0.0.1 >nul 2>&1
)

rem --- 5. The agent. Interactive and blocking: this window becomes the session.
echo.
echo Launching pi for %GS_GAMES_REL%\%GAMENAME% ...
call "%GS_ROOT%agent.cmd" %GS_GAMES_REL%\%GAMENAME%
exit /b %errorlevel%

:fail_mkdir
echo.
echo [ERROR] could not create %GS_GAMES%\%GAMENAME% - see the output above.
exit /b 1
