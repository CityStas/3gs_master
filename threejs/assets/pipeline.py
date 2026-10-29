"""High-level asset pipeline: text -> image -> background removal -> 3D -> three.js.

Everything lands in `assets/` under a name derived from the request:

    assets/images/<slug>.png          text-to-image result
    assets/masks/<slug>-nobg.png      alpha-cut version
    assets/3d/<slug>.glb              mesh ready for GLTFLoader
    assets/splats/<slug>.spz          Gaussian splat (economy path preview)
    assets/previews/<slug>.mp4        orbit turntable (when the workflow produces one)

Two 3D quality tiers exist because they are genuinely different products, not a
quality slider:

* **high** - Pixal3D / TRELLIS.2. ~17-18 min warm. Real mesh with UV unwrap and PBR
  textures. **This is the default**, because a mesh that ignores lighting is not a
  finished asset. `resolution` is the lever if it is too slow - match it to how big
  the thing actually renders in the game.
* **economy** - TripoSplat. ~2.5-3.5 min warm. Gaussian splat, photoreal, *no UVs*,
  `KHR_materials_unlit` so it ignores lights. Opt in for previews and throwaway props.
"""
from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, asdict
from pathlib import Path

from .. import config
from . import naming
from .comfy import ComfyClient, ComfyError, load_manifest, load_workflow, workflow_def
from .sd import SdClient
from .upscale import Upscaler

QUALITY = {"economy": "to_3d_economy", "high": "to_3d_high", "fast": "to_3d_economy", "best": "to_3d_high"}
KIND_DIR = {
    "image": config.ASSET_IMAGE_DIR,
    "mask": config.ASSET_MASK_DIR,
    "mesh": config.ASSET_3D_DIR,
    "splat": config.ASSET_SPLAT_DIR,
    "preview": config.ASSET_PREVIEW_DIR,
    "file": config.ASSET_3D_DIR,
}
KIND_SUFFIX = {"mask": "-nobg"}


class AssetInputError(FileNotFoundError):
    """An input image could not be located.

    Subclasses `FileNotFoundError`, so anything already catching that keeps working,
    but the message carries the paths that were tried. The bare
    `No such file or directory: 'public\\assets\\apple.png'` that ComfyUI used to
    raise deep inside the run told an agent nothing it could act on - it answered
    five of those by copying one finished cut-out over four other files.
    """


def _strip_kind_suffix(name: str, suffix: str) -> str:
    """`apple-nobg` -> `apple`. The suffix belongs to the pipeline, not the caller."""
    s = str(name or "").strip()
    if suffix and s.lower().endswith(suffix.lower()):
        return s[: -len(suffix)].rstrip("-_ ")
    return s


def locate_input(image: str | Path, *, project: str | Path | None = None) -> Path:
    """Resolve an input image to a real file. A relative path is project-first.

    `scheduler._resolve` already resolves a pack's `image`/`from` against the
    project. The single tools did not - they handed `Path(image)` straight to the
    pipeline, which resolved against the server's own working directory, so the
    same-looking argument meant two different things depending on which tool you
    called. Same contract everywhere now: **project first**, then the current
    directory, then the repo root.
    """
    raw = str(image or "").strip().strip('"').strip("'")
    if not raw:
        raise AssetInputError("no image given")
    p = Path(raw).expanduser()
    if p.is_absolute():
        if p.exists():
            return p
        raise AssetInputError(f"no such file: {p}")

    roots: list[Path] = []
    try:
        roots.append(config.resolve_project(project))
    except Exception:  # noqa: BLE001 - no active project is not fatal here
        pass
    roots += [Path.cwd(), config.THREE_RAG_HOME]

    tried: list[str] = []
    for root in roots:
        candidate = root / p
        if candidate.exists():
            return candidate.resolve()
        if str(candidate) not in tried:
            tried.append(str(candidate))
    raise AssetInputError(
        f"image '{raw}' not found. Tried:\n  " + "\n  ".join(tried) +
        "\nGive the path as it looks from the project root, or an absolute path."
    )


@dataclass
class Artefact:
    kind: str
    path: str
    bytes: int
    filename: str

    def to_dict(self) -> dict:
        return asdict(self)


class AssetPipeline:
    """`root` retargets the whole store.

    With no root, artefacts land in the repo-wide `assets/` tree described above. With
    `root=<project>/public/assets`, the same `images/ masks/ 3d/ splats/ previews/`
    layout is created under that root instead - which is how a generated pack ends up
    inside the game that asked for it.
    """

    def __init__(self, client: ComfyClient | None = None, root: Path | str | None = None,
                 sd: "SdClient | None" = None):
        self.client = client or ComfyClient()
        self.root = Path(root).resolve() if root else None
        #: z-image-turbo. Only `image_fast()` uses it; everything else needs ComfyUI.
        self.sd = sd or SdClient()
        #: Real-ESRGAN. Only `upscale()` uses it, and it needs no resident model.
        self.upscaler = Upscaler()

    def _kind_dir(self, kind: str) -> Path:
        if self.root is None:
            return KIND_DIR.get(kind, config.ASSET_3D_DIR)
        return self.root / config.ASSET_SUBDIR.get(kind, "3d")

    # ------------------------------------------------------------------ helpers
    def _run(self, workflow_id: str, *, images=None, prompt=None, params=None,
             extra_drop=None) -> list[dict]:
        definition = workflow_def(workflow_id)
        if definition is None:
            raise ComfyError(f"workflow '{workflow_id}' is not in the manifest")
        graph = load_workflow(workflow_id)
        # The manifest's `drop` is the graph's own UI-only nodes; `extra_drop` is what the
        # caller wants gone for this particular call (e.g. the LoadImage stations of an
        # orbit rig when fewer than four views are supplied). Merged, never replaced.
        drop = list(definition.get("drop") or []) + list(extra_drop or [])
        return self.client.run(
            graph,
            image_paths=images,
            image_nodes=definition.get("imageNodes"),
            prompt=prompt,
            prompt_node=definition.get("promptNode"),
            prompt_input=definition.get("promptInput", "prompt"),
            params=params,
            param_map=definition.get("paramMap"),
            drop=drop,
            outputs=definition.get("outputs"),
            timeout_s=(definition.get("timeoutMs") or 900000) / 1000.0,
        )

    def _save(self, blob: bytes, kind: str, slug: str, source_name: str) -> Artefact:
        directory = self._kind_dir(kind)
        suffix = KIND_SUFFIX.get(kind, "")
        ext = Path(source_name).suffix or ".bin"
        path = naming.unique_path(directory, slug, suffix, ext)
        path.write_bytes(blob)
        return Artefact(kind=kind, path=str(path), bytes=len(blob), filename=path.name)

    def _save_at(self, path: Path, blob: bytes, kind: str) -> Artefact:
        """Write to an exact path instead of into `assets/<kind>/`."""
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(blob)
        return Artefact(kind=kind, path=str(path), bytes=len(blob), filename=path.name)

    def _slug_for(self, kind: str, name: str, fallback: str) -> str:
        """Output slug, with the kind's own suffix never doubled.

        `remove_bg(name="ninja-chubby-nobg")` used to produce
        `ninja-chubby-nobg-nobg.png`, because `_save` appends
        `KIND_SUFFIX["mask"]` on top of a name that already carried it. Callers
        should not have to know the pipeline's naming convention to avoid that.
        """
        suffix = KIND_SUFFIX.get(kind, "")
        explicit = _strip_kind_suffix(name, suffix)
        if explicit:
            return naming.derive_name("", explicit)
        return naming.slugify(_strip_kind_suffix(fallback, suffix))

    # ------------------------------------------------------------------ status
    def status(self) -> dict:
        manifest = load_manifest()
        counts = {}
        for k, sub in config.ASSET_SUBDIR.items():
            directory = self._kind_dir(k)
            counts[sub] = len(list(directory.glob("*"))) if directory.exists() else 0
        return {
            "comfy": self.client.status(),
            "root": str(self.root) if self.root else str(config.ASSETS_DIR),
            "workflows": [
                {"id": w.get("id"), "title": w.get("title"), "kind": w.get("kind"),
                 "file": w.get("file"), "file_present": (config.ASSETS_DIR / "workflows" / w.get("file", "")).exists()}
                for w in manifest.get("workflows", [])
            ],
            "assets": counts,
        }

    # ------------------------------------------------------------------ image
    def image(
        self,
        prompt: str,
        name: str = "",
        *,
        resolution: int = 1024,
        aspect_ratio: str = "1:1 (Square)",
        megapixels: float | None = None,
        steps: int | None = None,
        seed: int | None = None,
    ) -> list[Artefact]:
        slug = naming.derive_name(prompt, name)
        params: dict = {"resolution": resolution, "aspect_ratio": aspect_ratio}
        # `resolution` is the text-encoder's pixel hint; the actual output size is
        # ResolutionSelector(aspect_ratio, megapixels). 1.0 MP ~= 1024x1024.
        if megapixels is not None:
            params["megapixels"] = megapixels
        if steps is not None:
            params["steps"] = steps
        if seed is not None:
            params["seed"] = seed
        out = self._run("t2i", prompt=prompt, params=params)
        return [self._save(f["bytes"], "image", slug, f["filename"]) for f in out]

    # ------------------------------------------------- image (z-image, fast)
    @staticmethod
    def _ratio(text: str) -> tuple[float, float]:
        m = re.match(r"\s*(\d+(?:\.\d+)?)\s*[:x/]\s*(\d+(?:\.\d+)?)", str(text or ""))
        if not m:
            return (1.0, 1.0)
        a, b = float(m.group(1)), float(m.group(2))
        return (a, b) if a > 0 and b > 0 else (1.0, 1.0)

    @staticmethod
    def _align(value: float, lo: int = 512, hi: int = 2048) -> int:
        """z-image wants a multiple of 64 - its latent grid - and a sane band."""
        v = int(round(float(value) / 64.0)) * 64
        return max(lo, min(hi, v))

    @classmethod
    def z_size(cls, width=None, height=None, aspect_ratio="1:1 (Square)",
               megapixels=None) -> tuple[int, int]:
        """Pixel size for the z-image path.

        An explicit width/height wins. Otherwise the size is solved from the aspect
        ratio and the megapixel budget, so a pack that already says
        `"aspect_ratio": "21:9 (Ultrawide)", "megapixels": 1.5` gets 1856x768 with no
        second number to keep in sync. Note that the ComfyUI path's `resolution` is
        only the text encoder's hint and is deliberately not used here.
        """
        if width and height:
            return cls._align(width), cls._align(height)
        a, b = cls._ratio(aspect_ratio)
        mp = float(megapixels or 1.0)
        # Solve w from the area budget, then derive h from the *aligned* w. Aligning
        # both independently rounds twice and drifts the ratio (1856x832 is 2.23, not
        # the 2.33 that was asked for); deriving keeps one dimension exact.
        w = (mp * 1_000_000.0 * a / b) ** 0.5
        h = w * b / a
        if width:
            w = float(width)
            h = w * b / a
        elif height:
            h = float(height)
            w = h * a / b
        w = cls._align(w)
        return w, cls._align(w * b / a)

    def image_fast(
        self,
        prompt: str,
        name: str = "",
        *,
        width: int | None = None,
        height: int | None = None,
        aspect_ratio: str = "1:1 (Square)",
        megapixels: float | None = None,
        steps: int | None = None,
        cfg: float | None = None,
        guidance: float | None = None,
        seed: int | None = None,
        negative: str = "",
    ) -> list[Artefact]:
        """Text -> image through z-image-turbo (stable-diffusion.cpp, :8687).

        Same contract as `image()` - PNG bytes in the pipeline's `images/` directory -
        but 30-40x cheaper: ~20 s for 8 steps at 768x768 against ~12 min for the
        Qwen-Image graph, and 3.8 GB of VRAM instead of 8.9 GB. This is the default
        for backgrounds and sprites; `image()` is what title art with legible
        lettering needs.
        """
        slug = naming.derive_name(prompt, name)
        w, h = self.z_size(width, height, aspect_ratio, megapixels)
        blob = self.sd.generate(prompt, width=w, height=h, steps=steps, cfg=cfg,
                                guidance=guidance, seed=seed, negative=negative)
        return [self._save(blob, "image", slug, f"{slug}.png")]

    def edit(self, images: list[str | Path], instruction: str, name: str = "",
             *, resolution: int | None = None, steps: int | None = None,
             seed: int | None = None, cfg: float | None = None) -> list[Artefact]:
        """Reference-driven generation on the Qwen-Image-Edit graph.

        The references ARE the composition: the graph builds its latent from them
        (`TextEncodeQwenImage21` -> the switch's `on_false`), so the output keeps the
        aspect ratio of the first image rather than following `aspect_ratio`. There
        is therefore no size knob here - to change the shape, change the reference.

        `resolution` is the text encoder's pixel hint, `steps`/`cfg`/`seed` the
        sampler's. All four are optional because the shipped graph already carries
        working values (25 steps, cfg 1).
        """
        srcs = [locate_input(p) for p in images]
        slug = naming.derive_name(instruction, name) if name else naming.slugify(srcs[0].stem + "-" + instruction)
        params = {}
        if resolution is not None:
            params["resolution"] = resolution
        if steps is not None:
            params["steps"] = steps
        if seed is not None:
            params["seed"] = seed
        if cfg is not None:
            params["cfg"] = cfg
        out = self._run("edit", images=srcs, prompt=instruction,
                        params=params or None)
        return [self._save(f["bytes"], "image", slug, f["filename"]) for f in out]

    # ------------------------------------------------------- upscale / restyle
    def upscale(self, image: str | Path, name: str = "", *, scale: int = 2,
                model: str = "realesrgan-x4plus") -> list[Artefact]:
        """Enlarge a finished picture with Real-ESRGAN - no diffusion involved.

        This is how a background gets big: z-image is cheap at 768-1856 px and
        super-linear past it, while Real-ESRGAN multiplies the finished pixels in
        seconds. Needs no resident model, so it runs whatever else is on the card.
        """
        src = locate_input(image)
        slug = (naming.derive_name("", name) if name
                else naming.slugify(f"{src.stem}-x{scale}"))
        info = self.upscaler.upscale(src, self._kind_dir("image") / f"{slug}.png",
                                     scale=scale, model=model)
        dst = Path(info["path"])
        return [Artefact(kind="image", path=str(dst), bytes=info["bytes"],
                         filename=dst.name)]

    def recolor(self, image: str | Path, instruction: str, name: str = "", *,
                strength: float = 0.65, width: int | None = None,
                height: int | None = None, steps: int | None = None,
                seed: int | None = None) -> list[Artefact]:
        """img2img through z-image - a *global* restyle, not a masked edit.

        The source's own pixel size is inherited when width/height are omitted, so a
        1856x768 layer stays 1856x768 instead of being squashed into a square.

        Two limits are worth knowing before reaching for this:

        * **No inpainting.** sd-server accepts `mask`/`mask_image` on
          `/sdapi/v1/img2img` and ignores them for Z-Image.
        * **Strength trades composition for obedience.** Measured at 768x768 on a
          mushroom sprite: `0.25` kept the silhouette almost exactly but left the
          colour nearly untouched, `0.55` applied the new palette and reinvented the
          framing. There is no setting that does both.

        So for "same sprite, different colour" the ComfyUI `color_swap` graph
        (Qwen-Image 2.1) is the correct tool - slower, and it actually holds the
        shape. Use this for variations and mood passes, where drifting is the point.
        """
        src = locate_input(image)
        slug = naming.derive_name(instruction, name)
        blob = self.sd.img2img(src, instruction, strength=strength, width=width,
                               height=height, steps=steps, seed=seed)
        return [self._save(blob, "image", slug, f"{slug}.png")]

    # ------------------------------------------------------------------ mask
    def _cut(self, image: Path, *, fast: bool) -> bytes:
        """Run the cut-out graph on ONE image and hand back the PNG bytes.

        The output is always a PNG regardless of the input's extension, which is
        why callers pass `".png"` rather than the source's suffix.
        """
        if fast:
            out = self._run("remove_bg_fast", images=[image])
        else:
            out = self._run("remove_bg", images=[image],
                            prompt="Remove the background completely. Keep the subject "
                                   "pixel-identical. Output transparent PNG.")
        if not out:
            raise ComfyError(f"cut-out produced no image for {image}")
        return out[0]["bytes"]

    def remove_bg(self, image: str | Path, name: str = "", *, fast: bool = True) -> list[Artefact]:
        """Cut ONE image out -> `assets/masks/<name>-nobg.png`.

        For several images use `remove_bg_many`: one call, one output per input.
        """
        src = locate_input(image)
        slug = self._slug_for("mask", name, src.stem)
        # Pass a full name, not ".png": `Path(".png").suffix` is empty, so `_save`
        # falls back to ".bin". The cut-out graph always returns a PNG.
        return [self._save(self._cut(src, fast=fast), "mask", slug, f"{slug}.png")]

    def remove_bg_many(self, images: list[str | Path], *, fast: bool = True,
                       out_dir: str | Path | None = None) -> list[Artefact]:
        """Cut SEVERAL images out in one call - one output per input, named after it.

        Written for the failure it prevents. The single tool took one image, so a
        batch meant N calls; when four of those N died on an unresolvable relative
        path, the agent answered with `cp <one cut-out> <four destinations>` and the
        ninja landed where the apple, burger, carrot and hotdog should have been -
        byte-identical, md5 `d23389b6f47c896249163e4f53440edd`, and nothing in the
        scene said so. Here the input->output mapping *is* the contract: every file
        is cut from its own source, in order, and a failure names the file it died on
        instead of leaving a slot to be filled in.

        With no `out_dir` each result lands **next to its source** as
        `<dir>/<stem>-nobg.png` - exactly where a page references it, so there is no
        move step left to get wrong.
        """
        results: list[Artefact] = []
        for item in images:
            src = locate_input(item)
            slug = _strip_kind_suffix(src.stem, KIND_SUFFIX["mask"]) or "asset"
            blob = self._cut(src, fast=fast)
            if out_dir is None:
                dest = src.with_name(f"{slug}{KIND_SUFFIX['mask']}.png")
            else:
                dest = naming.unique_path(Path(out_dir), slug, KIND_SUFFIX["mask"], ".png")
            results.append(self._save_at(dest, blob, "mask"))
        return results

    # ------------------------------------------------------------------ 3D
    def to_3d(
        self,
        image: str | Path,
        name: str = "",
        *,
        quality: str = "high",
        resolution: int | None = None,
        steps: int | None = None,
        faces: int | None = None,
        seed: int | None = None,
        remove_bg_first: bool = True,
    ) -> list[Artefact]:
        """Image -> mesh. Quality first: `high` (Pixal3D/TRELLIS.2) is the default.

        `high` costs ~16-18 min against ~3 min for `economy`, and the difference is
        not cosmetic: economy is a TripoSplat Gaussian splat with no UVs and
        `KHR_materials_unlit`, so it ignores every light in the scene. That is fine
        for a turntable preview and wrong for anything a player walks past.

        **`faces` is the lever that actually matters**, not `resolution`. The graph
        decimates to `186.target_face_count` (700 000 in the shipped workflow), and
        that number - not the input crop - is what you get out. Measured on the same
        concept: 512 and 1024 both came back at ~698 500 faces and ~40 MB, and the
        1024 run was the *faster* of the two. A prop that renders 200 px tall in a
        2D game wants 5 000-20 000 faces; anything past that is bytes the player
        downloads and the GPU throws away.

        `steps` is the linear cost dial: the graph runs four samplers (12 + 12 + 20
        + 12 = 56 steps), and halving them roughly halves the wall clock.

        `resolution` is kept for the one thing it does move - the size of the image
        the reconstruction is conditioned on - but do not expect a speed-up from it.
        """
        image = locate_input(image)
        workflow_id = QUALITY.get(str(quality).lower())
        if not workflow_id:
            raise ComfyError(f"unknown quality '{quality}'; use one of {sorted(QUALITY)}")
        slug = self._slug_for("mesh", name, image.stem)
        params: dict = {"removeBgFirst": remove_bg_first}
        if resolution is not None:
            params["resolution"] = resolution
        if steps is not None:
            params["steps"] = steps
        if faces is not None:
            params["faces"] = faces
        if seed is not None:
            params["seed"] = seed
        out = self._run(workflow_id, images=[image], params=params)
        saved = []
        for f in out:
            kind = "splat" if f["filename"].lower().endswith(".spz") else (
                "preview" if f["filename"].lower().endswith((".mp4", ".webm")) else "mesh")
            saved.append(self._save(f["bytes"], kind, slug, f["filename"]))
        return saved

    def to_3d_multiview(
        self,
        views: list[str | Path],
        name: str = "",
        *,
        steps: int | None = None,
        faces: int | None = None,
        seed: int | None = None,
    ) -> list[Artefact]:
        """Four orbit views -> mesh. The quality fix, not a speed one.

        `to_3d` conditions the reconstruction on a single image, so the model has to
        invent the back of everything it cannot see - that is where the mushy
        silhouette and the melted geometry come from. `Pixal3DMultiViewConditioning`
        takes up to four views on a fixed orbit (front, left, back, right, 90 deg
        apart) and pins the geometry from all of them.

        **Order is the contract:** the first view supplied is the front the mesh is
        posed to. Pass them `front, left, back, right`; a subset is allowed and the
        node rebases the rig onto the first one, but it warns when that is not
        `front`.

        Supplying fewer than four is a real path, not a degraded one. All four view
        inputs of `Pixal3DMultiViewConditioning` are declared `optional=True` and the
        node rebases every azimuth onto the first connected view, so front+left+back
        is a complete, well-posed request - the right side is then inferred by
        symmetry instead of being dictated. What made it *not* work before is on this
        side of the wire: the graph has one `LoadImage` per orbit station, `run()`
        only overrides the first N of them, and the leftover station kept pointing at
        its export-time default filename. Those stations are now dropped explicitly,
        which also unlinks the matching conditioning input.

        **Framing is the other contract.** Each view must be a *square* of the object
        on alpha or black, framed like a rig render: the object spans about 1/1.1 of
        the frame at its widest, and **the same scale in every view**. The node does
        not crop to the subject - it composites `rgb * alpha` and resizes to 1024.
        Views cropped to their own bounding box break the equal-scale rule (a front
        view is wider than a side view, so the mesh comes out sheared); that is why
        the recommended source is a four-panel character sheet split into equal
        squares (`tools/split_sheet.py`) or an orthographic render pass, not four
        independently cropped cut-outs.

        Cost is the same as `to_3d` (~17-18 min warm) plus the conditioning pass,
        which is cheap: the views are one extra batch through DINOv3, not one extra
        sampler run each. There is no `resolution` argument - the multiview graph has
        no crop-to-mask node to resize, the node normalises to 1024 itself.
        """
        paths = [locate_input(v) for v in views]
        if not paths:
            raise AssetInputError("to_3d_multiview needs at least one view")
        if len(paths) > 4:
            raise AssetInputError(
                f"the orbit rig has four stations (front, left, back, right); got {len(paths)}")
        slug = self._slug_for("mesh", name, paths[0].stem)
        params: dict = {}
        if steps is not None:
            params["steps"] = steps
        if faces is not None:
            params["faces"] = faces
        if seed is not None:
            params["seed"] = seed
        stations = (workflow_def("to_3d_high_multiview") or {}).get("imageNodes") or []
        out = self._run("to_3d_high_multiview", images=paths, params=params,
                        extra_drop=[str(n) for n in stations[len(paths):]])
        saved = []
        for f in out:
            kind = "splat" if f["filename"].lower().endswith(".spz") else (
                "preview" if f["filename"].lower().endswith((".mp4", ".webm")) else "mesh")
            saved.append(self._save(f["bytes"], kind, slug, f["filename"]))
        return saved

    # ------------------------------------------------------------------ flow
    def character(self, prompt: str, name: str = "", *, quality: str = "high",
                  steps_3d: int | None = None, resolution: int = 1024,
                  faces_3d: int | None = None,
                  aspect_ratio: str = "1:1 (Square)", seed: int | None = None) -> dict:
        """One call for the whole loop: text -> image -> cut-out -> 3D.

        This is the shape the agent should use for "make me a character". It keeps the
        intermediate files so a bad cut-out can be re-run without regenerating the image.
        """
        t0 = time.time()
        slug = naming.derive_name(prompt, name)
        steps_log: list[dict] = []

        imgs = self.image(prompt, slug, resolution=resolution, aspect_ratio=aspect_ratio, seed=seed)
        steps_log.append({"step": "image", "s": round(time.time() - t0, 1),
                          "files": [a.to_dict() for a in imgs]})

        cut = self.remove_bg(imgs[0].path, slug, fast=True)
        steps_log.append({"step": "remove_bg", "s": round(time.time() - t0, 1),
                          "files": [a.to_dict() for a in cut]})

        three = self.to_3d(cut[0].path, slug, quality=quality, steps=steps_3d,
                           faces=faces_3d, remove_bg_first=False)
        steps_log.append({"step": f"3d_{quality}", "s": round(time.time() - t0, 1),
                          "files": [a.to_dict() for a in three]})

        return {
            "slug": slug,
            "prompt": prompt,
            "total_s": round(time.time() - t0, 1),
            "mesh": next((a.path for a in three if a.kind == "mesh"), None),
            "steps": steps_log,
        }

    # ------------------------------------------------------------------ listing
    def list_assets(self, kind: str = "") -> list[dict]:
        rows = []
        kinds = [kind] if kind else sorted(set(config.ASSET_SUBDIR))
        for k in kinds:
            directory = self._kind_dir(k)
            if not directory.exists():
                continue
            for p in sorted(directory.iterdir(), key=lambda x: -x.stat().st_mtime if x.is_file() else 0):
                if p.is_file():
                    rows.append({"kind": k, "name": p.name, "path": str(p),
                                 "bytes": p.stat().st_size,
                                 "mtime": int(p.stat().st_mtime)})
        return rows
