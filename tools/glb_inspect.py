"""Read a .glb and report what is actually inside it.

Written because "the model looks broken" is not a diagnosis. A GLB that renders
as shards can be any of: geometry that is genuinely shattered, a mesh whose
normals are missing or inverted, a texture atlas that was unwrapped into
hundreds of disconnected charts, an accessor whose min/max do not match the
data, or simply a wrong node transform. Each of those is visible in the raw
buffers, so this reports the buffers.

Usage:  python tools/glb_inspect.py <file.glb> [more.glb ...]
"""

from __future__ import annotations

import json
import struct
import sys
from pathlib import Path

import numpy as np

COMPONENT = {
    5120: ("b", np.int8),
    5121: ("B", np.uint8),
    5122: ("h", np.int16),
    5123: ("H", np.uint16),
    5125: ("I", np.uint32),
    5126: ("f", np.float32),
}
TYPE_COUNT = {"SCALAR": 1, "VEC2": 2, "VEC3": 3, "VEC4": 4, "MAT4": 16}


def read_glb(path: Path):
    blob = path.read_bytes()
    magic, version, _length = struct.unpack_from("<4sII", blob, 0)
    if magic != b"glTF":
        raise ValueError(f"{path.name}: not a GLB (magic={magic!r})")

    offset = 12
    gltf = None
    binary = b""
    while offset < len(blob):
        chunk_len, chunk_type = struct.unpack_from("<II", blob, offset)
        payload = blob[offset + 8: offset + 8 + chunk_len]
        if chunk_type == 0x4E4F534A:  # 'JSON'
            gltf = json.loads(payload.decode("utf-8"))
        elif chunk_type == 0x004E4942:  # 'BIN'
            binary = payload
        offset += 8 + chunk_len + ((4 - chunk_len % 4) % 4 if chunk_len % 4 else 0)
    return version, gltf, binary


def accessor_array(gltf, binary, index):
    acc = gltf["accessors"][index]
    fmt, dtype = COMPONENT[acc["componentType"]]
    ncomp = TYPE_COUNT[acc["type"]]
    count = acc["count"]

    if "bufferView" not in acc:
        return np.zeros((count, ncomp), dtype=dtype)

    view = gltf["bufferViews"][acc["bufferView"]]
    stride = view.get("byteStride") or (np.dtype(dtype).itemsize * ncomp)
    start = view.get("byteOffset", 0) + acc.get("byteOffset", 0)

    if stride == np.dtype(dtype).itemsize * ncomp:
        flat = np.frombuffer(binary, dtype=dtype, count=count * ncomp, offset=start)
        return flat.reshape(count, ncomp)

    # Interleaved: walk the stride.
    out = np.empty((count, ncomp), dtype=dtype)
    for i in range(count):
        out[i] = np.frombuffer(binary, dtype=dtype, count=ncomp,
                               offset=start + i * stride)
    return out


def tri_area(p0, p1, p2):
    return 0.5 * np.linalg.norm(np.cross(p1 - p0, p2 - p0), axis=1)


def inspect(path: Path):
    print("=" * 78)
    print(f"FILE  {path}")
    print(f"      {path.stat().st_size:,} bytes")
    version, gltf, binary = read_glb(path)
    print(f"      glTF version {version}, BIN chunk {len(binary):,} bytes")
    print(f"      generator: {gltf.get('asset', {}).get('generator', '?')}")
    print(f"      extensionsUsed: {gltf.get('extensionsUsed', [])}")
    print(f"      nodes {len(gltf.get('nodes', []))}  meshes {len(gltf.get('meshes', []))} "
          f"materials {len(gltf.get('materials', []))} images {len(gltf.get('images', []))} "
          f"textures {len(gltf.get('textures', []))}")

    # Skins and animations decide what the file can *do*, not just what it looks like.
    # Every mesh out of the image->3D graph is static (skins 0, animations 0), so a
    # clip-less file is the normal state here, not a broken export - say so explicitly
    # rather than leaving the reader to infer it from a missing line.
    skins = gltf.get("skins", [])
    animations = gltf.get("animations", [])
    print(f"      skins {len(skins)}  animations {len(animations)}")
    for si, skin in enumerate(skins):
        print(f"      skin[{si}] name={skin.get('name', '?')!r} joints={len(skin.get('joints', []))}")
    for ai, anim in enumerate(animations):
        channels = len(anim.get("channels", []))
        samplers = len(anim.get("samplers", []))
        print(f"      anim[{ai}] name={anim.get('name', '?')!r} channels={channels} samplers={samplers}")
    if not skins and not animations:
        print("      -> static mesh: no rig, no clips. A player/AnimationMixer on this "
              "plays nothing; animate the transform, or rig it (Mesh2Motion / Blender).")
    elif skins and not animations:
        print("      -> rigged but clip-less: the skeleton is there, the motion is not.")
    elif skins and animations:
        print("      -> rigged and animated: playable as-is "
              "(three.js AnimationMixer / Godot AnimationPlayer).")

    for ni, node in enumerate(gltf.get("nodes", [])):
        bits = []
        if "mesh" in node:
            bits.append(f"mesh={node['mesh']}")
        for key in ("translation", "rotation", "scale"):
            if key in node:
                bits.append(f"{key}={[round(v, 4) for v in node[key]]}")
        if "matrix" in node:
            bits.append("matrix=yes")
        print(f"      node[{ni}] name={node.get('name', '?')!r} {' '.join(bits)}")

    total_tris = 0
    for mi, mesh in enumerate(gltf.get("meshes", [])):
        print(f"  MESH[{mi}] name={mesh.get('name', '?')!r} primitives={len(mesh['primitives'])}")
        for pi, prim in enumerate(mesh["primitives"]):
            attrs = prim["attributes"]
            mode = prim.get("mode", 4)
            pos = accessor_array(gltf, binary, attrs["POSITION"])
            idx = (accessor_array(gltf, binary, prim["indices"]).reshape(-1)
                   if "indices" in prim else np.arange(len(pos)))

            ntris = len(idx) // 3
            total_tris += ntris
            tris = idx[: ntris * 3].reshape(-1, 3)
            p = pos[tris]

            areas = tri_area(p[:, 0], p[:, 1], p[:, 2])
            bbox_min = pos.min(axis=0)
            bbox_max = pos.max(axis=0)
            extent = bbox_max - bbox_min

            print(f"    prim[{pi}] mode={mode} verts={len(pos):,} tris={ntris:,}")
            print(f"      bbox min {np.round(bbox_min, 4)}  max {np.round(bbox_max, 4)}")
            print(f"      extent {np.round(extent, 4)}  diag {np.linalg.norm(extent):.4f}")
            print(f"      material={prim.get('material', '-')} "
                  f"attrs={sorted(attrs.keys())}")

            acc_min = gltf["accessors"][attrs["POSITION"]].get("min")
            if acc_min is not None:
                drift = float(np.max(np.abs(np.asarray(acc_min) - bbox_min)))
                print(f"      accessor.min drift vs real data: {drift:.6f}"
                      f"{'  <-- STALE' if drift > 1e-4 else ''}")

            nan = int(np.isnan(pos).any(axis=1).sum())
            if nan:
                print(f"      NaN positions: {nan}  <-- BROKEN")

            degen = int((areas < 1e-12).sum())
            print(f"      triangle area: min {areas.min():.3e} median {np.median(areas):.3e} "
                  f"max {areas.max():.3e}")
            print(f"      degenerate (<1e-12 m^2): {degen:,} ({100 * degen / max(ntris, 1):.2f}%)")

            # A shattered mesh shows up as many disconnected components.
            try:
                parent = np.arange(len(pos))

                def find(a):
                    while parent[a] != a:
                        parent[a] = parent[parent[a]]
                        a = parent[a]
                    return a

                for a, b, c in tris:
                    ra, rb, rc = find(a), find(b), find(c)
                    parent[rb] = ra
                    parent[rc] = ra
                roots = np.array([find(i) for i in range(len(pos))])
                comps, counts = np.unique(roots, return_counts=True)
                print(f"      connected components: {len(comps):,} "
                      f"(largest {counts.max():,} verts = "
                      f"{100 * counts.max() / len(pos):.1f}% of mesh)")
            except Exception as exc:  # noqa: BLE001
                print(f"      components: n/a ({exc})")

            if "NORMAL" in attrs:
                nrm = accessor_array(gltf, binary, attrs["NORMAL"])
                ln = np.linalg.norm(nrm, axis=1)
                print(f"      normals: |n| min {ln.min():.4f} max {ln.max():.4f} "
                      f"(unit if ~1.0)")
                # Winding vs normals: dot of geometric normal with vertex normal.
                e1 = p[:, 1] - p[:, 0]
                e2 = p[:, 2] - p[:, 0]
                geo = np.cross(e1, e2)
                gl = np.linalg.norm(geo, axis=1, keepdims=True)
                gl[gl == 0] = 1
                geo /= gl
                vn = nrm[tris].mean(axis=1)
                vl = np.linalg.norm(vn, axis=1, keepdims=True)
                vl[vl == 0] = 1
                vn /= vl
                agree = float(np.mean(np.einsum("ij,ij->i", geo, vn) > 0))
                print(f"      winding agrees with normals: {100 * agree:.1f}%"
                      f"{'  <-- INVERTED' if agree < 0.5 else ''}")
            else:
                print("      normals: ABSENT  <-- flat/faceted shading")

            if "TEXCOORD_0" in attrs:
                uv = accessor_array(gltf, binary, attrs["TEXCOORD_0"])
                print(f"      uv0 range u[{uv[:, 0].min():.3f},{uv[:, 0].max():.3f}] "
                      f"v[{uv[:, 1].min():.3f},{uv[:, 1].max():.3f}]")
            else:
                print("      uv0: ABSENT  <-- untextured")

    print(f"  TOTAL triangles: {total_tris:,}")

    for mi, mat in enumerate(gltf.get("materials", [])):
        pbr = mat.get("pbrMetallicRoughness", {})
        print(f"  MATERIAL[{mi}] {mat.get('name', '?')!r} "
              f"baseColorTex={pbr.get('baseColorTexture', {}).get('index', '-')} "
              f"metal={pbr.get('metallicFactor', '-')} rough={pbr.get('roughnessFactor', '-')} "
              f"doubleSided={mat.get('doubleSided', False)}")
    for ii, img in enumerate(gltf.get("images", [])):
        view = gltf["bufferViews"][img["bufferView"]]
        print(f"  IMAGE[{ii}] {img.get('name', '?')!r} mime={img.get('mimeType')} "
              f"{view['byteLength']:,} bytes")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    for arg in argv[1:]:
        p = Path(arg)
        if not p.exists():
            print(f"MISSING {p}")
            continue
        inspect(p)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
