@echo off
setlocal
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0cmd\_env.cmd"

rem --- Resume the previous pi session for a project.
rem ---
rem ---   resume.cmd projects\games\my_game
rem ---   resume.cmd projects\games\my_game "@projects\games\my_game\brief.md"
rem ---
rem --- --continue is appended for you, so the session picks up where it stopped
rem --- instead of starting blank. Everything else is forwarded to agent.cmd
rem --- untouched - it already does the project/argument handling, so there is
rem --- no second copy of that loop here.

if "%~1"=="" (
  echo Usage: resume.cmd ^<project^> [pi args...]
  echo   e.g. resume.cmd projects\games\my_game
  exit /b 1
)

call "%GS_ROOT%agent.cmd" %* --continue
exit /b %errorlevel%
