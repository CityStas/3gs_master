"""z-image-turbo via stable-diffusion.cpp - the fast text-to-image engine.

Why this module exists
----------------------
The ComfyUI path (`comfy.py` -> Qwen-Image 2.1) is a 8.9 GB text-encoder +
transformer pair. Measured on this box it needs ~12 min for a 1.5 MP image, and
while it runs the 9B agent model has to be switched off because the card is
8 GB.

Z-Image Turbo is a 6-10 step distilled model whose three pieces are small enough
to share the card: the diffusion transformer (3.7 GB) and VAE (0.16 GB) in VRAM,
the Qwen3-4B text encoder (3.5 GB) in system RAM. It reports

    total params memory size = 7400.58MB (VRAM 3845.21MB, RAM 3555.38MB)

so it holds 3.8 GB of an 8 GB card, not 8.9 GB. Warm generation is ~20 s; the
one-off cost is ~60 s to load the three files. That is a 30-40x difference for
backgrounds and sprites, which is why z-image is the default engine and ComfyUI
is the fallback for the things z-image cannot do:

* **lettering** - Qwen-Image 2.1 draws words far more faithfully than a 6-step
  distilled model, so title art and menu splashes stay on the ComfyUI path;
* **cut-outs** - BiRefNet (`remove_bg_fast`) is a real segmentation model;
* **image-to-3D** - TripoSplat / Pixal3D only exist as ComfyUI graphs.

The two engines are never resident together: ComfyUI wants the whole card and
sd-server wants half of it, so the scheduler stops one before starting the other.

Server or CLI
-------------
Server mode is the only mode that makes sense for a pack: `sd-cli.exe` re-reads
~6.6 GB of weights per image (30-50 s of pure I/O each time), while
`sd-server.exe` loads once and then answers in ~20 s. The CLI route survives as
`sd-image.cmd` for a single hand-run image.

Tuning that is not obvious
--------------------------
* `--vae-tiling` is mandatory. Without it the VAE decode at 768 px asks for
  ~5.9 GB of compute buffer and dies with an OOM on this card.
* `te=cpu` is deliberate. Putting the text encoder on the GPU (`te=cuda0`) was
  measured at 26.2 s against 17.3 s - the 4 GB diffusion model and the 2.3 GB
  encoder strangle each other.
* `cache-dit` is deliberately absent. On Vulkan it is *harmful*: fixed cost grew
  from 5.7 s to 10.3 s and diffusion from 1.64 to 3.9 s/step.
* `--model-args qwen_image_zero_cond_t=true` is Z-Image-specific; without it the
  model loads but conditions wrongly.

Nothing here writes to stdout: this code also runs inside stdio MCP servers,
where anything printed corrupts the JSON-RPC stream.
"""
from __future__ import annotations

import base64
import json
import os
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

from .. import config
from .hardware import (CREATE_NO_WINDOW, DETACHED, SchedulerError, http_up,
                       kill_tree, port_pid, vram, wait_free_vram, wait_port_free)

#: Tuned on this box for 768x768 game art. `cfg` is 1.0 because the model is
#: distilled - the guidance signal travels in `distilled_guidance` instead.
DEFAULTS = {
    "width": 768, "height": 768, "steps": 8, "cfg": 1.0, "guidance": 3.5,
    "sample_method": "euler", "scheduler": "sgm_uniform",
}


class SdError(SchedulerError):
    pass


def model_paths() -> dict:
    """The three files Z-Image needs, as one bundle."""
    root = config.SD_MODEL_DIR
    return {
        "diffusion": root / "z_image_turbo-Q4_K.gguf",
        "vae": root / "ae.safetensors",
        "llm": root / "Qwen3-4B-Instruct-2507-Q4_K_M.gguf",
    }


def missing_models() -> list[str]:
    return [str(p) for p in model_paths().values() if not p.exists()]


def available() -> dict:
    """Can the z-image engine run at all? Answers without starting anything."""
    paths = model_paths()
    missing = missing_models()
    exe = config.SD_BIN_DIR / "sd-server.exe"
    return {
        "ok": not missing and exe.exists(),
        "exe": str(exe),
        "exe_present": exe.exists(),
        "models": {k: {"path": str(v), "exists": v.exists(),
                       "mb": round(v.stat().st_size / 1048576) if v.exists() else 0}
                   for k, v in paths.items()},
        "missing": missing,
    }


# --------------------------------------------------------------------- server
class SdServer:
    """The :8687 stable-diffusion.cpp server, seen as something to switch on and off.

    Mirrors `hardware.LlamaServer` on purpose: the scheduler already knows how to
    stop the LLM and wait for its VRAM to come back, and sd-server needs exactly
    the same treatment. Detached spawn for the same reason too - a plain child
    dies with the process tree, and the scheduler that started it is not always
    the one that outlives it.
    """

    def __init__(self, port: int | None = None, host: str | None = None,
                 exe: Path | str | None = None, log: Path | str | None = None):
        self.host = host or config.SD_HOST
        self.port = int(port or config.SD_PORT)
        self.base = f"http://{self.host}:{self.port}"
        self.exe = Path(exe) if exe else (config.SD_BIN_DIR / "sd-server.exe")
        self.log = Path(log) if log else (config.LOGS_DIR / "sd-sidecar.log")

    # -------------------------------------------------------------- state
    def alive(self) -> bool:
        return http_up(f"{self.base}/sdcpp/v1/capabilities")

    def pid(self) -> int:
        return port_pid(self.port)

    def info(self) -> dict:
        return {"alive": self.alive(), "port": self.port, "pid": self.pid(),
                "exe": str(self.exe), "log": str(self.log), "vram": vram(),
                "engine": available()}

    # ---------------------------------------------------------- lifecycle
    def stop(self, wait: float = 30.0) -> dict:
        pid = self.pid()
        if not pid:
            return {"stopped": False, "reason": f"nothing listening on :{self.port}",
                    "vram": vram()}
        before = vram()
        kill_tree(pid)
        freed = wait_port_free(self.port, wait)
        after = wait_free_vram(min_free_mb=max(0, (before.get("total_mb") or 8192) - 1500),
                               timeout=45.0)
        return {"stopped": True, "pid": pid, "port_free": freed,
                "vram_before": before, "vram_after": after}

    def command(self) -> list[str]:
        paths = model_paths()
        return [
            str(self.exe),
            "--diffusion-model", str(paths["diffusion"]),
            "--vae", str(paths["vae"]),
            "--llm", str(paths["llm"]),
            "--listen-port", str(self.port),
            "--diffusion-fa",
            "--vae-tiling",
            "--backend", "diffusion=vulkan0,te=cpu",
            "--model-args", "qwen_image_zero_cond_t=true",
        ]

    def start(self) -> dict:
        if self.alive():
            return {"started": False, "reason": "already running", "pid": self.pid()}
        if not self.exe.exists():
            raise SdError(f"sd-server.exe not found: {self.exe}")
        missing = missing_models()
        if missing:
            raise SdError("z-image weights missing: " + ", ".join(missing))
        self.log.parent.mkdir(parents=True, exist_ok=True)
        handle = self.log.open("ab")
        handle.write(f"\n=== start {time.strftime('%Y-%m-%d %H:%M:%S')}\n".encode())
        handle.flush()
        env = dict(os.environ)
        # The Vulkan build otherwise picks up whatever ICD the shell happens to
        # export; GGML_VK_VISIBLE_DEVICES pins it to the one card this box has.
        env.setdefault("GGML_VK_VISIBLE_DEVICES", "0")
        proc = subprocess.Popen(
            self.command(), cwd=str(config.SD_BIN_DIR), env=env,
            stdout=handle, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
            creationflags=DETACHED, close_fds=True,
        )
        handle.close()
        return {"started": True, "mode": "detached", "pid": proc.pid, "log": str(self.log)}

    def wait(self, timeout: float = 300.0) -> bool:
        t0 = time.monotonic()
        while time.monotonic() - t0 < timeout:
            if self.alive():
                return True
            time.sleep(1.5)
        return False

    def ensure(self, timeout: float = 300.0) -> dict:
        """Start if needed. `timeout` is generous because the load is ~60 s cold."""
        if self.alive():
            return {"started": False, "reason": "already running"}
        res = self.start()
        if not self.wait(timeout):
            raise SdError(
                f"sd-server did not answer on {self.base}/sdcpp/v1/capabilities "
                f"within {timeout:.0f}s. See {self.log}."
            )
        return res


# --------------------------------------------------------------------- client
class SdClient:
    """HTTP client for the two endpoints sd-server actually exposes.

    `POST /sdcpp/v1/img_gen` is asynchronous - it returns `{id, poll_url}` and the
    picture arrives later under `result.images[0].data` (base64). `POST
    /sdapi/v1/img2img` is the A1111-compatible synchronous form and is what a
    follow-up edit uses.
    """

    def __init__(self, server: SdServer | None = None, timeout: float = 600.0):
        self.server = server or SdServer()
        self.timeout = timeout
        self._opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

    # ------------------------------------------------------------- plumbing
    def _json(self, path: str, payload: dict | None = None, timeout: float | None = None):
        url = f"{self.server.base}{path}"
        data = json.dumps(payload).encode() if payload is not None else None
        req = urllib.request.Request(
            url, data=data, method="POST" if data is not None else "GET",
            headers={"Content-Type": "application/json"} if data is not None else {},
        )
        try:
            with self._opener.open(req, timeout=timeout or self.timeout) as r:
                body = r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[-300:]
            raise SdError(f"sd-server {path} HTTP {exc.code}: {detail}") from exc
        except Exception as exc:  # noqa: BLE001
            raise SdError(f"sd-server {path} unreachable: {type(exc).__name__}: {exc}") from exc
        try:
            return json.loads(body)
        except json.JSONDecodeError as exc:
            raise SdError(f"sd-server {path} returned non-JSON: {body[:200]}") from exc

    @staticmethod
    def _decode(job: dict) -> bytes:
        images = ((job.get("result") or {}).get("images") or [])
        if not images:
            raise SdError(f"sd-server returned no image (status={job.get('status')})")
        first = images[0]
        b64 = first.get("data") or first.get("b64_json") or ""
        if not b64:
            raise SdError("sd-server image entry has no data/b64_json field")
        if "," in b64[:64]:                      # tolerate a full data: URL
            b64 = b64.split(",", 1)[1]
        return base64.b64decode(b64)

    def capabilities(self) -> dict:
        return self._json("/sdcpp/v1/capabilities", timeout=15.0)

    def cancel(self, job_id: str) -> bool:
        try:
            self._json(f"/sdcpp/v1/jobs/{job_id}/cancel", {}, timeout=15.0)
            return True
        except SdError:
            return False

    # ------------------------------------------------------------ text->image
    def generate(self, prompt: str, *, width: int | None = None, height: int | None = None,
                 steps: int | None = None, cfg: float | None = None,
                 guidance: float | None = None, seed: int | None = None,
                 sample_method: str | None = None, scheduler: str | None = None,
                 negative: str = "", timeout: float | None = None) -> bytes:
        prompt = (prompt or "").strip()
        if not prompt:
            raise SdError("empty prompt")
        # 64 is the model's latent alignment: an odd width is rejected outright.
        width = int(width or DEFAULTS["width"]) // 64 * 64
        height = int(height or DEFAULTS["height"]) // 64 * 64
        body = {
            "prompt": prompt,
            "width": width,
            "height": height,
            "seed": int(seed if seed is not None else -1),
            "output_format": "png",
            "sample_params": {
                "sample_steps": int(steps or DEFAULTS["steps"]),
                "sample_method": sample_method or DEFAULTS["sample_method"],
                "scheduler": scheduler or DEFAULTS["scheduler"],
                "guidance": {
                    "txt_cfg": float(cfg if cfg is not None else DEFAULTS["cfg"]),
                    "distilled_guidance": float(guidance if guidance is not None
                                                else DEFAULTS["guidance"]),
                },
            },
        }
        if negative.strip():
            body["negative_prompt"] = negative.strip()

        queued = self._json("/sdcpp/v1/img_gen", body, timeout=60.0)
        job_id = str(queued.get("id") or (queued.get("poll_url") or "").rstrip("/").split("/")[-1])
        if not job_id:
            raise SdError(f"sd-server did not return a job id: {queued}")
        return self._await(job_id, timeout or self.timeout)

    def _await(self, job_id: str, timeout: float) -> bytes:
        t0 = time.monotonic()
        job: dict = {}
        while time.monotonic() - t0 < timeout:
            time.sleep(0.5)
            job = self._json(f"/sdcpp/v1/jobs/{job_id}", timeout=30.0)
            status = str(job.get("status") or "").lower()
            if status in ("completed", "failed", "cancelled", "error"):
                break
        else:
            self.cancel(job_id)
            raise SdError(f"sd-server job {job_id} timed out after {timeout:.0f}s")
        status = str(job.get("status") or "").lower()
        if status != "completed":
            err = job.get("error")
            if isinstance(err, (dict, list)):
                err = json.dumps(err, ensure_ascii=False)
            raise SdError(f"sd-server job {job_id} {status}{': ' + str(err) if err else ''}")
        return self._decode(job)

    # ------------------------------------------------------------ image edit
    @staticmethod
    def _png_size(path: Path) -> tuple[int, int] | None:
        """Width/height straight out of the PNG IHDR.

        Needed because img2img otherwise falls back to the 768x768 default and
        squashes a 1856x768 parallax layer into a square - the aspect ratio is part
        of the asset, not a preference.
        """
        try:
            with path.open("rb") as fh:
                head = fh.read(24)
        except OSError:
            return None
        if len(head) < 24 or head[:8] != b"\x89PNG\r\n\x1a\n" or head[12:16] != b"IHDR":
            return None
        return (int.from_bytes(head[16:20], "big"), int.from_bytes(head[20:24], "big"))

    def img2img(self, image: str | Path, prompt: str, *, strength: float = 0.65,
                width: int | None = None, height: int | None = None,
                steps: int | None = None, cfg: float | None = None,
                seed: int | None = None, sample_method: str | None = None,
                scheduler: str | None = None, negative: str = "",
                timeout: float | None = None) -> bytes:
        path = Path(image)
        if not path.exists():
            raise SdError(f"init image not found: {path}")
        if width is None or height is None:
            size = self._png_size(path)
            if size:
                width = width or size[0]
                height = height or size[1]
        payload = {
            "init_images": [base64.b64encode(path.read_bytes()).decode()],
            "prompt": prompt,
            "denoising_strength": max(0.1, min(0.95, float(strength))),
            "width": int(width or DEFAULTS["width"]),
            "height": int(height or DEFAULTS["height"]),
            "steps": int(steps or DEFAULTS["steps"]),
            "cfg_scale": float(cfg if cfg is not None else DEFAULTS["cfg"]),
            "seed": int(seed if seed is not None else -1),
            "sampler_name": sample_method or DEFAULTS["sample_method"],
            "scheduler": scheduler or DEFAULTS["scheduler"],
            "output_format": "png",
        }
        if negative.strip():
            payload["negative_prompt"] = negative.strip()
        res = self._json("/sdapi/v1/img2img", payload, timeout=timeout or self.timeout)
        b64 = (res.get("images") or [None])[0]
        if not b64:
            raise SdError(f"sd-server img2img returned no image: {str(res)[:200]}")
        return base64.b64decode(b64.split(",", 1)[1] if "," in b64[:64] else b64)


__all__ = ["DEFAULTS", "SdClient", "SdError", "SdServer", "available",
           "missing_models", "model_paths"]
