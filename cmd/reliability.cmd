@echo off
setlocal
rem --- this launcher lives in cmd\; the repo root is one level up ---
rem --- shared paths (GS_ROOT, GS_PROJECTS, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"
set "PY=%GS_ROOT%.venv\Scripts\python.exe"
if not exist "%PY%" ( echo [ERROR] Python venv not found: "%PY%" & exit /b 1 )
cd /d "%GS_ROOT%"

rem --- The reliability layer's diagnostic surface. Policy lives in mcp\reliability.json;
rem --- the live guard is pi-extensions\loop-guard.ts, which writes one JSONL line per tool
rem --- call into logs\reliability\. Everything below reads that back.
rem ---
rem ---   gs reliability                     policy + last run summary
rem ---   gs reliability state               step list of the newest run
rem ---   gs reliability state --run pi-123  a specific run
rem ---   gs reliability log --tail 40       raw events
rem ---   gs reliability log --code FILE_NOT_FOUND
rem ---   gs reliability selftest            the policy's own regression suite
rem ---   gs reliability prune               enforce the log retention policy
rem ---   gs reliability verify <path>       postcondition check on one file
rem ---
rem --- `gs reliability` with no argument means `status`, so the common case is one word.
set "SUB=%~1"
if "%SUB%"=="" (
  "%PY%" "%GS_ROOT%tools\reliability.py" status %*
  exit /b %errorlevel%
)
"%PY%" "%GS_ROOT%tools\reliability.py" %*
exit /b %errorlevel%
