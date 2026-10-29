@echo off
rem ===========================================================================
rem  ONE place that says where the user's projects live.
rem
rem  Moving the projects folder means editing the two GS_*_REL lines below and
rem  nothing else. Every launcher sources this file: dev, agent, studio, gs,
rem  serve-all and resume in the repo root, plus the twelve in cmd\.
rem
rem  DELIBERATELY NO `setlocal` HERE. This file must set the variables in the
rem  CALLER's environment; a `setlocal` would make them die on return and every
rem  launcher would receive empty paths. Scope is still bounded - each caller
rem  opens its own `setlocal` around the call.
rem
rem  The repo root is derived from %~dp0, i.e. from `cmd\` where this file
rem  lives - never from the current directory, so calling it works from
rem  anywhere, including a double click.
rem ===========================================================================

for %%I in ("%~dp0..") do set "GS_ROOT=%%~fI\"

rem --- projects root: relative form for messages, absolute form for work -----
set "GS_PROJECTS_REL=projects"
set "GS_GAMES_REL=%GS_PROJECTS_REL%\games"
set "GS_PROJECTS=%GS_ROOT%%GS_PROJECTS_REL%"
set "GS_GAMES=%GS_ROOT%%GS_GAMES_REL%"

set "PY=%GS_ROOT%.venv\Scripts\python.exe"

rem --- Blender: DCC-шаг пайплайна ассетов (риггинг/анимация/ретопо/конвертация) --
rem ComfyUI отдаёт сырой GLB; всё, что требует редактирования меша, идёт через
rem `blender --background --python`. Бинарь на этой машине:
rem E:\Programs\Blender\blender.exe (5.2.2 LTS). Пусто = Blender не найден, и
rem инструменты, которые на него опираются, просто не появятся.
if not defined BLENDER_EXE set "BLENDER_EXE=E:\Programs\Blender\blender.exe"
if not exist "%BLENDER_EXE%" set "BLENDER_EXE="

rem --- local servers must never go through a system proxy -------------------
set "NO_PROXY=127.0.0.1,localhost,::1,%NO_PROXY%"
set "no_proxy=%NO_PROXY%"

rem --- Where alternative GGUF builds live -----------------------------------
rem `tools\llm_models.py` scans this in addition to `models\`, and the llama.cpp router
rem on :8080 advertises everything it finds, so a model dropped here shows up in pi's
rem `/model` list after `cmd\models.cmd --refresh`. `;`-separated for a second drive.
if not defined GS_LLM_MODELS_DIR set "GS_LLM_MODELS_DIR=E:\Programs\LocalLLM\Models"
