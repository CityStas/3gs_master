@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"

set "LLAMA=%GS_ROOT%bin\llama\llama-server.exe"
set "MODEL=%GS_ROOT%models\bge-m3-q4_k_m.gguf"

if not exist "%LLAMA%" (
  echo [ERROR] llama-server.exe not found: "%LLAMA%"
  exit /b 1
)
if not exist "%MODEL%" (
  echo [ERROR] embedding model not found: "%MODEL%"
  exit /b 1
)

echo Starting embedding server on http://127.0.0.1:8081
echo   model : %MODEL%
echo   mode  : GPU ^(-ngl 99^), 4 slots, ctx 32768
echo Press Ctrl+C to stop.
echo.

rem --- -ngl 99, not 0 ----------------------------------------------------------
rem bge-m3 was originally pinned to the CPU to leave the whole 8 GB card to the
rem 9B model. Measured on this box, that is a bad trade: bulk embedding of the
rem Unity corpus ran 16.15 chunks/s end-to-end on CPU against 75-83 chunks/s with
rem the model offloaded, i.e. ~5x, with the card at 88-94 percent utilisation while the
rem LLM is idle. Weights end up in shared/host memory under WDDM, so nvidia-smi's
rem memory.used stays near 1 GB - the utilisation figure, not the memory figure,
rem is what proves the offload is live.
cd /d "%GS_ROOT%"
"%LLAMA%" -m "%MODEL%" ^
  --host 127.0.0.1 --port 8081 ^
  --embedding --pooling cls ^
  -c 32768 -ngl 99 -b 8192 -ub 8192 -np 4 --no-webui
