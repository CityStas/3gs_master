"""Clay turntable: the mesh with a plain diffuse material, no textures.

Separates geometry from texture. If a detail appears on both sides in clay it is real
geometry; if it only appears in the textured render it is a UV/projection problem. When
a viewer shows "a chest front and back", that distinction is the whole question.
"""
import math
import os
import sys

import bpy
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:]
src = argv[0]
out_dir = os.path.abspath(argv[1])
size = int(argv[2]) if len(argv) > 2 else 620
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

# Replace every material with a neutral clay one, so nothing of the baked texture
# survives into the render.
clay = bpy.data.materials.new("clay")
clay.use_nodes = True
bsdf = clay.node_tree.nodes["Principled BSDF"]
bsdf.inputs["Base Color"].default_value = (0.72, 0.70, 0.66, 1.0)
bsdf.inputs["Roughness"].default_value = 0.65
for ob in meshes:
    ob.data.materials.clear()
    ob.data.materials.append(clay)

SENSOR_MM, LENS_MM, PAD = 36.0, 85.0, 1.15
radius = max(ext) * PAD * LENS_MM / SENSOR_MM

world = bpy.data.worlds.new("W")
bpy.context.scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.05, 0.05, 0.06, 1)

key = bpy.data.objects.new("key", bpy.data.lights.new("key", type="SUN"))
key.data.energy = 3.2
bpy.context.collection.objects.link(key)
fill = bpy.data.objects.new("fill", bpy.data.lights.new("fill", type="SUN"))
fill.data.energy = 1.4
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
    key.rotation_euler = (math.radians(55), 0, a + math.radians(35))
    fill.rotation_euler = (math.radians(70), 0, a + math.radians(-120))
    scene.render.filepath = os.path.join(out_dir, "clay%03d.png" % az)
    bpy.ops.render.render(write_still=True)
    print("CLAY: az %d -> %s" % (az, scene.render.filepath))
print("CLAY: done")
