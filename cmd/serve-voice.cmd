@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"

set "LLAMA=%GS_ROOT%bin\llama\llama-server.exe"
set "MODEL=%GS_ROOT%models\llm\mini\qwen3.5-0.8b-q4_k_m\qwen3.5-0.8b-q4_k_m.gguf"

if not exist "%LLAMA%" (
  echo [ERROR] llama-server.exe not found: "%LLAMA%"
  exit /b 1
)
if not exist "%MODEL%" (
  echo [ERROR] voice model not found: "%MODEL%"
  exit /b 1
)

rem --- Why a FOURTH server, and why it runs on the CPU ------------------------
rem x_life's creature needs a VOICE, not an intellect: name the episode, state one
rem hypothesis, name a goal. That is about 120 tokens, asked every few hundred
rem ticks - so it has to be cheap, not clever. 0.8B q4 is 517 MiB.
rem
rem Port 8084. 8080 is the 9B builder, 8081 the embedder, 8082 the Qwen2.5-VL
rem vision server, 8083 the reranker - all four are taken.
rem
rem -ngl 0 is the DEFAULT on purpose. The card is 8 GB and the 9B builder holds
rem about 6.4 GiB of it at ctx 65536; a second resident model would not fit, and
rem the voice is called episodically, so CPU latency is acceptable. On the
rem i3-12100 that is roughly 15-25 tok/s, i.e. 5-8 s per reflection.
rem Set GS_VOICE_NGL=999 to put it on the GPU - sensible ONLY while :8080 is
rem down, which is the "clean run" mode of the experiment.
rem
rem -c 4096 is enough: the input is a compact digest and the output is three short
rem fields. A larger context buys KV cache cost and nothing else.
rem
rem The creature is never allowed to call this server on its own initiative:
rem the brain asks for a reflection on a schedule. See x_life_arch/SAFETY.md.
set "NGL=0"
if not "%GS_VOICE_NGL%"=="" set "NGL=%GS_VOICE_NGL%"

echo Starting x_life voice server on http://127.0.0.1:8084
echo   model : %MODEL%
echo   mode  : -ngl %NGL% ^(0 = CPU, the safe default^), ctx 4096
echo Press Ctrl+C to stop.
echo.

cd /d "%GS_ROOT%"
"%LLAMA%" -m "%MODEL%" ^
  --alias xlife-voice ^
  --host 127.0.0.1 --port 8084 ^
  --jinja -c 4096 -ngl %NGL% -fa on -np 1 --no-webui ^
  --temp 0.8 --top-p 0.95
