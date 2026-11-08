@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_PROJECTS, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"

rem ===========================================================================
rem  What models can pi pick from, which one is in VRAM, and where the weights
rem  come from when they are not here yet.
rem
rem    models.cmd              registered models + what the running router has
rem    models.cmd --refresh    rescan models\ and GS_LLM_MODELS_DIR, rewrite the
rem                            preset + pi-home*\models.json (no restart needed)
rem    models.cmd --live       only the router's own answer
rem    models.cmd --list       only the registry (works with the server down)
rem    models.cmd --paths      where the weights are, what is there, what is missing
rem                            (root = GS_MODELS_ROOT, default <repo>\models)
rem    models.cmd --fetch      download what is missing, per models.manifest.json
rem                            [llm,rag,vlm,image,3d,3d-x | all] [--mirror] [--yes]
rem    models.cmd --verify     re-hash what is on disk   [groups] [--strict]
rem
rem  A newly copied .gguf appears in pi's `/model` list after --refresh. If the router
rem  is already running it does NOT need a restart: the preset is read at startup, but
rem  pi re-reads models.json on its own launch, so the usual order is
rem  --refresh, then exit and relaunch pi.
rem ===========================================================================

if /i "%~1"=="--refresh" goto :refresh
if /i "%~1"=="--live"    goto :live
if /i "%~1"=="--list"    goto :list
if /i "%~1"=="--paths"   goto :paths
if /i "%~1"=="--where"   goto :paths
if /i "%~1"=="--fetch"   goto :fetch
if /i "%~1"=="--verify"  goto :verify

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

:paths
rem --- the ONE report of "where are the models" - same module the stack configs use.
"%PY%" "%GS_ROOT%model_paths.py"
exit /b %errorlevel%

:fetch
rem --- `%*` already starts with `--fetch`, which is the flag the downloader wants,
rem --- so nothing has to be reshuffled here. (An earlier version collected the tail
rem --- by hand with `shift`; cmd then refused to find the loop label on an LF-only
rem --- file, and the whole thing died on the first `goto`.)
"%PY%" "%GS_ROOT%tools\models_fetch.py" %*
if errorlevel 1 exit /b %errorlevel%
rem --- a new .gguf is invisible to the router until the preset is rewritten.
echo.
echo [i] gs models --refresh - чтобы роутер увидел новые GGUF
exit /b 0

:verify
"%PY%" "%GS_ROOT%tools\models_fetch.py" %*
exit /b %errorlevel%
