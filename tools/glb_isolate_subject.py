"""Remove detached scene debris from a generated GLB - the backdrop blade.

Why this exists. `glb_strip_base.py` removes the display disc that the shape stage welds
under the feet. It does not remove the *other* thing the same stage invents: a thin
vertical blade standing beside the subject. Measured on the x_life character
(2026-10-12, `public/assets/xlife_creature.glb`):

    body        x in [-0.100, +0.099]      <- the subject
    (empty)     x in [+0.099, +0.407]      <- 3x the body's own width, nothing at all
    blade       x in [+0.407, +0.429]      489 tris = 3.5% of the surface,
                                           a wall ~0.02 thick spanning the whole height

In the viewer it reads as a sliver of glass floating beside the creature and travelling
with it. The prompt cannot fix it (the source image had no such thing - BiRefNet cut it
clean), so the cure is geometric, exactly like the base.

How the cut is chosen. Project the vertices on each horizontal axis, bin them finely, and
look for an empty run of bins that has occupied bins on BOTH sides. On a single subject
every empty run is at the outermost edge; an empty run *between* occupied bins means the
mesh holds two things, and the side with more vertices is the subject. Nothing
model-specific is hardcoded - the gap does the work. A mesh with no interior gap is
written through unchanged and the tool says so.

    blender --background --python tools/glb_isolate_subject.py -- <in.glb> <out.glb> [bins]

Vertical axis is never cut: a subject is allowed to be hollow in the middle of its
height (the gap between a humanoid's legs), and cutting there would decapitate it.
"""
import os
import sys

import bmesh
import bpy

argv = sys.argv[sys.argv.index("--") + 1:]
src = argv[0]
dst = argv[1] if len(argv) > 1 else src.replace(".glb", "-subject.glb")
#: Bins per horizontal axis. Fine enough to resolve a 2%-of-width blade, cheap enough
#: that one pass over the vertices is free.
BINS = int(argv[2]) if len(argv) > 2 else 400
#: An empty run must be at least this fraction of the axis to count as a separation.
#: Below it we are looking at sparse sampling, not at two objects.
GAP_MIN = 0.02
#: How many times to split. One blade is one split; the cap stops a pathological mesh
#: from being nibbled down to nothing.
MAX_SPLITS = 4

bpy.ops.wm.read_factory_settings(use_empty=True)
if os.path.splitext(src)[1].lower() in (".glb", ".gltf"):
    bpy.ops.import_scene.gltf(filepath=src)
else:
    print("SUBJECT: unsupported extension")
    sys.exit(1)

objs = [o for o in bpy.context.scene.objects if o.type == "MESH"]
if not objs:
    print("SUBJECT: no mesh in %s" % src)
    sys.exit(1)


def coords(ob, axis):
    m = ob.matrix_world
    return [m @ v.co for v in ob.data.vertices], None


def occupancy(values, lo, hi, bins):
    """Bin indices that hold at least one vertex."""
    if hi - lo <= 0:
        return {0}
    step = (hi - lo) / bins
    return {min(bins - 1, int((v - lo) / step)) for v in values}


def widest_interior_gap(occupied, bins):
    """Largest run of empty bins with occupied bins on both sides. Returns (a, b) bins."""
    best = None
    run = 0
    for i in range(bins):
        if i in occupied:
            if run:
                if best is None or run > best[1] - best[0]:
                    best = (i - run, i)
                run = 0
        else:
            run += 1
    return best  # a trailing run has no occupied bin after it, so it is not returned


removed_total = 0
for ob in objs:
    me = ob.data
    for split in range(MAX_SPLITS):
        verts = [ob.matrix_world @ v.co for v in me.vertices]
        cut = None
        for axis, name in ((0, "X"), (1, "Y")):
            vals = [v[axis] for v in verts]
            lo, hi = min(vals), max(vals)
            if hi - lo <= 0:
                continue
            occ = occupancy(vals, lo, hi, BINS)
            gap = widest_interior_gap(occ, BINS)
            if gap is None:
                continue
            g0, g1 = gap
            if (g1 - g0) / BINS < GAP_MIN:
                continue
            edge = lo + (hi - lo) * g0 / BINS
            left = sum(1 for v in vals if v < edge)
            right = len(vals) - left
            print("SUBJECT: %s: empty run bins %d..%d (%.1f%% of extent) at %s=%.4f; "
                  "left %d verts, right %d -> keeping %s"
                  % (name, g0, g1, (g1 - g0) / BINS * 100, name, edge, left, right,
                     "left" if left >= right else "right"))
            if left >= right:
                cut = (axis, None, edge)          # keep below the gap
            else:
                cut = (axis, edge, None)          # keep above the gap
            break
        if cut is None:
            break
        axis, lo_keep, hi_keep = cut
        bm = bmesh.new()
        bm.from_mesh(me)
        bm.verts.ensure_lookup_table()
        doomed = []
        for f in bm.faces:
            for v in f.verts:
                w = ob.matrix_world @ v.co
                if lo_keep is not None and w[axis] < lo_keep:
                    doomed.append(f)
                    break
                if hi_keep is not None and w[axis] > hi_keep:
                    doomed.append(f)
                    break
        bmesh.ops.delete(bm, geom=doomed, context="FACES")
        removed_total += len(doomed)
        bm.to_mesh(me)
        bm.free()
        me.update()

    print("SUBJECT: %s: %d verts, %d faces left" % (ob.name, len(me.vertices), len(me.polygons)))

if removed_total == 0:
    print("SUBJECT: no interior gap found - single subject, mesh written through unchanged")
else:
    print("SUBJECT: removed %d faces of debris" % removed_total)

os.makedirs(os.path.dirname(os.path.abspath(dst)) or ".", exist_ok=True)
bpy.ops.export_scene.gltf(filepath=dst, export_format="GLB")
print("SUBJECT: wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))
