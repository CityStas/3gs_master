"""Prepare an AI-generated mesh for skinning: decimate, flatten transforms,
stand it on the floor and centre it.

Why each step matters for rigging:

* decimate      - auto-weights on ~700k triangles are noisy and produce spikes
                  at joints; 40-80k is the useful range for a game character.
* transforms    - the glTF importer leaves rotation/scale on the object.  If
                  they are not applied, the exporter writes a node transform and
                  some riggers compute bone lengths in the wrong space.
* floor + centre- skeleton auto-fit works from the bounding box, so a mesh that
                  floats or sits off-axis gets a shifted skeleton.

Usage (headless):

    blender --background --factory-startup --python tools/blender_mesh_prep.py -- \
        --in  Robo_3d.glb \
        --out Robo_rig_ready.glb \
        --tris 60000

Blender is Z-up while glTF is Y-up; the importer converts on the way in and the
exporter converts back, so all the geometry maths here is done in Blender's
Z-up space and "up" means +Z.
"""

from __future__ import annotations

import argparse
import sys

import bpy
from mathutils import Vector


def parse_args() -> argparse.Namespace:
    argv = sys.argv
    argv = argv[argv.index("--") + 1:] if "--" in argv else []
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="src", required=True)
    ap.add_argument("--out", dest="dst", required=True)
    ap.add_argument("--tris", type=int, default=60000, help="target triangle count")
    ap.add_argument("--no-floor", action="store_true", help="keep the original position")
    return ap.parse_args(argv)


def clear_scene() -> None:
    bpy.ops.wm.read_factory_settings(use_empty=True)


def import_glb(path: str) -> list:
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=path)
    return [o for o in bpy.data.objects if o not in before]


def tri_count(obj) -> int:
    me = obj.data
    me.calc_loop_triangles()
    return len(me.loop_triangles)


def world_bounds(objs) -> tuple[Vector, Vector]:
    lo = Vector((1e9, 1e9, 1e9))
    hi = Vector((-1e9, -1e9, -1e9))
    for o in objs:
        for corner in o.bound_box:
            p = o.matrix_world @ Vector(corner)
            for i in range(3):
                lo[i] = min(lo[i], p[i])
                hi[i] = max(hi[i], p[i])
    return lo, hi


def fmt(v: Vector) -> str:
    return f"({v.x:.3f}, {v.y:.3f}, {v.z:.3f})"


def main() -> int:
    args = parse_args()

    clear_scene()
    objs = import_glb(args.src)
    meshes = [o for o in objs if o.type == "MESH"]
    if not meshes:
        raise SystemExit("no mesh objects in the file")

    print(f"[prep] imported {len(meshes)} mesh object(s)")
    for o in meshes:
        print(f"[prep]   {o.name}: {tri_count(o)} tris, scale={fmt(o.scale)}")

    # --- one object: a single skinned mesh is what riggers expect -------------
    bpy.ops.object.select_all(action="DESELECT")
    for o in meshes:
        o.select_set(True)
    bpy.context.view_layer.objects.active = meshes[0]
    if len(meshes) > 1:
        bpy.ops.object.join()
    obj = bpy.context.view_layer.objects.active

    before_tris = tri_count(obj)
    lo, hi = world_bounds([obj])
    print(f"[prep] before: {before_tris} tris, bounds {fmt(lo)}..{fmt(hi)}")

    # --- apply rotation/scale so the exporter has no node transform ----------
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

    # --- decimate ------------------------------------------------------------
    if before_tris > args.tris:
        ratio = args.tris / before_tris
        mod = obj.modifiers.new(name="Decimate", type="DECIMATE")
        mod.decimate_type = "COLLAPSE"
        mod.ratio = ratio
        mod.use_collapse_triangulate = True
        bpy.ops.object.modifier_apply(modifier=mod.name)
        print(f"[prep] decimated {before_tris} -> {tri_count(obj)} tris (ratio {ratio:.4f})")
    else:
        print(f"[prep] already under {args.tris} tris, no decimation")

    # --- stand on the floor, centre on X/Y -----------------------------------
    if not args.no_floor:
        lo, hi = world_bounds([obj])
        shift = Vector((-(lo.x + hi.x) / 2.0, -(lo.y + hi.y) / 2.0, -lo.z))
        obj.location += shift
        bpy.context.view_layer.update()
        bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
        lo, hi = world_bounds([obj])
        print(f"[prep] moved by {fmt(shift)} -> bounds {fmt(lo)}..{fmt(hi)}")
        print(f"[prep] height {hi.z - lo.z:.4f}, width {hi.x - lo.x:.4f}, depth {hi.y - lo.y:.4f}")

    # --- export --------------------------------------------------------------
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.export_scene.gltf(
        filepath=args.dst,
        export_format="GLB",
        use_selection=True,
        export_apply=True,
        export_yup=True,
        export_materials="EXPORT",
        export_image_format="AUTO",
    )
    print(f"[prep] wrote {args.dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
