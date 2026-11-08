@echo off
setlocal EnableExtensions
rem ===========================================================================
rem  From nothing to a working 3GS_Master, in one command.
rem
rem    setup.cmd                 venv + deps + weights + doctor
rem    setup.cmd --no-models     venv + deps + doctor (weights later)
rem    setup.cmd --mirror        download through hf-mirror.com
rem
rem  Idempotent: everything already in place is skipped, so running it twice is
rem  safe and cheap. Weights land in %GS_MODELS_ROOT% (LOCAL_LLM_MODELS if the
rem  machine has it, else <repo>\models) - no drive letter is assumed anywhere.
rem
rem  A .cmd on purpose: this is the first thing a person runs, before any shell
rem  integration exists, so it must not require PowerShell.
rem ===========================================================================
call "%~dp0cmd\_env.cmd"

set "WANT_MODELS=1"
set "MIRROR="
:args
if "%~1"=="" goto :python
if /i "%~1"=="--no-models" set "WANT_MODELS=0"
if /i "%~1"=="--mirror" set "MIRROR=--mirror"
shift
goto :args

:python
echo.
echo 3GS_Master setup
echo   root    : %GS_ROOT%
echo   models  : %GS_MODELS_ROOT%
echo.

set "PYBASE="
where py >nul 2>nul && set "PYBASE=py"
if not defined PYBASE ( where python >nul 2>nul && set "PYBASE=python" )
if not defined PYBASE goto :no_python
echo [ok] python: %PYBASE%

rem --- venv ------------------------------------------------------------------
if exist "%PY%" goto :venv_ok
echo [..] creating .venv
if /i "%PYBASE%"=="py" ( py -3 -m venv "%GS_ROOT%.venv" ) else ( python -m venv "%GS_ROOT%.venv" )
if not exist "%PY%" goto :no_venv
echo [ok] venv created
goto :deps
:venv_ok
echo [ok] venv already at %GS_ROOT%.venv

rem --- dependencies ----------------------------------------------------------
:deps
echo [..] pip install -r requirements.txt
"%PY%" -m pip install --upgrade pip --quiet
"%PY%" -m pip install -r "%GS_ROOT%requirements.txt" --quiet
if errorlevel 1 goto :no_deps
echo [ok] dependencies

rem --- what is missing -------------------------------------------------------
echo.
"%PY%" "%GS_ROOT%tools\models_fetch.py" --group llm,rag,vlm,image,3d
if "%WANT_MODELS%"=="0" goto :skipped

echo.
echo [..] downloading weights into %GS_MODELS_ROOT%
echo      the long part: ~39 GB on a fresh machine, resumes if interrupted
"%PY%" "%GS_ROOT%tools\models_fetch.py" --fetch %MIRROR% --yes
if errorlevel 1 echo [WARN] not everything downloaded - re-run `gs models --fetch`, it resumes
goto :doctor

:skipped
echo.
echo [i] weights skipped (--no-models); later: gs models --fetch

rem --- sanity ----------------------------------------------------------------
:doctor
echo.
"%PY%" "%GS_ROOT%tools\doctor.py" --quick
echo.
echo Next:
echo   1. gs models --paths      what is present, what is missing
echo   2. dev.cmd my_game        services + agent for a new Three.js project
echo   3. gs --help              every command
exit /b 0

:no_python
echo [FAIL] Python not found on PATH.
echo        Install Python 3.11+ from https://www.python.org/downloads/windows/
echo        tick "Add python.exe to PATH", then run this again.
exit /b 1

:no_venv
echo [FAIL] venv was not created - is the "venv" module available in this Python?
exit /b 1

:no_deps
echo [FAIL] pip install failed - see the output above.
exit /b 1
