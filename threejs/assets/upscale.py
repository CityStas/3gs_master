"""Real-ESRGAN upscaling - the last step before a background goes into a game.

Why this is separate from the diffusion path
--------------------------------------------
z-image is fastest at 768-1856 px, and pushing the diffusion model past that costs
super-linearly. Real-ESRGAN is a small ncnn/Vulkan executable with no Python and no
PyTorch: it takes the finished picture and multiplies it, so a 1856x768 layer
becomes 3712x1536 in seconds instead of minutes.

It also has nothing to do with the GPU arbitration in `hardware.py`: the executable
holds a few hundred MB, not gigabytes, so it can run while sd-server is up. It is
deliberately *not* counted as a resident model.

Models shipped in `bin/Real-ESRGAN-ncnn-vulkan/models/`:

    realesrgan-x4plus         photos and painted art - the default
    realesrgan-x4plus-anime   line art and flat cel shading
    realesr-animevideov3-x2/3/4   smaller, faster, video-oriented
"""
from __future__ import annotations

import os
import subprocess
import time
from pathlib import Path

from .. import config
from .hardware import CREATE_NO_WINDOW, SchedulerError

MODELS = ("realesrgan-x4plus", "realesrgan-x4plus-anime",
          "realesr-animevideov3-x2", "realesr-animevideov3-x3",
          "realesr-animevideov3-x4")


def exe_path() -> Path:
    return config.ESRGAN_DIR / "realesrgan-ncnn-vulkan.exe"


def available() -> dict:
    exe = exe_path()
    found = [m for m in MODELS if (config.ESRGAN_DIR / "models" / f"{m}.param").exists()]
    return {"ok": exe.exists() and bool(found), "exe": str(exe),
            "exe_present": exe.exists(), "models": found}


class Upscaler:
    """`realesrgan-ncnn-vulkan.exe`, wrapped so a pack can call it like anything else.

    The `-s` scale is the *output* multiplier and must match the model family: the
    x4plus weights are trained for 4x, and asking for 2x makes ncnn run the 4x net
    and downsample. That is why a 2x request is not twice as fast as a 4x one.
    """

    def __init__(self, exe: Path | str | None = None, timeout: float = 900.0):
        self.exe = Path(exe) if exe else exe_path()
        self.timeout = timeout

    def upscale(self, image: str | Path, out: str | Path, *, scale: int = 2,
                model: str = "realesrgan-x4plus", tile: int = 0) -> dict:
        src, dst = Path(image), Path(out)
        if not src.exists():
            raise SchedulerError(f"upscale input not found: {src}")
        if not self.exe.exists():
            raise SchedulerError(f"realesrgan-ncnn-vulkan.exe not found: {self.exe}")
        if model not in MODELS:
            raise SchedulerError(f"unknown upscale model {model!r}; use one of {MODELS}")
        scale = max(1, min(4, int(scale)))
        dst.parent.mkdir(parents=True, exist_ok=True)
        args = [str(self.exe), "-i", str(src), "-o", str(dst),
                "-s", str(scale), "-n", model, "-f", "png"]
        if tile:
            args += ["-t", str(tile)]
        t0 = time.time()
        proc = subprocess.run(args, cwd=str(config.ESRGAN_DIR), capture_output=True,
                              timeout=self.timeout, creationflags=CREATE_NO_WINDOW)
        if proc.returncode != 0 or not dst.exists():
            tail = (proc.stderr or proc.stdout or b"").decode("utf-8", "replace")[-300:]
            raise SchedulerError(f"realesrgan failed (exit {proc.returncode}): {tail}")
        return {"path": str(dst), "bytes": dst.stat().st_size, "scale": scale,
                "model": model, "s": round(time.time() - t0, 1)}


__all__ = ["MODELS", "Upscaler", "available", "exe_path"]
