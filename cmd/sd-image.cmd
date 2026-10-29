@echo off
setlocal enabledelayedexpansion
rem --- this launcher lives in cmd\; the repo root is one level up ---
rem --- shared paths (GS_ROOT, GS_GAMES, PY, NO_PROXY) come from one place ----
call "%~dp0_env.cmd"

rem --- z-image-turbo text-to-image via stable-diffusion.cpp (Vulkan) --------------
rem Standalone alternative to the ComfyUI Qwen-Image path. No server, one process
rem per image, ~4-8 s on a warm Vulkan device. The text encoder (Qwen3-4B) runs on
rem CPU on purpose: the 8 GB card has to hold the 3.9 GB diffusion model + VAE.

set "SD=%GS_ROOT%bin\sd-vulkan\sd-cli.exe"
set "DIFF=%GS_ROOT%models\image\z-image-turbo\z_image_turbo-Q4_K.gguf"
set "VAE=%GS_ROOT%models\image\z-image-turbo\ae.safetensors"
set "TE=%GS_ROOT%models\image\z-image-turbo\Qwen3-4B-Instruct-2507-Q4_K_M.gguf"

if not exist "%SD%"  ( echo [ERROR] sd-cli.exe not found: "%SD%" & exit /b 1 )
if not exist "%DIFF%" ( echo [ERROR] diffusion model not found: "%DIFF%" & exit /b 1 )

if "%~1"=="" (
  echo Usage: sd-image.cmd "your prompt" [output.png] [steps] [width] [height]
  echo   default: steps=8  width=1024  height=1024
  echo   output default: assets\images\zimage-^<timestamp^>.png
  exit /b 2
)

set "PROMPT=%~1"
set "OUT=%~2"
set "STEPS=%~3"
set "W=%~4"
set "H=%~5"

if "%OUT%"==""   set "OUT=%GS_ROOT%assets\images\zimage.png"
if "%STEPS%"=="" set "STEPS=8"
if "%W%"==""     set "W=1024"
if "%H%"==""     set "H=1024"

if not exist "%GS_ROOT%assets\images" mkdir "%GS_ROOT%assets\images"

cd /d "%GS_ROOT%"
echo z-image-turbo  %W%x%H%  steps=%STEPS%
echo prompt: %PROMPT%
echo output: %OUT%
echo.

"%SD%" -M img_gen ^
  --diffusion-model "%DIFF%" ^
  --vae "%VAE%" ^
  --llm "%TE%" ^
  -p "%PROMPT%" ^
  -o "%OUT%" ^
  -W %W% -H %H% ^
  --steps %STEPS% --cfg-scale 1.0 --guidance 1.0 ^
  --sampling-method euler --scheduler discrete ^
  --diffusion-fa --vae-tiling ^
  --backend diffusion=vulkan0,te=cpu

if errorlevel 1 ( echo. & echo [FAILED] sd-cli returned an error. & exit /b 1 )
echo.
echo done: %OUT%
