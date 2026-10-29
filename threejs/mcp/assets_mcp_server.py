"""MCP server exposing the local asset pipeline to the Three.js agent.

Registered in `.pi/mcp.json` as `assets`. The ComfyUI sidecar is a *backend detail*:
the agent asks for "a character", not for "workflow 3d_pixal3d_trellis2_8gb node 322".

Tool surface
------------
  asset_generate_pack  - PREFERRED. A whole asset list in one serialised run; the
                         language model is switched off while ComfyUI works
  assets_scheduler     - is the LLM up, is ComfyUI up, free VRAM, is a run in progress
  assets_status        - is ComfyUI up, which workflows exist, what has been produced
  asset_image          - text -> image (single asset; pays a start/stop per call)
  asset_edit           - image(s) + instruction -> image
  asset_remove_bg      - image(s) -> alpha PNG; pass `images` to cut out a whole batch
                         in one call (never one call per file)
  asset_to_3d          - image -> GLB (economy: TripoSplat / high: Pixal3D-TRELLIS.2)
  asset_to_3d_multiview- 4 orbit views -> GLB (same graph, conditioned on all views)
  asset_character      - the whole loop in one call: text -> image -> cut-out -> GLB
  asset_list           - what is in assets/
  comfy_control        - start / stop / status of the sidecar

Every returned path is a real file under `assets/`, named after the request.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from mcp.server.fastmcp import FastMCP  # noqa: E402

from threejs.assets.pipeline import AssetPipeline  # noqa: E402
from threejs.assets.scheduler import GenerationScheduler  # noqa: E402

mcp = FastMCP("3gs-assets")
_pipeline: AssetPipeline | None = None
_scheduler: GenerationScheduler | None = None


def _p() -> AssetPipeline:
    global _pipeline
    if _pipeline is None:
        _pipeline = AssetPipeline()
    return _pipeline


def _s() -> GenerationScheduler:
    """One scheduler per server process, so it keeps one ComfyClient and one
    LlamaServer - and therefore knows the PID of a ComfyUI it started earlier."""
    global _scheduler
    if _scheduler is None:
        _scheduler = GenerationScheduler(comfy=_p().client)
    return _scheduler


def _j(payload) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=1)


@mcp.tool()
def asset_generate_pack(project: str = "", jobs: list[dict] | None = None,
                        jobs_json: str = "", stop_llm: bool = True,
                        keep_comfy: bool = False) -> str:
    """Generate a WHOLE asset pack in one serialised run. Prefer this over one call
    per asset.

    Write the complete list of images and 3D models the game needs, then hand it over
    once. While this call runs your own model is switched off: the llama-server process
    is stopped and the GPU is given to ComfyUI, then restarted before the result comes
    back. So expect minutes of silence, not a hang - on an 8 GB card this is the only
    way generation runs at full speed. One call for six assets is one server start and
    one model reload; six calls would pay that six times.

    Each job is an object:

      kind         "image" | "mask" | "3d"  ("character" is an alias of "3d")
      name         short slug used for the filename; derived from the prompt if omitted
      prompt       the generation prompt (required for kind="image"; for kind="3d" it is
                   optional - with no input it makes the image and its cut-out first)
      from         name of an EARLIER job in this same list to take the input image from
                   (kind="mask"/"3d"). This is how "images first, then the 3D models"
                   happens inside one ComfyUI session.
      image        alternative to `from`: a path to an existing image, relative to the
                   project
      out          where the finished file goes, relative to the project, e.g.
                   "public/assets/models/player/nova.glb". Defaults to
                   public/assets/<images|masks|3d>/<name>.<ext>. Give the extension or
                   omit it and the natural one is used.
      quality      kind="3d" only: "economy" (TripoSplat, ~3 min) or "high"
                   (Pixal3D/TRELLIS.2, ~18 min, UV + PBR - this is the one for a lit scene)
      resolution   the text encoder's pixel hint (default 1024)
      megapixels   the ACTUAL size of the picture, in megapixels. 1.0 ~= 1024x1024,
                   0.25 ~= 512x512. Use it to make generation faster - cost scales with
                   area, so 0.25 MP is roughly four times cheaper than the default.
      aspect_ratio e.g. "1:1 (Square)", "16:9 (Widescreen)", "9:16 (Portrait)"
      steps, seed, steps_3d, fast, remove_bg_first   optional overrides

    Example:
      [{"kind": "image", "name": "nova-concept", "prompt": "a small blue fox with a "
        "glowing tail, full body, plain background", "out": "src/assets/nova-concept.png"},
       {"kind": "3d", "name": "nova", "from": "nova-concept", "quality": "economy",
        "out": "public/assets/models/player/nova.glb"}]

    Pass the list as `jobs`, or as a JSON string in `jobs_json`. Returns every written
    file with its project-relative path, a `/...` URL for anything under `public/`, the
    per-job timing, and the VRAM/timeline evidence that the model really was off.

    `stop_llm=False` keeps your own model resident and gives up the speed-up.
    """
    if jobs is None and jobs_json.strip():
        try:
            jobs = json.loads(jobs_json)
        except json.JSONDecodeError as e:
            return _j({"ok": False, "error": f"jobs_json is not valid JSON: {e}"})
    try:
        return _j(_s().generate_pack(project, jobs or [], stop_llm=stop_llm, keep_comfy=keep_comfy))
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def assets_scheduler() -> str:
    """Is the GPU free, and who is holding it?

    Reports the language model (:8080), the ComfyUI sidecar (:8188), free VRAM and
    whether a generation run currently holds the lock. The invariant is that at most
    one of the two models is resident; if both show `alive: true`, generation will be
    slow and something bypassed the scheduler."""
    try:
        return _j(_s().status())
    except Exception as e:  # noqa: BLE001
        return _j({"error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def assets_status() -> str:
    """State of the asset pipeline: ComfyUI sidecar (alive, VRAM, port), available
    workflows, and how many artefacts already exist in assets/. Call this before a
    long generation to see whether the backend is warm."""
    try:
        return _j(_p().status())
    except Exception as e:  # noqa: BLE001
        return _j({"error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def asset_image(prompt: str, name: str = "", resolution: int = 1024,
                aspect_ratio: str = "1:1 (Square)", steps: int = 0, seed: int = 0) -> str:
    """Generate an image from a text prompt (Qwen-Image 2.1, local, uncensored).

    `name` overrides the filename slug; otherwise it is derived from the prompt.
    `resolution` is the megapixel target, `aspect_ratio` is e.g. "1:1 (Square)",
    "16:9 (Widescreen)", "9:16 (Portrait)". `steps`/`seed` of 0 keep the workflow default.
    Returns the written file path(s) under assets/images/.
    """
    try:
        files = _p().image(prompt, name, resolution=resolution, aspect_ratio=aspect_ratio,
                           steps=steps or None, seed=seed or None)
        return _j({"ok": True, "files": [f.to_dict() for f in files]})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def asset_edit(images: list[str], instruction: str, name: str = "") -> str:
    """Edit image(s) by instruction. One path = img2img; two paths = transfer from the
    second reference onto the first (e.g. clothing onto a person).

    Paths may be relative to the project root - the same rule as `asset_generate_pack`
    - or absolute.
    """
    try:
        files = _p().edit(images, instruction, name)
        return _j({"ok": True, "files": [f.to_dict() for f in files]})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def asset_remove_bg(image: str = "", name: str = "", fast: bool = True,
                    images: list[str] | None = None) -> str:
    """Cut the background out of an image and write an alpha PNG.

    ONE image: pass `image` (plus `name` if you want to choose the slug) and the
    result lands in assets/masks/<name>-nobg.png.

    SEVERAL images: pass them ALL in `images` in a single call. This is the correct
    way to cut out more than one file - do not call this tool once per file, and never
    copy one cut-out over another file's name. Each image is cut from its own source
    and the result is written **next to that source** as <dir>/<stem>-nobg.png, which
    is where the page will reference it. The reply pairs every input with its output,
    so the mapping is checkable.

    Paths may be relative to the project root - the same rule as `asset_generate_pack`
    - or absolute. A relative path that cannot be resolved comes back with the list of
    locations that were tried; fix the path and call again rather than working around
    it.

    Do NOT put the `-nobg` suffix in `name`: the tool appends it, and passing it
    yourself is what produced `ninja-chubby-nobg-nobg.png`. It is stripped now, but the
    name you pass should be the plain slug.

    `fast=True` (default) uses BiRefNet - a real segmentation model: ~seconds, sharp
    edges, and it handles hair and soft alpha correctly. Use it unless you have seen it
    fail on this specific image.

    `fast=False` re-renders the image through Qwen-Image 2.1: ~12 min, it takes the whole
    8 GB card and forces the agent model off. It is NOT "better BiRefNet" - it is a
    diffusion re-render, so it can alter the subject too. Reach for it only when BiRefNet
    has demonstrably mangled a specific cut-out.
    """
    try:
        if images:
            files = _p().remove_bg_many(images, fast=fast)
            return _j({"ok": True, "files": [f.to_dict() for f in files]})
        if not image:
            return _j({"ok": False, "error": "pass `image` for one file, or `images` for several"})
        files = _p().remove_bg(image, name, fast=fast)
        return _j({"ok": True, "files": [f.to_dict() for f in files]})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def asset_to_3d(image: str, name: str = "", quality: str = "economy",
                resolution: int = 0, steps: int = 0, seed: int = 0,
                remove_bg_first: bool = True) -> str:
    """Turn an image into a 3D asset.

    quality="economy" -> TripoSplat, ~2.5-3.5 min warm. Gaussian splat + vertex-colour
      mesh, no UVs, unlit material. Use for previews, AR, props that need no lighting.
    quality="high"    -> Pixal3D / TRELLIS.2, ~17-18 min warm. UV-unwrapped PBR mesh -
      this is the one that belongs in a lit three.js scene.

    Output lands in assets/3d/<name>.glb (plus .spz for the economy path). Load it in
    three.js with GLTFLoader from that path. The input path may be relative to the
    project root - the same rule as `asset_generate_pack` - or absolute.
    """
    try:
        files = _p().to_3d(image, name, quality=quality, resolution=resolution or None,
                           steps=steps or None, seed=seed or None,
                           remove_bg_first=remove_bg_first)
        mesh = next((f.path for f in files if f.kind == "mesh"), None)
        return _j({"ok": True, "mesh": mesh, "files": [f.to_dict() for f in files]})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def asset_to_3d_multiview(views: list[str], name: str = "", steps: int = 0,
                          faces: int = 0, seed: int = 0) -> str:
    """Turn FOUR orbit views into one mesh. Higher quality than `asset_to_3d`, not faster.

    `asset_to_3d` sees one image, so the model invents whatever is hidden - that is the
    source of the soft silhouette and the melted back. This conditions the same Pixal3D /
    TRELLIS.2 graph on up to four views on a fixed orbit, 90 degrees apart.

    **Order is the contract:** `front, left, back, right`. The first view becomes the
    front the mesh is posed to. A subset is allowed (the rig rebases onto the first
    view) but it warns when that is not `front`.

    **Framing is the other contract:** each view must be a *square* of the object on
    alpha or black, the object filling about 1/1.1 of the frame, and **the same scale in
    every view**. Four independently cropped cut-outs break the equal-scale rule and the
    mesh comes out sheared. Produce the views with `tools/split_sheet.py` (splits a
    four-panel character sheet into equal squares with one shared crop box) or an
    orthographic render pass.

    Cost is the same as `asset_to_3d` at quality="high" (~17-18 min warm); the extra
    views are one batch through DINOv3, not four extra sampler runs. Output lands in
    assets/3d/<name>.glb. Paths follow the same rule as `asset_to_3d`.
    """
    try:
        files = _p().to_3d_multiview(views, name, steps=steps or None,
                                     faces=faces or None, seed=seed or None)
        mesh = next((f.path for f in files if f.kind == "mesh"), None)
        return _j({"ok": True, "mesh": mesh, "files": [f.to_dict() for f in files]})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def asset_character(prompt: str, name: str = "", quality: str = "economy",
                    resolution: int = 1024, aspect_ratio: str = "1:1 (Square)",
                    seed: int = 0) -> str:
    """The full loop in one call: text -> image -> background cut-out -> 3D mesh.

    Use this when the user asks for a character/prop/object to put into a three.js scene.
    Intermediate files are kept, so a bad cut-out can be redone without regenerating the
    image. Returns the mesh path plus a per-step timing log.
    """
    try:
        return _j({"ok": True, **_p().character(prompt, name, quality=quality, resolution=resolution,
                                                aspect_ratio=aspect_ratio, seed=seed or None)})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def asset_list(kind: str = "") -> str:
    """List produced artefacts. `kind` is one of image, mask, mesh, splat, preview;
    empty lists everything. Newest first."""
    try:
        return _j({"ok": True, "assets": _p().list_assets(kind)})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


@mcp.tool()
def comfy_control(action: str = "status") -> str:
    """Control the ComfyUI sidecar. action="start" (loads ~1-3 min cold),
    "stop" (frees RAM/VRAM), "status".

    Starting ComfyUI by hand leaves it resident next to the language model, which is
    exactly the contention that made a single 512x512 image take 725 s on this machine.
    For real work use `asset_generate_pack`, which stops the LLM first and stops ComfyUI
    again afterwards. `action="start"` here is for warming up before a run, or for
    debugging a workflow while the agent is idle."""
    action = (action or "status").lower()
    try:
        client = _p().client
        if action == "start":
            return _j({"ok": True, **client.ensure()})
        if action == "stop":
            return _j({"ok": True, **client.stop()})
        return _j({"ok": True, **client.status()})
    except Exception as e:  # noqa: BLE001
        return _j({"ok": False, "error": f"{type(e).__name__}: {e}"})


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
