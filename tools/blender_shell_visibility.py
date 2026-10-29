"""Render a mesh twice - all shells, then with the small shells dropped - so the
visibility of a detached fragment can be measured instead of assumed.

    blender --background --python tools/blender_shell_visibility.py -- <in> <out_dir> [size] [azimuths]

Writes `with_azNNN.png` and `without_azNNN.png` pairs; the caller diffs them. A fragment
that changes no pixel is interior or buried, so dropping it cannot alter the silhouette.
"""
import math
import os
import sys

import bpy
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:]
src = argv[0]
out_dir = os.path.abspath(argv[1])
size = int(argv[2]) if len(argv) > 2 else 600
azimuths = [int(v) for v in argv[3].split(",")] if len(argv) > 3 else [0, 90, 180, 270]

bpy.ops.wm.read_factory_settings(use_empty=True)
suffix = os.path.splitext(src)[1].lower()
if suffix in (".glb", ".gltf"):
    bpy.ops.import_scene.gltf(filepath=src)
elif suffix == ".fbx":
    bpy.ops.import_scene.fbx(filepath=src)

meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
for ob in list(bpy.context.scene.objects):
    if ob.type != "MESH":
        bpy.data.objects.remove(ob, do_unlink=True)
if len(meshes) > 1:
    bpy.ops.object.select_all(action="DESELECT")
    for ob in meshes:
        ob.select_set(True)
    bpy.context.view_layer.objects.active = meshes[0]
    bpy.ops.object.join()
ob = [o for o in bpy.context.scene.objects if o.type == "MESH"][0]
me = ob.data

# Frame on the FULL model so both passes share a camera.
lo = Vector((float("inf"),) * 3)
hi = Vector((float("-inf"),) * 3)
for c in ob.bound_box:
    w = ob.matrix_world @ Vector(c)
    for i in range(3):
        lo[i] = min(lo[i], w[i])
        hi[i] = max(hi[i], w[i])
ext = hi - lo
centre = (hi + lo) / 2.0
SENSOR_MM, LENS_MM, PAD = 36.0, 85.0, 1.15
radius = max(ext) * PAD * LENS_MM / SENSOR_MM

world = bpy.data.worlds.new("W")
bpy.context.scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.05, 0.05, 0.06, 1)
for light_name, energy, rot in (
    ("key", 4.0, (math.radians(55), 0, math.radians(35))),
    ("fill", 1.8, (math.radians(70), 0, math.radians(-120))),
):
    light = bpy.data.objects.new(light_name, bpy.data.lights.new(light_name, type="SUN"))
    light.data.energy = energy
    light.rotation_euler = rot
    bpy.context.collection.objects.link(light)

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

os.makedirs(out_dir, exist_ok=True)


def shoot(tag):
    for az in azimuths:
        a = math.radians(az)
        cam.location = (centre.x + radius * math.sin(a),
                        centre.y - radius * math.cos(a), centre.z + ext.z * 0.12)
        cam.rotation_euler = (centre - Vector(cam.location)).to_track_quat("-Z", "Y").to_euler()
        scene.render.filepath = os.path.join(out_dir, "%s_az%03d.png" % (tag, az))
        bpy.ops.render.render(write_still=True)
        print("VIS: %s az %d -> %s" % (tag, az, scene.render.filepath))


shoot("with")

# Drop every component except the largest.
parent = list(range(len(me.vertices)))


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


for e in me.edges:
    a, b = find(e.vertices[0]), find(e.vertices[1])
    if a != b:
        parent[a] = b

groups = {}
for i in range(len(me.vertices)):
    groups.setdefault(find(i), []).append(i)
ordered = sorted(groups.values(), key=len, reverse=True)
print("VIS: components %s" % [len(g) for g in ordered[:6]])
keep = set(ordered[0])
kill = [i for i in range(len(me.vertices)) if i not in keep]
print("VIS: dropping %d verts in %d shell(s)" % (len(kill), len(ordered) - 1))

bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="DESELECT")
bpy.ops.object.mode_set(mode="OBJECT")
for i in kill:
    me.vertices[i].select = True
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.delete(type="VERT")
bpy.ops.object.mode_set(mode="OBJECT")
print("VIS: after drop %d verts %d faces" % (len(me.vertices), len(me.polygons)))

shoot("without")
print("VIS: done")
