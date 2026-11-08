@echo off
rem ===========================================================================
rem  MACHINE-LOCAL OVERRIDES - copy to `local.env.cmd` and edit that copy.
rem
rem  `cmd\_env.cmd` calls `local.env.cmd` LAST, so anything set here wins over
rem  every default in the repo. The real file is gitignored: absolute paths are
rem  a property of one machine and must never travel with the code.
rem
rem      copy local.env.example.cmd local.env.cmd
rem
rem  Nothing here is required. An empty (or missing) local.env.cmd means:
rem  weights in <repo>\models, no extra chat roots, no Blender.
rem ===========================================================================

rem --- weights root --------------------------------------------------------
rem Default is <repo>\models. Set this to keep ~65 GB of GGUF/ComfyUI on another
rem disk. Both the Python side (tools\model_paths.py) and the batch side
rem (vlm.cmd, sd-image.cmd, serve-llm.cmd) read the same variable.
rem
rem   set "GS_MODELS_ROOT=D:\AI\Models"

rem --- extra chat roots (optional, ';'-separated) --------------------------
rem Scanned IN ADDITION to the models root by tools\llm_models.py, and advertised
rem by the llama.cpp router on :8080. Only chat GGUFs belong here - embedding,
rem rerank, VLM and 3D models must live in GS_MODELS_ROOT.
rem
rem   set "GS_LLM_MODELS_DIR=E:\Programs\LocalLLM\Models"

rem --- Blender (asset pipeline: rigging, retopo, GLB->FBX) -----------------
rem
rem   set "BLENDER_EXE=E:\Programs\Blender\blender.exe"

rem --- Unity editor (compile gate, batch mode) -----------------------------
rem Auto-detected from Unity Hub installs; override only when that fails.
rem
rem   set "UNITY_EDITOR=C:\Program Files\Unity\Hub\Editor\6000.3.0f1\Editor\Unity.exe"

rem --- Roblox Studio MCP launcher ------------------------------------------
rem Auto-detected at %LOCALAPPDATA%\Roblox\mcp.bat.
rem
rem   set "ROBLOX_STUDIO_MCP=C:\...\StudioMCP.exe"
