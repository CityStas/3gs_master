"""Convert a GLB into a rig-ready FBX for AccuRIG / Mesh2Motion.

Usage:
    blender --background --python glb_to_rig_ready_fbx.py -- <in.glb> <out.fbx> [merge_mm] [min_shell_frac]

What "rig-ready" means here, and why each step exists:

1. gltfpack splits vertices at every UV/normal seam, so the naive vertex graph
   of our exported GLB reports ~2000 disconnected islands. Auto-riggers walk
   that graph to place joints, so it has to be welded first. Merging by distance
   welds the surface without touching UVs, because Blender stores UVs per loop
   and not per vertex.
2. The FBX exporter is asked for centimetre units and a single mesh object,
   which is what AccuRIG expects on import.
3. Anything that is not a mesh (empties, lights, cameras) is dropped, so the
   importer sees one clean object instead of a hierarchy it has to untangle.
4. `min_shell_frac` (default 0 = keep everything) drops shells smaller than that
   fraction of the total vertex count. The image->3D reconstruction leaves one
   buried interior flap behind (360 of 229800 verts). It is invisible - measured
   at 4 changed pixels out of 490000 over four views - but an auto-rigger skins
   each shell separately, so it is a stray bone waiting to happen. Dropping a
   shell cannot open a hole in the main surface, because it was never connected
   to it. Pass e.g. 0.01 to enable.
"""
import os
import sys

import bpy

argv = sys.argv[sys.argv.index("--") + 1:]
src = argv[0]
dst = argv[1]
merge_mm = float(argv[2]) if len(argv) > 2 else 0.5
min_shell_frac = float(argv[3]) if len(argv) > 3 else 0.0

os.makedirs(os.path.dirname(os.path.abspath(dst)), exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=src)

meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
if not meshes:
    print("CONVERT: no mesh imported from %s" % src)
    sys.exit(1)

# Drop everything that is not a mesh.
for ob in list(bpy.context.scene.objects):
    if ob.type != "MESH":
        bpy.data.objects.remove(ob, do_unlink=True)

before_v = sum(len(o.data.vertices) for o in meshes)
before_f = sum(len(o.data.polygons) for o in meshes)
print("CONVERT: imported %d mesh object(s), %d verts, %d faces"
      % (len(meshes), before_v, before_f))


def island_sizes(ob):
    """Connected components over the edge graph, as a list of vertex counts."""
    parent = list(range(len(ob.data.vertices)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for e in ob.data.edges:
        a, b = find(e.vertices[0]), find(e.vertices[1])
        if a != b:
            parent[a] = b

    counts = {}
    for i in range(len(ob.data.vertices)):
        r = find(i)
        counts[r] = counts.get(r, 0) + 1
    return sorted(counts.values(), reverse=True)


def island_count(ob):
    return len(island_sizes(ob))


def describe_islands(ob, total_v):
    sizes = island_sizes(ob)
    head = ", ".join(str(s) for s in sizes[:6])
    more = "" if len(sizes) <= 6 else " (+%d more)" % (len(sizes) - 6)
    print("CONVERT: islands = %d, sizes: %s%s" % (len(sizes), head, more))
    if len(sizes) > 1:
        biggest = sizes[0] / float(total_v) if total_v else 0.0
        print("CONVERT: largest island holds %.1f%% of the vertices" % (biggest * 100))
    return sizes


if len(meshes) > 1:
    bpy.ops.object.select_all(action="DESELECT")
    for ob in meshes:
        ob.select_set(True)
    bpy.context.view_layer.objects.active = meshes[0]
    bpy.ops.object.join()
    meshes = [bpy.context.view_layer.objects.active]

ob = meshes[0]
bpy.context.view_layer.objects.active = ob
ob.select_set(True)

print("CONVERT: before weld ->")
describe_islands(ob, len(ob.data.vertices))

bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="SELECT")
bpy.ops.mesh.remove_doubles(threshold=merge_mm / 1000.0)
bpy.ops.mesh.normals_make_consistent(inside=False)
bpy.ops.object.mode_set(mode="OBJECT")

after_v = len(ob.data.vertices)
print("CONVERT: weld %.2f mm -> %d verts (was %d)" % (merge_mm, after_v, before_v))
sizes = describe_islands(ob, after_v)

if min_shell_frac > 0 and len(sizes) > 1:
    threshold = max(1, int(after_v * min_shell_frac))
    doomed = [s for s in sizes if s < threshold]
    if doomed:
        # Rebuild the island membership, then delete every vertex that is not in a
        # shell at or above the threshold.
        parent = list(range(len(ob.data.vertices)))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for e in ob.data.edges:
            a, b = find(e.vertices[0]), find(e.vertices[1])
            if a != b:
                parent[a] = b
        groups = {}
        for i in range(len(ob.data.vertices)):
            groups.setdefault(find(i), []).append(i)
        keep = set()
        for idxs in groups.values():
            if len(idxs) >= threshold:
                keep.update(idxs)
        kill = [i for i in range(len(ob.data.vertices)) if i not in keep]
        print("CONVERT: dropping %d shell(s) below %d verts -> removing %d verts"
              % (len(doomed), threshold, len(kill)))
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="DESELECT")
        bpy.ops.object.mode_set(mode="OBJECT")
        for i in kill:
            ob.data.vertices[i].select = True
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.delete(type="VERT")
        bpy.ops.object.mode_set(mode="OBJECT")
        print("CONVERT: after drop -> %d verts %d faces"
              % (len(ob.data.vertices), len(ob.data.polygons)))
        sizes = describe_islands(ob, len(ob.data.vertices))

if len(sizes) > 1:
    print("CONVERT: NOTE - %d shells remain. For a hard-surface robot that is "
          "expected (head / limbs are separate castings); for an organic "
          "character it means real holes. An auto-rigger skins each shell "
          "separately, so check them in the viewport before trusting the result."
          % len(sizes))

# AccuRIG expects a sane, visible, transform-free object.
ob.name = os.path.splitext(os.path.basename(src))[0]
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

bpy.ops.export_scene.fbx(
    filepath=dst,
    use_selection=True,
    object_types={"MESH"},
    global_scale=1.0,
    apply_unit_scale=True,
    apply_scale_options="FBX_SCALE_NONE",
    path_mode="COPY",
    embed_textures=True,
    mesh_smooth_type="FACE",
    use_mesh_modifiers=True,
    bake_space_transform=False,
)
print("CONVERT: wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))
