# Splitting a monolithic .blend into GLB parts with explicit pivots

## When to use

A downloaded/modelled car, weapon, machine or character arrives as **one mesh object with
several material slots**. In the browser you want each logical part to move on its own -
detach, explode, swap. A single mesh cannot do that: three.js transforms whole `Object3D`s,
not face groups. So the split must happen **before** export, in Blender, and the resulting
GLB must carry one node per part with a **correct pivot**.

Do not try to split at runtime in the browser. Index ranges are fragile, materials are
merged by the glTF exporter, and there is no way to reconstruct a hinge axis from vertex
data alone.

## Hard-won rules

1. **Split by `polygon.material_index`, not by loose parts.** Converted models usually have
   every panel welded into one shell; `bmesh.ops.split_edges` / "separate by loose parts"
   yields one blob. Materials are the only reliable semantic grouping that survived the
   original authoring.
2. **When a material spans two logical parts, split it geometrically.** Example: `Red Lights`
   covers both the rear cluster and the front markers. Split the face list on world-space Y
   (`face_center_world(...).y > 0.30` → front). Same trick separates left/right wheels
   (`x * sign > 0`) and the two pop-up headlight pods.
3. **Rebase geometry so the object origin is the pivot.** After the split, subtract the
   pivot from every vertex in **world space**. The node then lives at the pivot in the GLB
   and rotates about the right point with zero extra code in the browser.
4. **Pivot choice is the whole game.**
   - wheel → centre of the rim bbox (not the tyre, not the mesh origin);
   - pop-up headlight pod → the **hinge**: rear edge (`y_min`) at the top surface (`z_max`),
     X at the pod's own centre;
   - everything else → bbox centre of its own faces.
5. **Delete coincident duplicate shells.** Converted models often carry doubled geometry:
   two faces with identical vertices. Inside one mesh that is invisible; once the body is
   split into separate meshes the two copies z-fight and panel seams render as **dashed
   lines**. Remove faces whose sorted, rounded vertex tuple already exists *and* whose
   normal points the same way.
6. **Parent the parts to an Empty at the pivot** when the part is a group (wheel = tyre +
   rim + disc; headlight = housing + lens + cover). The Empty is the transform handle;
   children inherit it. In the GLB this becomes a parent node - three.js `attach()`es
   children to it and rotating the parent rotates the whole assembly.
7. **Blender is Z-up, glTF is Y-up.** Convert with `to_gl(v) = [v.x, v.z, -v.y]`. Do this
   for the manifest (pivots, bboxes) and let `export_yup=True` handle the mesh data.

## Headless run

```bat
blender.exe -b "source/Toyota Corolla AE86.blend" -P tools/export_parts.py -- build/ae86.glb build/parts.json
```

`-b` (background) means no GUI, no scene file is saved, the script runs and Blender exits.
Arguments after `--` are read with `sys.argv[sys.argv.index("--") + 1:]`.

## Core helper - carve a part out of a source mesh

```python
import bpy, bmesh
from mathutils import Vector, Matrix

def group_by_material(ob):
    """material name -> list of polygon indices"""
    g = {}
    for p in ob.data.polygons:
        mat = ob.data.materials[p.material_index]
        g.setdefault(mat.name if mat else "_none", []).append(p.index)
    return g

def face_center_world(ob, fi):
    mw = ob.matrix_world
    vs = ob.data.polygons[fi].vertices
    acc = Vector((0, 0, 0))
    for vi in vs:
        acc += mw @ ob.data.vertices[vi].co
    return acc / len(vs)

def make_part(src, faces, mat_name, name, pivot, parent=None):
    """New mesh object holding only `faces`, geometry rebased so origin == pivot (world space)."""
    bm = bmesh.new()
    bm.from_mesh(src.data)
    bm.verts.ensure_lookup_table()
    bm.faces.ensure_lookup_table()
    keep = set(faces)
    bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.index not in keep], context='FACES')

    # drop coincident opposite duplicate shells (they z-fight once split)
    bm.faces.ensure_lookup_table()
    seen, dupes = {}, []
    for f in bm.faces:
        key = tuple(sorted(tuple(round(c, 5) for c in v.co) for v in f.verts))
        prev = seen.get(key)
        if prev is None:
            seen[key] = f
        elif prev.normal.dot(f.normal) > 0.5:
            dupes.append(f)
    if dupes:
        bmesh.ops.delete(bm, geom=dupes, context='FACES')

    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()

    mw = src.matrix_world
    for v in me.vertices:
        v.co = (mw @ v.co) - pivot          # <-- origin becomes the pivot

    mat = bpy.data.materials.get(mat_name)
    if mat:
        me.materials.append(mat)

    ob = bpy.data.objects.new(name, me)
    bpy.context.scene.collection.objects.link(ob)
    if parent is not None:
        ob.parent = parent
        ob.matrix_parent_inverse = Matrix.Identity(4)
    ob.matrix_world = Matrix.Translation(pivot)
    return ob

def make_empty(name, pivot):
    e = bpy.data.objects.new(name, None)
    e.empty_display_type = 'PLAIN_AXES'
    e.empty_display_size = 0.05
    bpy.context.scene.collection.objects.link(e)
    e.matrix_world = Matrix.Translation(pivot)
    return e

def to_gl(v):
    """Blender Z-up world -> glTF/three.js Y-up."""
    return [round(v[0], 5), round(v[2], 5), round(-v[1], 5)]
```

`matrix_parent_inverse = Matrix.Identity(4)` is mandatory. Blender otherwise stores an
inverse of the parent transform and the child lands somewhere else entirely.

## Deriving a wheel pivot from the rim

The rim is the most symmetric sub-mesh, so its bbox centre *is* the hub. Derive it before
creating the parts, then reuse the same pivot for tyre, rim and disc:

```python
WHEEL_SRC = {'FL': (FL, -1), 'FR': (FR, 1), 'RL': (RW, -1), 'RR': (RW, 1)}
WMAT = {'Tire': 'tire', 'Rims': 'rim', 'Disk': 'disc'}

hub = {}
for key, (src, sign) in WHEEL_SRC.items():
    g = group_by_material(src)
    for mat, suffix in WMAT.items():
        if mat not in g:
            continue
        side = [fi for fi in g[mat] if face_center_world(src, fi).x * sign > 0]
        if side and suffix == 'rim':
            mn, mx = bbox_of_faces(src, side)
            hub[key] = (mn + mx) * 0.5
```

## Deriving a pop-up headlight hinge

The hinge is the **rear-top edge of the pod**. `y_min` is the rearmost point, `z_max` the
top surface; X is the pod's own centre so left and right rotate about parallel axes.

```python
lg = group_by_material(LIGHTS)
lg_min, lg_max = bbox_of_faces(LIGHTS, [i for v in lg.values() for i in v])
hinge_y, hinge_z = lg_min.y, lg_max.z

for key, sign in (('L', -1), ('R', 1)):
    faces = [fi for v in lg.values() for fi in v
             if face_center_world(LIGHTS, fi).x * sign > 0]
    mn, mx = bbox_of_faces(LIGHTS, faces)
    piv = Vector(((mn.x + mx.x) * 0.5, hinge_y, hinge_z))
    parent = make_empty('headlight_' + key, piv)
    # ... create housing / lens / cover with parent=parent
```

Then in the browser `headlight_L.rotation.x = +50°` *opens* the lights. Verify the sign by
rendering candidate hinges - a 6-candidate sweep rendered headless is faster than guessing:

```python
# tools/test_popup.py - render 6 hinge candidates to tools/_popup/
for i, (hy, hz) in enumerate(candidates):
    ...  # set pod rotation, Workbench render, save
```

## Manifest alongside the GLB

The GLB alone loses the semantics: which node is a wheel, what it may be swapped for, where
its pivot is. Emit a JSON manifest in the same run:

```python
rec = {
    "id": name, "material": mat, "role": role, "swap": swap,
    "pivot": to_gl(piv), "bbox": [to_gl(mn), to_gl(mx)], "size": to_gl(mx - mn),
    "parent": None,
}
```

`role` (`shell` / `panel` / `glass` / `wheel` / `light` / `detail` / `pivot`) drives
grouping and default explode direction; `swap` (`paint` / `paint2` / `rim` / `lens` /
`glass` / `exhaust` / `plate`) tells the UI which category of variants applies to the part;
`parent` lets the loader skip nested children when building the movable set.

Also dump the Principled BSDF values per material so the web app can rebuild materials with
full PBR fidelity:

```python
b = next((n for n in m.node_tree.nodes if n.type == 'BSDF_PRINCIPLED'), None)
mats[m.name] = {
    "color": [round(float(x), 4) for x in b.inputs["Base Color"].default_value],
    "metallic": round(float(b.inputs["Metallic"].default_value), 3),
    "roughness": round(float(b.inputs["Roughness"].default_value), 3),
    "alpha": round(float(b.inputs["Alpha"].default_value), 3),
    "emissive": [round(float(x), 4) for x in b.inputs["Emission Color"].default_value],
    "emissiveIntensity": round(float(b.inputs["Emission Strength"].default_value), 3),
}
```

## Export

```python
for ob in list(bpy.data.objects):
    if ob not in created:                 # keep only the split parts + empties
        bpy.data.objects.remove(ob, do_unlink=True)

bpy.context.view_layer.update()
kw = dict(filepath=OUT_GLB, export_format='GLB', use_selection=False,
          export_apply=True, export_yup=True, export_materials='EXPORT',
          export_cameras=False, export_lights=False, export_extras=True)
try:
    bpy.ops.export_scene.gltf(**kw)
except TypeError as e:                     # older Blender without export_extras
    kw.pop('export_extras', None)
    bpy.ops.export_scene.gltf(**kw)
```

`export_apply=True` bakes modifiers (mirrors, subdivision) into the exported mesh.
`use_selection=False` exports everything still in the file, which after the cleanup pass is
exactly the parts plus the pivot empties.

## Verifying the result without a browser

Parse the GLB's JSON chunk directly - no loader needed:

```js
// tools/glb_info.js
const buf = fs.readFileSync(glb);
const jsonLen = buf.readUInt32LE(12);
const json = JSON.parse(buf.subarray(20, 20 + jsonLen).toString('utf8'));
// print node tree, parents, translations, mesh tri counts
```

Expected sanity output for a car split by material:

```text
PARTS 30 -> build/ae86.glb
DEDUP: removed 2 coincident faces across 30 parts
```

30 nodes, ~2.3 MB GLB, ~30 k tris. If `DEDUP` reports hundreds of faces, the source model
was authored with intentional doubled shells (thin panels modelled as two coincident
surfaces) - in that case **disable** the dedup pass for those parts, or the panel becomes
single-sided and disappears when viewed from behind.

## Pitfalls

| Symptom | Cause |
|---|---|
| Dashed panel seams in the browser | Coincident duplicate shells survived the split; z-fighting |
| Part rotates about the wrong point | Pivot not rebased into the geometry; object origin still at the mesh centre |
| Child part jumps on export | `matrix_parent_inverse` not reset to identity |
| Wheels double up on one side | Side filter used the local, not world-space X |
| Pop-up lights rotate the wrong way | Hinge picked on the front edge; use `y_min` (rear) |
| Red lights: front markers stuck in the rear cluster | Material split not refined by Y |
| Panel disappears from behind | Dedup removed a legitimately doubled thin shell |
