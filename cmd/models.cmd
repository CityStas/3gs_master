@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"

rem ===========================================================================
rem  What models can pi pick from, and which one is in VRAM right now.
rem
rem    models.cmd              registered models + what the running router has
rem    models.cmd --refresh    rescan models\ and GS_LLM_MODELS_DIR, rewrite the
rem                            preset + pi-home*\models.json (no restart needed)
rem    models.cmd --live       only the router's own answer
rem    models.cmd --list       only the registry (works with the server down)
rem
rem  A newly copied .gguf appears in pi's `/model` list after --refresh. If the router
rem  is already running it does NOT need a restart: the preset is read at startup, but
rem  pi re-reads models.json on its own launch, so the usual order is
rem  --refresh, then exit and relaunch pi.
rem ===========================================================================

if /i "%~1"=="--refresh" goto :refresh
if /i "%~1"=="--live"    goto :live
if /i "%~1"=="--list"    goto :list

"%PY%" "%GS_ROOT%tools\llm_models.py" --list
echo.
"%PY%" "%GS_ROOT%tools\llm_models.py" --live
exit /b 0

:refresh
"%PY%" "%GS_ROOT%tools\llm_models.py"
echo.
echo Restart the LLM window (or serve-all.cmd --restart) so the router picks up the
echo new preset; pi picks up models.json on its next launch.
exit /b %errorlevel%

:live
"%PY%" "%GS_ROOT%tools\llm_models.py" --live
exit /b %errorlevel%

:list
"%PY%" "%GS_ROOT%tools\llm_models.py" --list
exit /b %errorlevel%
