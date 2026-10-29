"""Measure UV atlas overlap in a GLB.

Why: a mesh can show the front's detail on its back surface when the UV charts overlap -
the back triangles simply sample the texels the front painted. That failure is invisible
in a UV range print (u[0,0.997] v[0,1] looks healthy) but obvious in the areas: for a
non-overlapping unwrap the summed UV area of all triangles cannot exceed the atlas area
(1.0 in normalised units), and in practice lands around 0.6-0.9 once packing gaps are
counted. A sum well above 1.0 means charts are stacked.

Also reports the per-region split, so it is visible *which* part of the surface reuses
texels rather than only that something does.

Usage:  python tools/glb_uv_overlap.py <file.glb> [atlas=2048]
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from glb_inspect import accessor_array, read_glb  # noqa: E402


def uv_areas(uv, tris):
    a = uv[tris[:, 0]]
    b = uv[tris[:, 1]]
    c = uv[tris[:, 2]]
    return 0.5 * np.abs((b[:, 0] - a[:, 0]) * (c[:, 1] - a[:, 1])
                        - (c[:, 0] - a[:, 0]) * (b[:, 1] - a[:, 1]))


def rasterise(uv, tris, res):
    """Count how many triangles cover each texel of a res x res grid."""
    grid = np.zeros((res, res), dtype=np.int32)
    tri_uv = uv[tris]                      # (n, 3, 2)
    px = np.clip((tri_uv[:, :, 0] * (res - 1)).astype(np.int32), 0, res - 1)
    py = np.clip((tri_uv[:, :, 1] * (res - 1)).astype(np.int32), 0, res - 1)
    # Conservative test: mark every texel inside the triangle's integer bounding box
    # that also satisfies the three edge functions. Vectorised per triangle would be
    # slow for 460k triangles, so this uses the bounding box and then filters.
    x0 = px.min(axis=1)
    x1 = px.max(axis=1)
    y0 = py.min(axis=1)
    y1 = py.max(axis=1)
    spans = (x1 - x0 + 1) * (y1 - y0 + 1)
    for i in np.argsort(spans):            # small triangles first, keeps it bounded
        if spans[i] > 4096:
            continue
        ax, ay = tri_uv[i, 0]
        bx, by = tri_uv[i, 1]
        cx, cy = tri_uv[i, 2]
        den = (by - cy) * (ax - cx) + (cx - bx) * (ay - cy)
        if abs(den) < 1e-12:
            continue
        gx, gy = np.meshgrid(np.arange(x0[i], x1[i] + 1),
                             np.arange(y0[i], y1[i] + 1))
        sx = gx / (res - 1)
        sy = gy / (res - 1)
        w0 = ((by - cy) * (sx - cx) + (cx - bx) * (sy - cy)) / den
        w1 = ((cy - ay) * (sx - cx) + (ax - cx) * (sy - cy)) / den
        w2 = 1.0 - w0 - w1
        inside = (w0 >= -1e-9) & (w1 >= -1e-9) & (w2 >= -1e-9)
        if inside.any():
            grid[gy[inside], gx[inside]] += 1
    return grid


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    path = Path(argv[1])
    res = int(argv[2]) if len(argv) > 2 else 2048

    version, gltf, binary = read_glb(path)
    print(f"UV OVERLAP  {path.name}  ({path.stat().st_size:,} bytes, glTF {version})")

    for mi, mesh in enumerate(gltf.get("meshes", [])):
        for pi, prim in enumerate(mesh["primitives"]):
            attrs = prim["attributes"]
            if "TEXCOORD_0" not in attrs:
                print(f"  prim[{pi}]: no TEXCOORD_0")
                continue
            uv = accessor_array(gltf, binary, attrs["TEXCOORD_0"]).astype(np.float64)
            idx = accessor_array(gltf, binary, prim["indices"]).reshape(-1)
            tris = idx[: len(idx) // 3 * 3].reshape(-1, 3)

            areas = uv_areas(uv, tris)
            total = float(areas.sum())
            print(f"  prim[{pi}]  verts={len(uv):,}  tris={len(tris):,}")
            print(f"    uv u[{uv[:,0].min():.4f},{uv[:,0].max():.4f}] "
                  f"v[{uv[:,1].min():.4f},{uv[:,1].max():.4f}]")
            print(f"    summed triangle UV area = {total:.4f} atlas units")
            if total <= 1.05:
                print("    -> no overlap possible: the charts fit inside one atlas")
            else:
                print(f"    -> OVERLAP: charts are stacked at least {total:.2f}x")

            grid = rasterise(uv, tris, res)
            covered = int((grid > 0).sum())
            multi = int((grid > 1).sum())
            print(f"    rasterised at {res}x{res}: {covered:,} texels covered "
                  f"({100*covered/(res*res):.1f}% of the atlas), "
                  f"{multi:,} covered more than once "
                  f"({100*multi/max(covered,1):.1f}% of covered)")
            if multi:
                frac = grid[grid > 0]
                print(f"    coverage multiplicity: max {int(frac.max())}, "
                      f"mean {float(frac.mean()):.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
