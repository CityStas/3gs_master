"""Extract the images embedded in a GLB, and report which material slot uses which.

Written to answer "is the wrong thing painted into the atlas, or is the atlas fine and
the mesh sampling the wrong part of it". A base-colour atlas that contains two copies
of the chest-pocket region is a bake/projection problem; an atlas that contains one
copy is a UV-mapping problem.

Usage:  python tools/glb_extract_textures.py <file.glb> <out_dir>
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from glb_inspect import read_glb  # noqa: E402

SLOT = {0: "baseColor", 1: "metallicRoughness", 2: "normal", 3: "occlusion",
        4: "emissive"}


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 1
    src = Path(argv[1])
    out = Path(argv[2])
    out.mkdir(parents=True, exist_ok=True)

    version, gltf, binary = read_glb(src)
    print(f"EXTRACT {src.name}: {len(gltf.get('images', []))} image(s), "
          f"{len(gltf.get('textures', []))} texture(s), "
          f"{len(gltf.get('materials', []))} material(s)")

    # Which texture index each material slot points at.
    for mi, mat in enumerate(gltf.get("materials", [])):
        pbr = mat.get("pbrMetallicRoughness", {})
        slots = {
            "baseColor": pbr.get("baseColorTexture", {}).get("index"),
            "metallicRoughness": pbr.get("metallicRoughnessTexture", {}).get("index"),
            "normal": mat.get("normalTexture", {}).get("index"),
            "occlusion": mat.get("occlusionTexture", {}).get("index"),
            "emissive": mat.get("emissiveTexture", {}).get("index"),
        }
        for name, ti in slots.items():
            if ti is None:
                continue
            image_index = gltf["textures"][ti].get("source")
            print(f"  material[{mi}] {mat.get('name','?')!r}: {name} -> texture {ti} "
                  f"-> image {image_index}")

    for ii, img in enumerate(gltf.get("images", [])):
        view = gltf["bufferViews"][img["bufferView"]]
        start = view.get("byteOffset", 0)
        blob = binary[start:start + view["byteLength"]]
        mime = img.get("mimeType", "image/png")
        ext = ".png" if "png" in mime else ".jpg"
        name = img.get("name") or f"image_{ii}"
        dst = out / f"{ii}_{name}{ext}"
        dst.write_bytes(blob)
        print(f"  image[{ii}] {name!r} {mime} {len(blob):,} bytes -> {dst}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
