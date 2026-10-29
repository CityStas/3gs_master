@echo off
setlocal
rem --- shared paths (GS_ROOT, PY, NO_PROXY) come from one place -----------------
call "%~dp0cmd\_env.cmd"

if not exist "%PY%" (
  echo [ERROR] Python venv not found: "%PY%"
  echo Create it with:  python -m venv .venv
  exit /b 1
)

rem --- Live view of the parallax hero: projects\research\web_1 ----------------
rem
rem   web1.cmd            http://127.0.0.1:8901/projects/research/web_1/index.html
rem   web1.cmd 8902       another port
rem
rem --- Why a server at all: the page is one <script type="module"> with an
rem --- import map pointing at ../../../vendor/three/. Opening index.html as a
rem --- file:// URL fails on two counts - module scripts are blocked by CORS and
rem --- the import map's relative path has nothing to resolve against. It has to
rem --- be HTTP, served from the REPO ROOT, because that is what the three levels
rem --- of ".." walk up to.
rem
rem --- Nothing here is a build step: index.html is the deliverable, edits are
rem --- live on reload.

set "PORT=%~1"
if not defined PORT set "PORT=8901"
set "URL=http://127.0.0.1:%PORT%/projects/research/web_1/index.html"

echo Serving %GS_ROOT%
echo   page : %URL%
echo   stop : Ctrl+C
echo.

rem --- Open the browser a moment AFTER the server binds, or the tab lands on a
rem --- connection refused and has to be reloaded by hand.
start "" cmd /c "ping -n 3 127.0.0.1 >nul & start """" ""%URL%"""

rem --- GS_ROOT ends with a backslash ("...\3GS_Master\"), and a backslash
rem --- immediately before the closing quote is an ESCAPED QUOTE to the Windows
rem --- argv parser. --directory "%GS_ROOT%" therefore arrived as
rem ---   F:\...\3GS_Master"
rem --- with a literal quote glued to the path, the directory did not exist, and
rem --- every request - including "/" - answered 404 "File not found". Strip the
rem --- trailing separator before handing the path over.
set "DOCROOT=%GS_ROOT%"
if "%DOCROOT:~-1%"=="\" set "DOCROOT=%DOCROOT:~0,-1%"

"%PY%" -m http.server %PORT% --bind 127.0.0.1 --directory "%DOCROOT%"
set "RC=%errorlevel%"
if not "%RC%"=="0" (
  echo.
  echo Exit code: %RC%
  pause
)
exit /b %RC%
