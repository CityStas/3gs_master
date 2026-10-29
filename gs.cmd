@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0cmd\_env.cmd"

rem --- Service launchers live in cmd\; the day-to-day ones stay in the root. ---
set "BIN=%GS_ROOT%cmd"

set "SUB=%~1"
if "%SUB%"=="" goto :usage

rem --- Collect everything after the subcommand. The loop must stay OUTSIDE
rem --- parentheses: inside a block cmd substitutes %1 once at parse time and
rem --- `shift` would never be seen.
set "ARGS="
shift
:collect
if "%~1"=="" goto :route
set "ARGS=%ARGS% "%~1""
shift
goto :collect

:route
set "T="
if /i "%SUB%"=="up"      set "T=serve-all.cmd"
if /i "%SUB%"=="dev"     set "T=dev.cmd"
if /i "%SUB%"=="agent"   set "T=agent.cmd"
if /i "%SUB%"=="resume"  set "T=resume.cmd"
if /i "%SUB%"=="studio"  set "T=studio.cmd"
if /i "%SUB%"=="ask"     set "T=cmd\ask.cmd"
if /i "%SUB%"=="doctor"  set "T=cmd\doctor.cmd"
if /i "%SUB%"=="index"   set "T=cmd\index.cmd"
if /i "%SUB%"=="gen"     set "T=cmd\gen.cmd"
if /i "%SUB%"=="img"     set "T=cmd\sd-image.cmd"
if /i "%SUB%"=="check"   set "T=cmd\check.cmd"
if /i "%SUB%"=="newgame" set "T=cmd\newgame.cmd"
if /i "%SUB%"=="test"    set "T=cmd\test.cmd"
if /i "%SUB%"=="log"     set "T=cmd\pi-log.cmd"
if /i "%SUB%"=="llm"     set "T=cmd\serve-llm.cmd"
if /i "%SUB%"=="models"  set "T=cmd\models.cmd"
if /i "%SUB%"=="embed"   set "T=cmd\serve-embed.cmd"
if /i "%SUB%"=="rerank"  set "T=cmd\serve-rerank.cmd"
if /i "%SUB%"=="vlm"     set "T=cmd\vlm.cmd"
if /i "%SUB%"=="voice" set "T=cmd\serve-voice.cmd"
if /i "%SUB%"=="unity-fetch" set "T=cmd\unity-fetch.cmd"
if /i "%SUB%"=="unity-index" set "T=cmd\unity-index.cmd"
if /i "%SUB%"=="unity-check" set "T=cmd\unity-check.cmd"
if /i "%SUB%"=="unity-doctor" set "T=cmd\unity-doctor.cmd"
if /i "%SUB%"=="help"    goto :usage
if /i "%SUB%"=="-h"      goto :usage
if /i "%SUB%"=="--help"  goto :usage
if /i "%SUB%"=="?"       goto :usage

if not defined T (
  echo [ERROR] unknown command: %SUB%
  echo.
  goto :usage
)

call "%GS_ROOT%%T%" %ARGS%
exit /b %errorlevel%

:usage
echo Usage: gs ^<command^> [args...]
echo.
echo   up        start the model servers (serve-all) and wait until they answer
echo   dev       models + doctor + agent in one go  ^<game^> [--studio]
echo   agent     interactive pi session        [project] [@brief]
echo   ask       one-shot pi task              "task text"
echo   resume    continue a pi session         project [@brief]
echo   studio    studio in one window          [game] [port]
echo.
echo   newgame   scaffold projects\games\^<name^>  [--sync] [--force]
echo   gen       asset pack (generate.py)      -p ^<game^> -j ^<plan^>
echo   img       text-to-image                 "prompt" [out] [steps] [w] [h]
echo   check     tsc gate                      ^<game^> [--full^|--json^|--code ^<code^>]
echo   index     build the RAG index
echo   doctor    environment check
echo   test      run the test suite
echo   log       pi session log                [--last^|--session ^<id^>]
echo.
echo   llm ^| embed ^| rerank ^| vlm ^| voice   start a single model server directly
echo                             ^(rerank :8083 optional; voice :8084 = x_life creature^)
echo   models    models pi can pick from         [--refresh^|--live^|--list]
echo.
echo   unity-fetch   fetch the Unity docs corpus   [--with-source]
echo   unity-index   build the Unity RAG index
echo   unity-check   lint (+ optional --compile) a Unity project
echo   unity-doctor  Unity stack environment check
echo.
echo Day-to-day launchers (up/agent/resume/studio) live in the repo root;
echo the rest live in cmd\ - `gs` is just a front door to both.
exit /b 2
