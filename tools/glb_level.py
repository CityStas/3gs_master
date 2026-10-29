"""Level a reconstructed prop so its resting face is horizontal.

The problem
-----------
TRELLIS.2 / Pixal3D return a mesh in the *conditioning camera's* frame, not in an
object frame. Measured on the pack in this repo, by clustering area-weighted face
normals (`tools/glb_up_axis.py`):

    mug       25.2 deg off +Y   (24.5% of surface area agrees on that flat)
    keyboard  38.1 deg off +Y   (22.8%)
    jelly     17.0 deg off +Y   (15.0%)

A mug standing on a desk with a 25-degree list is not a subtle artefact, and it
is worse than cosmetic: `normaliseHeight` in the scene scales the bounding box's
*Y extent* to the target height, so a tilted prop is scaled by its tilted
diagonal. The keyboard's AABB is 0.861 x 0.377 x 0.515 for a shape that is really
0.86 x 0.10 x 0.30 - its height is inflated 3.7x, so it comes out a third of the
size it should be.

Why the tilt is a camera pose, and why it is per-job
---------------------------------------------------
The workflow estimates the camera *from the input image* (`MoGeInference` ->
`MoGeGeometryToFOV`, and a `camera_angle_x` of 49.13 for the keyboard hero). So
the frame each mesh arrives in is its own image's estimated camera, and the tilt
is that camera's pose. It differs per job - which is what the measurements show
(the mug 25.2 deg from a default framing, the keyboard 38.1 deg from an
explicitly lowered camera) - and it carries a little roll as well as pitch (the
mug's flat reads 3.0 deg off the YZ plane, the keyboard's -5.9 deg).

The mesh is therefore `R_cam . W` for an upright world pose `W`, and the
correction is `R_cam^-1`. That is recovered, up to a harmless yaw, by the
minimal rotation that carries the dominant flat onto the axis it truly belongs
to. Two things are worth spelling out because both are easy to get wrong:

* **Base vs front is a fact about the prop, not the mesh.** A monitor lying on
  its back rests stably on its own rear panel, so "the largest flat" and "the
  bottom" are not the same question and no amount of geometry can separate them.
  `--flat-target` is where that fact is supplied: `y` for a base, `z` for a
  vertical front face (whose true base is a thin edge).
* **For a front face the target is -Z, not +Z.** `clusters()` folds normals into
  the +Y hemisphere, and the same fold that made the normal point "up" made it
  point *away* from the camera. Aiming it at +Z rotates the object 180 deg.

What this does
--------------
Rotates the vertices so the dominant flat lands on its target axis, then
(optionally) yaws so the longest horizontal axis runs along X. Positions,
normals and tangents are all rotated; UVs, indices and textures are untouched.
The GLB is rewritten in place unless `--out` is given.

`--report` prints the cluster it used, its share of area and the residual roll,
so every choice is auditable; `--rotate-axis x:DEG` is the manual override.

Usage
-----
    python tools/glb_level.py <file.glb> [...] --report
    python tools/glb_level.py <file.glb> --level --flat-target z
    python tools/glb_level.py <file.glb> --level --align-longest-x
    python tools/glb_level.py <file.glb> --rotate-axis x:25.2
"""

from __future__ import annotations

import argparse
import json
import struct
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from glb_inspect import COMPONENT, TYPE_COUNT  # noqa: E402
from glb_up_axis import face_normals  # noqa: E402

JSON_CHUNK = 0x4E4F534A
BIN_CHUNK = 0x004E4942

#: Below this share of total area the "dominant flat" is not a flat at all, it is
#: whichever direction happened to win among noisy normals - the jelly blob sits
#: at 15.0%, the mug and keyboard at 24.5% and 22.8%. Rotating a prop by a noise
#: direction is worse than leaving it tilted, so leveling refuses instead.
MIN_SHARE = 0.18

#: The pitch model says the flat lies in the YZ plane, so its X component ("roll")
#: must be near zero. A big one means the dominant flat is a *side* face - a
#: headphone's ear cup faces +/-X - and the model does not apply to it.
MAX_ROLL = 25.0


# --------------------------------------------------------------------- reading
def parse_glb(path: Path):
    blob = path.read_bytes()
    magic, version, _length = struct.unpack_from("<4sII", blob, 0)
    if magic != b"glTF":
        raise ValueError(f"{path.name}: not a GLB")

    offset = 12
    gltf = None
    binary = bytearray()
    json_span = None
    bin_span = None
    while offset < len(blob):
        chunk_len, chunk_type = struct.unpack_from("<II", blob, offset)
        start = offset + 8
        if chunk_type == JSON_CHUNK:
            gltf = json.loads(blob[start:start + chunk_len].decode("utf-8"))
            json_span = (start, start + chunk_len)
        elif chunk_type == BIN_CHUNK:
            binary = bytearray(blob[start:start + chunk_len])
            bin_span = (start, start + chunk_len)
        offset = start + chunk_len + ((4 - chunk_len % 4) % 4 if chunk_len % 4 else 0)
    return version, gltf, binary, json_span, bin_span


def view_array(gltf, binary, accessor_index: int) -> np.ndarray:
    acc = gltf["accessors"][accessor_index]
    _fmt, dtype = COMPONENT[acc["componentType"]]
    ncomp = TYPE_COUNT[acc["type"]]
    view = gltf["bufferViews"][acc["bufferView"]]
    stride = view.get("byteStride") or np.dtype(dtype).itemsize * ncomp
    start = view.get("byteOffset", 0) + acc.get("byteOffset", 0)
    if stride == np.dtype(dtype).itemsize * ncomp:
        return np.frombuffer(bytes(binary), dtype=dtype, count=acc["count"] * ncomp,
                             offset=start).reshape(acc["count"], ncomp)
    out = np.empty((acc["count"], ncomp), dtype=dtype)
    for i in range(acc["count"]):
        out[i] = np.frombuffer(bytes(binary), dtype=dtype, count=ncomp,
                               offset=start + i * stride)
    return out


def write_array(gltf, binary: bytearray, accessor_index: int, values: np.ndarray) -> None:
    acc = gltf["accessors"][accessor_index]
    view = gltf["bufferViews"][acc["bufferView"]]
    start = view.get("byteOffset", 0) + acc.get("byteOffset", 0)
    raw = np.ascontiguousarray(values).tobytes()
    binary[start:start + len(raw)] = raw


# ------------------------------------------------------------------ rotations
def rotation_between(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Minimal rotation matrix taking unit vector `a` to unit vector `b`."""
    a = a / np.linalg.norm(a)
    b = b / np.linalg.norm(b)
    v = np.cross(a, b)
    c = float(np.dot(a, b))
    s = float(np.linalg.norm(v))
    if s < 1e-9:
        if c > 0:
            return np.eye(3)
        # Antiparallel: any perpendicular axis will do.
        axis = np.array([1.0, 0.0, 0.0])
        if abs(a[0]) > 0.9:
            axis = np.array([0.0, 1.0, 0.0])
        perp = np.cross(a, axis)
        perp /= np.linalg.norm(perp)
        return 2.0 * np.outer(perp, perp) - np.eye(3)
    vx = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    return np.eye(3) + vx + vx @ vx * ((1 - c) / (s * s))


def rotation_about(axis: str, degrees: float) -> np.ndarray:
    t = np.radians(degrees)
    c, s = np.cos(t), np.sin(t)
    if axis == "x":
        return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    if axis == "y":
        return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def rotation_angle(rotation: np.ndarray) -> float:
    """Magnitude of a rotation, in degrees - used to pick the smaller candidate."""
    trace = float(np.trace(rotation))
    return float(np.degrees(np.arccos(np.clip((trace - 1.0) / 2.0, -1.0, 1.0))))


# ------------------------------------------------------------------- measure
def measure_up(path: Path, tolerance: float):
    """Return (flat normal, share, tri count, angle off +Y, residual roll)."""
    normal, area = face_normals(path)
    from glb_up_axis import clusters
    found = clusters(normal, area, tolerance, top=1)
    if not found:
        raise ValueError(f"{path.name}: no face normals")
    centre, share, count = found[0]
    angle = float(np.degrees(np.arccos(np.clip(centre[1], -1.0, 1.0))))
    # The pitch model predicts no X component on the flat. Anything here is roll
    # the model cannot explain, so it is reported rather than silently ignored.
    roll = float(np.degrees(np.arcsin(np.clip(centre[0], -1.0, 1.0))))
    return centre, share, count, angle, roll


def pitch_from_flat(up: np.ndarray, flat_target: str) -> float:
    """Camera pitch in degrees, read off the dominant flat's normal.

    Kept for reporting and for the audit trail; the correction itself uses the
    minimal rotation onto the target axis, which is equivalent for a flat in the
    YZ plane and additionally removes the camera's roll.
    """
    pitch = np.degrees(np.arctan2(up[2], up[1]))
    if flat_target == "z":
        pitch -= 90.0
    return float(pitch)


# ---------------------------------------------------------------------- apply
def level(path: Path, *, do_level: bool, align_longest_x: bool,
          manual: np.ndarray | None, tolerance: float, out: Path | None,
          report_only: bool, flat_target: str = "y") -> dict:
    up, share, count, angle, roll = measure_up(path, tolerance)
    version, gltf, binary, _js, _bs = parse_glb(path)

    attrs = [p["attributes"] for m in gltf["meshes"] for p in m["primitives"]]
    positions = [a["POSITION"] for a in attrs if "POSITION" in a]
    if not positions:
        raise ValueError(f"{path.name}: no POSITION")

    all_pos = np.concatenate([view_array(gltf, binary, i).astype(np.float64)
                              for i in positions])

    rotation = np.eye(3)
    steps = []
    skipped = None
    if manual is not None:
        rotation = manual
        steps.append("manual")
    elif do_level and share < MIN_SHARE:
        # Not a flat, just the loudest noise. Leave the tilt alone.
        skipped = f"flat only {share * 100:.1f}% of area (< {MIN_SHARE * 100:.0f}%)"
    elif do_level and abs(roll) > MAX_ROLL:
        # A side face won, so this is not a pitch we can read. Leave the tilt.
        skipped = f"flat is a side face (roll {roll:+.1f} deg > {MAX_ROLL:.0f})"
    elif do_level:
        # Align the dominant flat onto its true axis. `rotation_between` gives the
        # minimal rotation, which recovers the camera rotation up to a harmless yaw
        # and also removes the camera's roll - so a base lands at exactly 0 deg,
        # not at the few degrees of roll a pitch-only correction would leave.
        if flat_target == "y":
            rotation = rotation_between(up, np.array([0.0, 1.0, 0.0]))
        else:
            # A front face faces the camera, but `clusters()` folded the normal
            # into the +Y hemisphere, and that fold may have reversed it - so
            # whether the truth is +Z or -Z is not recoverable from `up` alone.
            # Both are candidates; the camera sits well under 90 deg off the desk,
            # so the true correction is the *smaller* of the two. Taking the
            # smaller one is what stops a fold from flipping the prop 180 deg.
            plus = rotation_between(up, np.array([0.0, 0.0, 1.0]))
            minus = rotation_between(up, np.array([0.0, 0.0, -1.0]))
            rotation = plus if rotation_angle(plus) <= rotation_angle(minus) else minus
        steps.append(f"flat {angle:5.1f} -> {flat_target} ({share * 100:.0f}%)")

    if align_longest_x:
        p = all_pos @ rotation.T
        horiz = p.copy()
        horiz[:, 1] = 0
        # The horizontal direction of greatest spread is the object's long axis.
        centred = horiz - horiz.mean(0)
        _u, _s, vt = np.linalg.svd(centred, full_matrices=False)
        long_axis = vt[0]
        target = np.array([1.0, 0.0, 0.0])
        yaw = rotation_between(long_axis, target)
        rotation = yaw @ rotation
        steps.append(f"yaw {np.degrees(np.arccos(np.clip(abs(long_axis[0]), -1, 1))):.1f} deg")

    if report_only:
        return {"path": str(path), "angle": angle, "share": share, "tris": count,
                "roll": roll, "steps": steps, "applied": False, "skipped": skipped}

    if skipped is not None and not align_longest_x:
        # Identity rotation - nothing to write, and leaving the bytes alone keeps
        # a no-op run from touching mtimes or risking a bad rewrite.
        return {"path": str(path), "angle": angle, "share": share, "tris": count,
                "roll": roll, "steps": steps, "applied": False, "skipped": skipped}

    centre = all_pos.mean(0)
    for accessor_index in positions:
        p = view_array(gltf, binary, accessor_index).astype(np.float64)
        p = (p - centre) @ rotation.T + centre
        write_array(gltf, binary, accessor_index, p.astype(np.float32))
        acc = gltf["accessors"][accessor_index]
        acc["min"] = [float(x) for x in p.min(0)]
        acc["max"] = [float(x) for x in p.max(0)]

    for attribute in ("NORMAL", "TANGENT"):
        for a in attrs:
            if attribute not in a:
                continue
            index = a[attribute]
            v = view_array(gltf, binary, index).astype(np.float64)
            xyz = v[:, :3] @ rotation.T
            v[:, :3] = xyz
            write_array(gltf, binary, index, v.astype(np.float32))

    payload = json.dumps(gltf, separators=(",", ":")).encode("utf-8")
    payload += b" " * ((4 - len(payload) % 4) % 4)
    body = bytearray()
    body += struct.pack("<II", len(payload), JSON_CHUNK) + payload
    body += struct.pack("<II", len(binary), BIN_CHUNK) + bytes(binary)
    blob = struct.pack("<4sII", b"glTF", version, 12 + len(body)) + bytes(body)

    destination = out or path
    destination.write_bytes(blob)
    return {"path": str(destination), "angle": angle, "share": share, "tris": count,
            "roll": roll, "steps": steps, "applied": True, "skipped": None,
            "bytes": len(blob)}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--level", action="store_true",
                    help="undo the conditioning camera's pitch")
    ap.add_argument("--flat-target", choices=("y", "z"), default="y",
                    help="is the dominant flat the base (y) or the front (z)?")
    ap.add_argument("--align-longest-x", action="store_true",
                    help="then yaw so the longest horizontal axis runs along X")
    ap.add_argument("--rotate-axis", metavar="AXIS:DEG",
                    help="manual override, e.g. x:25.2")
    ap.add_argument("--tolerance", type=float, default=10.0)
    ap.add_argument("--report", action="store_true", help="measure, change nothing")
    ap.add_argument("--out", help="write here instead of in place (single file only)")
    args = ap.parse_args(argv[1:])

    manual = None
    if args.rotate_axis:
        axis, _, deg = args.rotate_axis.partition(":")
        manual = rotation_about(axis.strip().lower(), float(deg))

    if args.out and len(args.files) > 1:
        print("--out needs exactly one input")
        return 2

    for f in args.files:
        p = Path(f)
        if not p.exists():
            print(f"MISSING {p}")
            continue
        info = level(p, do_level=args.level, align_longest_x=args.align_longest_x,
                     manual=manual, tolerance=args.tolerance, flat_target=args.flat_target,
                     out=Path(args.out) if args.out else None,
                     report_only=args.report)
        verb = "would" if args.report else "did"
        detail = ("skipped - " + info["skipped"]) if info.get("skipped") else \
                 ("+".join(info["steps"]) if info["steps"] else "nothing")
        print(f"  {p.name:<22} flat {info['angle']:5.1f} deg off +Y  "
              f"({info['share'] * 100:4.1f}% of area, {info['tris']} tris, "
              f"roll {info['roll']:+5.1f})  {verb} {detail}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
