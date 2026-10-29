"""Rotate a generated mesh so it faces the conventional direction.

Why this exists. `to_3d_high_multiview` returns the character facing **glTF -Z**. The
convention for characters is **+Z** (Blender's default front view, three.js
`OrbitControls` and most viewers all look at the +Z side), so opening the GLB shows the
model's back: measured on `scout-mv.glb` the face and the chest pockets sit at azimuth
180 and the back of the head at azimuth 0. A clay render (no textures) shows the same
split, so it is geometry, not a bad texture projection.

It is a **180 degree yaw, not a mirror**. The reconstruction is a learned shape model
conditioned on the orbit views; mirroring is not one of its failure modes, and the
vertical axis is already correct - the mesh stands along glTF +Y with the right height,
it is only the facing that is flipped. A mirror would additionally move the holster to
the other hip and swap the sleeve patch; a yaw keeps them.

The permanent fix belongs in the graph - a core `RotateMesh` node between the final mesh
and `MeshToFile3D` would correct every future run - but its euler angles are documented
as being about "the world axes" without saying whether that world is the Z-up
conditioning frame or the Y-up save frame, and each guess costs a ~14 min validation
run. This tool is the certain, immediate fix and stays useful as a normaliser for
third-party meshes.

Angles are in **Blender space** (Z up), i.e. what you would type after importing the
GLB: yaw about Z, pitch about Y, roll about X.

    blender --background --python tools/glb_orient.py -- <in.glb> <out.glb> [yaw] [pitch] [roll]
"""
import math
import os
import sys

import bpy
from mathutils import Euler, Matrix, Vector

argv = sys.argv[sys.argv.index("--") + 1:]
src = argv[0]
dst = argv[1] if len(argv) > 1 else src.replace(".glb", "-oriented.glb")
yaw = float(argv[2]) if len(argv) > 2 else 180.0
pitch = float(argv[3]) if len(argv) > 3 else 0.0
roll = float(argv[4]) if len(argv) > 4 else 0.0

bpy.ops.wm.read_factory_settings(use_empty=True)

suffix = os.path.splitext(src)[1].lower()
if suffix in (".glb", ".gltf"):
    bpy.ops.import_scene.gltf(filepath=src)
elif suffix == ".fbx":
    bpy.ops.import_scene.fbx(filepath=src)
elif suffix == ".obj":
    bpy.ops.wm.obj_import(filepath=src)
else:
    print("ORIENT: unsupported extension %s" % suffix)
    sys.exit(1)

meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
if not meshes:
    print("ORIENT: no mesh objects imported")
    sys.exit(1)

bpy.ops.object.select_all(action="DESELECT")
for ob in meshes:
    ob.select_set(True)
bpy.context.view_layer.objects.active = meshes[0]
if len(meshes) > 1:
    bpy.ops.object.join()
ob = bpy.context.view_layer.objects.active
# Bake the import transform through the mesh data rather than through
# `bpy.ops.object.transform_apply`. The operator silently did nothing here in
# background mode - the file came back out with a byte-identical bounding box,
# asymmetry included, i.e. unrotated - and it has no return value to check. Rotating
# the vertices directly cannot fail quietly.
ob.data.transform(ob.matrix_world)
ob.matrix_world = Matrix.Identity(4)


def bbox(o):
    lo = Vector((float("inf"),) * 3)
    hi = Vector((float("-inf"),) * 3)
    for v in o.data.vertices:
        for i in range(3):
            lo[i] = min(lo[i], v.co[i])
            hi[i] = max(hi[i], v.co[i])
    return lo, hi


lo0, hi0 = bbox(ob)
print("ORIENT: before  X %.4f..%.4f  Y %.4f..%.4f  Z %.4f..%.4f"
      % (lo0.x, hi0.x, lo0.y, hi0.y, lo0.z, hi0.z))

rot = Euler((math.radians(roll), math.radians(pitch), math.radians(yaw)), "XYZ")
ob.data.transform(rot.to_matrix().to_4x4())
ob.data.update()

lo1, hi1 = bbox(ob)
print("ORIENT: after   X %.4f..%.4f  Y %.4f..%.4f  Z %.4f..%.4f  (yaw %.1f pitch %.1f roll %.1f)"
      % (lo1.x, hi1.x, lo1.y, hi1.y, lo1.z, hi1.z, yaw, pitch, roll))
if abs((hi0.z - lo0.z) - (hi1.z - lo1.z)) > 1e-4:
    print("ORIENT: WARNING - height changed, so this was not a pure yaw")
if abs(hi0.x - hi1.x) < 1e-6 and abs(lo0.x - lo1.x) < 1e-6 and yaw % 360:
    print("ORIENT: WARNING - bounding box did not move, the rotation may not have applied")

bpy.ops.export_scene.gltf(
    filepath=os.path.abspath(dst),
    export_format="GLB",
    use_selection=True,
    export_apply=True,
    export_yup=True,
)
print("ORIENT: wrote %s (%d bytes)" % (dst, os.path.getsize(os.path.abspath(dst))))
