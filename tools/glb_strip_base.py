"""Strip a display base / floor disc from a generated GLB.

Why this exists. `to_3d_multiview` on a character turnaround sheet reliably comes back
with a flat disc welded under the feet - measured on our first run, the bottom 3.3 % of
the height held 128 565 vertices spanning 1.00 of the model's full width, and the slice
immediately above it collapsed to 0.37 (the boots). The boots stand *on* the disc as
separate geometry, with a visible rim.

It is not inherited from the input. The source views were cut out with BiRefNet and
their alpha is clean to the pixel - no contact shadow survives - so the disc is invented
by the shape stage. The likeliest reason is the training distribution: a character
turnaround sheet on a plain background looks exactly like a figurine product shot, and
figurine datasets are full of models standing on a round display base. Whatever the
cause, the cure is the same and it is geometric, not prompt-level.

How the cut is chosen. Slice the height into fine bands and measure each band's
horizontal extent. A base reads as a run of bands at the bottom whose extent is close to
the model's full width; the subject above is far narrower. Cut just above the last band
that is still "wide". Nothing model-specific is hardcoded - the ratio does the work.

    blender --background --python tools/glb_strip_base.py -- <in.glb> <out.glb>
    blender --background --python tools/glb_strip_base.py -- in.glb out.glb 0.5 0.004

A file with no base is left alone: if the bottom band is already narrow, the tool
reports that and writes the mesh through unchanged rather than guessing.
"""
import os
import sys

import bmesh
import bpy

argv = sys.argv[sys.argv.index("--") + 1:]
src = argv[0]
dst = argv[1] if len(argv) > 1 else src.replace(".glb", "-nobase.glb")
#: A band counts as "base" while its extent is above this fraction of the full width.
RATIO = float(argv[2]) if len(argv) > 2 else 0.5
#: Cut slightly above the last wide band, as a fraction of total height. The rim of a
#: base is rounded, so the very top band can be marginally narrower than the ones under
#: it; this keeps a thin lip from being left behind.
EXTRA = float(argv[3]) if len(argv) > 3 else 0.004
#: Band count. Fine enough that the base's thickness is resolved to a fraction of a
#: percent, cheap enough not to matter (a slice is one pass over the vertices).
BANDS = 400

bpy.ops.wm.read_factory_settings(use_empty=True)

suffix = os.path.splitext(src)[1].lower()
if suffix in (".glb", ".gltf"):
    bpy.ops.import_scene.gltf(filepath=src)
elif suffix == ".fbx":
    bpy.ops.import_scene.fbx(filepath=src)
elif suffix == ".obj":
    bpy.ops.wm.obj_import(filepath=src)
else:
    print("BASE: unsupported extension %s" % suffix)
    sys.exit(1)

meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
if not meshes:
    print("BASE: no mesh objects imported")
    sys.exit(1)

# Join into one object so the cut is decided on the whole silhouette, then bake the
# transform so local coordinates are world coordinates and the bmesh edit can be a
# plain z comparison.
bpy.ops.object.select_all(action="DESELECT")
for ob in meshes:
    ob.select_set(True)
bpy.context.view_layer.objects.active = meshes[0]
if len(meshes) > 1:
    bpy.ops.object.join()
ob = bpy.context.view_layer.objects.active
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

me = ob.data
verts_before = len(me.vertices)
faces_before = len(me.polygons)

zs = [v.co.z for v in me.vertices]
lo, hi = min(zs), max(zs)
h = hi - lo
if h <= 0:
    print("BASE: degenerate mesh (height %.6f)" % h)
    sys.exit(1)

full = max(max(v.co.x for v in me.vertices) - min(v.co.x for v in me.vertices),
           max(v.co.y for v in me.vertices) - min(v.co.y for v in me.vertices))
print("BASE: %d verts, z %.4f..%.4f (h %.4f), full extent %.4f"
      % (verts_before, lo, hi, h, full))

# Horizontal extent per band.
ext = []
for i in range(BANDS):
    a, b = lo + h * i / BANDS, lo + h * (i + 1) / BANDS
    sel = [v.co for v in me.vertices if a <= v.co.z < b]
    if not sel:
        ext.append(0.0)
        continue
    ex = max(p.x for p in sel) - min(p.x for p in sel)
    ey = max(p.y for p in sel) - min(p.y for p in sel)
    ext.append(max(ex, ey))

limit = RATIO * full
print("BASE: bottom band extent %.4f (%.2f of full), threshold %.4f"
      % (ext[0], ext[0] / full, limit))

if ext[0] <= limit:
    print("BASE: bottom is already narrow - no base plate detected, nothing removed")
else:
    last_wide = 0
    for i, e in enumerate(ext):
        if e > limit:
            last_wide = i
        else:
            # Stop at the first narrow band *after* the wide run: above it is subject.
            break
    z_cut = lo + h * (last_wide + 1) / BANDS + h * EXTRA
    print("BASE: base occupies %.1f%% of height, cutting at z %.4f (%.2f%% up)"
          % ((last_wide + 1) / BANDS * 100, z_cut, (z_cut - lo) / h * 100))

    bm = bmesh.new()
    bm.from_mesh(me)
    doomed = [f for f in bm.faces
              if sum(v.co.z for v in f.verts) / len(f.verts) < z_cut]
    bmesh.ops.delete(bm, geom=doomed, context="FACES")
    loose = [v for v in bm.verts if not v.link_faces]
    if loose:
        bmesh.ops.delete(bm, geom=loose, context="VERTS")
    bm.to_mesh(me)
    bm.free()
    me.update()

    zs2 = [v.co.z for v in me.vertices]
    print("BASE: removed %d faces, %d verts; %d verts / %d faces left, z %.4f..%.4f"
          % (faces_before - len(me.polygons), verts_before - len(me.vertices),
             len(me.vertices), len(me.polygons), min(zs2), max(zs2)))

bpy.ops.object.select_all(action="DESELECT")
ob.select_set(True)
bpy.context.view_layer.objects.active = ob
bpy.ops.export_scene.gltf(
    filepath=os.path.abspath(dst),
    export_format="GLB",
    use_selection=True,
    export_apply=True,
    export_yup=True,
)
print("BASE: wrote %s (%d bytes)" % (dst, os.path.getsize(os.path.abspath(dst))))
