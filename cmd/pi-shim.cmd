@echo off
setlocal
rem ===========================================================================
rem  Make the bare word `pi` engine-aware everywhere on this machine.
rem
rem    cmd\pi-shim.cmd              status (default)
rem    cmd\pi-shim.cmd --install    write the forwarders
rem    cmd\pi-shim.cmd --uninstall  restore the managed launchers
rem
rem  What it touches: TWO files inside the managed pi install, both backed up
rem  next to themselves on the first install.
rem
rem    %USERPROFILE%\.pi\agent\bin\pi.cmd   -> cmd\pi.cmd   (cmd.exe)
rem    %USERPROFILE%\.pi\agent\bin\pi       -> tools\pi_launch.py  (sh/bash)
rem
rem  Neither the launcher JS nor anything else in the pi install is modified.
rem  `pi update` rewrites bin\pi.cmd and bin\pi from the release tarball, so the
rem  shim disappears on an update - run `gs pi-shim --install` again (status
rem  says so out loud).
rem
rem  Why not PATH: the pi bin dir is the FIRST entry of the user PATH, so a
rem  shim placed anywhere else would never win, and moving pi out of the way
rem  would break every other checkout on this machine.
rem ===========================================================================

set "GS_ROOT=%~dp0..\"
for %%I in ("%GS_ROOT%.") do set "GS_ROOT=%%~fI\"
set "BIN=%USERPROFILE%\.pi\agent\bin"
set "PY=%GS_ROOT%.venv\Scripts\python.exe"
set "MARKER=3GS-Master-pi-shim"

set "MODE=%~1"
if "%MODE%"=="" set "MODE=--status"

if /i "%MODE%"=="--install"   goto :install
if /i "%MODE%"=="--uninstall" goto :uninstall
if /i "%MODE%"=="--status"    goto :status
echo Usage: pi-shim.cmd [--install ^| --uninstall ^| --status]
exit /b 2

rem ---------------------------------------------------------------------------
:status
if not exist "%BIN%\pi.cmd" (
  echo [ERROR] the pi install is not where it is expected: %BIN%\pi.cmd
  exit /b 1
)
rem --- findstr, not find: a Git-Bash PATH puts the Unix `find` first and the
rem --- check would then answer "not installed" while the shim is right there.
findstr /C:"%MARKER%" "%BIN%\pi.cmd" >nul 2>&1
if errorlevel 1 (
  echo shim      : NOT installed  ^(pi runs the global ~/.pi/agent profile^)
  echo install   : cmd\pi-shim.cmd --install
  exit /b 1
)
echo shim      : installed
echo forwarder : %BIN%\pi.cmd  -^>  %GS_ROOT%cmd\pi.cmd
if exist "%BIN%\pi.cmd.orig" echo backup    : %BIN%\pi.cmd.orig
echo project   : cd projects\^<engine^>\^<name^>  then  pi
exit /b 0

rem ---------------------------------------------------------------------------
:install
if not exist "%BIN%\pi.cmd" (
  echo [ERROR] no managed pi install at %BIN% - install pi first:  pi update
  exit /b 1
)
if not exist "%BIN%\pi.cmd.orig" (
  copy /y "%BIN%\pi.cmd" "%BIN%\pi.cmd.orig" >nul
  if errorlevel 1 (
    echo [ERROR] could not back up %BIN%\pi.cmd
    exit /b 1
  )
  echo backed up : %BIN%\pi.cmd  -^>  pi.cmd.orig
)
> "%BIN%\pi.cmd" echo @ECHO off
>>"%BIN%\pi.cmd" echo rem %MARKER% - engine profile from the nearest engine.json.
>>"%BIN%\pi.cmd" echo rem Installed by "%GS_ROOT%cmd\pi-shim.cmd". Restore with --uninstall.
>>"%BIN%\pi.cmd" echo call "%GS_ROOT%cmd\pi.cmd" %%*

if exist "%BIN%\pi" (
  if not exist "%BIN%\pi.orig" copy /y "%BIN%\pi" "%BIN%\pi.orig" >nul
  > "%BIN%\pi" echo #!/bin/sh
  >>"%BIN%\pi" echo # %MARKER% - engine profile from the nearest engine.json.
  >>"%BIN%\pi" echo exec "%PY%" "%GS_ROOT%tools\pi_launch.py" "$@"
)

echo installed  : %BIN%\pi.cmd  -^>  %GS_ROOT%cmd\pi.cmd
echo verify     : cmd\pi-shim.cmd --status
exit /b 0

rem ---------------------------------------------------------------------------
:uninstall
if exist "%BIN%\pi.cmd.orig" (
  copy /y "%BIN%\pi.cmd.orig" "%BIN%\pi.cmd" >nul
  del "%BIN%\pi.cmd.orig" >nul 2>&1
  echo restored   : %BIN%\pi.cmd
) else (
  echo [WARN] no backup at %BIN%\pi.cmd.orig - `pi update` reinstalls the original.
)
if exist "%BIN%\pi.orig" (
  copy /y "%BIN%\pi.orig" "%BIN%\pi" >nul
  del "%BIN%\pi.orig" >nul 2>&1
  echo restored   : %BIN%\pi
)
exit /b 0
