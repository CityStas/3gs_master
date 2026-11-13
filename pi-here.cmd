@echo off
setlocal
rem --- pi in THIS directory: engine from ./engine.json, model from whichever server is up.
rem ---
rem ---   pi-here.cmd                 start pi with this project's profile
rem ---   pi-here.cmd --router-models what the router advertises, then exit
rem ---   pi-here.cmd --list-models   any pi arguments are passed through
rem ---
rem --- Why this exists. `agent.cmd` already picks pi-home-<engine> from engine.json,
rem --- but it wants a project name and lives in the repo root. A bare `pi` typed
rem --- inside a project has no PI_CODING_AGENT_DIR, so it silently uses the global
rem --- ~/.pi/agent profile - the Three.js one by accident, with none of the engine's
rem --- MCP servers or skills.
rem ---
rem --- Model choice is not left to /model either: both providers exist in every
rem --- profile (ollama :1234 = start-ollama.cmd, 3gs :8080 = serve-all.cmd), and the
rem --- one whose port answers wins. :8080 first - it is the 3GS router with RAG.
rem ---
rem --- Default weights: qwen3.5-4b, not the 9B distill that used to be here. The
rem --- distill is 5512 MB on an 8 GB card, which left ~1 GB and pinned the GPU for the
rem --- whole session; the 4B is the same qwen35 family at 2614 MB (4681 MiB resident).
rem --- Nothing was removed from the registry - the 9B builds under GS_LLM_MODELS_DIR
rem --- included - so switching back is one argument, not an edit:
rem ---
rem ---   pi-here.cmd --model 3gs/omnicoder-2-9b    any id the router advertises
rem ---   pi-here.cmd --router-models               print those ids and exit
rem ---   /model inside pi                          same list, interactive
rem ---
rem --- GS_PI_MODEL overrides the default for one shell without touching this file:
rem ---   set GS_PI_MODEL=3gs/ornith-1.5-9b-uncensored
call "%~dp0cmd\_env.cmd"
set "PY=%GS_ROOT%.venv\Scripts\python.exe"
if not exist "%PY%" (
  echo [ERROR] Python venv not found: "%PY%"
  exit /b 1
)

rem --- Before anything that needs a project: this only reads what is on disk.
if /i "%~1"=="--router-models" (
  "%PY%" "%GS_ROOT%tools\llm_models.py" --list
  exit /b %errorlevel%
)

set "ENGINE="
if exist "engine.json" (
  rem --- No quotes around %PY%: cmd's for/f backtick parser treats the first quote
  rem --- as the command boundary and hands python.exe only the word "import".
  for /f "usebackq delims=" %%E in (`%PY% -c "import json;print(json.load(open('engine.json',encoding='utf-8-sig')).get('engine',''))"`) do set "ENGINE=%%E"
)
if not defined ENGINE (
  echo [WARN] no engine.json in "%CD%" - falling back to the Three.js profile.
  echo        Create it first:  echo {"engine":"threejs"}^> engine.json
  set "ENGINE=threejs"
)

if /i "%ENGINE%"=="godot" (
  set "PI_CODING_AGENT_DIR=%GS_ROOT%pi-home-godot"
) else if /i "%ENGINE%"=="unity" (
  set "PI_CODING_AGENT_DIR=%GS_ROOT%pi-home-unity"
) else if /i "%ENGINE%"=="roblox" (
  set "PI_CODING_AGENT_DIR=%GS_ROOT%pi-home-roblox"
) else (
  set "PI_CODING_AGENT_DIR=%GS_ROOT%pi-home-three"
)

rem --- Router first: it is the only mode with RAG (:8081/:8083) and 64K contexts.
set "ROUTER=0"
for /f "usebackq delims=" %%P in (`%PY% -c "import socket;s=socket.socket();s.settimeout(0.4);print(1 if s.connect_ex(('127.0.0.1',8080))==0 else 0)"`) do set "ROUTER=%%P"
rem --- Ollama keeps the distill id: the router's 4B is not in Ollama's manifests, so a
rem --- 4B name here would 404 on the first request, and this branch is the fallback.
set "PI_MODEL=--model ollama/qwen3.5-9b-distill-deepseek-v4.1-flash"
set "SERVER=ollama :1234"
if "%ROUTER%"=="1" (
  set "PI_MODEL=--model 3gs/qwen3.5-4b"
  set "SERVER=3gs router :8080"
)
if defined GS_PI_MODEL set "PI_MODEL=--model %GS_PI_MODEL%"
set "MODEL_ID=%PI_MODEL:--model =%"

rem --- A system proxy swallows loopback calls: pi sends HTTP_PROXY to 127.0.0.1:1234
rem --- and hangs. Keep localhost out of it for this process tree.
set "NO_PROXY=127.0.0.1,localhost,::1,%NO_PROXY%"
set "no_proxy=%NO_PROXY%"
set "PI_SKIP_VERSION_CHECK=1"
set "PI_TELEMETRY=0"

echo pi profile : %ENGINE%  (%PI_CODING_AGENT_DIR%)
echo server     : %SERVER%
echo model      : %MODEL_ID%   (other: --model ^<provider^>/^<id^>, list: --router-models)
echo.

set "HAS_MODEL="
echo %* | find "--model" >nul 2>&1 && set "HAS_MODEL=1"
if defined HAS_MODEL (
  pi %*
) else (
  pi %PI_MODEL% %*
)
