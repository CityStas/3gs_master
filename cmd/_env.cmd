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
rem Layout is projects\<engine>\<name>, one folder per engine, no shared "games"
rem folder - see project_layout.py. Which project is "active" is decided in Python
rem (tools\find_project.py), never guessed from these paths.
set "GS_PROJECTS_REL=projects"
set "GS_PROJECTS=%GS_ROOT%%GS_PROJECTS_REL%"

set "PY=%GS_ROOT%.venv\Scripts\python.exe"

rem --- weights root: relative by default, no drive letter in the repo ---------
rem ~65 GB of GGUF/ComfyUI is NOT in git, so "where the models are" is a property
rem of the MACHINE, not of the checkout. Order, same as model_paths.py:
rem
rem   GS_MODELS_ROOT    this project only (wins)
rem   LOCAL_LLM_MODELS  the shared root - a neutral name any other local-model tool
rem                     can read, so one folder serves several apps
rem   <repo>\models     default, which is what makes `git clone` + `gs models fetch`
rem                     work on any drive letter without editing a single file
rem
rem To keep the weights on a bigger disk, set the shared one ONCE per machine:
rem     setx LOCAL_LLM_MODELS "D:\AI\Models"
rem or put one line in `local.env.cmd` (machine-local, not tracked - see
rem `local.env.example.cmd`):
rem     set "GS_MODELS_ROOT=D:\AI\Models"
if not defined GS_MODELS_ROOT if defined LOCAL_LLM_MODELS set "GS_MODELS_ROOT=%LOCAL_LLM_MODELS%"
if not defined GS_MODELS_ROOT set "GS_MODELS_ROOT=%GS_ROOT%models"

rem --- Where alternative GGUF builds live (optional) --------------------------
rem `tools\llm_models.py` scans these IN ADDITION to the models root, and the
rem llama.cpp router on :8080 advertises everything it finds, so a model dropped
rem here shows up in pi's `/model` list after `cmd\models.cmd --refresh`.
rem `;`-separated for a second drive. Empty by default: a machine without extra
rem builds simply has fewer entries in /model.
rem     set "GS_LLM_MODELS_DIR=E:\Programs\LocalLLM\Models"

rem --- machine-local overrides ----------------------------------------------
rem Last, so it can override anything above (paths to Blender, Unity, Studio MCP,
rem model roots). The file is gitignored on purpose: absolute paths differ per
rem machine and must never travel with the repo.
if exist "%GS_ROOT%local.env.cmd" call "%GS_ROOT%local.env.cmd"

rem --- Blender: DCC-шаг пайплайна ассетов (риггинг/анимация/ретопо/конвертация) --
rem ComfyUI отдаёт сырой GLB; всё, что требует редактирования меша, идёт через
rem `blender --background --python`. Путь задаётся в `local.env.cmd`
rem (BLENDER_EXE); пусто = Blender не найден, и инструменты, которые на него
rem опираются, просто не появятся.
if defined BLENDER_EXE if not exist "%BLENDER_EXE%" set "BLENDER_EXE="

rem --- local servers must never go through a system proxy -------------------
set "NO_PROXY=127.0.0.1,localhost,::1,%NO_PROXY%"
set "no_proxy=%NO_PROXY%"
