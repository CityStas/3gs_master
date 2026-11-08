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

rem --- weights root: relative by default, no drive letter in the repo ---------
rem ~65 GB of GGUF/ComfyUI is NOT in git, so "where the models are" is a property
rem of the MACHINE, not of the checkout. The default is `<repo>\models`, which is
rem what makes `git clone` + `gs models fetch` work on any drive letter.
rem
rem `model_paths.py` reads the SAME two variables (GS_MODELS_ROOT,
rem GS_LLM_MODELS_DIR) with the same defaults, so batch and Python never disagree.
rem
rem To keep the weights on a bigger disk, put ONE line in `local.env.cmd`
rem (machine-local, not tracked - see `local.env.example.cmd`):
rem     set "GS_MODELS_ROOT=D:\AI\Models"
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
