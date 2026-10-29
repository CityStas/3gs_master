"""Four-azimuth turntable with the key light following the camera.

Why the light follows. `blender_preview.py` keeps the key light in world space, so any
view past ~90 deg is rendered on its unlit side and reads as a dark silhouette - which
is exactly how a "the back looks wrong" report gets missed. Here the light is rotated
with the azimuth so every station is lit the same way and the four images are directly
comparable.

    blender --background --python tools/blender_turntable.py -- <in> <out_dir> [size]
"""
import math
import os
import sys

import bpy
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:]
src = argv[0]
out_dir = os.path.abspath(argv[1])
size = int(argv[2]) if len(argv) > 2 else 700
azimuths = [int(v) for v in argv[3].split(",")] if len(argv) > 3 else [0, 90, 180, 270]

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
    print("TURN: unsupported extension %s" % suffix)
    sys.exit(1)

meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
lo = Vector((float("inf"),) * 3)
hi = Vector((float("-inf"),) * 3)
for ob in meshes:
    for c in ob.bound_box:
        w = ob.matrix_world @ Vector(c)
        for i in range(3):
            lo[i] = min(lo[i], w[i])
            hi[i] = max(hi[i], w[i])
ext = hi - lo
centre = (hi + lo) / 2.0

SENSOR_MM, LENS_MM, PAD = 36.0, 85.0, 1.15
radius = max(ext) * PAD * LENS_MM / SENSOR_MM
print("TURN: extent X=%.4f Y=%.4f Z=%.4f  radius %.4f" % (ext.x, ext.y, ext.z, radius))

world = bpy.data.worlds.new("W")
bpy.context.scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.05, 0.05, 0.06, 1)
world.node_tree.nodes["Background"].inputs[1].default_value = 1.0

key = bpy.data.objects.new("key", bpy.data.lights.new("key", type="SUN"))
key.data.energy = 4.0
bpy.context.collection.objects.link(key)
fill = bpy.data.objects.new("fill", bpy.data.lights.new("fill", type="SUN"))
fill.data.energy = 1.8
bpy.context.collection.objects.link(fill)

cam_data = bpy.data.cameras.new("cam")
cam_data.lens = LENS_MM
cam = bpy.data.objects.new("cam", cam_data)
bpy.context.collection.objects.link(cam)
bpy.context.scene.camera = cam

scene = bpy.context.scene
scene.render.resolution_x = size
scene.render.resolution_y = size
scene.render.image_settings.file_format = "PNG"
scene.render.engine = "CYCLES"
scene.cycles.device = "CPU"
scene.cycles.samples = 24
scene.cycles.use_denoising = False
scene.cycles.max_bounces = 4

for az in azimuths:
    a = math.radians(az)
    cam.location = (centre.x + radius * math.sin(a), centre.y - radius * math.cos(a),
                    centre.z + ext.z * 0.12)
    cam.rotation_euler = (centre - Vector(cam.location)).to_track_quat("-Z", "Y").to_euler()
    # Light rotates with the camera, so each station gets the same modelling.
    key.rotation_euler = (math.radians(55), 0, a + math.radians(35))
    fill.rotation_euler = (math.radians(70), 0, a + math.radians(-120))
    scene.render.filepath = os.path.join(out_dir, "az%03d.png" % az)
    bpy.ops.render.render(write_still=True)
    print("TURN: az %d -> %s" % (az, scene.render.filepath))

print("TURN: done")
