@echo off
setlocal
rem --- this launcher lives in cmd\; the repo root is one level up ---
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"
set "PY=%GS_ROOT%.venv\Scripts\python.exe"
if not exist "%PY%" ( echo [ERROR] Python venv not found: "%PY%" & exit /b 1 )
cd /d "%GS_ROOT%"
"%PY%" "%GS_ROOT%tools\pi_log.py" %*
exit /b %errorlevel%
