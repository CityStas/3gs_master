"""Close-up render of a region of a model, for inspecting details.

Usage:
    blender --background --python blender_closeup.py -- <in> <out_dir> <tx> <ty> <tz> <radius> [size] [name]

The target point is in the model's own coordinates, which is what the bbox
report from blender_preview.py prints.

`out_dir` is taken as absolute and resolved before any bpy call. Blender resolves a
relative render filepath against its own working directory, and `read_factory_settings`
resets that - so an absolute path computed afterwards can still land outside the
project (this tool used to write into `C:/assets/...`). Taking the directory rather
than a file path keeps the same shape as blender_preview.py / blender_turntable.py.
"""
import math
import os
import sys

import bpy
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:]
src = argv[0]
# Absolute, and computed before bpy touches the working directory.
out_dir = os.path.abspath(argv[1])
target = Vector((float(argv[2]), float(argv[3]), float(argv[4])))
radius = float(argv[5])
size = int(argv[6]) if len(argv) > 6 else 720
# Not `name`: the light loop below used to reuse that identifier and clobbered it,
# so every render came out named after the last light ("fill_*.png").
stem = argv[7] if len(argv) > 7 else "probe"

suffix = os.path.splitext(src)[1].lower()
bpy.ops.wm.read_factory_settings(use_empty=True)
if suffix in (".glb", ".gltf"):
    bpy.ops.import_scene.gltf(filepath=src)
elif suffix == ".fbx":
    bpy.ops.import_scene.fbx(filepath=src)

world = bpy.data.worlds.new("W")
bpy.context.scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.06, 0.06, 0.07, 1)

for light_name, energy, rot in (
    ("key", 4.5, (math.radians(60), 0, math.radians(30))),
    ("fill", 2.0, (math.radians(75), 0, math.radians(-110))),
):
    light = bpy.data.objects.new(light_name, bpy.data.lights.new(light_name, type="SUN"))
    light.data.energy = energy
    light.rotation_euler = rot
    bpy.context.collection.objects.link(light)

cam_data = bpy.data.cameras.new("cam")
cam_data.lens = 90
cam = bpy.data.objects.new("cam", cam_data)
bpy.context.collection.objects.link(cam)
bpy.context.scene.camera = cam

scene = bpy.context.scene
scene.render.resolution_x = size
scene.render.resolution_y = size
scene.render.image_settings.file_format = "PNG"
scene.render.engine = "CYCLES"
scene.cycles.device = "CPU"
scene.cycles.samples = 32
scene.cycles.use_denoising = False
scene.cycles.max_bounces = 4

os.makedirs(out_dir, exist_ok=True)
for label, azimuth in (("front", 0), ("threequarter", 35)):
    a = math.radians(azimuth)
    cam.location = (
        target.x + radius * math.sin(a),
        target.y - radius * math.cos(a),
        target.z + radius * 0.18,
    )
    direction = target - Vector(cam.location)
    cam.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    scene.render.filepath = os.path.join(out_dir, "%s_%s.png" % (stem, label))
    bpy.ops.render.render(write_still=True)
    print("CLOSEUP: wrote %s" % scene.render.filepath)
