"""Prepare a generated mesh for skinning by rebuilding it as one closed surface.

AI 3D generators (TRELLIS / Pixal3D / Hunyuan3D) emit a *soup of patches*:
hundreds or thousands of disconnected shells with open borders. Blender's
bone-heat skinning solver needs a connected, closed surface, so on such a mesh
it fails on every vertex and every bone ends up with an empty vertex group.
That is what produces the "mesh stretches and goes crooked" symptom when a
rig is applied -- not the animation and usually not the proportions.

This script fixes the geometry, then bakes the original textures onto the new
surface so nothing is lost:

    import -> voxel remesh (one manifold) -> decimate -> unwrap UV
           -> bake baseColor / normal / roughness / metallic -> export GLB

Run:
    blender.exe -b --factory-startup --python tools/blender_rig_prep.py -- \
        --in  path/to/model.glb \
        --out path/to/model_rig_ready.glb

Optional:
    --voxel 0.004     voxel size in metres (auto: height / 210)
    --tris 60000      target triangle count after decimation
    --tex 2048        baked texture resolution
    --keep-source     also export the un-decimated remesh
"""

from __future__ import annotations

import argparse
import os
import sys

import bpy
from mathutils import Vector


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #

def log(msg: str) -> None:
    print("[rigprep] %s" % msg, flush=True)


def parse_args() -> argparse.Namespace:
    argv = sys.argv
    argv = argv[argv.index("--") + 1:] if "--" in argv else []
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="src", required=True)
    ap.add_argument("--out", dest="dst", required=True)
    ap.add_argument("--voxel", type=float, default=0.0)
    ap.add_argument("--tris", type=int, default=60000)
    ap.add_argument("--tex", type=int, default=2048)
    ap.add_argument("--samples", type=int, default=1)
    ap.add_argument("--texdir", default="")
    ap.add_argument("--keep-source", action="store_true")
    return ap.parse_args(argv)


def world_bounds(obj) -> tuple[Vector, Vector]:
    lo = Vector((1e9, 1e9, 1e9))
    hi = Vector((-1e9, -1e9, -1e9))
    mw = obj.matrix_world
    for v in obj.data.vertices:
        p = mw @ v.co
        for i in range(3):
            lo[i] = min(lo[i], p[i])
            hi[i] = max(hi[i], p[i])
    return lo, hi


def tri_count(obj) -> int:
    """Triangle count, not face count.

    Voxel remesh emits quads, so a face count says nothing about the real
    budget. Decimate's ratio is expressed in triangles, which is why the
    ratio has to be derived from this number.
    """
    return sum(len(p.vertices) - 2 for p in obj.data.polygons)


def count_shells(obj) -> int:
    import bmesh

    bm = bmesh.new()
    bm.from_mesh(obj.data)
    bm.faces.ensure_lookup_table()
    seen: set[int] = set()
    shells = 0
    for f in bm.faces:
        if f.index in seen:
            continue
        shells += 1
        stack = [f]
        while stack:
            cur = stack.pop()
            if cur.index in seen:
                continue
            seen.add(cur.index)
            for e in cur.edges:
                for nf in e.link_faces:
                    if nf.index not in seen:
                        stack.append(nf)
    bm.free()
    return shells


def activate(obj) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


def prune_materials() -> None:
    """Drop every material/image we are not using so the GLB stays small."""
    for mat in list(bpy.data.materials):
        if mat.users == 0:
            bpy.data.materials.remove(mat)
    for img in list(bpy.data.images):
        if img.users == 0:
            bpy.data.images.remove(img)


# --------------------------------------------------------------------------- #
# stage 1 - rebuild geometry
# --------------------------------------------------------------------------- #

def rebuild_geometry(obj, voxel: float, tris: int):
    before_faces = len(obj.data.polygons)
    before_tris = tri_count(obj)
    before_shells = count_shells(obj)
    log("source: %d faces / %d tris, %d shells"
        % (before_faces, before_tris, before_shells))

    lo, hi = world_bounds(obj)
    height = hi.z - lo.z
    if voxel <= 0.0:
        voxel = height / 210.0
    log("height %.4f -> voxel size %.5f" % (height, voxel))

    activate(obj)
    obj.data.remesh_voxel_size = voxel
    obj.data.remesh_voxel_adaptivity = 0.0
    try:
        obj.data.use_remesh_fix_poles = True
    except AttributeError:
        pass
    bpy.ops.object.voxel_remesh()

    remeshed_faces = len(obj.data.polygons)
    remeshed_tris = tri_count(obj)
    log("voxel remesh: %d faces / %d tris -> %d faces / %d tris, %d shells"
        % (before_faces, before_tris, remeshed_faces, remeshed_tris,
           count_shells(obj)))

    if tris and remeshed_tris > tris:
        ratio = tris / remeshed_tris
        activate(obj)
        mod = obj.modifiers.new(name="Decimate", type="DECIMATE")
        mod.decimate_type = "COLLAPSE"
        mod.ratio = ratio
        mod.use_collapse_triangulate = True
        bpy.ops.object.modifier_apply(modifier=mod.name)
        log("decimated %d -> %d tris (ratio %.4f)"
            % (remeshed_tris, tri_count(obj), ratio))

    # smooth the voxel stair-stepping a little without eating detail
    activate(obj)
    mod = obj.modifiers.new(name="Smooth", type="SMOOTH")
    mod.factor = 0.5
    mod.iterations = 2
    bpy.ops.object.modifier_apply(modifier=mod.name)

    # floor + centre
    lo, hi = world_bounds(obj)
    shift = Vector((-(lo.x + hi.x) / 2.0, -(lo.y + hi.y) / 2.0, -lo.z))
    obj.location += shift
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
    lo, hi = world_bounds(obj)
    log("bounds: (%.4f, %.4f, %.4f)..(%.4f, %.4f, %.4f)"
        % (lo.x, lo.y, lo.z, hi.x, hi.y, hi.z))
    log("height %.4f  width %.4f  depth %.4f"
        % (hi.z - lo.z, hi.x - lo.x, hi.y - lo.y))


# --------------------------------------------------------------------------- #
# stage 2 - UV unwrap
# --------------------------------------------------------------------------- #

def unwrap(obj) -> None:
    activate(obj)
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.uv.smart_project(angle_limit=1.1519, island_margin=0.003,
                             correct_aspect=True, scale_to_bounds=False)
    bpy.ops.object.mode_set(mode="OBJECT")
    log("unwrapped: %d uv loops over %d faces"
        % (len(obj.data.uv_layers.active.data), len(obj.data.polygons)))


# --------------------------------------------------------------------------- #
# stage 3 - bake textures from the original surface
# --------------------------------------------------------------------------- #

def new_image(name: str, size: int, srgb: bool):
    img = bpy.data.images.new(name, width=size, height=size, alpha=False,
                              float_buffer=False)
    img.colorspace_settings.name = "sRGB" if srgb else "Non-Color"
    return img


def save_image(image, directory: str) -> str:
    """Write a baked image to disk as a real PNG.

    Generated images that only live in memory do not survive the glTF export
    reliably: the sRGB base colour came through, but every Non-Color image
    (normal, roughness, metallic) was embedded as solid black. Giving each bake
    a file on disk makes the exporter read the same bytes we just verified.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "%s.png" % image.name)
    image.filepath_raw = path
    image.file_format = "PNG"
    image.save()
    log("saved %s (%.1f KB)" % (path, os.path.getsize(path) / 1024.0))
    return path


def find_source_sockets(src_mat):
    """Locate the baseColor / normal / roughness / metallic image inputs."""
    nt = src_mat.node_tree
    principled = next((n for n in nt.nodes if n.type == "BSDF_PRINCIPLED"), None)
    if principled is None:
        return None

    def upstream_image(sock):
        """Walk back from a Principled input to the first image texture."""
        if not sock.is_linked:
            return None, None
        link = sock.links[0]
        node = link.from_node
        if node.type == "TEX_IMAGE" and node.image:
            return node.image, None
        if node.type == "SEPARATE_COLOR" and node.inputs[0].is_linked:
            up = node.inputs[0].links[0].from_node
            if up.type == "TEX_IMAGE" and up.image:
                return up.image, link.from_socket.name
        if node.type == "NORMAL_MAP" and node.inputs["Color"].is_linked:
            up = node.inputs["Color"].links[0].from_node
            if up.type == "TEX_IMAGE" and up.image:
                return up.image, None
        return None, None

    out = {}
    for key, sock_name in (("base", "Base Color"), ("rough", "Roughness"),
                           ("metal", "Metallic"), ("normal", "Normal")):
        sock = principled.inputs.get(sock_name)
        if sock is None:
            continue
        img, channel = upstream_image(sock)
        if img is not None:
            out[key] = (img, channel)
    return out


def emission_material(image, channel, name: str):
    """A throw-away material whose Emission colour is one texture channel."""
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    emit = nt.nodes.new("ShaderNodeEmission")
    tex = nt.nodes.new("ShaderNodeTexImage")
    tex.image = image
    emit.inputs["Strength"].default_value = 1.0

    if channel and channel in ("Red", "Green", "Blue"):
        sep = nt.nodes.new("ShaderNodeSeparateColor")
        nt.links.new(tex.outputs["Color"], sep.inputs["Color"])
        nt.links.new(sep.outputs[channel], emit.inputs["Color"])
    else:
        nt.links.new(tex.outputs["Color"], emit.inputs["Color"])

    nt.links.new(emit.outputs["Emission"], out.inputs["Surface"])
    out.location = (300, 0)
    emit.location = (100, 0)
    tex.location = (-100, 0)
    return mat


def setup_bake(extrusion: float) -> None:
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.device = "CPU"
    scene.cycles.samples = 1
    scene.cycles.use_denoising = False
    bake = scene.render.bake
    bake.use_selected_to_active = True
    bake.cage_extrusion = extrusion
    bake.max_ray_distance = extrusion * 3.0
    bake.margin = 8
    bake.use_clear = True
    bake.use_cage = False
    bake.normal_space = "TANGENT"
    bake.target = "IMAGE_TEXTURES"


def image_stats(image, label: str) -> None:
    """Print what actually landed in a baked image.

    A bake can return FINISHED and still leave the target black, so every pass
    is measured instead of trusted. `coverage` is the share of pixels that got
    any colour at all -- a value near 0 means nothing was written.
    """
    import numpy as np

    w, h = image.size
    px = np.array(image.pixels[:], dtype=np.float32).reshape(-1, 4)[:, :3]
    coverage = float((px.max(axis=1) > 0.02).mean())
    log("  %-10s R=%.3f G=%.3f B=%.3f  max=%.2f  coverage=%.1f%%"
        % (label, px[:, 0].mean(), px[:, 1].mean(), px[:, 2].mean(),
           float(px.max()), coverage * 100.0))


def bake_pass(src, dst, dst_mat, image, bake_type: str, label: str) -> bool:
    """Bake one image from src (selected) onto dst (active)."""
    node = dst_mat.node_tree.nodes.get("BAKE_TARGET")
    if node is None:
        node = dst_mat.node_tree.nodes.new("ShaderNodeTexImage")
        node.name = "BAKE_TARGET"
    node.image = image
    node.select = True
    dst_mat.node_tree.nodes.active = node

    bpy.ops.object.select_all(action="DESELECT")
    src.select_set(True)
    dst.select_set(True)
    bpy.context.view_layer.objects.active = dst

    result = bpy.ops.object.bake(type=bake_type, margin=8, use_clear=True,
                                 use_selected_to_active=True)
    log("baked %s -> %dx%d (%s)"
        % (label, image.size[0], image.size[1], result))
    image_stats(image, label)
    return "FINISHED" in result


def split_orm(orm, size: int):
    """Pull roughness (G) and metallic (B) out of a baked ORM image.

    Baking the packed ORM as a plain emission copy and splitting it afterwards
    is far more reliable than baking each channel through its own
    Separate Color node -- that path produced solid black.
    """
    import numpy as np

    w, h = orm.size
    px = np.array(orm.pixels[:], dtype=np.float32).reshape(h, w, 4)
    if size != w:
        step = max(1, w // size)
        px = px[::step, ::step, :][:size, :size, :]

    out = {}
    for key, chan, name in (("rough", 1, "baked_roughness"),
                            ("metal", 2, "baked_metallic")):
        img = new_image(name, px.shape[1], False)
        flat = np.empty((px.shape[0], px.shape[1], 4), dtype=np.float32)
        flat[:, :, 0] = px[:, :, chan]
        flat[:, :, 1] = px[:, :, chan]
        flat[:, :, 2] = px[:, :, chan]
        flat[:, :, 3] = 1.0
        img.pixels.foreach_set(flat.ravel())
        img.update()
        out[key] = img
        image_stats(img, key)
    return out


def bake_textures(src, dst, size: int, texdir: str) -> dict:
    src_mats = [s.material for s in src.material_slots if s.material]
    if not src_mats:
        log("source has no material - skipping bake")
        return {}
    sockets = find_source_sockets(src_mats[0])
    if not sockets:
        log("no Principled BSDF on source - skipping bake")
        return {}
    log("source sockets: %s"
        % {k: (v[0].name, v[1]) for k, v in sockets.items()})

    lo, hi = world_bounds(dst)
    setup_bake(extrusion=(hi.z - lo.z) * 0.012)

    dst_mat = bpy.data.materials.new("RoboBaked")
    dst_mat.use_nodes = True
    nt = dst_mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    for s in dst.material_slots:
        s.material = dst_mat
    if not dst.material_slots:
        dst.data.materials.append(dst_mat)

    result = {}
    original_src_mat = src.material_slots[0].material

    def emit_copy(image, px, srgb, label):
        """Bake a straight copy of one source texture onto the new UVs."""
        tmp = emission_material(image, None, "BakeSrc_%s" % label)
        for s in src.material_slots:
            s.material = tmp
        target = new_image("baked_%s" % label, px, srgb)
        bake_pass(src, dst, dst_mat, target, "EMIT", label)
        save_image(target, texdir)
        for s in src.material_slots:
            s.material = original_src_mat
        bpy.data.materials.remove(tmp)
        return target

    if "base" in sockets:
        result["base"] = emit_copy(sockets["base"][0], size, True, "baseColor")

    orm_entry = sockets.get("rough") or sockets.get("metal")
    if orm_entry is not None:
        orm = emit_copy(orm_entry[0], size, False, "orm")
        result.update(split_orm(orm, size // 2))
        for img in result.values():
            if img.name.startswith("baked_") and not img.filepath:
                save_image(img, texdir)
        bpy.data.images.remove(orm)

    if "normal" in sockets:
        target = new_image("baked_normal", size, False)
        ok = bake_pass(src, dst, dst_mat, target, "NORMAL", "normal")
        if ok:
            save_image(target, texdir)
            result["normal"] = target

    # --- wire the bakes into the destination material --------------------- #
    def hook(image, sock_name, non_color=True):
        node = nt.nodes.new("ShaderNodeTexImage")
        node.image = image
        node.location = (-500, 0)
        if non_color:
            node.image.colorspace_settings.name = "Non-Color"
        nt.links.new(node.outputs["Color"], bsdf.inputs[sock_name])
        return node

    if "base" in result:
        hook(result["base"], "Base Color", non_color=False)
    if "rough" in result:
        hook(result["rough"], "Roughness")
    if "metal" in result:
        hook(result["metal"], "Metallic")
    if "normal" in result:
        nmap = nt.nodes.new("ShaderNodeNormalMap")
        nmap.location = (-250, -400)
        tex = nt.nodes.new("ShaderNodeTexImage")
        tex.image = result["normal"]
        tex.image.colorspace_settings.name = "Non-Color"
        tex.location = (-500, -400)
        nt.links.new(tex.outputs["Color"], nmap.inputs["Color"])
        nt.links.new(nmap.outputs["Normal"], bsdf.inputs["Normal"])

    for node in list(nt.nodes):
        if node.name == "BAKE_TARGET":
            nt.nodes.remove(node)

    return result


# --------------------------------------------------------------------------- #
# stage 4 - export
# --------------------------------------------------------------------------- #

def export(path: str) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.export_scene.gltf(
        filepath=path,
        export_format="GLB",
        use_selection=True,
        export_apply=True,
        export_yup=True,
        export_image_format="AUTO",
        export_texture_dir="",
        export_normals=True,
        export_tangents=False,
        export_materials="EXPORT",
    )
    log("wrote %s (%.2f MB)" % (path, os.path.getsize(path) / 1048576.0))


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def main() -> int:
    args = parse_args()
    if not os.path.isfile(args.src):
        log("ERROR: no such file %s" % args.src)
        return 2

    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=args.src)
    meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
    if not meshes:
        log("ERROR: no mesh in %s" % args.src)
        return 2
    if len(meshes) > 1:
        log("merging %d mesh objects into one" % len(meshes))
        activate(meshes[0])
        for other in meshes[1:]:
            other.select_set(True)
        bpy.ops.object.join()
    src = bpy.context.view_layer.objects.active
    src.name = "RoboSource"

    # the untouched original stays around as the bake source
    dst = src.copy()
    dst.data = src.data.copy()
    dst.name = "RoboRig"
    bpy.context.collection.objects.link(dst)

    rebuild_geometry(dst, args.voxel, args.tris)
    unwrap(dst)
    texdir = args.texdir or os.path.join(os.path.dirname(os.path.abspath(args.dst)),
                                         "_rigprep_tex")
    bake_textures(src, dst, args.tex, texdir)
    prune_materials()

    # remove the high-poly bake source from the scene before exporting
    bpy.data.objects.remove(src, do_unlink=True)
    bpy.context.view_layer.objects.active = dst
    dst.select_set(True)

    export(args.dst)

    lo, hi = world_bounds(dst)
    log("final: %d tris, %d shells, height %.4f, feet at %.4f"
        % (tri_count(dst), count_shells(dst), hi.z - lo.z, lo.z))
    return 0


if __name__ == "__main__":
    sys.exit(main())
