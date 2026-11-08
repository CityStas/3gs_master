@echo off
setlocal
rem ===========================================================================
rem  `pi` inside projects\<engine>\<project> - engine profile picked from where
rem  you are standing.
rem
rem    cd projects\three\my_game
rem    pi                       -> pi-home-three + threejs-rag + threejs skills
rem
rem  How it works: tools\pi_launch.py walks UP for engine.json, writes the
rem  `set` lines into a temp .cmd, this file sources them and then starts the
rem  REAL launcher (pi-launcher.js) as a direct child of this console. Python
rem  never sits in front of the TUI, so the terminal behaves exactly as before.
rem
rem  Three cases fall straight through to plain pi, unchanged:
rem    * PI_CODING_AGENT_DIR already set  (agent.cmd / pi-here.cmd decided)
rem    * cwd is outside the repo          (any other project on the machine)
rem    * no engine.json up to the repo root
rem
rem  Installed as `pi` by `cmd\pi-shim.cmd --install` (a forwarder in
rem  %USERPROFILE%\.pi\agent\bin replaces the managed pi.cmd; `pi update`
rem  restores the original, so re-run `gs pi-shim` after an update).
rem ===========================================================================

set "GS_ROOT=%~dp0..\"
for %%I in ("%GS_ROOT%.") do set "GS_ROOT=%%~fI\"
set "PY=%GS_ROOT%.venv\Scripts\python.exe"
set "REAL=%USERPROFILE%\.pi\agent\bin\pi-launcher.js"

if not exist "%PY%" goto :raw
if not exist "%REAL%" goto :raw

set "ENVF=%TEMP%\gs_pi_env_%RANDOM%%RANDOM%.cmd"
"%PY%" "%GS_ROOT%tools\pi_launch.py" --env-file "%ENVF%" -- %*
if errorlevel 1 goto :raw
if not exist "%ENVF%" goto :raw

call "%ENVF%"
del "%ENVF%" >nul 2>&1

rem --- PI_MODEL_ARGS / PI_SP_ARGS are empty when the caller supplied --model or
rem --- when the profile was already chosen by an outer launcher.
node "%REAL%" %PI_MODEL_ARGS% %PI_SP_ARGS% %*
exit /b %errorlevel%

:raw
node "%REAL%" %*
exit /b %errorlevel%
