"""Find a mesh's 'up' axis from its face normals, and say how far off +Y it is.

Why this is not just PCA
------------------------
The obvious probe - the inertia tensor's smallest eigenvector - is wrong for
exactly the objects that matter. A mug's thinnest direction is its diameter, not
its axis; a keyboard's is its thickness, but only if the case and the keycaps
agree. PCA on an asymmetric object mixes the axes and reports a tilt that is not
there.

The mean face normal is no better: a cylinder's wall contributes area in every
azimuth, and after folding the hemispheres those cancel, dragging the mean off
the true axis. That is why this *clusters* instead of averaging - it looks for
the single direction that the most surface area agrees on, which for a resting
object is the flat it stands on.

Method
------
1. Area-weight every triangle normal, folded into a hemisphere (a keyboard's top
   and bottom are parallel and both say "this is the axis").
2. Greedy farthest-point seeds, then keep the direction with the most area
   within `tolerance`.
3. Refine that cluster to its own area-weighted mean.

`--all` prints every cluster, which is how you tell "this mesh is level" from
"this mesh is a blob with no flats at all".

Usage:
  python tools/glb_up_axis.py <file.glb> [more.glb ...] [--all] [--tolerance 10]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from glb_inspect import accessor_array, read_glb  # noqa: E402


def face_normals(path: Path):
    _v, gltf, binary = read_glb(path)
    prim = gltf["meshes"][0]["primitives"][0]
    pos = accessor_array(gltf, binary, prim["attributes"]["POSITION"]).astype(np.float64)
    idx = accessor_array(gltf, binary, prim["indices"]).reshape(-1).astype(np.int64)
    tris = idx[: len(idx) // 3 * 3].reshape(-1, 3)
    p = pos[tris]

    cross = np.cross(p[:, 1] - p[:, 0], p[:, 2] - p[:, 0])
    length = np.linalg.norm(cross, axis=1, keepdims=True)
    area = 0.5 * length[:, 0]
    keep = length[:, 0] > 1e-14
    normal = cross[keep] / length[keep]
    area = area[keep]

    # Fold to a hemisphere: a face and its parallel opposite describe the same axis.
    normal = np.where(normal[:, 1:2] < 0, -normal, normal)
    return normal, area


def clusters(normal, area, tolerance_deg: float, top: int = 4):
    """Greedy: repeatedly take the heaviest direction, absorb its neighbourhood."""
    tol = np.radians(tolerance_deg)
    alive = np.ones(len(normal), dtype=bool)
    out = []
    for _ in range(top):
        if not alive.any():
            break
        n, a = normal[alive], area[alive]
        # Seed with the heaviest single normal, then let the cluster's own mean
        # pull the centre - a plain argmax lands on an outlier of a noisy flat.
        centre = n[np.argmax(a)].copy()
        for _ in range(8):
            near = (n @ centre) > np.cos(tol)
            if not near.any():
                break
            weighted = (n[near] * a[near, None]).sum(0)
            norm = np.linalg.norm(weighted)
            if norm < 1e-12:
                break
            centre = weighted / norm
        near = (n @ centre) > np.cos(tol)
        out.append((centre, float(a[near].sum() / area.sum()), int(near.sum())))
        # Remove the absorbed set from the working pool.
        idx = np.nonzero(alive)[0][near]
        alive[idx] = False
    return out


def report(path: Path, tolerance: float, show_all: bool) -> None:
    normal, area = face_normals(path)
    total = float(area.sum())
    found = clusters(normal, area, tolerance)

    print(f"== {path.name}  ({len(normal):,} tris, area {total:.5f})")
    for centre, share, count in found:
        angle = float(np.degrees(np.arccos(np.clip(centre[1], -1.0, 1.0))))
        bar = "#" * int(round(share * 40))
        flag = "  <-- UP AXIS" if share >= 0.15 else ""
        print(f"   n=[{centre[0]:+.3f} {centre[1]:+.3f} {centre[2]:+.3f}]  "
              f"{angle:5.1f} deg off +Y   area {share * 100:5.1f}%  "
              f"{count:>6} tris  {bar}{flag}")
        if not show_all and share < 0.15:
            break


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--tolerance", type=float, default=10.0)
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args(argv[1:])

    for f in args.files:
        p = Path(f)
        if not p.exists():
            print(f"MISSING {p}")
            continue
        report(p, args.tolerance, args.all)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
