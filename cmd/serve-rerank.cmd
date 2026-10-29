@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"

set "LLAMA=%GS_ROOT%bin\llama\llama-server.exe"
set "MODEL=%GS_ROOT%models\bge-reranker-v2-m3-Q8_0.gguf"

if not exist "%LLAMA%" (
  echo [ERROR] llama-server.exe not found: "%LLAMA%"
  exit /b 1
)
if not exist "%MODEL%" (
  echo [ERROR] reranker model not found: "%MODEL%"
  exit /b 1
)

rem --- Why a THIRD server is needed ------------------------------------------
rem The reranker is a CROSS-encoder: it reads the query and ONE document TOGETHER,
rem so it cannot be served by :8081. That endpoint encodes each side alone and
rem never sees the pair, which is exactly the information a reranker adds. Same
rem llama.cpp binary, second pass over the fused shortlist (RERANK_TOP_K=50).
rem
rem Port 8083, NOT 8082: :8082 is the Qwen2.5-VL vision server (`cmd\vlm.cmd`).
rem The two would fight for the port and one of them would silently fail to start.
rem
rem Optional by design: if this server is down the retrievers degrade to plain
rem hybrid search and count the failure - relevance drops, answers do not stop.
rem That is why serve-all starts it but wait_ready.py does not REQUIRE it.
rem
rem -c 8192 -np 4 -> 2048 tokens PER SLOT. A document longer than one slot makes
rem llama-server answer HTTP 400, so the client clips to RERANK_MAX_CHARS=2000
rem before sending. Keep the two numbers in step if you change -c or -np.
rem
rem -ngl 99: measured on this box 0.67-1.06 s for 50 real chunks on GPU against
rem 1.45-2.37 s on CPU. The model is 0.6 GB, so the offload is cheap.
echo Starting reranker server on http://127.0.0.1:8083
echo   model : %MODEL%
echo   mode  : cross-encoder ^(-ngl 99^), 4 slots x 2048 tokens
echo Press Ctrl+C to stop.
echo.

cd /d "%GS_ROOT%"
"%LLAMA%" -m "%MODEL%" ^
  --host 127.0.0.1 --port 8083 ^
  --rerank --pooling rank ^
  -c 8192 -ngl 99 -b 2048 -ub 2048 -np 4 --no-webui
