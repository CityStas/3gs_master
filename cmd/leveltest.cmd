@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"

set "PY=%GS_ROOT%.venv\Scripts\python.exe"
if not exist "%PY%" ( echo [ERROR] Python venv not found: "%PY%" & exit /b 1 )
cd /d "%GS_ROOT%"

rem --- offline by default (fixtures + scorer, no server). Add --live when :8080 is up.
"%PY%" "%GS_ROOT%tools\level_autotest.py" %*
exit /b %errorlevel%
