"""Isolate and render the small detached shell of a mesh, so it can be identified.

A multi-shell mesh is normal for a hard-surface model and suspicious for an organic one.
This deletes every component except the smallest, frames that component's own bounding
box, and renders it from four azimuths - so the fragment is identifiable by eye instead
of being guessed at from its bounding box.

    blender --background --python tools/blender_shell_isolate.py -- <in> <out_dir> [size]
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

bpy.ops.wm.read_factory_settings(use_empty=True)
suffix = os.path.splitext(src)[1].lower()
if suffix in (".glb", ".gltf"):
    bpy.ops.import_scene.gltf(filepath=src)
elif suffix == ".fbx":
    bpy.ops.import_scene.fbx(filepath=src)
else:
    print("SHELL: unsupported %s" % suffix)
    sys.exit(1)

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
print("SHELL: %d component(s), sizes %s" % (len(ordered), [len(g) for g in ordered[:5]]))
if len(ordered) < 2:
    print("SHELL: only one component, nothing to isolate")
    sys.exit(0)

keep = set(ordered[1])
kill = [i for i in range(len(me.vertices)) if i not in keep]
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

pts = [ob.matrix_world @ v.co for v in me.vertices]
lo = Vector((min(p[k] for p in pts) for k in range(3)))
hi = Vector((max(p[k] for p in pts) for k in range(3)))
ext = hi - lo
centre = (hi + lo) / 2
print("SHELL: kept %d verts, %d faces, bbox min %s max %s size %s"
      % (len(me.vertices), len(me.polygons), [round(v, 5) for v in lo],
         [round(v, 5) for v in hi], [round(v, 5) for v in ext]))

world = bpy.data.worlds.new("W")
bpy.context.scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.05, 0.05, 0.06, 1)
for light_name, energy, rot in (
    ("key", 5.0, (math.radians(60), 0, math.radians(30))),
    ("fill", 2.4, (math.radians(75), 0, math.radians(-110))),
):
    light = bpy.data.objects.new(light_name, bpy.data.lights.new(light_name, type="SUN"))
    light.data.energy = energy
    light.rotation_euler = rot
    bpy.context.collection.objects.link(light)

cam_data = bpy.data.cameras.new("cam")
cam_data.lens = 60
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
radius = max(max(ext), 0.01) * 2.2
for az in (0, 90, 180, 270):
    a = math.radians(az)
    cam.location = (centre.x + radius * math.sin(a), centre.y - radius * math.cos(a),
                    centre.z + ext.z * 0.25)
    cam.rotation_euler = (centre - Vector(cam.location)).to_track_quat("-Z", "Y").to_euler()
    scene.render.filepath = os.path.join(out_dir, "shell_az%03d.png" % az)
    bpy.ops.render.render(write_still=True)
    print("SHELL: az %d -> %s" % (az, scene.render.filepath))
print("SHELL: done")
