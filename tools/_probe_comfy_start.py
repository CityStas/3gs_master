#!/usr/bin/env python
"""Measure a cold ComfyUI start under the custom-node whitelist and prove the
classes our workflows need are actually registered.

    .venv/Scripts/python.exe tools/_probe_comfy_start.py [--keep]

`--keep` leaves the server running so a follow-up pack run can reuse it.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from threejs import config  # noqa: E402
from threejs.assets.comfy import ComfyClient  # noqa: E402

# Everything `assets/workflows/*.json` asks for that is not plain ComfyUI core.
NEEDED = [
    # trellis2 / pixal3d / moge
    "Trellis2ShapeStage", "Trellis2TextureStage", "Trellis2UpsampleStage",
    "Trellis2Conditioning", "Pixal3DConditioning", "EmptyTrellis2LatentStructure",
    "VaeDecodeShapeTrellis", "VaeDecodeStructureTrellis2", "VaeDecodeTextureTrellis",
    "VoxelToMesh", "ApplyTextureToMesh", "PaintMesh", "RemeshMesh", "DecimateMesh",
    "UnwrapMesh", "RenderUVAtlas", "BakeTextureFromVoxel", "BakeNormalMapFromMesh",
    "BakeAmbientOcclusion", "MeshSmoothNormals", "GetMeshInfo", "PrimitiveBoolean",
    "Save3DAdvanced", "MeshToFile3D", "Preview3DAdvanced",
    "LoadMoGeModel", "MoGeInference", "MoGeGeometryToFOV",
    # triposplat
    "TripoSplatConditioning", "TripoSplatPreprocessImage", "TripoSplatSamplingPreview",
    "VAEDecodeTripoSplat", "RenderSplat", "SplatToMesh", "SplatToFile3D",
    "CreateCameraInfo", "SaveGLB",
    # background removal
    "LoadBackgroundRemovalModel", "RemoveBackground",
    # gguf loader (the one real custom pack)
    "UnetLoaderGGUF",
]


def main() -> int:
    keep = "--keep" in sys.argv
    c = ComfyClient()
    print(f"root         : {c.root}")
    print(f"custom_nodes : {c.custom_nodes if c.custom_nodes is not None else 'ALL'}")
    print(f"vram_mode    : {c.vram_mode}")
    print(f"alive before : {c.is_alive()}")

    t0 = time.time()
    try:
        info = c.ensure(timeout=600.0)
    except Exception as exc:  # noqa: BLE001
        print(f"ensure FAILED after {time.time() - t0:.1f}s: {type(exc).__name__}: {exc}")
        return 1
    dt = time.time() - t0
    print(f"ensure OK in {dt:.1f}s -> {info}")

    try:
        oi = c._get("/object_info", timeout=180)
    except Exception as exc:  # noqa: BLE001
        print(f"object_info failed: {type(exc).__name__}: {exc}")
        return 1
    missing = [n for n in NEEDED if n not in oi]
    print(f"object_info  : {len(oi)} classes registered")
    print(f"missing      : {missing if missing else '(none)'}")

    st = c.status()
    print("status       : " + json.dumps(
        {k: st.get(k) for k in ("alive", "device", "vram_total_mb", "vram_free_mb",
                                "custom_nodes")}, ensure_ascii=False))

    if keep:
        print("--keep: leaving the server up")
        return 0
    print("stop         : " + json.dumps(c.stop()))
    return 0 if not missing else 2


if __name__ == "__main__":
    raise SystemExit(main())
