"""Serialised generation: the game model plans, then gets out of the way.

The shape of a run
------------------
The Three.js agent decides what the game needs *first* - a list of images and 3D
models with prompts and target paths - and then hands the whole list over in one
`generate_pack()` call. From that moment the language model is switched off: its
process is stopped, its VRAM and ~6.4 GB of system RAM go to ComfyUI, and it is
started again only after the finished files have been moved into the project.

    1. plan        agent writes the job list
    2. llm off     llama-server :8080 killed, VRAM verified free
    3. comfy up    one session for the whole pack - no restarts between jobs
    4. generate    every job runs back to back into data/gen-staging/<run>/
    5. comfy off   the card is handed back
    6. place       artefacts move into the project at their final paths
    7. llm on      llama-server restarted; the agent resumes with real files

Steps 4 and 5 are the reason this exists: on 8 GB, running the two models
together cost 725 s for a single 512x512 four-step image (see `hardware.py`).
One at a time is the whole optimisation.

Why a batch and not one call per asset
--------------------------------------
Every call boundary would pay for a ComfyUI start/stop pair (1-3 min) and every
call would kill and reload the 9B. A pack of six images is one server start and
one model reload, not six.

Failure policy
--------------
A failing job does not abort the pack: five good assets out of six beat none.
Jobs that depend on a failed job are skipped with that reason. The LLM is
restarted from a `finally` block, so an exception anywhere still leaves the
agent able to think - the alternative is a session that is bricked until a human
notices.
"""
from __future__ import annotations

import json
import os
import shutil
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

from .. import config
from . import naming
from .comfy import ComfyClient
from .hardware import (GenLock, LlamaServer, SchedulerError, kill_tree, port_pid,
                       vram, wait_port_free)
from .pipeline import AssetPipeline
from .sd import SdClient, SdServer

#: Which artefact of a job is the one `out` names. A 3D job also produces a splat
#: and sometimes a turntable; those become siblings, never the primary.
PRIMARY_KIND = {"image": "image", "mask": "mask", "3d": "mesh",
                "upscale": "image", "recolor": "image", "edit": "image"}
KIND_ALIASES = {
    "image": "image", "img": "image", "picture": "image", "texture": "image",
    "t2i": "image", "text2image": "image",
    "mask": "mask", "alpha": "mask", "nobg": "mask", "remove_bg": "mask", "removebg": "mask",
    "3d": "3d", "mesh": "3d", "model": "3d", "glb": "3d", "character": "3d", "char": "3d",
    "upscale": "upscale", "esrgan": "upscale", "hires": "upscale", "enlarge": "upscale",
    "recolor": "recolor", "img2img": "recolor", "restyle": "recolor", "variation": "recolor",
    "edit": "edit", "reference": "edit", "ref": "edit",
}


@dataclass
class Job:
    """One requested artefact.

    `kind="image"`  prompt -> PNG
    `kind="mask"`   source image -> alpha PNG (BiRefNet by default)
    `kind="3d"`     source image -> GLB; with no source but a prompt, the image (and
                    its cut-out) are generated first, so `kind="3d"` alone is the full
                    text -> 3D loop. `character` is accepted as an alias.
    `kind="upscale"` source image -> larger PNG (Real-ESRGAN, no diffusion, no model
                    resident - it runs alongside whatever else is up).
    `kind="recolor"` source image + prompt -> PNG (z-image img2img). Global restyle,
                    not a masked edit; see `AssetPipeline.recolor`.
    `kind="edit"`   one or more source images + instruction -> PNG, on the
                    Qwen-Image-Edit graph. This is the kind that keeps a NEW asset
                    consistent with an EXISTING one: "keep this composition, swap
                    the character for the one in the second reference". Unlike
                    `recolor` it holds the composition (denoise = 1, but the latent
                    is built from the references) and it can write legible lettering,
                    which is why it lives on ComfyUI and not on z-image.

    The input for `mask`/`3d`/`upscale`/`recolor` comes from `from` - the *name* of an
    earlier job in the same pack, which is how "images first, then the things built
    from them" stays inside one session - or from `image`, a path relative to the
    project. `kind=edit` takes the same two spellings, but as a LIST (`images`), and
    the order is the order the graph numbers them: the first entry becomes `<image1>`.
    """

    index: int
    name: str
    kind: str
    prompt: str = ""
    out: str = ""
    source: str = ""
    #: 3D tier. `high` is the default: Pixal3D/TRELLIS.2 gives a UV-unwrapped PBR
    #: mesh that reacts to scene lighting; `economy` is an unlit TripoSplat splat.
    quality: str = "high"
    resolution: int = 1024
    megapixels: float | None = None
    aspect_ratio: str = "1:1 (Square)"
    steps: int | None = None
    steps_3d: int | None = None
    #: Reconstruction resolution for `kind=3d`. Measured to be close to a no-op: it
    #: crops the conditioning image, and TRELLIS.2 re-fits it internally, so 512 and
    #: 1024 came back with the same ~698 500 faces and the same wall clock. Kept
    #: because it is a documented knob, not because it buys anything.
    resolution_3d: int | None = None
    #: Decimation target for `kind=3d` - **the lever that actually sets the output**.
    #: The shipped workflow decimates to 700 000 faces, which is ~40 MB per prop and
    #: absurd for a 2D game. A sprite-scale prop wants 5 000-20 000.
    faces_3d: int | None = None
    seed: int | None = None
    fast: bool = True
    remove_bg_first: bool = True
    #: Which backend draws a `kind=image` job. `auto` means z-image, because it is
    #: 30-40x cheaper per image; `comfy` pins the job to Qwen-Image 2.1, which is
    #: the right call for anything with legible lettering in it.
    engine: str = "auto"
    #: Explicit pixel size for the z-image path. When both are absent the size is
    #: derived from `aspect_ratio` + `megapixels`, aligned down to a multiple of 64.
    width: int | None = None
    height: int | None = None
    negative: str = ""
    cfg: float | None = None
    guidance: float | None = None
    #: `kind=upscale`: output multiplier and which Real-ESRGAN net to use.
    scale: int = 2
    upscale_model: str = "realesrgan-x4plus"
    #: `kind=recolor`: how far img2img is allowed to drift (0.1-0.95).
    strength: float = 0.65
    #: `kind=edit`: the reference images, in graph order (`<image1>`, `<image2>`).
    #: Each entry is an earlier job's name or a path relative to the project.
    images: tuple[str, ...] = ()
    raw: dict = field(default_factory=dict)

    @classmethod
    def from_dict(cls, raw: dict, index: int) -> "Job":
        if not isinstance(raw, dict):
            raise SchedulerError(f"job #{index} is not an object: {raw!r}")
        kind = KIND_ALIASES.get(str(raw.get("kind") or "").strip().lower())
        if not kind:
            raise SchedulerError(
                f"job #{index}: unknown kind {raw.get('kind')!r}. Use one of "
                f"image, mask, 3d (character)."
            )
        prompt = str(raw.get("prompt") or "").strip()
        source = str(raw.get("from") or raw.get("image") or raw.get("source") or "").strip()
        # `images` is the plural spelling, and only `kind=edit` uses it. `from`/`image`
        # stay valid for it so a single-reference edit reads like every other kind.
        raw_images = raw.get("images")
        if isinstance(raw_images, (list, tuple)):
            images = tuple(str(x).strip() for x in raw_images if str(x).strip())
        elif raw_images:
            images = (str(raw_images).strip(),)
        else:
            images = ()
        if source and source not in images:
            images = (source,) + images
        name = naming.derive_name(prompt, str(raw.get("name") or ""))
        if name == "asset" and (source or images):
            name = naming.slugify(Path(source or images[0]).stem)
        if kind == "image" and not prompt:
            raise SchedulerError(f"job #{index} ({name}): kind=image needs a prompt")
        if kind in ("upscale", "recolor") and not source:
            raise SchedulerError(
                f"job #{index} ({name}): kind={kind} needs from=<earlier job> or "
                f"image=<path>"
            )
        if kind == "recolor" and not prompt:
            raise SchedulerError(f"job #{index} ({name}): kind=recolor needs a prompt")
        if kind == "edit" and not images:
            raise SchedulerError(
                f"job #{index} ({name}): kind=edit needs images=[...] - one or more "
                f"references, each an earlier job's name or a path"
            )
        if kind == "edit" and not prompt:
            raise SchedulerError(
                f"job #{index} ({name}): kind=edit needs a prompt - that is the edit "
                f"instruction, and it is what names <image1>, <image2>"
            )
        if kind == "3d" and not (prompt or source):
            raise SchedulerError(
                f"job #{index} ({name}): kind=3d needs from=<earlier job> or image=<path>, "
                f"or a prompt so the image can be generated first"
            )
        return cls(
            index=index, name=name, kind=kind, prompt=prompt,
            out=str(raw.get("out") or "").replace("\\", "/").lstrip("./"),
            source=source,
            images=images,
            quality=str(raw.get("quality") or "high").lower(),
            resolution=int(raw.get("resolution") or 1024),
            resolution_3d=int(raw["resolution_3d"]) if raw.get("resolution_3d") else None,
            faces_3d=int(raw["faces_3d"]) if raw.get("faces_3d") else None,
            # `resolution` is only the text encoder's pixel hint. The size of the picture
            # that comes out is ResolutionSelector(aspect_ratio, megapixels), so a job that
            # wants a small - and therefore fast - image has to say so here.
            megapixels=float(raw["megapixels"]) if raw.get("megapixels") else None,
            aspect_ratio=str(raw.get("aspect_ratio") or "1:1 (Square)"),
            steps=int(raw["steps"]) if raw.get("steps") else None,
            steps_3d=int(raw["steps_3d"]) if raw.get("steps_3d") else None,
            seed=int(raw["seed"]) if raw.get("seed") else None,
            fast=bool(raw.get("fast", True)),
            remove_bg_first=bool(raw.get("remove_bg_first", True)),
            engine=str(raw.get("engine") or "auto").strip().lower(),
            width=int(raw["width"]) if raw.get("width") else None,
            height=int(raw["height"]) if raw.get("height") else None,
            negative=str(raw.get("negative") or "").strip(),
            cfg=float(raw["cfg"]) if raw.get("cfg") is not None else None,
            guidance=float(raw["guidance"]) if raw.get("guidance") is not None else None,
            scale=int(raw.get("scale") or 2),
            upscale_model=str(raw.get("upscale_model") or "realesrgan-x4plus"),
            strength=float(raw["strength"]) if raw.get("strength") is not None else 0.65,
            raw=dict(raw),
        )


class GenerationScheduler:
    """Owns the invariant: at most one of {llama-server :8080, ComfyUI :8188} resident."""

    def __init__(self, comfy: ComfyClient | None = None, llm: LlamaServer | None = None,
                 sd: SdServer | None = None,
                 log_path: Path | str | None = None, lock_path: Path | str | None = None,
                 status_path: Path | str | None = None, staging_dir: Path | str | None = None):
        self.comfy = comfy or ComfyClient()
        self.llm = llm or LlamaServer()
        #: z-image-turbo (stable-diffusion.cpp). The default engine for plain images.
        self.sd = sd or SdServer()
        #: The pipeline talks HTTP, the scheduler owns the process - two objects.
        self.sd_client = SdClient(self.sd)
        self.log_path = Path(log_path) if log_path else config.GENERATE_LOG
        self.lock_path = Path(lock_path) if lock_path else config.GEN_LOCK_FILE
        self.status_path = Path(status_path) if status_path else config.GEN_STATUS_FILE
        self.staging_dir = Path(staging_dir) if staging_dir else config.GEN_STAGING_DIR
        self._comfy_timeout = 600.0
        # Cold z-image load is ~60 s of disk + VRAM setup, and the first job after it
        # pays another ~80 s of lazy graph construction. Be patient.
        self._sd_timeout = 300.0
        self.timeline: list[dict] = []
        self._jobs: list[Job] = []
        self._t0 = 0.0

    # ------------------------------------------------------------- reporting
    def _log(self, message: str) -> None:
        line = f"[{time.strftime('%H:%M:%S')}] {message}"
        try:
            self.log_path.parent.mkdir(parents=True, exist_ok=True)
            with self.log_path.open("a", encoding="utf-8") as fh:
                fh.write(line + "\n")
        except OSError:
            pass
        # Never stdout: this module also runs inside a stdio MCP server, where stdout
        # is the JSON-RPC channel.
        if os.environ.get("THREE_GEN_VERBOSE"):
            print(line, file=sys.stderr, flush=True)

    def _mark(self, step: str, **extra) -> dict:
        # Callers splat a dict straight in (`**self.llm.stop()`), so a key that collides
        # with the two reserved names would raise TypeError instead of logging.
        extra.pop("step", None)
        extra.pop("t", None)
        entry = {"step": step, "t": round(time.time() - self._t0, 1), **extra}
        self.timeline.append(entry)
        detail = " ".join(f"{k}={v}" for k, v in extra.items() if k != "timeline")
        self._log(f"{step} {detail}".rstrip())
        self._write_status()
        return entry

    def _mark_vram(self, step: str, data: dict) -> dict:
        """`_mark` with the current VRAM reading merged in.

        Exists because `stop()` returns a `vram` key in its "nothing was listening"
        branch, which makes the obvious `_mark(step, vram=vram(), **data)` a TypeError
        *at the call site* - and that call site is the teardown path, the one place that
        must not throw. Merging first keeps exactly one `vram` key, the fresh reading.
        """
        return self._mark(step, **{**data, "vram": vram()})

    def _write_status(self) -> None:
        """A live snapshot a human can watch with `type data\\gen-status.json`."""
        payload = {
            "run": getattr(self, "_run_id", ""),
            "project": str(getattr(self, "_project", "")),
            "updated": time.strftime("%Y-%m-%d %H:%M:%S"),
            "vram": vram(),
            "llm_alive": self.llm.alive(),
            "comfy_alive": self.comfy.is_alive(),
            "timeline": self.timeline[-40:],
        }
        try:
            self.status_path.parent.mkdir(parents=True, exist_ok=True)
            self.status_path.write_text(json.dumps(payload, ensure_ascii=False, indent=1),
                                        encoding="utf-8")
        except OSError:
            pass

    # ---------------------------------------------------------------- status
    def status(self) -> dict:
        holder = {}
        if self.lock_path.exists():
            try:
                holder = json.loads(self.lock_path.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001
                holder = {"unreadable": True}
        return {
            "invariant": ("at most one of llama-server :8080, sd-server :8687 and "
                          "ComfyUI :8188 is resident (Real-ESRGAN is exempt - it holds "
                          "a few hundred MB)"),
            "llm": self.llm.info(),
            "comfy": self.comfy.status(),
            "sd": self.sd.info(),
            "vram": vram(),
            "lock": holder or None,
            "log": str(self.log_path),
        }

    # ------------------------------------------------------------ lifecycle
    def _safe_comfy_stop(self) -> dict:
        try:
            res = self.comfy.stop()
            # stop() only knows the PID it started or the one in data/comfy.pid. A server
            # adopted from an earlier session can slip past that, and leaving it resident
            # is exactly the thing this module exists to prevent - so verify.
            if self.comfy.is_alive():
                pid = port_pid(self.comfy.port)
                kill_tree(pid)
                wait_port_free(self.comfy.port, 20)
                res = {**res, "escalated": pid, "port_free": not self.comfy.is_alive()}
            return res
        except Exception as exc:  # noqa: BLE001
            return {"stopped": False, "error": f"{type(exc).__name__}: {exc}"}

    def _restore_llm(self, was_up: bool, enabled: bool, timeout: float) -> dict:
        if not enabled:
            return {"restored": False, "reason": "stop_llm=False - the LLM was never stopped"}
        if not was_up:
            return {"restored": False, "reason": "the LLM was not running before this run"}
        try:
            res = self.llm.ensure(timeout=timeout)
            return {"restored": True, **res, "vram": vram()}
        except Exception as exc:  # noqa: BLE001
            return {"restored": False, "error": f"{type(exc).__name__}: {exc}",
                    "hint": f"start it by hand: {self.llm.launcher}  (see {self.llm.log})"}

    def _prune_staging(self, keep_days: float = 7.0) -> None:
        cutoff = time.time() - keep_days * 86400
        for child in self.staging_dir.glob("*"):
            try:
                if child.is_dir() and child.stat().st_mtime < cutoff:
                    shutil.rmtree(child, ignore_errors=True)
            except OSError:
                pass

    # ------------------------------------------------------------------ jobs
    def _engine_for(self, job: Job) -> str:
        """Which backend serves this job.

        `auto` sends plain images to z-image: 8 steps of a distilled model in ~20 s,
        holding 3.8 GB of the card, against ~12 min and 8.9 GB for the Qwen-Image
        path. Everything else stays on ComfyUI because it has no z-image equivalent -
        BiRefNet cut-outs, and the TripoSplat/Pixal3D mesh graphs. A job can pin
        either side: `"engine": "comfy"` for anything with lettering that has to be
        legible, `"engine": "z-image"` to force the fast path.
        """
        want = (job.engine or "auto").strip().lower()
        if job.kind == "upscale":
            # Real-ESRGAN is a small ncnn executable, not a resident model: it needs
            # no backend of its own and must not disturb whichever one is up.
            return "none"
        if want in ("z-image", "zimage", "z_image", "sd", "fast"):
            if job.kind not in ("image", "recolor"):
                raise SchedulerError(
                    f"job '{job.name}': engine=z-image serves kind=image/recolor only, "
                    f"not {job.kind}"
                )
            return "z-image"
        if want in ("comfy", "comfyui", "qwen", "qwen-image"):
            return "comfy"
        if want != "auto":
            raise SchedulerError(
                f"job '{job.name}': unknown engine {job.engine!r} - use auto, "
                f"z-image or comfy"
            )
        return "z-image" if job.kind in ("image", "recolor") else "comfy"

    def _safe_sd_stop(self) -> dict:
        try:
            return self.sd.stop()
        except Exception as exc:  # noqa: BLE001
            return {"stopped": False, "error": f"{type(exc).__name__}: {exc}"}

    def _switch_backend(self, engine: str, current: str | None) -> str:
        """Make `engine` the resident one. The card holds one of them, never both."""
        if engine == current:
            return engine
        if current == "comfy":
            self._mark_vram("comfy_stopped", self._safe_comfy_stop())
        elif current == "z-image":
            self._mark_vram("sd_stopped", self._safe_sd_stop())
        if engine == "comfy":
            started = self.comfy.ensure(timeout=self._comfy_timeout)
            self._mark_vram("comfy_ready", started)
        else:
            started = self.sd.ensure(timeout=self._sd_timeout)
            self._mark_vram("sd_ready", started)
        return engine

    def _run_jobs(self, staging: Path, project: Path) -> dict:
        pipeline = AssetPipeline(self.comfy, root=staging, sd=self.sd_client)
        state: dict[str, dict] = {"done": {}, "failed": {}}
        rows: list[dict] = []
        current: str | None = None
        switches = 0
        for job in self._jobs:
            row = {"index": job.index, "name": job.name, "kind": job.kind, "ok": False,
                   "engine": "", "s": 0.0, "files": [], "error": None}
            t0 = time.time()
            try:
                engine = self._engine_for(job)
                row["engine"] = engine
                # Fail fast on a broken dependency. `_source` raises the same thing, but
                # only *after* the switch below has already paid for a backend start -
                # a wasted ~47 s ComfyUI boot to then discover the input never existed.
                if job.source and job.source in state["failed"]:
                    raise SchedulerError(
                        f"job '{job.name}' skipped: its input '{job.source}' failed "
                        f"({state['failed'][job.source]})"
                    )
                # "none" (upscale) needs no resident model, so it never forces a switch.
                if engine != current and engine != "none":
                    switches += 1
                    current = self._switch_backend(engine, current)
                self._mark("job_begin", job=job.name, kind=job.kind, engine=engine)
                artefacts = self._run_one(pipeline, job, state, project)
                row["ok"] = True
                row["files"] = [a.to_dict() for a in artefacts]
                state["done"][job.name] = artefacts
            except Exception as exc:  # noqa: BLE001
                row["error"] = f"{type(exc).__name__}: {exc}"
                state["failed"][job.name] = row["error"]
            row["s"] = round(time.time() - t0, 1)
            self._mark("job_end", job=job.name, ok=row["ok"], s=row["s"],
                       error=row["error"] or "")
            rows.append(row)
        return {"jobs": rows, "error": None, "placed": [], "staging": str(staging),
                "engine_last": current, "switches": switches}

    def _run_one(self, pipeline: AssetPipeline, job: Job, state: dict, project: Path) -> list:
        if job.kind == "image":
            if self._engine_for(job) == "z-image":
                return pipeline.image_fast(
                    job.prompt, job.name, width=job.width, height=job.height,
                    aspect_ratio=job.aspect_ratio, megapixels=job.megapixels,
                    steps=job.steps, cfg=job.cfg, guidance=job.guidance,
                    seed=job.seed, negative=job.negative)
            return pipeline.image(job.prompt, job.name, resolution=job.resolution,
                                  aspect_ratio=job.aspect_ratio, megapixels=job.megapixels,
                                  steps=job.steps, seed=job.seed)

        if job.kind == "upscale":
            return pipeline.upscale(self._source(job, state, project), job.name,
                                    scale=job.scale, model=job.upscale_model)

        if job.kind == "recolor":
            return pipeline.recolor(self._source(job, state, project), job.prompt,
                                    job.name, strength=job.strength,
                                    width=job.width, height=job.height,
                                    steps=job.steps, seed=job.seed)

        if job.kind == "mask":
            return pipeline.remove_bg(self._source(job, state, project), job.name, fast=job.fast)

        if job.kind == "edit":
            return pipeline.edit(self._sources(job, state, project), job.prompt, job.name)

        source = self._source(job, state, project, optional=True)
        artefacts: list = []
        if source is None:
            # No input image: this is the full text -> image -> cut-out -> mesh loop, run
            # as one job so the intermediate image is available too if the mesh disappoints.
            images = pipeline.image(job.prompt, job.name, resolution=job.resolution,
                                    aspect_ratio=job.aspect_ratio, megapixels=job.megapixels,
                                    steps=job.steps, seed=job.seed)
            artefacts += images
            cut = pipeline.remove_bg(images[0].path, job.name, fast=True)
            artefacts += cut
            source, remove_bg_first = cut[0].path, False
        else:
            remove_bg_first = job.remove_bg_first
        artefacts += pipeline.to_3d(source, job.name, quality=job.quality,
                                     resolution=job.resolution_3d,
                                     faces=job.faces_3d,
                                     steps=job.steps_3d, seed=job.seed,
                                     remove_bg_first=remove_bg_first)
        return artefacts

    def _source(self, job: Job, state: dict, project: Path, optional: bool = False):
        return self._resolve(job, job.source, state, project, optional)

    def _sources(self, job: Job, state: dict, project: Path) -> list[Path]:
        """Every reference of a `kind=edit` job, in the order the graph numbers them.

        Order is not cosmetic: `imageNodes` maps the first entry to `<image1>` and the
        second to `<image2>`, and the instruction addresses them by those names. It is
        also the first image that sets the output's aspect ratio.
        """
        return [self._resolve(job, spec, state, project) for spec in job.images]

    def _resolve(self, job: Job, spec: str, state: dict, project: Path,
                 optional: bool = False):
        if spec:
            if spec in state["done"]:
                artefacts = state["done"][spec]
                # Prefer the picture over the mesh: a `mask`/`3d` job wants pixels in.
                for want in ("image", "mask", "mesh", "splat"):
                    hit = next((a for a in artefacts if a.kind == want), None)
                    if hit:
                        return Path(hit.path)
                raise SchedulerError(f"job '{job.name}': '{spec}' produced no usable image")
            if spec in state["failed"]:
                raise SchedulerError(
                    f"job '{job.name}' skipped: its input '{spec}' failed "
                    f"({state['failed'][spec]})"
                )
            path = Path(spec)
            if not path.is_absolute():
                path = project / path
            if path.exists():
                return path
            raise SchedulerError(
                f"job '{job.name}': input '{spec}' is neither an earlier job in this "
                f"pack nor a file ({path})"
            )
        if optional:
            return None
        raise SchedulerError(f"job '{job.name}': kind={job.kind} needs from=<job> or image=<path>")

    # --------------------------------------------------------------- placing
    def _dest(self, job: Job, artefact: dict, project: Path, primary: bool) -> Path:
        ext = Path(artefact["filename"]).suffix or ".bin"
        if not job.out:
            sub = config.ASSET_SUBDIR.get(artefact["kind"], "3d")
            return project / config.PROJECT_ASSET_ROOT / sub / f"{job.name}{ext}"
        base = Path(job.out)
        if not base.is_absolute():
            base = project / base
        if primary:
            return base if base.suffix else base.with_suffix(ext)
        return base.with_name(f"{base.stem}-{artefact['kind']}{ext}")

    @staticmethod
    def _place_file(src: Path, dst: Path) -> dict:
        dst.parent.mkdir(parents=True, exist_ok=True)
        overwrote = dst.exists()
        try:
            os.replace(src, dst)          # same volume: atomic, overwrites in place
        except OSError:
            shutil.copy2(src, dst)        # staging on another drive
            src.unlink(missing_ok=True)
        return {"path": str(dst), "bytes": dst.stat().st_size, "overwrote": overwrote}

    def _place_all(self, report: dict, project: Path) -> list[dict]:
        by_index = {r["index"]: r for r in report.get("jobs", [])}
        placed: list[dict] = []
        for job in self._jobs:
            row = by_index.get(job.index)
            if not row or not row["ok"]:
                continue
            files = row["files"]
            primary_kind = PRIMARY_KIND.get(job.kind, "mesh")
            primary_at = next((i for i, f in enumerate(files) if f["kind"] == primary_kind), 0)
            for i, artefact in enumerate(files):
                src = Path(artefact["path"])
                if not src.exists():
                    continue
                dst = self._dest(job, artefact, project, primary=(i == primary_at))
                info = self._place_file(src, dst)
                try:
                    rel = dst.relative_to(project).as_posix()
                except ValueError:
                    rel = ""
                url = ""
                public = project / "public"
                try:
                    url = "/" + dst.relative_to(public).as_posix()
                except ValueError:
                    pass
                placed.append({"job": job.name, "kind": artefact["kind"], "rel": rel,
                               "url": url, **info})
        return placed

    # -------------------------------------------------------------- entry point
    def generate_pack(self, project: str = "", jobs=None, *, stop_llm: bool = True,
                      keep_comfy: bool = False, lock_timeout: float = 30.0,
                      comfy_timeout: float = 600.0, llm_timeout: float = 300.0) -> dict:
        """Plan in, files out. The LLM is off for the duration and back afterwards."""
        if isinstance(jobs, (str, bytes)):
            jobs = json.loads(jobs)
        project_path = config.resolve_project(project)
        self._jobs = [Job.from_dict(raw, i) for i, raw in enumerate(jobs or [])]
        if not self._jobs:
            raise SchedulerError("empty pack: pass at least one job")

        self._t0 = time.time()
        self._run_id = time.strftime("%Y%m%d-%H%M%S")
        self._project = project_path
        self.timeline = []
        staging = self.staging_dir / self._run_id
        staging.mkdir(parents=True, exist_ok=True)
        self._prune_staging()

        self._log(f"=== pack {self._run_id}: {len(self._jobs)} job(s) -> {project_path}")
        self._mark("pack_begin", jobs=len(self._jobs), project=str(project_path), vram=vram())

        lock = GenLock(self.lock_path)
        lock.acquire(lock_timeout)
        try:
            return self._run_locked(staging, project_path, stop_llm, keep_comfy,
                                    comfy_timeout, llm_timeout)
        finally:
            lock.release()
            self._write_status()

    def _run_locked(self, staging: Path, project: Path, stop_llm: bool, keep_comfy: bool,
                    comfy_timeout: float, llm_timeout: float) -> dict:
        llm_was_up = self.llm.alive()
        vram_before = vram()
        report: dict = {"jobs": [], "placed": [], "error": None}
        comfy_stop: dict = {}
        sd_stop: dict = {}
        restore: dict = {}
        vram_during: dict = {}
        self._comfy_timeout = comfy_timeout

        if stop_llm and llm_was_up:
            self._mark("llm_stop", vram_before=vram_before)
            self._mark("llm_stopped", **self.llm.stop())
        elif stop_llm:
            self._mark("llm_absent", note="the LLM was not running - the card is already free")

        try:
            try:
                # Backends are started lazily by `_run_jobs`, per engine, because a pack
                # may mix z-image and ComfyUI jobs and only one of them fits on the card.
                report = self._run_jobs(staging, project)
                vram_during = vram()
            except Exception as exc:  # noqa: BLE001
                report["error"] = f"{type(exc).__name__}: {exc}"
                self._mark("run_failed", error=report["error"])

            if keep_comfy:
                self._mark("backends_kept",
                           note="keep_comfy=True - ComfyUI/sd-server still resident")
            else:
                # Stopped by name, not by "whichever we started": a server adopted from
                # an earlier session would otherwise survive, and leaving one resident is
                # the exact thing this module exists to prevent.
                comfy_stop = self._safe_comfy_stop()
                self._mark_vram("comfy_stopped", comfy_stop)
                sd_stop = self._safe_sd_stop()
                self._mark_vram("sd_stopped", sd_stop)

            report["placed"] = self._place_all(report, project)
            self._mark("placed", files=len(report["placed"]))
        finally:
            restore = self._restore_llm(llm_was_up, stop_llm, llm_timeout)
            self._mark("llm_restored", **{k: v for k, v in restore.items() if k != "vram"})

        failed = [r["name"] for r in report.get("jobs", []) if not r["ok"]]
        ok = not report.get("error") and not failed
        result = {
            "ok": ok,
            "project": str(project),
            "run": self._run_id,
            "total_s": round(time.time() - self._t0, 1),
            "llm": {"was_up": llm_was_up, **restore},
            "comfy": {"stopped": comfy_stop},
            "sd": {"stopped": sd_stop},
            "engine_switches": report.get("switches", 0),
            "vram": {"before": vram_before, "during": vram_during, "after": vram()},
            "jobs": report.get("jobs", []),
            "files": report.get("placed", []),
            "failed": failed,
            "error": report.get("error"),
            "timeline": self.timeline,
        }
        if failed or report.get("error"):
            result["staging"] = str(staging)
            result["note"] = ("staging kept for inspection; it is pruned automatically after 7 days")
        else:
            shutil.rmtree(staging, ignore_errors=True)
        self._log(f"=== pack {self._run_id} done ok={ok} in {result['total_s']}s "
                  f"files={len(result['files'])}")
        return result
