@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0cmd\_env.cmd"

set "PY=%GS_ROOT%.venv\Scripts\python.exe"
if not exist "%PY%" (
  echo [ERROR] Python venv not found: "%PY%"
  exit /b 1
)

rem --- flags -------------------------------------------------------------------
rem   --no-wait   return as soon as the windows are spawned
rem   --restart   kill whatever holds :8080/:8081/:8083 first, then start fresh
set "WAIT=1"
set "RESTART=0"
:parse
if "%~1"=="" goto :parsed
if /i "%~1"=="--no-wait" set "WAIT=0"
if /i "%~1"=="--restart" set "RESTART=1"
shift
goto :parse
:parsed

rem --- Already up? -------------------------------------------------------------
rem Starting a second pair would only spawn two windows that die on a busy port
rem while the OLD instances keep answering - a false success. So we do not spawn.
rem But we say so LOUDLY and show who holds the ports, because closing the console
rem window does not always kill llama-server: it can survive as an orphan, keep the
rem port, and then this script opens NO windows at all. That reads as "serve-all
rem stopped opening terminals" while the launcher is in fact behaving correctly.
"%PY%" "%GS_ROOT%tools\wait_ready.py" --check --quiet >nul 2>&1
if errorlevel 1 goto :spawn
if "%RESTART%"=="0" goto :already

echo Both servers are already running - --restart given, stopping them first.
"%PY%" "%GS_ROOT%tools\wait_ready.py" --stop
ping -n 3 127.0.0.1 >nul 2>&1
goto :spawn

:already
echo.
echo   Both servers are ALREADY running - NO windows opened, and that is on purpose.
echo   A second pair would die on the busy port while the old ones keep answering.
echo.
"%PY%" "%GS_ROOT%tools\wait_ready.py" --status
echo.
call :rerank
echo   Restart : serve-all.cmd --restart
echo   Stop    : "%PY%" "%GS_ROOT%tools\wait_ready.py" --stop
echo.
goto :summary

:spawn
echo Starting the llama.cpp servers in separate windows...
start "3gs-llm" cmd /c ""%GS_ROOT%cmd\serve-llm.cmd""
ping -n 3 127.0.0.1 >nul 2>&1
start "3gs-embed" cmd /c ""%GS_ROOT%cmd\serve-embed.cmd""
call :rerank

if "%WAIT%"=="0" goto :summary

rem --- Block until both ports answer. `start` returns instantly, so a chain like
rem ---   serve-all.cmd && doctor.cmd && agent.cmd
rem --- used to reach doctor while the 9B model was still loading (about 30 s).
rem --- doctor then exited 1 and cmd silently skipped everything after it.
echo.
echo Waiting for the servers to finish loading (9B needs about 30 s)...
"%PY%" "%GS_ROOT%tools\wait_ready.py" --timeout 300
if errorlevel 1 (
  echo.
  echo [ERROR] servers did not come up. Nothing was launched.
  exit /b 1
)

:summary
echo.
echo   LLM    : http://127.0.0.1:8080
echo   EMBED  : http://127.0.0.1:8081
echo   RERANK : http://127.0.0.1:8083  (optional - hybrid search works without it)
echo.
echo Close those windows to stop the servers.
exit /b 0

rem --- Reranker: OPTIONAL, so start it only when its port is free --------------
rem Unconditional spawn would repeat the false-success bug of the other two: the
rem new instance dies instantly on the busy port while the old one keeps serving.
rem It is also NOT part of wait_ready's wait - the retrievers degrade to plain
rem hybrid search when it is missing, so blocking a startup on it would turn a
rem relevance drop into a hard stop.
:rerank
"%PY%" "%GS_ROOT%tools\wait_ready.py" --check-rerank --quiet >nul 2>&1
if not errorlevel 1 exit /b 0
echo   reranker :8083 is down - starting that one window
start "3gs-rerank" cmd /c ""%GS_ROOT%cmd\serve-rerank.cmd""
exit /b 0
