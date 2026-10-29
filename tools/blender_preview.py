"""Headless turntable-ish preview of a GLB: front / side / three-quarter.

Usage:
    blender --background --python blender_preview.py -- <in.glb> <out_dir> [size]

Renders three orthographic-ish views with Cycles CPU so it works without a GL
context. Also prints a bbox report, which is what actually answers "what pose is
this mesh in".

`out_dir` is taken as absolute: Blender resolves a relative render filepath against
its own working directory, so a relative path quietly writes the PNGs somewhere
else while the script reports the path it meant.
"""
import math
import os
import sys

import bpy
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:]
src = argv[0]
# Absolute, because Blender resolves a relative render filepath against its own
# working directory, not the caller's. A relative path here silently wrote the
# renders to C:\assets\... while the script printed the project-relative name it
# thought it had used.
out_dir = os.path.abspath(argv[1])
size = int(argv[2]) if len(argv) > 2 else 640

os.makedirs(out_dir, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)

suffix = os.path.splitext(src)[1].lower()
if suffix in (".glb", ".gltf"):
    bpy.ops.import_scene.gltf(filepath=src)
elif suffix == ".fbx":
    bpy.ops.import_scene.fbx(filepath=src)
elif suffix == ".obj":
    bpy.ops.wm.obj_import(filepath=src)
else:
    print("PREVIEW: unsupported extension %s" % suffix)
    sys.exit(1)

meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
if not meshes:
    print("PREVIEW: no mesh objects imported")
    sys.exit(1)

# --- world-space bounding box over evaluated geometry -----------------------
lo = Vector((float("inf"),) * 3)
hi = Vector((float("-inf"),) * 3)
tris = 0
for ob in meshes:
    for corner in ob.bound_box:
        w = ob.matrix_world @ Vector(corner)
        for i in range(3):
            lo[i] = min(lo[i], w[i])
            hi[i] = max(hi[i], w[i])
    tris += len(ob.data.polygons)

ext = hi - lo
centre = (hi + lo) / 2.0
print("PREVIEW: objects=%d tris=%d" % (len(meshes), tris))
print("PREVIEW: bbox min (%.4f %.4f %.4f) max (%.4f %.4f %.4f)"
      % (lo.x, lo.y, lo.z, hi.x, hi.y, hi.z))
print("PREVIEW: extent X=%.4f Y=%.4f Z=%.4f" % (ext.x, ext.y, ext.z))

# Which axis is up? glTF is Y-up but Blender's importer normally converts to
# Z-up, so Z should dominate for a standing character.
vert = max(ext, key=lambda v: v)
axes = "XYZ"
print("PREVIEW: dominant axis = %s (%.4f)" % (axes[list(ext).index(vert)], vert))

# Width-to-height ratio is the T-pose tell: a T-pose humanoid is about as wide
# as it is tall, an A-pose or arms-down figure is much narrower.
span = max(ext.x, ext.y)
if vert > 0:
    ratio = span / vert
    print("PREVIEW: width/height ratio = %.3f" % ratio)
    if ratio > 0.85:
        print("PREVIEW: -> arms likely extended sideways (T-pose-ish)")
    elif ratio > 0.5:
        print("PREVIEW: -> arms likely down / A-pose-ish")
    else:
        print("PREVIEW: -> narrow silhouette: arms tight to body, or not a humanoid")

# Camera distance, solved rather than guessed. The render is square, so the frame
# must be at least as large as the model's largest dimension; the frame width at
# distance `d` is `d * sensor / lens`. The old `radius = max(ext) * 1.9` ignored
# that relation: at lens 85 / sensor 36 the frame came out `max(ext) * 0.805`,
# *smaller* than the model, so every preview was cropped at the knees and the crown
# and the tighter the lens the worse it got.
SENSOR_MM = 36.0   # Blender's default sensor width
LENS_MM = 85.0
FRAME_PAD = 1.15   # headroom, so the silhouette never touches the frame edge
frame = max(ext) * FRAME_PAD
radius = frame * LENS_MM / SENSOR_MM
print("PREVIEW: frame %.4f at radius %.4f (lens %.0fmm)" % (frame, radius, LENS_MM))

# --- lighting ---------------------------------------------------------------
world = bpy.data.worlds.new("W")
bpy.context.scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.05, 0.05, 0.06, 1)
world.node_tree.nodes["Background"].inputs[1].default_value = 1.0

key = bpy.data.objects.new("key", bpy.data.lights.new("key", type="SUN"))
key.data.energy = 4.0
key.rotation_euler = (math.radians(55), 0, math.radians(35))
bpy.context.collection.objects.link(key)

fill = bpy.data.objects.new("fill", bpy.data.lights.new("fill", type="SUN"))
fill.data.energy = 1.5
fill.rotation_euler = (math.radians(70), 0, math.radians(-120))
bpy.context.collection.objects.link(fill)

# --- camera + render --------------------------------------------------------
cam_data = bpy.data.cameras.new("cam")
cam_data.lens = LENS_MM
cam = bpy.data.objects.new("cam", cam_data)
bpy.context.collection.objects.link(cam)
bpy.context.scene.camera = cam

scene = bpy.context.scene
scene.render.resolution_x = size
scene.render.resolution_y = size
scene.render.film_transparent = False
scene.render.image_settings.file_format = "PNG"

scene.render.engine = "CYCLES"
scene.cycles.device = "CPU"
scene.cycles.samples = 24
scene.cycles.use_denoising = False
scene.cycles.max_bounces = 4

# glTF import leaves Z up. Orbit in the XY plane, keep the camera level.
for label, azimuth in (("front", 0), ("threequarter", 45), ("side", 90)):
    a = math.radians(azimuth)
    cam.location = (
        centre.x + radius * math.sin(a),
        centre.y - radius * math.cos(a),
        centre.z + ext.z * 0.12,
    )
    direction = centre - Vector(cam.location)
    cam.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    scene.render.filepath = os.path.join(out_dir, "view_%s.png" % label)
    bpy.ops.render.render(write_still=True)
    print("PREVIEW: wrote %s" % scene.render.filepath)

print("PREVIEW: done")
