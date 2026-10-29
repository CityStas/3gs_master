@echo off
setlocal
rem --- this launcher lives in cmd\; the repo root is one level up ---
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"
set "PY=%GS_ROOT%.venv\Scripts\python.exe"
if not exist "%PY%" ( echo [ERROR] Python venv not found: "%PY%" & exit /b 1 )
cd /d "%GS_ROOT%"

rem --- every file in tests\ that ends in _test.py or starts with test_ ---
set "RC=0"
for %%F in (tests\test_smoke.py tests\test_scheduler.py tests\test_asset_paths.py tests\test_project_paths.py tests\test_pagecheck.py tests\test_unity.py tests\test_rag_parity.py tests\test_level_autotest.py projects\research\x_life\tests\test_core.py projects\research\x_life\tests\test_modules.py projects\research\x_life\tests\test_life.py) do (
  echo.
  echo === %%F ===
  "%PY%" "%%F" %*
  if errorlevel 1 set "RC=1"
)

echo.
if "%RC%"=="0" (echo ALL TEST FILES PASSED) else (echo SOME TESTS FAILED)
exit /b %RC%
