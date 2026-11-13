@echo off
setlocal enabledelayedexpansion
rem --- shared paths (GS_ROOT, GS_PROJECTS, PY, NO_PROXY) come from one place ----
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
rem --- `agent.cmd three/test_space` and `agent.cmd skateshop` both have to mean the
rem --- folder: projects live in projects/<engine>/<name> since 2026-11-08, and the
rem --- resolution rules (absolute, cwd, repo root, projects/<path>,
rem --- projects/<engine>/<name>) are owned by project_layout.py. There is NO
rem --- legacy projects/games/ parent any more. Batch must not re-implement the
rem --- rules - it calls the same resolver the stacks use.
if not "%PROJ%"=="" if not exist "%PROJ%" (
  for /f "usebackq delims=" %%P in (`%PY% "%GS_ROOT%tools\find_project.py" "%PROJ%" 2^>nul`) do set "PROJ=%%P"
)
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
  echo        Usage: agent.cmd projects\^<engine^>\^<name^>   ^(or a bare name^)
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
rem --- guesses a folder from the task wording ("demo" -> projects/three/demo) and invents
rem --- files it was never told about. `--append-system-prompt` is applied on every
rem --- launch, so the answer does not depend on the model remembering to read a file.
rem ---
rem --- Nothing else is appended: no brief filename, no task file. The message the
rem --- agent is launched with IS the task, and naming a file here (even to forbid
rem --- it) only plants the idea that such a file exists.
rem --- engine marker: projects/<game>/engine.json. Read here so the banner shows it,
rem --- and pi-extensions/engine-gate.ts reads the same file to pick the MCP surface.
set "ENGINE=threejs"
rem --- utf-8-sig, not utf-8: a BOM written by `Set-Content -Encoding utf8` makes
rem --- plain json.load throw, and the engine silently falls back to threejs.
if defined PROJ "%PY%" -c "import json,os,sys;p=sys.argv[1];b=sys.argv[2];d=p if os.path.isabs(p) else os.path.join(b,p);print(json.load(open(os.path.join(d,'engine.json'),encoding='utf-8-sig')).get('engine','threejs'))" "%PROJ%" "%GS_ROOT:~0,-1%" > "%TEMP%\gs_engine.txt" 2>nul
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
if not "%PROJ%"=="" set "PI_SP=Active project: %PROJ% (engine: %ENGINE%) - work ONLY inside it; never create another project or a sibling folder unless the user asks for one by name. The working dir stays the repo root; reach the project with a relative path such as projects/<engine>/<name>/ - that is where your files go. data\active_project.txt and THREE_PROJECT hold the same value."
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
rem --- Model: whichever local server answers, router (:8080, serve-all.cmd) first,
rem --- Ollama (:1234, start-ollama.cmd) otherwise. Both providers are declared in
rem --- every profile, so the same session works in either mode and /model is not
rem --- the place where a dead port has to be diagnosed.
set "HAS_MODEL="
echo %PI_ARGS% | find "--model" >nul 2>&1 && set "HAS_MODEL=1"
if not defined HAS_MODEL (
  set "ROUTER=0"
  rem --- no quotes around %PY% inside for/f: cmd would cut the command at the quote
  for /f "usebackq delims=" %%P in (`%PY% -c "import socket;s=socket.socket();s.settimeout(0.4);print(1 if s.connect_ex(('127.0.0.1',8080))==0 else 0)"`) do set "ROUTER=%%P"
  if "!ROUTER!"=="1" (
    set "PI_ARGS=--model 3gs/qwen3.5-4b !PI_ARGS!"
  ) else (
    set "PI_ARGS=--model ollama/qwen3.5-9b-distill-deepseek-v4.1-flash !PI_ARGS!"
  )
)

if not "%PI_SP%"=="" (pi --append-system-prompt "%PI_SP%" %PI_ARGS%) else (pi %PI_ARGS%)
