@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"

rem ===========================================================================
rem  LLM server on :8080 - llama.cpp ROUTER mode.
rem
rem  It used to load exactly one file (Qwen_Qwen3.5-9B-Q4_K_M.gguf). Now it reads an
rem  INI registry, advertises every entry on /v1/models, loads a model the first time a
rem  request names it, and evicts the least-recently-used one when the cap is hit:
rem
rem      curl :8080/v1/models                       -> every registered model id
rem      {"model":"omnicoder-9b", ...}              -> loads it, then answers
rem
rem  Why a router and not one server per port: the card is 8 GB, so exactly one 9B fits.
rem  Two servers would have to fight for VRAM; the router serialises them by design and
rem  keeps ONE baseUrl for pi, so switching models inside a session is just `/model`.
rem
rem  The registry is generated - models\llm-preset.ini comes from tools\llm_models.py,
rem  which scans models\ and GS_LLM_MODELS_DIR, reads each GGUF's KV geometry and picks a
rem  context that fits. Hand edits there are lost on every launch: put them in
rem  models\llm-overrides.json instead.
rem ===========================================================================

set "LLAMA=%GS_ROOT%bin\llama\llama-server.exe"
set "PRESET=%GS_ROOT%models\llm-preset.ini"

if not exist "%LLAMA%" (
  echo [ERROR] llama-server.exe not found: "%LLAMA%"
  exit /b 1
)

rem --- Regenerate the registry before starting. Cheap - only GGUF headers are read, no
rem --- weights are touched - and it is what makes a newly dropped .gguf appear without
rem --- anyone editing a file by hand.
echo Scanning local GGUF models...
"%PY%" "%GS_ROOT%tools\llm_models.py"
if errorlevel 1 (
  echo.
  echo [ERROR] model registry could not be built - nothing was started.
  exit /b 1
)
if not exist "%PRESET%" (
  echo [ERROR] no preset written: "%PRESET%"
  exit /b 1
)

rem --- Context. Per-model values now live in the preset; GS_LLM_CTX acts as a CEILING
rem --- applied during generation (tools\llm_models.py --ctx-cap), so exporting it
rem --- shrinks every model at once instead of being silently ignored.
rem ---
rem Qwen3.5-9B is a HYBRID architecture: only 8 of 33 blocks use full attention
rem (full_attention_interval=4), the rest are SSM with CONSTANT state. So the KV cache
rem is charged for 8 layers, not 33: 17 KiB/token at q8_0.
rem
rem   ctx  8192 -> KV   136 MiB | total VRAM ~5.6 GiB
rem   ctx 65536 -> KV  1088 MiB | total VRAM ~6.4 GiB | ~1.0 GiB left for the browser
rem   ctx 98304 -> KV  1632 MiB | total VRAM ~7.1 GiB | too tight
rem
rem The numbers in the preset, pi-home-*\models.json:contextWindow and
rem pi-home-*\settings.json:compaction.reserveTokens MUST agree: pi computes the
rem compaction threshold as contextWindow - reserveTokens and never asks the server.
set "MAXMODELS=1"
if not "%GS_LLM_MAXMODELS%"=="" set "MAXMODELS=%GS_LLM_MAXMODELS%"

rem --- Thinking. This build (0.6.0-dev, b11435) defaults `--reasoning auto`, which asks
rem the qwen35 chat template - and that template ALWAYS enables thinking. The pi session
rem logs (2026-10-12T10-06) show the cost: 47 assistant turns with a median 105-char
rem "thinking" block, 20 repeated-failed tool calls, and a compaction caught mid-task.
rem The model is not deliberating, it is pattern-matching into a tool call and then
rem re-issuing the same failed call.
rem
rem `off` is the known-good setting for the agent loop: it removes the <think> block the
rem tool-call parser trips over and cuts prompt-eval cost. Set GS_LLM_REASONING=on to get
rem the old behaviour back, or =budget to keep thinking under a hard cap
rem (GS_LLM_THINK_BUDGET tokens) - the middle ground worth testing.
set "REASONING=off"
if not "%GS_LLM_REASONING%"=="" set "REASONING=%GS_LLM_REASONING%"
set "THINK_BUDGET=1024"
if not "%GS_LLM_THINK_BUDGET%"=="" set "THINK_BUDGET=%GS_LLM_THINK_BUDGET%"

set "REASONING_ARGS=--reasoning %REASONING%"
if /i "%REASONING%"=="budget" set "REASONING_ARGS=--reasoning on --reasoning-budget %THINK_BUDGET%"

echo Starting LLM ROUTER on http://127.0.0.1:8080
echo   preset   : %PRESET%
echo   resident : up to %MAXMODELS% model(s) at a time (LRU evicts the rest)
echo   think    : %REASONING%
echo.
echo Switch models inside pi with /model, or ask the server directly:
echo   curl -s http://127.0.0.1:8080/v1/models
echo.
echo Press Ctrl+C to stop.
echo.

cd /d "%GS_ROOT%"
"%LLAMA%" --models-preset "%PRESET%" ^
  --models-max %MAXMODELS% ^
  --host 127.0.0.1 --port 8080 ^
  --jinja -ngl 999 -fa on -np 1 --no-webui ^
  --cache-type-k q8_0 --cache-type-v q8_0 ^
  %REASONING_ARGS% ^
  --temp 0.6 --top-p 0.95 --top-k 20
