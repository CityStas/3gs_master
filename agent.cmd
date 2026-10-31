@echo off
setlocal enabledelayedexpansion
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0cmd\_env.cmd"

set "PY=%GS_ROOT%.venv\Scripts\python.exe"
if not exist "%PY%" (
  echo [ERROR] Python venv not found: "%PY%"
  echo Create it with:  python -m venv .venv
  exit /b 1
)

rem --- isolated pi config per engine. PI_CODING_AGENT_DIR is set further down, once the
rem --- project's engine.json is known: pi-home-godot for engine=godot, pi-home-unity for
rem --- unity, pi-home-roblox for roblox, pi-home-three otherwise.
rem --- Each profile holds its own SYSTEM.md, skills/, mcp.json, models.json, settings.json.
rem --- NOTE: PI_OFFLINE is deliberately NOT set - cloud providers need the network.
set "PI_SKIP_VERSION_CHECK=1"
set "PI_TELEMETRY=0"

set "PROJ=%~1"
rem --- a flag is not a project: `agent.cmd --help` once wrote "--help" into active_project.txt
if "%PROJ:~0,1%"=="-" set "PROJ="
set "PROJ_FROM_POINTER="
if "%PROJ%"=="" (
  if exist "%GS_ROOT%data\active_project.txt" (
    set /p PROJ=<"%GS_ROOT%data\active_project.txt"
    if not "!PROJ!"=="" set "PROJ_FROM_POINTER=1"
  )
)

rem --- A pointer is a hint, never a fact. With no argument the block above re-reads the
rem --- file and the block below writes it straight back, so a project deleted since the
rem --- last run would be resurrected on EVERY launch and the agent would start pointed at
rem --- a directory that is not there. Only the POINTER is checked - an explicit argument is
rem --- the caller's business. The check is delegated to tools\active_project.py on purpose:
rem --- the three stacks already own the resolution rules (absolute, repo-relative, bare
rem --- name, stale -> error), and re-implementing them in batch would drift from them.
if defined PROJ_FROM_POINTER (
  "%PY%" "%GS_ROOT%tools\active_project.py" >nul 2>nul
  if errorlevel 1 (
    echo.
    echo [ERROR] The active project is stale - it was deleted or renamed:
    echo         %PROJ%
    echo.
    echo         Point the system at a live project and re-run:  dev.cmd ^<name^>
    echo         Clearing the stale pointer so the next run asks for one.
    type nul >"%GS_ROOT%data\active_project.txt"
    set "PROJ="
  )
)

if not "%PROJ%"=="" (
  >"%GS_ROOT%data\active_project.txt" echo %PROJ%
  set "THREE_PROJECT=%PROJ%"
  echo Active project: %PROJ%
) else (
  echo [WARN] No project set.
  echo        Usage: agent.cmd projects\games\^<name^>
  echo        The agent can still answer API questions from RAG.
)

rem --- Anything after the project path is forwarded to pi. That is how a task brief
rem --- gets attached with pi's @file argument, which is a CLI argument and NOT
rem --- something you can type inside a message. The file is whatever you name it:
rem --- there is no brief filename convention and nothing is auto-detected.
rem --- The loop must stay outside parentheses: inside a block cmd substitutes %1 once
rem --- at parse time and `shift` would never be seen.
set "PI_ARGS="
if "%~2"=="" goto :args_done
shift
:collect_args
if "%~1"=="" goto :args_done
set "PI_ARGS=%PI_ARGS% "%~1""
shift
goto :collect_args
:args_done

echo.
echo --- environment check ---
rem --- --quick: полный doctor ходит в ComfyUI :8188, поднимает Blender и ждёт
rem --- `agent-reach doctor` до 90 с. Это диагностика, а не условие запуска: на
rem --- запуске нужен быстрый режим, иначе старт пилота стоит минуты.
"%PY%" "%GS_ROOT%tools\doctor.py" --quick

cd /d "%GS_ROOT%"

rem --- Pin the active game into the SYSTEM PROMPT, not just the environment.
rem --- pi starts in the repo root and never reads THREE_PROJECT, so without this
rem --- the model only knows <cwd>=repo-root: it cannot tell which game it is in,
rem --- guesses a folder from the task wording ("demo" -> projects/games/demo) and invents
rem --- files it was never told about. `--append-system-prompt` is applied on every
rem --- launch, so the answer does not depend on the model remembering to read a file.
rem ---
rem --- Nothing else is appended: no brief filename, no task file. The message the
rem --- agent is launched with IS the task, and naming a file here (even to forbid
rem --- it) only plants the idea that such a file exists.
rem --- engine marker: projects/<game>/engine.json. Read here so the banner shows it,
rem --- and .pi/extensions/engine-gate.ts reads the same file to pick the MCP surface.
set "ENGINE=threejs"
if defined PROJ "%PY%" -c "import json,os,sys;p=sys.argv[1];b=sys.argv[2];d=p if os.path.isabs(p) else os.path.join(b,p);print(json.load(open(os.path.join(d,'engine.json'),encoding='utf-8')).get('engine','threejs'))" "%PROJ%" "%GS_ROOT:~0,-1%" > "%TEMP%\gs_engine.txt" 2>nul
if defined PROJ if not errorlevel 1 for /f "usebackq delims=" %%E in ("%TEMP%\gs_engine.txt") do set "ENGINE=%%E"
rem --- choose the agent profile from the engine. Godot, Unity and Roblox each get their own
rem --- profile (SYSTEM.md, skills/, mcp.json, models.json); everything else (threejs, or
rem --- no engine.json) gets the Three.js profile.
if /i "%ENGINE%"=="godot" (
  set "PI_CODING_AGENT_DIR=%GS_ROOT%pi-home-godot"
) else if /i "%ENGINE%"=="unity" (
  set "PI_CODING_AGENT_DIR=%GS_ROOT%pi-home-unity"
) else if /i "%ENGINE%"=="roblox" (
  set "PI_CODING_AGENT_DIR=%GS_ROOT%pi-home-roblox"
) else (
  set "PI_CODING_AGENT_DIR=%GS_ROOT%pi-home-three"
)

set "PI_SP="
if not "%PROJ%"=="" set "PI_SP=Active project: %PROJ% (engine: %ENGINE%) - work ONLY inside it; never create another project or a sibling folder unless the user asks for one by name. The working dir stays the repo root; reach the project with a relative path such as projects/games/<name>/ - that is where your files go. data\active_project.txt and THREE_PROJECT hold the same value."
if not "%PROJ%"=="" (
  rem --- also keep the file in sync so the studio and any in-session read agree
  >"%GS_ROOT%data\active_project.txt" echo %PROJ%
)

echo.
echo Launching pi (%ENGINE% agent)
echo   agent config : %PI_CODING_AGENT_DIR%
echo   project      : %THREE_PROJECT%
echo   engine       : %ENGINE%   (read from "%PROJ%\engine.json")
echo.
if not "%PI_SP%"=="" (pi --append-system-prompt "%PI_SP%" %PI_ARGS%) else (pi %PI_ARGS%)
