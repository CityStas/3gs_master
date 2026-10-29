@echo off
setlocal
rem --- this launcher lives in cmd\; the repo root is one level up ---
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"

rem --- Qwen2.5-VL-7B vision server (llama-mtmd) ----------------------------------
rem OpenAI-compatible endpoint on http://127.0.0.1:8082/v1 . Useful for "look at this
rem render and tell me what is wrong" loops. Kept separate from the 9B coding model
rem because both together do not fit in 8 GB of VRAM.

set "LLAMA=%GS_ROOT%bin\llama-mtmd\llama-server.exe"
set "MODEL=%GS_ROOT%models\vlm\Qwen2.5-VL-7B\Qwen2.5-VL-7B-Instruct-Q4_K_M.gguf"
set "MMPROJ=%GS_ROOT%models\vlm\Qwen2.5-VL-7B\mmproj-Qwen2.5-VL-7B-Instruct-Q8_0.gguf"

if not exist "%LLAMA%"  ( echo [ERROR] llama-server.exe not found: "%LLAMA%" & exit /b 1 )
if not exist "%MODEL%"  ( echo [ERROR] VLM model not found: "%MODEL%" & exit /b 1 )
if not exist "%MMPROJ%" ( echo [ERROR] mmproj not found: "%MMPROJ%" & exit /b 1 )

set "PORT=8082"
if not "%GS_VLM_PORT%"=="" set "PORT=%GS_VLM_PORT%"

echo Starting VLM server on http://127.0.0.1:%PORT%
echo   model  : %MODEL%
echo   mmproj : %MMPROJ%
echo   ctx    : 8192, -ngl 99
echo Press Ctrl+C to stop.
echo.

cd /d "%GS_ROOT%"
"%LLAMA%" -m "%MODEL%" --mmproj "%MMPROJ%" ^
  --host 127.0.0.1 --port %PORT% ^
  -ngl 99 -c 8192 -fa on --no-webui
