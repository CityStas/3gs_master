---
name: EditableMesh
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "Object which allows for the runtime creation and manipulation of meshes."
---

# Class: EditableMesh

> Object which allows for the runtime creation and manipulation of meshes.

## Description

`EditableMesh` changes the applied visual mesh when linked to a
[MeshPart](/docs/reference/engine/classes/MeshPart.md), allowing for querying and modification of the mesh both in
Studio and in-game.

#### Enabling for published games

For security purposes, using `EditableMesh` fails by default in published
games. To enable it, open the
[Creator Dashboard](https://create.roblox.com/dashboard/creations), go to the
game's **Configure**&nbsp;⟩ **Settings**, and toggle on **Enable Mesh / Image
APIs**. Alternatively, in Studio, open **Experience Settings** and toggle on
**Allow Mesh / Image APIs** under **Security**. Remember to review the
[Terms of Use](https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use#creators-restrictions-on-use)
before enabling the toggle.

#### Permissions

To prevent misuse, [AssetService:CreateEditableMeshAsync()](/docs/reference/engine/classes/AssetService.md) only allows
you to load and edit mesh assets if any of the following is true:

- Owned by or explicitly shared with the game owner.
- Owned by or explicitly shared with the logged in Studio user.
- Owned by or explicitly shared with the logged in player if the
  `EditableMesh` is on the client side.
- Owned by a group where the game owner, Studio user, or player has a role
  with permission to edit the group's assets. See
  [Roles and permissions](/docs/en-us/projects/groups.md#roles-and-permissions)
  for more information.

See [Grant permissions](/docs/en-us/projects/assets/privacy.md#grant-permissions)
to learn how to share assets with users or groups.

The APIs throw an error if they are used to load an asset that does not meet
the criteria above.

#### Memory limits

Editable assets are currently expensive for memory usage. To minimize its
impact on client performance, `EditableMesh` has strict client-side memory
budgets, although the server, Studio, and plugins operate with unlimited
memory. Using [FixedSize](/docs/reference/engine/classes/EditableMesh.md) may help you stay
within the memory budget and, in some scenarios, linking one `EditableMesh` to
multiple [MeshParts](/docs/reference/engine/classes/MeshPart.md) (multi-referencing) can help with memory
optimization.

#### Creation and display

An `EditableMesh` can be created from an existing [Content](/docs/reference/engine/datatypes/Content.md) of a
[MeshPart](/docs/reference/engine/classes/MeshPart.md) or a mesh ID using
[AssetService:CreateEditableMeshAsync()](/docs/reference/engine/classes/AssetService.md), or a blank `EditableMesh` can
be created with [AssetService:CreateEditableMesh()](/docs/reference/engine/classes/AssetService.md). It can then be
displayed, modified, and its collision model updated. Not all of the steps are
necessary; for example, you might want to create an `EditableMesh` just to
raycast without ever displaying it.

```lua
local AssetService = game:GetService("AssetService")

-- Create empty EditableMesh
local editableMesh = AssetService:CreateEditableMesh()

-- Create EditableMesh from asset ID
local editableMeshFromAsset = nil
local success, errorMessage = pcall(function()
	editableMeshFromAsset = AssetService:CreateEditableMeshAsync(Content.fromAssetId(ASSET_ID))
end)

-- Create EditableMesh from another EditableMesh
local editableMeshFromAnother = nil
local success, errorMessage = pcall(function()
	editableMeshFromAnother = AssetService:CreateEditableMeshAsync(Content.fromObject(OTHER_EDITABLE_MESH))
end)

-- Create EditableMesh from MeshPart
local editableMeshFromMeshPart = nil
local success, errorMessage = pcall(function()
	editableMeshFromMeshPart = AssetService:CreateEditableMeshAsync(MESH_PART.MeshContent)
end)
```

An `EditableMesh` is displayed when it's linked to a new [MeshPart](/docs/reference/engine/classes/MeshPart.md),
through [AssetService:CreateMeshPartAsync()](/docs/reference/engine/classes/AssetService.md). You can create more
[MeshPart](/docs/reference/engine/classes/MeshPart.md) instances that reference the same `EditableMesh`
[Content](/docs/reference/engine/datatypes/Content.md), or link to an existing [MeshPart](/docs/reference/engine/classes/MeshPart.md) through
[MeshPart:ApplyMesh()](/docs/reference/engine/classes/MeshPart.md).

```lua
local AssetService = game:GetService("AssetService")
local Workspace = game:GetService("Workspace")

-- Create EditableMesh from asset ID
local editableMeshFromAsset = nil
local success, errorMessage = pcall(function()
	editableMeshFromAsset = AssetService:CreateEditableMeshAsync(Content.fromAssetId(ASSET_ID))
end)

-- Create new MeshPart linked to the EditableMesh
local newMeshPart = nil
local success, errorMessage = pcall(function()
	newMeshPart = AssetService:CreateMeshPartAsync(Content.fromObject(editableMeshFromAsset))
end)

-- Alternatively, link the new MeshPart created above to an existing MeshPart
local existingMeshPart = Workspace:FindFirstChild("EXISTING_MESH_PART")
existingMeshPart:ApplyMesh(newMeshPart)
```

To recalculate collision and fluid geometry after editing, you can again call
[AssetService:CreateMeshPartAsync()](/docs/reference/engine/classes/AssetService.md) and [MeshPart:ApplyMesh()](/docs/reference/engine/classes/MeshPart.md) to
update an existing [MeshPart](/docs/reference/engine/classes/MeshPart.md). It's generally recommended to do this at
the end of a conceptual edit, not after individual calls to methods that
manipulate geometry. Visual changes to the mesh will always be immediately
reflected by the engine, without the need to call
[AssetService:CreateMeshPartAsync()](/docs/reference/engine/classes/AssetService.md).

#### Fixed-size meshes

When creating an `EditableMesh` from an existing mesh asset (via
[AssetService:CreateEditableMeshAsync()](/docs/reference/engine/classes/AssetService.md)), the resulting editable mesh
is fixed-size by default. Fixed-size meshes are more efficient in terms of
memory but you cannot change the number of vertices, faces, or attributes.
Only the values of vertex attributes and positions can be edited.

```lua
local AssetService = game:GetService("AssetService")

-- Create EditableMesh without fixed-size default
local editableMeshFromAsset = nil
local success, errorMessage = pcall(function()
	editableMeshFromAsset = AssetService:CreateEditableMeshAsync(Content.fromAssetId(ASSET_ID), {FixedSize = false})
end)
```

#### Stable IDs

Many `EditableMesh` methods take **vertex**, **normal**, **UV**, **color** and
**face** IDs. These are represented as integers in Luau but they require some
special handling. The main difference is that IDs are stable and they remain
the same even if other parts of the mesh change. For example, if an
`EditableMesh` has five vertices `{1, 2, 3, 4, 5}` and you remove vertex `4`,
the new vertices will be `{1, 2, 3, 5}`.

Note that the IDs are not guaranteed to be in order and there may be holes in
the numbering, so when iterating through vertices or faces, you should iterate
through the table returned by [GetVertices()](/docs/reference/engine/classes/EditableMesh.md)
or [GetFaces()](/docs/reference/engine/classes/EditableMesh.md).

For debugging purposes, it can be very helpful to get a more readable string
for a stable ID with [IdDebugString()](/docs/reference/engine/classes/EditableMesh.md).

#### Split vertex attributes

A **vertex** is a corner of a face, and topologically connects faces together.
Each vertex has a single **position**, while its **normal**, **UV
coordinate**, and **color** (with transparency) are stored per face corner. A
vertex shared by multiple faces can use the same values on every face, or
different values on each.

Sometimes it's useful for all faces that touch a vertex to use the same
attribute values, but sometimes you'll want different faces to use different
attribute values on the same vertex. For example, on a smooth sphere, each
vertex will only have a single normal. In contrast, at the corner of a cube,
the vertex will have 3 different normals (one for each adjacent face). You can
also have seams in the UV coordinates or sharp changes in the vertex colors.

When creating faces with [AddFace()](/docs/reference/engine/classes/EditableMesh.md) or
[AddTriangle()](/docs/reference/engine/classes/EditableMesh.md), each corner of the new face
is automatically assigned a normal, UV, and color attribute. If a vertex
already belongs to an existing face, the new face **reuses** that vertex's
existing attributes (producing smooth shading and continuous UVs). If the
vertex is new, fresh attribute IDs are created with default values
(auto-computed normal, UV of `(0, 0)`, white color). To create a seam, you
should create new attributes and set them on the face. For example, this code
will create a sharp cube:

```lua
local AssetService = game:GetService("AssetService")

-- Given 4 vertex IDs, adds a new normal and a quad face, making a sharp quad
local function addSharpQuad(editableMesh, vid0, vid1, vid2, vid3)
	local nid = editableMesh:AddNormal() -- This creates a normal ID which is automatically computed

	local fid = editableMesh:AddFace(vid0, vid1, vid2, vid3)
	editableMesh:SetFaceNormals(fid, {nid, nid, nid, nid})
end

-- Makes a cube with creased edges between the 6 sides
local function makeSharpCube()
	local editableMesh = AssetService:CreateEditableMesh()

	local v1 = editableMesh:AddVertex(Vector3.new(0, 0, 0))
	local v2 = editableMesh:AddVertex(Vector3.new(1, 0, 0))
	local v3 = editableMesh:AddVertex(Vector3.new(0, 1, 0))
	local v4 = editableMesh:AddVertex(Vector3.new(1, 1, 0))
	local v5 = editableMesh:AddVertex(Vector3.new(0, 0, 1))
	local v6 = editableMesh:AddVertex(Vector3.new(1, 0, 1))
	local v7 = editableMesh:AddVertex(Vector3.new(0, 1, 1))
	local v8 = editableMesh:AddVertex(Vector3.new(1, 1, 1))

	addSharpQuad(editableMesh, v5, v6, v8, v7) -- Front
	addSharpQuad(editableMesh, v1, v3, v4, v2) -- Back
	addSharpQuad(editableMesh, v1, v5, v7, v3) -- Left
	addSharpQuad(editableMesh, v2, v4, v8, v6) -- Right
	addSharpQuad(editableMesh, v1, v2, v6, v5) -- Bottom
	addSharpQuad(editableMesh, v3, v7, v8, v4) -- Top

	editableMesh:RemoveUnused()
	return editableMesh
end
```

#### Winding

Mesh faces have a front side and a back side. When drawing meshes, only the
front of the faces are drawn by default, although you can change this by
setting the mesh' [DoubleSided](/docs/reference/engine/classes/MeshPart.md) property to `true`.

The order of the vertices around the face determines whether you are looking
at the front or the back. The front of the face is visible when the vertices
go counterclockwise around it.

![Order of the vertices around the face](../../../assets/engine-api/classes/EditableMesh/Winding.png)

#### FACS poses

Animatable heads use the Facial Action Coding System (FACS). See the
[FACS poses reference](/docs/en-us/avatar/dynamic-heads/facs-poses-reference.md)
for helpful information when using
[GetFacsPoses()](/docs/reference/engine/classes/EditableMesh.md) and similar methods.

Each FACS pose is specified by an [FacsActionUnit](/docs/reference/engine/enums/FacsActionUnit.md) value. For the FACS
pose, virtual bones can each have a [CFrame](/docs/reference/engine/datatypes/CFrame.md) that transforms the
bones' initial [CFrame](/docs/reference/engine/datatypes/CFrame.md) in the bind pose of the mesh into the
[CFrame](/docs/reference/engine/datatypes/CFrame.md) for that FACS action unit's pose. All bone
[CFrames](/docs/reference/engine/datatypes/CFrame.md) are in the mesh's local space.

These FACS poses are blended together during animation. Sometimes, the
blending of the base poses produces poor results. In those cases, you can
override the blending of specific combinations of base poses with a
[corrective pose](/docs/en-us/art/characters/facial-animation/create-basic-heads.md#combination-poses)
that is more pleasing. A corrective pose is specified by 2 or 3
[FacsActionUnit](/docs/reference/engine/enums/FacsActionUnit.md) values. Like a base FACS pose, for a corrective pose,
virtual bones can each have a [CFrame](/docs/reference/engine/datatypes/CFrame.md) that transforms the bones'
initial [CFrame](/docs/reference/engine/datatypes/CFrame.md) in the bind pose of the mesh into the
[CFrame](/docs/reference/engine/datatypes/CFrame.md) for that FACS corrective.

Please note that corrective poses that operate on both left and right action
units are not currently expressible. For example, using `LeftCheekPuff` and
`RightEyeClosed` together in a corrective pose is not currently possible.

#### Batching

The **batch** methods let you create, read, update, and remove many mesh
elements in a single call instead of invoking the singular methods
([AddVertex()](/docs/reference/engine/classes/EditableMesh.md),
[SetPosition()](/docs/reference/engine/classes/EditableMesh.md),
[GetColor()](/docs/reference/engine/classes/EditableMesh.md), and so on) once per element.
Batching your mesh operations is typically much more performant than handling
them one by one.

Rather than one method per attribute, each batch method shares a small set of
general entry points and uses an [MeshAttribute](/docs/reference/engine/enums/MeshAttribute.md) value (or the type
already encoded in each mesh ID) to determine which attribute you mean. For
example, [BatchSetValues()](/docs/reference/engine/classes/EditableMesh.md) sets positions
when called with vertex IDs, but sets normals when called with normal IDs. You
cannot mix-and-match ID types within a single call.

Batch setters take parallel arrays: element `i` of every argument array
describes the same logical operation. In
[BatchSetValues(ids, values)](/docs/reference/engine/classes/EditableMesh.md), `values[i]`
is written to `ids[i]`. All argument arrays must be the same length or the
call errors. Batch getters take an array of IDs and return results in the same
order.

If a mesh ID is invalid, batching still applies updates to all elements before
the invalid ID, then stops.

#### Limitations

`EditableMesh` currently has a limit of 60,000 vertices and 20,000 triangles.
Faces can be triangles or quads, and each quad counts as 2 triangles toward
the triangle limit. Attempting to add too many vertices or triangles will
cause an error.

## Properties

### Property: EditableMesh.FixedSize

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "DynamicGeneration"
  ]
}
```

Fixed-sized meshes allow changing the values of vertex attributes but do
not allow vertices and faces to be added or deleted.

## Methods

### Method: EditableMesh:AddBone

**Signature:** `EditableMesh:AddBone(boneProperties: Dictionary): int64`

Adds a new bone to the mesh and returns a bone ID that persists across
topology changes. An error is thrown if the bone name is already in use,
the parent ID is invalid, or the mesh already contains the maximum number
of bones.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `boneProperties` | `Dictionary` |  | Options table containing bone parameters:  - `Name` — A string that specifies the bone name. Note that all bone   names in a mesh must be unique, and the maximum length is 100   characters. - `ParentId` — Optional bone ID of the new bone's parent. - `CFrame` — Initial [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the bone in the bind pose of   the mesh, in the mesh's local space. - `Virtual` — Boolean that specifies whether this bone is virtual.   Virtual bones can only be bound to a [FaceControls](/docs/reference/engine/classes/FaceControls.md) instance. |

**Returns:** `int64` — Bone ID of the new bone.

### Method: EditableMesh:AddColor

**Signature:** `EditableMesh:AddColor(color: Color3, alpha: float): int64`

Adds a new vertex color attribute to the mesh and returns a color ID.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `color` | `Color3` |  | The new color. |
| `alpha` | `float` |  | The color alpha (transparency). `0` is fully transparent, and `1` is fully opaque. |

**Returns:** `int64` — Color ID of the new color.

### Method: EditableMesh:AddFace

**Signature:** `EditableMesh:AddFace(vertexIds: Tuple): int64`

Adds a new face from the given vertex IDs and returns a stable face ID. A
face is either a **triangle** (3 vertex IDs) or a **quad** (4 vertex IDs);
any other count throws an error. For adding triangles specifically, this
method is equivalent to [AddTriangle()](/docs/reference/engine/classes/EditableMesh.md).

For rendering and collision, each quad is internally split into 2
triangles, so a quad counts as 2 triangles toward the mesh's triangle
limit.

#### Automatic attribute assignment

`AddFace()` only takes vertex IDs as arguments. For each vertex of the new
face, it automatically assigns normal, UV, and color attributes using the
following logic:

- If the vertex **already belongs to another face**, the new face corner
  **reuses** the same normal, UV, and color IDs from the existing face.
  This produces smooth shading and continuous UVs across adjacent faces by
  default.
- If the vertex **does not yet belong to any face**, new normal, UV, and
  color IDs are created with default values (auto-computed normal, UV
  coordinate of `(0, 0)`, and white color).

![Two adjacent faces sharing vertex attribute IDs at their common vertices](../../../assets/engine-api/classes/EditableMesh/Shared-Attributes.png)

#### Overriding attributes after adding a face

The auto-assigned attributes can be customized after adding a face. The
approach depends on whether you want to change attribute **values** while
keeping the topology intact, or create entirely new attribute IDs to add
or remove **seams** between faces.

**To change values in-place**, retrieve the auto-created IDs with methods
like [GetVertexFaceUV()](/docs/reference/engine/classes/EditableMesh.md) and set
their values directly. This is more performant and avoids leaving unused
IDs in the mesh:

```lua
-- Create a triangle
local faceId = editableMesh:AddFace(v0, v1, v2)

-- Get the UV IDs that were automatically created
local uvId0 = editableMesh:GetVertexFaceUV(v0, faceId)
local uvId1 = editableMesh:GetVertexFaceUV(v1, faceId)
local uvId2 = editableMesh:GetVertexFaceUV(v2, faceId)

-- Set UV values on those existing UV IDs
editableMesh:SetUV(uvId0, Vector2.new(0, 0))
editableMesh:SetUV(uvId1, Vector2.new(1, 0))
editableMesh:SetUV(uvId2, Vector2.new(0, 1))
```

**To create a seam** — where the same vertex needs different attribute
values on different faces (for example, a UV seam or a sharp edge) —
create new attribute IDs with [AddUV()](/docs/reference/engine/classes/EditableMesh.md),
[AddNormal()](/docs/reference/engine/classes/EditableMesh.md), or
[AddColor()](/docs/reference/engine/classes/EditableMesh.md), then assign them to the face
with [SetFaceUVs()](/docs/reference/engine/classes/EditableMesh.md),
[SetFaceNormals()](/docs/reference/engine/classes/EditableMesh.md), or
[SetFaceColors()](/docs/reference/engine/classes/EditableMesh.md):

```lua
-- Create a triangle
local faceId = editableMesh:AddFace(v0, v1, v2)

-- Create new UV IDs with custom coordinates
local uv0 = editableMesh:AddUV(Vector2.new(0, 0))
local uv1 = editableMesh:AddUV(Vector2.new(1, 0))
local uv2 = editableMesh:AddUV(Vector2.new(0, 1))

-- Replace the face's UV IDs (creates a seam if the vertex had different UVs on another face)
editableMesh:SetFaceUVs(faceId, {uv0, uv1, uv2})
```

#### Normal sharing and smooth vs. sharp edges

Because new faces reuse normal IDs from adjacent faces by default, meshes
appear smooth. To create a **sharp edge** (crease) between faces, create a
separate normal ID for each face and assign it with
[SetFaceNormals()](/docs/reference/engine/classes/EditableMesh.md):

![Two adjacent faces with separate normal IDs producing flat shading](../../../assets/engine-api/classes/EditableMesh/Faceted-Normals.png)

```lua
-- Two triangles sharing vertices v0 and v1, but with a sharp edge between them
local fid1 = editableMesh:AddFace(v0, v1, v2)
local fid2 = editableMesh:AddFace(v0, v3, v1)

-- Create separate normals for each face to produce a hard edge
local n1 = editableMesh:AddNormal() -- Auto-computed for fid1
local n2 = editableMesh:AddNormal() -- Auto-computed for fid2
editableMesh:SetFaceNormals(fid1, {n1, n1, n1})
editableMesh:SetFaceNormals(fid2, {n2, n2, n2})
```

See also [SetNormal()](/docs/reference/engine/classes/EditableMesh.md) to manually specify
a normal vector, and [ResetNormal()](/docs/reference/engine/classes/EditableMesh.md) to
revert a normal back to automatic computation.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexIds` | `Tuple` |  | The new face's vertex IDs passed as separate arguments in order around the face. Provide 3 IDs to create a triangle or 4 IDs to create a quad. |

**Returns:** `int64` — Face ID of the new face.

### Method: EditableMesh:AddNormal

**Signature:** `EditableMesh:AddNormal(normal: Vector3?): int64`

Adds a new normal to the geometry and returns a normal ID. If the normal
value isn't specified, the normal will be automatically calculated.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `normal` | `Vector3?` |  | The normal vector. If the normal value isn't specified, the normal will be automatically calculated. |

**Returns:** `int64` — Normal ID of the new normal.

### Method: EditableMesh:AddTriangle

**Signature:** `EditableMesh:AddTriangle(vertexId0: int64, vertexId1: int64, vertexId2: int64): int64`

Adds a new triangle to the mesh and returns a stable face ID. This is
equivalent to calling [AddFace()](/docs/reference/engine/classes/EditableMesh.md) with 3
vertex IDs.

See [AddFace()](/docs/reference/engine/classes/EditableMesh.md) for information on how all
faces are added, including those added by
[AddTriangle()](/docs/reference/engine/classes/EditableMesh.md). This includes details
related to automatic attribute assignment, overriding attributes, and
more.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId0` | `int64` |  | ID of the first vertex of the triangle. |
| `vertexId1` | `int64` |  | ID of the second vertex of the triangle. |
| `vertexId2` | `int64` |  | ID of the third vertex of the triangle. |

**Returns:** `int64` — Stable face ID of the new face.

### Method: EditableMesh:AddUV

**Signature:** `EditableMesh:AddUV(uv: Vector2): int64`

Adds a new UV coordinate attribute to the mesh and returns a UV ID.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `uv` | `Vector2` |  | The new UV coordinate. |

**Returns:** `int64` — UV ID of the new UV.

### Method: EditableMesh:AddVertex

**Signature:** `EditableMesh:AddVertex(p: Vector3): int64`

Adds a new vertex to the mesh and returns a vertex ID. The position is
specified in the mesh's local object space. An error is thrown if the mesh
already contains 60,000 vertices.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `p` | `Vector3` |  | Position in the mesh's local object space. |

**Returns:** `int64` — Vertex ID of the new vertex.

### Method: EditableMesh:BatchAdd

**Signature:** `EditableMesh:BatchAdd(attr: MeshAttribute, data: Array): Array`

Creates new mesh elements of the given attribute type and returns their
IDs in the same order as the input data. This method always requires an
explicit [MeshAttribute](/docs/reference/engine/enums/MeshAttribute.md) because its input is raw values with no
existing IDs to inspect. Throws an error if the attribute type is invalid,
the data format does not match, or adding the elements would exceed mesh
limits.

```lua
local vIds = mesh:BatchAdd(Enum.MeshAttribute.Vertex, positions)     -- Positions: {Vector3}
local nIds = mesh:BatchAdd(Enum.MeshAttribute.Normal, normals)       -- Normals: {Vector3}
local uIds = mesh:BatchAdd(Enum.MeshAttribute.UV, uvs)               -- UVs: {Vector2}
local cIds = mesh:BatchAdd(Enum.MeshAttribute.Color, colors, alphas) -- Colors: {Color3}, Alphas: {number}
local fIds = mesh:BatchAdd(Enum.MeshAttribute.Face, {
    {vIds[1], vIds[2], vIds[3]},
    {vIds[1], vIds[3], vIds[4]},
})
```

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `attr` | `MeshAttribute` |  | The [MeshAttribute](/docs/reference/engine/enums/MeshAttribute.md) type of element to create. |
| `data` | `Array` |  | Values to initialize the new elements. An array of [Vector3](/docs/reference/engine/datatypes/Vector3.md) for [Vertex](/docs/reference/engine/enums/MeshAttribute.md) or [Normal](/docs/reference/engine/enums/MeshAttribute.md); an array of [Vector2](/docs/reference/engine/datatypes/Vector2.md) for [UV](/docs/reference/engine/enums/MeshAttribute.md); an array of [Color3](/docs/reference/engine/datatypes/Color3.md) followed by a matching array of alpha numbers (same length) for [Color](/docs/reference/engine/enums/MeshAttribute.md); a 2D array of vertex-ID arrays for [Face](/docs/reference/engine/enums/MeshAttribute.md). |

**Returns:** `Array` — Ordered array of new element IDs matching the input order.

### Method: EditableMesh:BatchGetFaceAttributes

**Signature:** `EditableMesh:BatchGetFaceAttributes(attr: MeshAttribute, faceIds: Array): Array`

Returns, for each face, the array of per-corner attribute IDs, one per
corner in the same order as
[GetFaceVertices()](/docs/reference/engine/classes/EditableMesh.md).

```lua
local faceNormals = mesh:BatchGetFaceAttributes(Enum.MeshAttribute.Normal, faceIds) -- {{normalId}}
local faceVerts = mesh:BatchGetFaceAttributes(Enum.MeshAttribute.Vertex, faceIds)   -- {{vertexId}}
```

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `attr` | `MeshAttribute` |  | The attribute to retrieve for each face's corners. Must be [MeshAttribute.Vertex](/docs/reference/engine/enums/MeshAttribute.md), [MeshAttribute.Normal](/docs/reference/engine/enums/MeshAttribute.md), [MeshAttribute.Color](/docs/reference/engine/enums/MeshAttribute.md), or [MeshAttribute.UV](/docs/reference/engine/enums/MeshAttribute.md); [MeshAttribute.Face](/docs/reference/engine/enums/MeshAttribute.md) is not supported and throws an error. |
| `faceIds` | `Array` |  | Faces to query. |

**Returns:** `Array` — 2D array where `result[i]` is the array of attribute IDs at the
corners of `faceIds[i]`.

### Method: EditableMesh:BatchGetValues

**Signature:** `EditableMesh:BatchGetValues(ids: Array): Tuple`

Returns attribute values for the given IDs in the same order as the input.
Passing an empty array returns an empty result.

```lua
local positions = mesh:BatchGetValues(vertexIds)     -- {Vector3}
local normals = mesh:BatchGetValues(normalIds)       -- {Vector3}
local uvs = mesh:BatchGetValues(uvIds)               -- {Vector2}
local colors, alphas = mesh:BatchGetValues(colorIds) -- {Color3}, {number}
```

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `ids` | `Array` |  | IDs of the elements to read. All must be the same attribute type — vertex, normal, color, or UV. The attribute is determined by the ID type, so no [MeshAttribute](/docs/reference/engine/enums/MeshAttribute.md) argument is needed. Mixing types, or passing face or bone IDs, throws an error. |

**Returns:** `Tuple` — A tuple of two values. The first is an array of attribute values:
[Vector3](/docs/reference/engine/datatypes/Vector3.md) for vertex or normal IDs, [Vector2](/docs/reference/engine/datatypes/Vector2.md) for UV
IDs, [Color3](/docs/reference/engine/datatypes/Color3.md) for color IDs. The second is `nil` for all
attribute types except color, where it is an array of alpha numbers.

### Method: EditableMesh:BatchGetVertexAttributes

**Signature:** `EditableMesh:BatchGetVertexAttributes(attr: MeshAttribute, vertexIds: Array): Array`

Returns, for each vertex, the array of associated attribute IDs, gathered
across all faces adjacent to that vertex. For example, using
[MeshAttribute.Face](/docs/reference/engine/enums/MeshAttribute.md) returns every face that references each vertex.

```lua
local adjFaces = mesh:BatchGetVertexAttributes(Enum.MeshAttribute.Face, vertexIds) -- {{faceId}}
```

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `attr` | `MeshAttribute` |  | The attribute type to look up. Must be [MeshAttribute.Face](/docs/reference/engine/enums/MeshAttribute.md) (faces that reference each vertex), [MeshAttribute.Normal](/docs/reference/engine/enums/MeshAttribute.md), [MeshAttribute.Color](/docs/reference/engine/enums/MeshAttribute.md), or [MeshAttribute.UV](/docs/reference/engine/enums/MeshAttribute.md); [MeshAttribute.Vertex](/docs/reference/engine/enums/MeshAttribute.md) is not supported and throws an error (to read vertex positions, use [BatchGetValues()](/docs/reference/engine/classes/EditableMesh.md)). |
| `vertexIds` | `Array` |  | Vertices to query. |

**Returns:** `Array` — 2D array where `result[i]` is the array of attribute IDs associated
with `vertexIds[i]`.

### Method: EditableMesh:BatchGetVertexFaceAttributes

**Signature:** `EditableMesh:BatchGetVertexFaceAttributes(attr: MeshAttribute, vertexIds: Array, faceIds: Array): Array`

Returns the attribute ID at each corner specified by a vertex–face pair.

```lua
local cornerColors = mesh:BatchGetVertexFaceAttributes(Enum.MeshAttribute.Color, vertexIds, faceIds)
```

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `attr` | `MeshAttribute` |  | The attribute to retrieve. Must be [MeshAttribute.Normal](/docs/reference/engine/enums/MeshAttribute.md), [MeshAttribute.Color](/docs/reference/engine/enums/MeshAttribute.md), or [MeshAttribute.UV](/docs/reference/engine/enums/MeshAttribute.md); [MeshAttribute.Vertex](/docs/reference/engine/enums/MeshAttribute.md) and [MeshAttribute.Face](/docs/reference/engine/enums/MeshAttribute.md) are not supported and throw an error. |
| `vertexIds` | `Array` |  | Vertices that identify each corner. |
| `faceIds` | `Array` |  | Faces that identify each corner. Must be the same length as `vertexIds`. |

**Returns:** `Array` — Array of attribute IDs at each corner, in the same order as the
inputs.

### Method: EditableMesh:BatchRemove

**Signature:** `EditableMesh:BatchRemove(faceIds: Array): ()`

Removes a batch of faces. As with
[RemoveFace()](/docs/reference/engine/classes/EditableMesh.md), the vertices and
attributes used by the removed faces are not automatically deleted; call
[RemoveUnused()](/docs/reference/engine/classes/EditableMesh.md) afterward to clean up
unused elements.

```lua
mesh:BatchRemove(faceIds)
```

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `faceIds` | `Array` |  | Face IDs to remove. An invalid or already-removed ID throws an error and removes nothing; duplicate IDs are collapsed to a single removal. |

**Returns:** `()`

### Method: EditableMesh:BatchSetFaceAttributes

**Signature:** `EditableMesh:BatchSetFaceAttributes(faceIds: Array, attrIdArrays: Array): ()`

Sets the per-corner attribute IDs for each face.

```lua
-- Assign normal IDs to every corner of two faces
mesh:BatchSetFaceAttributes(faceIds, {
	{n1, n2, n3},
	{n4, n5, n6},
})
```

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `faceIds` | `Array` |  | Face IDs to update. Must be the same length as `attrIdArrays`. |
| `attrIdArrays` | `Array` |  | 2D array. `attrIdArrays[i]` is the list of attribute IDs for the corners of `faceIds[i]`, in order. Each inner array must have one entry per corner of the face. All IDs must be of the same attribute type — vertex, normal, color, or UV; mixing types (or passing another ID type) throws an error. |

**Returns:** `()`

### Method: EditableMesh:BatchSetValues

**Signature:** `EditableMesh:BatchSetValues(ids: Array, values: Array): ()`

Writes attribute values to the given IDs. `values[i]` is written to
`ids[i]`; the `ids` and `values` arrays must be the same length, unless
`values` is `nil` to reset normals.

For color IDs, pass an array of [Color3](/docs/reference/engine/datatypes/Color3.md) to set the colors, or an
array of numbers to set the alphas. Mixing types in one call is an error.

```lua
mesh:BatchSetValues(vertexIds, positions) -- Positions: {Vector3}
mesh:BatchSetValues(normalIds, normals)   -- Normals: {Vector3}
mesh:BatchSetValues(uvIds, uvs)           -- UVs: {Vector2}
mesh:BatchSetValues(colorIds, colors)     -- Colors: {Color3}
mesh:BatchSetValues(colorIds, alphas)     -- Alphas: {number}
mesh:BatchSetValues(normalIds, nil)       -- Resets each normal to auto-computed
```

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `ids` | `Array` |  | IDs of the elements to write. All must be the same attribute type — vertex, normal, color, or UV. The attribute is determined by the ID type, so no [MeshAttribute](/docs/reference/engine/enums/MeshAttribute.md) argument is needed. Mixing types, or passing face or bone IDs, throws an error. |
| `values` | `Array` |  | Values to assign. Type depends on the ID type: [Vector3](/docs/reference/engine/datatypes/Vector3.md) for vertex or normal IDs, [Vector2](/docs/reference/engine/datatypes/Vector2.md) for UV IDs, [Color3](/docs/reference/engine/datatypes/Color3.md) or a number for color IDs. Pass `nil` for normal IDs to reset each normal to auto-computed values, equivalent to calling [ResetNormal()](/docs/reference/engine/classes/EditableMesh.md) on each. |

**Returns:** `()`

### Method: EditableMesh:BatchSetVertexFaceAttributes

**Signature:** `EditableMesh:BatchSetVertexFaceAttributes(vertexIds: Array, faceIds: Array, attrIds: Array): ()`

Sets the attribute at a specific corner — identified by a vertex–face pair
— for each element in the batch. For each index `i`, the attribute at
corner `(vertexIds[i], faceIds[i])` is set to `attrIds[i]`.

```lua
mesh:BatchSetVertexFaceAttributes(vertexIds, faceIds, colorIds)
```

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexIds` | `Array` |  | Vertex IDs that identify each corner. |
| `faceIds` | `Array` |  | Face IDs that identify each corner. Must be the same length as `vertexIds`. |
| `attrIds` | `Array` |  | Attribute IDs to assign, one per pair; must be the same length as `vertexIds`. All must be the same attribute type — normal, color, or UV; passing a vertex or face ID throws an error. |

**Returns:** `()`

### Method: EditableMesh:Clear

**Signature:** `EditableMesh:Clear(): ()`

Removes all vertex data (including positions, normals, UV coordinates, and
colors), faces, bones, and FACS data without destroying the
[EditableMesh](/docs/reference/engine/classes/EditableMesh.md) or its allocated space.

This method cannot be called on a fixed-size mesh (where
[FixedSize](/docs/reference/engine/classes/EditableMesh.md) is `true`). Attempting to do so
throws an error because fixed-size meshes do not allow adding or removing
elements.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Returns:** `()`

### Method: EditableMesh:Destroy

**Signature:** `EditableMesh:Destroy(): ()`

Destroys the contents of the mesh, immediately reclaiming used memory.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Returns:** `()`

### Method: EditableMesh:FindClosestPointOnSurface

**Signature:** `EditableMesh:FindClosestPointOnSurface(point: Vector3): Tuple`

Finds the closest point on the mesh's surface. Returns the face ID, point
on the mesh in local object space, the barycentric coordinates of the
position within the face, and the 3 vertex IDs that the barycentric
coordinates correspond to. See
[RaycastLocal()](/docs/reference/engine/classes/EditableMesh.md) for more information on
barycentric coordinates, including how they apply to quad faces. When the
mesh is skinned, this query operates against the bind-pose geometry, not
the deformed mesh as it appears at runtime.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `point` | `Vector3` |  | Point position in the mesh's local object space. |

**Returns:** `Tuple` — Tuple of the face ID, point on the mesh in local object space, the
barycentric coordinate of the position within the face, and the 3
vertex IDs that the barycentric coordinate weights.

### Method: EditableMesh:FindClosestVertex

**Signature:** `EditableMesh:FindClosestVertex(toThisPoint: Vector3): int64`

Finds the closest vertex to a specific point in space and returns a vertex
ID. When the mesh is skinned, this query operates against the bind-pose
geometry, not the deformed mesh as it appears at runtime.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `toThisPoint` | `Vector3` |  | Point position in the mesh's local object space. |

**Returns:** `int64` — Closest vertex ID to the specified point in space.

### Method: EditableMesh:FindVerticesWithinSphere

**Signature:** `EditableMesh:FindVerticesWithinSphere(center: Vector3, radius: float): Array`

Finds all vertices within a specific sphere and returns a list of vertex
IDs. When the mesh is skinned, this query operates against the bind-pose
geometry, not the deformed mesh as it appears at runtime.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `center` | `Vector3` |  | Center of the sphere in the mesh's local object space. |
| `radius` | `float` |  | Radius of the sphere. |

**Returns:** `Array` — List of vertex IDs within the requested sphere.

### Method: EditableMesh:GetAdjacentFaces

**Signature:** `EditableMesh:GetAdjacentFaces(faceId: int64): Array`

Given a face ID, returns a list of adjacent faces.

![Adjacent faces indicated around requested face](../../../assets/engine-api/classes/EditableMesh/GetAdjacentTriangles.png)

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `faceId` | `int64` |  | Face ID for which to get adjacent faces. |

**Returns:** `Array` — List of face IDs adjacent to the given face.

### Method: EditableMesh:GetAdjacentVertices

**Signature:** `EditableMesh:GetAdjacentVertices(vertexId: int64): Array`

Given a vertex ID, returns a list of adjacent vertices.

![Adjacent vertices indicated around requested vertex](../../../assets/engine-api/classes/EditableMesh/GetAdjacentVertices.png)

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID around which to get adjacent vertices. |

**Returns:** `Array` — List of IDs of adjacent vertices around the given vertex ID.

### Method: EditableMesh:GetBoneByName

**Signature:** `EditableMesh:GetBoneByName(boneName: string): int64`

Finds the bone ID of the bone with the given name. Errors if no bone with
that name exists.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `boneName` | `string` |  | Bone name to search for. |

**Returns:** `int64` — Bone ID of the bone with the given name.

### Method: EditableMesh:GetBoneCFrame

**Signature:** `EditableMesh:GetBoneCFrame(boneId: int64): CFrame`

Returns the initial [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the bone in the bind pose of the
mesh, in the mesh's local space.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `boneId` | `int64` |  | Bone ID for which to get the [CFrame](/docs/reference/engine/datatypes/CFrame.md). |

**Returns:** `CFrame` — Initial [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the bone in the bind pose of the mesh, in
the mesh's local space.

### Method: EditableMesh:GetBoneIsVirtual

**Signature:** `EditableMesh:GetBoneIsVirtual(boneId: int64): boolean`

Returns `true` if the bone is virtual. Virtual bones can only be bound to
a [FaceControls](/docs/reference/engine/classes/FaceControls.md) instance.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `boneId` | `int64` |  | Bone ID for which to get whether the bone is virtual. |

**Returns:** `boolean` — Whether the bone with the given bone ID is virtual. Virtual bones can
only be bound to a [FaceControls](/docs/reference/engine/classes/FaceControls.md) instance.

### Method: EditableMesh:GetBoneName

**Signature:** `EditableMesh:GetBoneName(boneId: int64): string`

Returns the name string of the bone identified by the given bone ID. Bone
names are unique within the mesh and can be up to 100 characters long.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `boneId` | `int64` |  | Bone ID for which to get the name. |

**Returns:** `string` — Name of the bone with the given bone ID.

### Method: EditableMesh:GetBoneParent

**Signature:** `EditableMesh:GetBoneParent(boneId: int64): int64`

Returns the bone ID of the parent bone in the bone hierarchy. If the bone
has no parent, returns `0`.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `boneId` | `int64` |  | Bone ID for which to get the parent. |

**Returns:** `int64` — Bone ID for the parent of the bone with the given bone ID. If there is
no parent, returns `0`.

### Method: EditableMesh:GetBones

**Signature:** `EditableMesh:GetBones(): Array`

Returns all bones of the mesh as a list of bone IDs.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Returns:** `Array` — List of bone IDs.

### Method: EditableMesh:GetCenter

**Signature:** `EditableMesh:GetCenter(): Vector3`

Returns the center of the mesh's axis-aligned bounding box, in the mesh's
local object space.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Returns:** `Vector3` — Center of the bounding box of the `EditableMesh`.

### Method: EditableMesh:GetColor

**Signature:** `EditableMesh:GetColor(colorId: int64): Color3?`

Returns the [Color3](/docs/reference/engine/datatypes/Color3.md) value stored at the given color ID. Use
[GetColorAlpha()](/docs/reference/engine/classes/EditableMesh.md) to retrieve the alpha
component separately.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `colorId` | `int64` |  | Color ID for which to get the color. |

**Returns:** `Color3?` — Color for the requested color ID.

### Method: EditableMesh:GetColorAlpha

**Signature:** `EditableMesh:GetColorAlpha(colorId: int64): float?`

Returns the alpha component of the vertex color at the given color ID as a
number between `0` (fully transparent) and `1` (fully opaque). Use
[GetColor()](/docs/reference/engine/classes/EditableMesh.md) to retrieve the RGB component.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `colorId` | `int64` |  | Color ID for which to get the alpha. |

**Returns:** `float?` — Color alpha at the request color ID.

### Method: EditableMesh:GetColors

**Signature:** `EditableMesh:GetColors(): Array`

Returns all colors of the mesh as a list of color IDs.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Returns:** `Array` — List of color IDs.

### Method: EditableMesh:GetFaceColors

**Signature:** `EditableMesh:GetFaceColors(faceId: int64): Array`

Returns an array of color IDs, one per vertex corner of the specified
face, in the same order as
[GetFaceVertices()](/docs/reference/engine/classes/EditableMesh.md). Use these IDs
with [GetColor()](/docs/reference/engine/classes/EditableMesh.md) and
[GetColorAlpha()](/docs/reference/engine/classes/EditableMesh.md) to read the actual
color values.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `faceId` | `int64` |  | Face ID for which to get the color IDs. |

**Returns:** `Array` — List of color IDs used for the vertices on the given face.

### Method: EditableMesh:GetFaceNormals

**Signature:** `EditableMesh:GetFaceNormals(faceId: int64): Array`

Returns an array of normal IDs, one per vertex corner of the specified
face, in the same order as
[GetFaceVertices()](/docs/reference/engine/classes/EditableMesh.md). Use these IDs
with [GetNormal()](/docs/reference/engine/classes/EditableMesh.md) to read the actual
normal vectors.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `faceId` | `int64` |  | Face ID for which to get the normal IDs. |

**Returns:** `Array` — List of normal IDs used for the vertices on the given face.

### Method: EditableMesh:GetFaces

**Signature:** `EditableMesh:GetFaces(): Array`

Returns all faces of the mesh as a list of face IDs.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Returns:** `Array` — List of face IDs.

### Method: EditableMesh:GetFacesWithColor

**Signature:** `EditableMesh:GetFacesWithColor(colorId: int64): Array`

Returns an array of face IDs that use the given color ID. Use together
with [GetVerticesWithColor()](/docs/reference/engine/classes/EditableMesh.md) to
obtain all face/vertex pairs.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `colorId` | `int64` |  | Color ID to find faces for. |

**Returns:** `Array` — List of face IDs that use the provided color ID.

### Method: EditableMesh:GetFacesWithNormal

**Signature:** `EditableMesh:GetFacesWithNormal(normalId: int64): Array`

Returns an array of face IDs that use the given normal ID. Use together
with [GetVerticesWithNormal()](/docs/reference/engine/classes/EditableMesh.md)
to obtain all face/vertex pairs.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `normalId` | `int64` |  | Normal ID to find faces for. |

**Returns:** `Array` — List of face IDs that use the provided normal ID.

### Method: EditableMesh:GetFacesWithUV

**Signature:** `EditableMesh:GetFacesWithUV(uvId: int64): Array`

Returns an array of face IDs that use the given UV ID. Use together with
[GetVerticesWithUV()](/docs/reference/engine/classes/EditableMesh.md) to obtain all
face/vertex pairs.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `uvId` | `int64` |  | UV ID to find faces for. |

**Returns:** `Array` — List of face IDs that use the provided UV ID.

### Method: EditableMesh:GetFaceUVs

**Signature:** `EditableMesh:GetFaceUVs(faceId: int64): Array`

Returns an array of UV IDs, one per vertex corner of the specified face,
in the same order as
[GetFaceVertices()](/docs/reference/engine/classes/EditableMesh.md). Use these IDs
with [GetUV()](/docs/reference/engine/classes/EditableMesh.md) to read the actual UV
coordinates.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `faceId` | `int64` |  | Face ID for which to get the UV IDs. |

**Returns:** `Array` — List of UV IDs used for the vertices on the given face.

### Method: EditableMesh:GetFaceVertices

**Signature:** `EditableMesh:GetFaceVertices(faceId: int64): Array`

Returns an array of vertex IDs that define the corners of the given face,
in the same order used when the face was created.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `faceId` | `int64` |  | Face ID for which to get the vertex IDs. |

**Returns:** `Array` — List of vertex IDs around the given face.

### Method: EditableMesh:GetFacsCorrectivePose

**Signature:** `EditableMesh:GetFacsCorrectivePose(actions: Array): Tuple`

Returns bone IDs and bone [CFrames](/docs/reference/engine/datatypes/CFrame.md) for all bones in a
specific FACS corrective pose. Each bone [CFrame](/docs/reference/engine/datatypes/CFrame.md) transforms the
bone from the initial bone [CFrame](/docs/reference/engine/datatypes/CFrame.md) in the bind pose of the mesh
to the combined bone [CFrame](/docs/reference/engine/datatypes/CFrame.md) for this pose. All
[CFrames](/docs/reference/engine/datatypes/CFrame.md) are in the mesh's local space.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actions` | `Array` |  | Array or 2 or 3 [FacsActionUnit](/docs/reference/engine/enums/FacsActionUnit.md) values that specify a corrective pose. |

**Returns:** `Tuple` — Array of bone IDs and corresponding array of bone
[CFrames](/docs/reference/engine/datatypes/CFrame.md).

### Method: EditableMesh:GetFacsCorrectivePoses

**Signature:** `EditableMesh:GetFacsCorrectivePoses(): Array`

Returns all FACS corrective poses that are in use. Each corrective pose is
specified by 2 or 3 [FacsActionUnit](/docs/reference/engine/enums/FacsActionUnit.md) values.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Returns:** `Array` — Array of corrective poses. Each corrective pose is specified by a
small array of 2 or 3 [FacsActionUnit](/docs/reference/engine/enums/FacsActionUnit.md) values.

### Method: EditableMesh:GetFacsPose

**Signature:** `EditableMesh:GetFacsPose(action: FacsActionUnit): Tuple`

Returns bone IDs and bone [CFrames](/docs/reference/engine/datatypes/CFrame.md) for all bones in a
specific FACS action unit. Each bone [CFrame](/docs/reference/engine/datatypes/CFrame.md) transforms the bone
from the initial bone [CFrame](/docs/reference/engine/datatypes/CFrame.md) in the bind pose of the mesh to
the combined bone [CFrame](/docs/reference/engine/datatypes/CFrame.md) for this pose. All
[CFrames](/docs/reference/engine/datatypes/CFrame.md) are in the mesh's local space.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `action` | `FacsActionUnit` |  | FACS action unit for which to get the pose. |

**Returns:** `Tuple` — Array of bone IDs and corresponding array of bone [CFrame](/docs/reference/engine/datatypes/CFrame.md).

### Method: EditableMesh:GetFacsPoses

**Signature:** `EditableMesh:GetFacsPoses(): Array`

Returns an array of [FacsActionUnit](/docs/reference/engine/enums/FacsActionUnit.md) values representing all base
FACS poses currently defined on this mesh. Use each returned value with
[GetFacsPose()](/docs/reference/engine/classes/EditableMesh.md) to retrieve the bone
transforms for that pose. See also
[GetFacsCorrectivePoses()](/docs/reference/engine/classes/EditableMesh.md) for
corrective poses.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Returns:** `Array` — Array of [FacsActionUnit](/docs/reference/engine/enums/FacsActionUnit.md), one for each FACS action unit that has
a pose defined.

### Method: EditableMesh:GetNormal

**Signature:** `EditableMesh:GetNormal(normalId: int64): Vector3?`

Returns the [Vector3](/docs/reference/engine/datatypes/Vector3.md) normal vector at the given normal ID. If
the normal vector was manually specified it will return that vector. If
the normal vector was not specified or was reset, this will return an
automatically calculated normal vector based on the shape of the mesh.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `normalId` | `int64` |  | Normal ID for which to get the normal vector. |

**Returns:** `Vector3?` — Normal vector at the requested normal ID.

### Method: EditableMesh:GetNormals

**Signature:** `EditableMesh:GetNormals(): Array`

Returns all normals of the mesh as a list of normal IDs.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Returns:** `Array` — List of normal IDs.

### Method: EditableMesh:GetPosition

**Signature:** `EditableMesh:GetPosition(vertexId: int64): Vector3`

Gets the position of a vertex in the mesh's local object space.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID for which to get the position. |

**Returns:** `Vector3` — Position of a vertex in the mesh's local object space.

### Method: EditableMesh:GetSize

**Signature:** `EditableMesh:GetSize(): Vector3`

Returns the size of the mesh's axis-aligned bounding box, in the mesh's
local object space.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Returns:** `Vector3` — Size of the `EditableMesh`.

### Method: EditableMesh:GetUV

**Signature:** `EditableMesh:GetUV(uvId: int64): Vector2?`

Returns the [Vector2](/docs/reference/engine/datatypes/Vector2.md) texture coordinate stored at the given UV
ID. UV coordinates map the mesh surface to a 2D texture.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `uvId` | `int64` |  | UV ID for which to get the UV coordinate. |

**Returns:** `Vector2?` — UV coordinates at the requested UV ID.

### Method: EditableMesh:GetUVs

**Signature:** `EditableMesh:GetUVs(): Array`

Returns all UVs of the mesh as a list of UV IDs.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Returns:** `Array` — List of UV IDs.

### Method: EditableMesh:GetVertexBones

**Signature:** `EditableMesh:GetVertexBones(vertexId: int64): Array`

Returns an array of bone IDs that influence the given vertex during
skinning deformation. A vertex can be influenced by up to 4 bones. The
returned array corresponds index-by-index with the weights returned by
[GetVertexBoneWeights()](/docs/reference/engine/classes/EditableMesh.md) for the
same vertex.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID for which to get the associated bones. |

**Returns:** `Array` — Bone IDs associated with the vertex for skinning.

### Method: EditableMesh:GetVertexBoneWeights

**Signature:** `EditableMesh:GetVertexBoneWeights(vertexId: int64): Array`

Returns an array of blend weights (each between `0` and `1`) for the bones
influencing this vertex during skeletal deformation. The returned array
corresponds index-by-index with the bone IDs returned by
[GetVertexBones()](/docs/reference/engine/classes/EditableMesh.md) for the same
vertex.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID for which to get the associated bone weights. |

**Returns:** `Array` — Skinning blend weights for each bone that is associated with the
vertex.

### Method: EditableMesh:GetVertexColors

**Signature:** `EditableMesh:GetVertexColors(vertexId: int64): Array`

Returns an array of color IDs used on all face corners that reference the
given vertex. A vertex shared by multiple faces can have different color
IDs on each face (a color seam); this method returns all of them.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID to find color IDs. |

**Returns:** `Array` — Array of color IDs of faces attached to the given vertex.

### Method: EditableMesh:GetVertexFaceColor

**Signature:** `EditableMesh:GetVertexFaceColor(vertexId: int64, faceId: int64): int64`

Returns the color ID assigned to a specific corner of a face, identified
by the vertex/face pair. This is useful when a vertex is shared by
multiple faces and you need the color for one particular face corner
rather than all of them.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID. |
| `faceId` | `int64` |  | Face ID. |

**Returns:** `int64` — Color ID of the vertex/face pair.

### Method: EditableMesh:GetVertexFaceNormal

**Signature:** `EditableMesh:GetVertexFaceNormal(vertexId: int64, faceId: int64): int64`

Returns the normal ID assigned to a specific corner of a face, identified
by the vertex/face pair. This is useful when a vertex has split normals (a
sharp edge) and you need the normal for one particular face corner rather
than all of them.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID. |
| `faceId` | `int64` |  | Face ID. |

**Returns:** `int64` — Normal ID of the vertex/face pair.

### Method: EditableMesh:GetVertexFaces

**Signature:** `EditableMesh:GetVertexFaces(vertexId: int64): Array`

Returns an array of face IDs for all faces that have the given vertex as
one of their corners. Use this to traverse the mesh topology around a
vertex, for example to find all faces affected by moving a vertex.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID to find faces for. |

**Returns:** `Array` — Array of face IDs attached to the given vertex.

### Method: EditableMesh:GetVertexFaceUV

**Signature:** `EditableMesh:GetVertexFaceUV(vertexId: int64, faceId: int64): int64`

Returns the UV ID assigned to a specific corner of a face, identified by
the vertex/face pair. This is useful when a vertex has a UV seam and you
need the UV for one particular face corner rather than all of them.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID. |
| `faceId` | `int64` |  | Face ID. |

**Returns:** `int64` — UV ID of the vertex/face pair.

### Method: EditableMesh:GetVertexNormals

**Signature:** `EditableMesh:GetVertexNormals(vertexId: int64): Array`

Returns an array of normal IDs used on all face corners that reference the
given vertex. A vertex shared by multiple faces can have different normal
IDs on each face (a hard/sharp edge); this method returns all of them.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID to find normal IDs. |

**Returns:** `Array` — Array of normal IDs of faces attached to the given vertex.

### Method: EditableMesh:GetVertexUVs

**Signature:** `EditableMesh:GetVertexUVs(vertexId: int64): Array`

Returns an array of UV IDs used on all face corners that reference the
given vertex. A vertex shared by multiple faces can have different UV IDs
on each face (a UV seam); this method returns all of them.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID to find UV IDs. |

**Returns:** `Array` — Array of UV IDs of faces attached to the given vertex.

### Method: EditableMesh:GetVertices

**Signature:** `EditableMesh:GetVertices(): Array`

Returns all vertex IDs in the mesh as a list of IDs. The IDs may not be
contiguous. Use this list to iterate over vertices safely, rather than
assuming consecutive numbering.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Returns:** `Array` — List of vertex IDs.

### Method: EditableMesh:GetVerticesWithColor

**Signature:** `EditableMesh:GetVerticesWithColor(colorId: int64): Array`

Returns an array of vertex IDs that use the given color ID. Use together
with [GetFacesWithColor()](/docs/reference/engine/classes/EditableMesh.md) to
obtain all face/vertex pairs.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `colorId` | `int64` |  | Color ID to find faces for. |

**Returns:** `Array` — List of face IDs that use the provided color ID.

### Method: EditableMesh:GetVerticesWithNormal

**Signature:** `EditableMesh:GetVerticesWithNormal(normalId: int64): Array`

Returns an array of vertex IDs that use the given normal ID. Use together
with [GetFacesWithNormal()](/docs/reference/engine/classes/EditableMesh.md) to
obtain all face/vertex pairs.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `normalId` | `int64` |  | Normal ID to find vertices for. |

**Returns:** `Array` — List of vertex IDs that use the provided normal ID.

### Method: EditableMesh:GetVerticesWithUV

**Signature:** `EditableMesh:GetVerticesWithUV(uvId: int64): Array`

Returns an array of vertex IDs that use the given UV ID. Use together with
[GetFacesWithUV()](/docs/reference/engine/classes/EditableMesh.md) to obtain all
face/vertex pairs.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `uvId` | `int64` |  | UV ID to find vertices for. |

**Returns:** `Array` — List of vertex IDs that use the provided UV ID.

### Method: EditableMesh:IdDebugString

**Signature:** `EditableMesh:IdDebugString(id: int64): string`

Returns a string describing an ID, useful for debugging purposes, like
`f17` or `v12`, containing the type, ID number, and version.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `id` | `int64` |  | ID for which to return a debugging information string. |

**Returns:** `string` — String that describes the ID in human-readable format.

### Method: EditableMesh:MergeVertices

**Signature:** `EditableMesh:MergeVertices(mergeTolerance: float): Map`

Merges vertices that touch together, to use a single vertex ID but keep
the other original attribute IDs.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `mergeTolerance` | `float` |  | The distance at which the vertices are considered to touch each other. |

**Returns:** `Map` — A mapping of old vertex ID to new vertex ID for vertices that have
been merged.

### Method: EditableMesh:RaycastLocal

**Signature:** `EditableMesh:RaycastLocal(origin: Vector3, direction: Vector3): Tuple`

Casts a ray and returns the face ID, point of intersection, barycentric
coordinates, and the 3 vertex IDs that the barycentric coordinates
correspond to. The inputs and outputs of this method are in the mesh's
local object space. When the mesh is skinned, this raycast operates
against the bind-pose geometry, not the deformed mesh as it appears at
runtime.

A **barycentric coordinate** is a way of specifying a point within a
triangle as a weighted combination of the triangle's 3 vertices. This is
useful as a general way of blending vertex attributes. See this method's
code sample as an illustration.

Because a barycentric coordinate is defined over exactly 3 vertices, when
the hit face is a quad, the coordinate and the returned vertex IDs refer
to 3 of the quad's 4 vertices forming the corners of the sub-triangle that
was hit. Use the returned vertex IDs, rather than the face's full vertex
list, to identify which vertices the weights apply to.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `origin` | `Vector3` |  | Origin of the ray in the mesh's local object space. |
| `direction` | `Vector3` |  | Direction of the ray. |

**Returns:** `Tuple` — Tuple of the face ID, point of intersection, barycentric coordinates,
and the 3 vertex IDs that the barycentric coordinates weight.

**EditableMesh:RaycastLocal()**

This code finds the position and UV coordinates of the closest point on an
[EditableMesh](/docs/reference/engine/classes/EditableMesh.md) to the input point.

```lua
local AssetService = game:GetService("AssetService")
local Workspace = game:GetService("Workspace")

-- Initialize EditableMesh in space
local editableMesh = nil
local success, errorMsg = pcall(function()
	editableMesh = AssetService:CreateEditableMeshAsync(Content.fromUri("rbxassetid://ASSET_ID"))
end)

local meshPart = nil
if success and editableMesh then
	meshPart = AssetService:CreateMeshPartAsync(
		Content.fromObject(editableMesh),
		{ CollisionFidelity = Enum.CollisionFidelity.Hull }
	)
	meshPart.Parent = Workspace
else
	warn(errorMsg)
end

-- Function that will cast a ray from the given point, returning the world point of the hit and the UV coordinate
local function castRayFromCamera(meshPart: MeshPart, editableMesh: EditableMesh, viewportPoint: Vector3)
	if not meshPart then
		return
	end

	-- Calculate how much the object is being scaled in each dimension
	local renderScale = meshPart.Size / meshPart.MeshSize

	-- Create ray from camera along the direction of a clicked point
	local ray = Workspace.CurrentCamera:ViewportPointToRay(viewportPoint.X, viewportPoint.Y)

	-- Convert to object space to use with RaycastLocal()
	local relativeOrigin = meshPart.CFrame:PointToObjectSpace(ray.Origin) / renderScale
	local relativeTarget = meshPart.CFrame:PointToObjectSpace(ray.Origin + ray.Direction * 100) / renderScale
	local relativeDirection = relativeTarget - relativeOrigin

	local faceId, point, barycentricCoordinate, vertId1, vertId2, vertId3 =
		editableMesh:RaycastLocal(relativeOrigin, relativeDirection)

	if not faceId then
		-- Didn't hit any faces
		return
	end

	-- Compute the hit point in world space
	local worldHitPoint = meshPart.CFrame:PointToWorldSpace(point * renderScale)

	-- Get the UVs on the face
	local uvId1 = editableMesh:GetVertexFaceUV(vertId1, faceId)
	local uvId2 = editableMesh:GetVertexFaceUV(vertId2, faceId)
	local uvId3 = editableMesh:GetVertexFaceUV(vertId3, faceId)

	local uv1 = editableMesh:GetUV(uvId1)
	local uv2 = editableMesh:GetUV(uvId2)
	local uv3 = editableMesh:GetUV(uvId3)

	-- Interpolate UVs within the face based on the barycentric coordinate
	local u = (barycentricCoordinate.x * uv1.x) + (barycentricCoordinate.y * uv2.x) + (barycentricCoordinate.z * uv3.x)
	local v = (barycentricCoordinate.x * uv1.y) + (barycentricCoordinate.y * uv2.y) + (barycentricCoordinate.z * uv3.y)

	return worldHitPoint, Vector2.new(u, v)
end
```

### Method: EditableMesh:RemoveBone

**Signature:** `EditableMesh:RemoveBone(boneId: int64): ()`

Removes a bone from the mesh using its bone ID. Any vertex skinning
weights that referenced the removed bone are also cleared.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `boneId` | `int64` |  | Bone ID of the bone to remove. |

**Returns:** `()`

### Method: EditableMesh:RemoveFace

**Signature:** `EditableMesh:RemoveFace(faceId: int64): ()`

Removes a face from the mesh using its face ID. The vertices and
attributes that were used by the face are **not** automatically deleted;
call [RemoveUnused()](/docs/reference/engine/classes/EditableMesh.md) afterward if you
want to clean up unused vertices and attributes.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `faceId` | `int64` |  | Face ID of the face to remove. |

**Returns:** `()`

### Method: EditableMesh:RemoveUnused

**Signature:** `EditableMesh:RemoveUnused(): Array`

Removes all vertices, normals, UVs, and colors which are not used in any
face, and returns the removed IDs.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Returns:** `Array` — All of the removed IDs.

### Method: EditableMesh:ResetNormal

**Signature:** `EditableMesh:ResetNormal(normalId: int64): ()`

Reset this normal ID to be automatically calculated based on the shape of
the mesh, instead of manually set.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `normalId` | `int64` |  | Normal ID to reset. |

**Returns:** `()`

### Method: EditableMesh:SetBoneCFrame

**Signature:** `EditableMesh:SetBoneCFrame(boneId: int64, cframe: CFrame): ()`

Set the initial [CFrame](/docs/reference/engine/datatypes/CFrame.md) for a bone in the mesh's bind pose, in
the mesh's local space.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `boneId` | `int64` |  | Bone ID for which to set the initial [CFrame](/docs/reference/engine/datatypes/CFrame.md). |
| `cframe` | `CFrame` |  | Initial [CFrame](/docs/reference/engine/datatypes/CFrame.md) for the bone in the mesh's bind pose, in the mesh's local space. |

**Returns:** `()`

### Method: EditableMesh:SetBoneIsVirtual

**Signature:** `EditableMesh:SetBoneIsVirtual(boneId: int64, virtual: boolean): ()`

Set whether a bone is virtual. Virtual bones can only be bound to a
[FaceControls](/docs/reference/engine/classes/FaceControls.md) instance.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `boneId` | `int64` |  | Bone ID for which to set whether the bone is virtual. |
| `virtual` | `boolean` |  | Whether the bone should be virtual. |

**Returns:** `()`

### Method: EditableMesh:SetBoneName

**Signature:** `EditableMesh:SetBoneName(boneId: int64, name: string): ()`

Sets the name for a bone. Bone names can be 100 characters long and must
be unique in the mesh.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `boneId` | `int64` |  | Bone ID for which to set the name. |
| `name` | `string` |  | Bone name to set. |

**Returns:** `()`

### Method: EditableMesh:SetBoneParent

**Signature:** `EditableMesh:SetBoneParent(boneId: int64, parentBoneId: int64): ()`

Sets the parent of a bone in the bone hierarchy. Pass a valid bone ID to
parent the bone, or `0` to make it a root bone. The engine validates that
the new parent does not create a cycle in the bone hierarchy and throws an
error if the parent ID is invalid or would produce a circular dependency.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `boneId` | `int64` |  | Bone ID for which to set the parent. |
| `parentBoneId` | `int64` |  | Parent bone ID. |

**Returns:** `()`

### Method: EditableMesh:SetColor

**Signature:** `EditableMesh:SetColor(colorId: int64, color: Color3): ()`

Sets the [Color3](/docs/reference/engine/datatypes/Color3.md) value for a color ID. This changes the vertex
color for every face corner that references this color ID. Use
[SetColorAlpha()](/docs/reference/engine/classes/EditableMesh.md) to change the alpha
component separately.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `colorId` | `int64` |  | Color ID for which to set the color. |
| `color` | `Color3` |  | Color to set. |

**Returns:** `()`

### Method: EditableMesh:SetColorAlpha

**Signature:** `EditableMesh:SetColorAlpha(colorId: int64, alpha: float): ()`

Sets the alpha (transparency) component of the vertex color at the given
color ID. The value is a number between `0` (fully transparent) and `1`
(fully opaque). This changes the alpha for every face corner that
references this color ID.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `colorId` | `int64` |  | Color ID for which to set the color alpha. |
| `alpha` | `float` |  | Alpha to set. |

**Returns:** `()`

### Method: EditableMesh:SetFaceColors

**Signature:** `EditableMesh:SetFaceColors(faceId: int64, ids: Array): ()`

Assigns new color IDs to the corners of a face, replacing whatever color
IDs were previously set. The array must contain one color ID per vertex of
the face, in the same winding order as
[GetFaceVertices()](/docs/reference/engine/classes/EditableMesh.md). Use this to
create a color seam at a vertex shared by multiple faces.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `faceId` | `int64` |  | Face ID for which to update the vertex colors. |
| `ids` | `Array` |  | List of new color IDs to use for the given face's vertices. |

**Returns:** `()`

### Method: EditableMesh:SetFaceNormals

**Signature:** `EditableMesh:SetFaceNormals(faceId: int64, ids: Array): ()`

Assigns new normal IDs to the corners of a face, replacing whatever normal
IDs were previously set. The array must contain one normal ID per vertex
of the face, in the same winding order as
[GetFaceVertices()](/docs/reference/engine/classes/EditableMesh.md). Use this to
create a hard/sharp edge by giving adjacent faces different normals at the
same vertex.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `faceId` | `int64` |  | Face ID for which to update the vertex normals. |
| `ids` | `Array` |  | List of new normal IDs to use for the given face's vertices. |

**Returns:** `()`

### Method: EditableMesh:SetFaceUVs

**Signature:** `EditableMesh:SetFaceUVs(faceId: int64, ids: Array): ()`

Assigns new UV IDs to the corners of a face, replacing whatever UV IDs
were previously set. The array must contain one UV ID per vertex of the
face, in the same winding order as
[GetFaceVertices()](/docs/reference/engine/classes/EditableMesh.md). Use this to
create a UV seam at a vertex shared by multiple faces.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `faceId` | `int64` |  | Face ID for which to update the vertex UVs. |
| `ids` | `Array` |  | List of new UV IDs to use for the given face's vertices. |

**Returns:** `()`

### Method: EditableMesh:SetFaceVertices

**Signature:** `EditableMesh:SetFaceVertices(faceId: int64, ids: Array): ()`

Replaces the vertex IDs at each corner of the given face, in winding
order. Passing 3 vertex IDs makes the face a triangle and 4 makes it a
quad, so this can convert a face between a triangle and a quad while
keeping the same face ID.

The normal, UV, and color attributes on each of the existing corners are
preserved. If a new corner is added, it follows the same automatic
attribute assignment described in
[AddFace()](/docs/reference/engine/classes/EditableMesh.md).

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `faceId` | `int64` |  | Face ID for which to update the vertices. |
| `ids` | `Array` |  | List of new vertex IDs to use for the given face. |

**Returns:** `()`

### Method: EditableMesh:SetFacsBonePose

**Signature:** `EditableMesh:SetFacsBonePose(action: FacsActionUnit, boneId: int64, cframe: CFrame): ()`

Sets the [CFrame](/docs/reference/engine/datatypes/CFrame.md) for a single bone within a specific FACS action
unit pose, without modifying the other bones in that pose. The bone must
be virtual. The [CFrame](/docs/reference/engine/datatypes/CFrame.md) transforms the bone from its initial
bind-pose position to the target pose position, in the mesh's local space.
Use this for incremental edits to a FACS pose; use
[SetFacsPose()](/docs/reference/engine/classes/EditableMesh.md) to set all bones in a
pose at once.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `action` | `FacsActionUnit` |  | FACS action unit for which to set the pose. |
| `boneId` | `int64` |  | Bone to set a [CFrame](/docs/reference/engine/datatypes/CFrame.md) for this pose. |
| `cframe` | `CFrame` |  | [CFrame](/docs/reference/engine/datatypes/CFrame.md) which transforms the bone from the initial bone [CFrame](/docs/reference/engine/datatypes/CFrame.md) in the bind pose of the mesh to the combined bone [CFrame](/docs/reference/engine/datatypes/CFrame.md) for this pose. All [CFrames](/docs/reference/engine/datatypes/CFrame.md) are in the mesh's local space. |

**Returns:** `()`

### Method: EditableMesh:SetFacsCorrectivePose

**Signature:** `EditableMesh:SetFacsCorrectivePose(actions: Array, boneIds: Array, cframes: Array): ()`

Sets all bone transforms for a FACS corrective pose, which overrides the
blended result of 2 or 3 base poses when they are active simultaneously.
The `actions` array must contain exactly 2 or 3 [FacsActionUnit](/docs/reference/engine/enums/FacsActionUnit.md)
values that identify the combination. All referenced bones must be
virtual. The `boneIds` and `cframes` arrays must be the same length; each
[CFrame](/docs/reference/engine/datatypes/CFrame.md) transforms the bone from the bind pose to the corrective
target, in the mesh's local space. Throws if the action combination is not
a valid corrective.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actions` | `Array` |  | Array or 2 or 3 [FacsActionUnit](/docs/reference/engine/enums/FacsActionUnit.md) values to apply as a corrective pose. |
| `boneIds` | `Array` |  | Bones to set a [CFrame](/docs/reference/engine/datatypes/CFrame.md) for this pose. |
| `cframes` | `Array` |  | [CFrame](/docs/reference/engine/datatypes/CFrame.md) transforms for the bones in this corrective pose.  Each bone [CFrame](/docs/reference/engine/datatypes/CFrame.md) transforms the bone from the initial bone [CFrame](/docs/reference/engine/datatypes/CFrame.md) in the bind pose of the mesh to the combined bone [CFrame](/docs/reference/engine/datatypes/CFrame.md) for this pose. All [CFrames](/docs/reference/engine/datatypes/CFrame.md) are in the mesh's local space. |

**Returns:** `()`

### Method: EditableMesh:SetFacsPose

**Signature:** `EditableMesh:SetFacsPose(action: FacsActionUnit, boneIds: Array, cframes: Array): ()`

Sets all bone transforms for a FACS base pose (a single action unit). The
`boneIds` and `cframes` arrays must be the same length; each
[CFrame](/docs/reference/engine/datatypes/CFrame.md) transforms the bone from the bind pose to the target
pose, in the mesh's local space. All referenced bones must be virtual
(non-virtual bones throw an error). This replaces any previously defined
pose for the given action unit.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `action` | `FacsActionUnit` |  | FACS action unit to set the pose for. |
| `boneIds` | `Array` |  | Bones for which to set a [CFrame](/docs/reference/engine/datatypes/CFrame.md) for this pose. |
| `cframes` | `Array` |  | [CFrame](/docs/reference/engine/datatypes/CFrame.md) transforms for the bones in this pose.  Each bone [CFrame](/docs/reference/engine/datatypes/CFrame.md) transforms the bone from the initial bone [CFrame](/docs/reference/engine/datatypes/CFrame.md) in the bind pose of the mesh to the combined bone [CFrame](/docs/reference/engine/datatypes/CFrame.md) for this pose. All [CFrames](/docs/reference/engine/datatypes/CFrame.md) are in the mesh's local space. |

**Returns:** `()`

### Method: EditableMesh:SetNormal

**Signature:** `EditableMesh:SetNormal(normalId: int64, normal: Vector3): ()`

Set the normal for a normal ID. This will change the normal value for
every face vertex which is using the normal ID.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `normalId` | `int64` |  | Normal ID for which to set the normal vector. |
| `normal` | `Vector3` |  | Normal vector to set. |

**Returns:** `()`

### Method: EditableMesh:SetPosition

**Signature:** `EditableMesh:SetPosition(vertexId: int64, p: Vector3): ()`

Sets a vertex position in the mesh's local object space. Please note that
collision and other physics data on linked [MeshParts](/docs/reference/engine/classes/MeshPart.md) is
not updated until you call [AssetService:CreateMeshPartAsync()](/docs/reference/engine/classes/AssetService.md) and
[MeshPart:ApplyMesh()](/docs/reference/engine/classes/MeshPart.md).

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID of the vertex to position. |
| `p` | `Vector3` |  | Position in the mesh's local object space. |

**Returns:** `()`

### Method: EditableMesh:SetUV

**Signature:** `EditableMesh:SetUV(uvId: int64, uv: Vector2): ()`

Sets the [Vector2](/docs/reference/engine/datatypes/Vector2.md) texture coordinate for a UV ID. This changes
the UV mapping for every face corner that references this UV ID.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `uvId` | `int64` |  | UV ID for which to set the UV coordinates. |
| `uv` | `Vector2` |  | UV coordinates. |

**Returns:** `()`

### Method: EditableMesh:SetVertexBones

**Signature:** `EditableMesh:SetVertexBones(vertexId: int64, boneIDs: Array): ()`

Assign a list of bones with the vertex for skinning.

Corresponds with the skinning blend weights used in
[SetVertexBoneWeights()](/docs/reference/engine/classes/EditableMesh.md). In
other words,
[GetVertexBoneWeights(vertexId)[i]](/docs/reference/engine/classes/EditableMesh.md)
is the weight on this vertex for
[GetVertexBones(vertexId)[i]](/docs/reference/engine/classes/EditableMesh.md).

This method should be called before calling
[SetVertexBoneWeights()](/docs/reference/engine/classes/EditableMesh.md).

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID to set vertex skinning bones. |
| `boneIDs` | `Array` |  | Bone IDs to use with this vertex for skinning. |

**Returns:** `()`

### Method: EditableMesh:SetVertexBoneWeights

**Signature:** `EditableMesh:SetVertexBoneWeights(vertexId: int64, boneWeights: Array): ()`

Sets skinning blend weights for each bone associated with the vertex.

Corresponds with the bone IDs used in
[SetVertexBones()](/docs/reference/engine/classes/EditableMesh.md). In other words,
[GetVertexBoneWeights(vertexId)[i]](/docs/reference/engine/classes/EditableMesh.md)
is the weight on this vertex for
[GetVertexBones(vertexId)[i]](/docs/reference/engine/classes/EditableMesh.md).

This method should be called after calling
[SetVertexBones()](/docs/reference/engine/classes/EditableMesh.md).

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID on which to set skinning blend weights. |
| `boneWeights` | `Array` |  | Skinning blend weights to set on the vertex. |

**Returns:** `()`

### Method: EditableMesh:SetVertexFaceColor

**Signature:** `EditableMesh:SetVertexFaceColor(vertexId: int64, faceId: int64, colorId: int64): ()`

Sets the color ID for a specific corner of a face, identified by the
vertex/face pair. This is equivalent to changing just one element of the
array set by [SetFaceColors()](/docs/reference/engine/classes/EditableMesh.md), and is
useful for creating or removing a color seam at a single vertex without
affecting the other corners of the face.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID. |
| `faceId` | `int64` |  | Face ID. |
| `colorId` | `int64` |  | Color ID to set for the vertex/face pair. |

**Returns:** `()`

### Method: EditableMesh:SetVertexFaceNormal

**Signature:** `EditableMesh:SetVertexFaceNormal(vertexId: int64, faceId: int64, normalId: int64): ()`

Sets the normal ID for a specific corner of a face, identified by the
vertex/face pair. This is equivalent to changing just one element of the
array set by [SetFaceNormals()](/docs/reference/engine/classes/EditableMesh.md), and
is useful for creating or removing a hard edge at a single vertex without
affecting the other corners of the face.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID. |
| `faceId` | `int64` |  | Face ID. |
| `normalId` | `int64` |  | Normal ID to set for the vertex/face pair. |

**Returns:** `()`

### Method: EditableMesh:SetVertexFaceUV

**Signature:** `EditableMesh:SetVertexFaceUV(vertexId: int64, faceId: int64, uvId: int64): ()`

Sets the UV ID for a specific corner of a face, identified by the
vertex/face pair. This is equivalent to changing just one element of the
array set by [SetFaceUVs()](/docs/reference/engine/classes/EditableMesh.md), and is useful
for creating or removing a UV seam at a single vertex without affecting
the other corners of the face.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `vertexId` | `int64` |  | Vertex ID. |
| `faceId` | `int64` |  | Face ID. |
| `uvId` | `int64` |  | UV ID to set for the vertex/face pair. |

**Returns:** `()`

### Method: EditableMesh:Triangulate

**Signature:** `EditableMesh:Triangulate(): ()`

Splits every quad face on the mesh into two triangle faces each. A
heuristic is used to determine which diagonal each quad should be split
along to produce better-shaped triangles. If your code relies on faces
being triangles, call this method after
[AssetService:CreateEditableMeshAsync()](/docs/reference/engine/classes/AssetService.md), which may produce quad
faces.

*Security: None · Thread Safety: Unsafe · Capabilities: DynamicGeneration*

**Returns:** `()`

### Method: EditableMesh:GetFacesWithAttribute

**Signature:** `EditableMesh:GetFacesWithAttribute(id: int64): Array`

> **Deprecated:** This method is deprecated. Do not use it for new work.

Returns a list of faces that use a given vertex ID, normal ID, UV ID, or
color ID.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `id` | `int64` |  | Attribute ID for which to find faces that use it. |

**Returns:** `Array` — List of face IDs which use the given attribute ID.

### Method: EditableMesh:GetVerticesWithAttribute

**Signature:** `EditableMesh:GetVerticesWithAttribute(id: int64): Array`

> **Deprecated:** This method is deprecated. Do not use it for new work.

Returns a list of vertices that use a given face ID, normal ID, UV ID, or
color ID.

*Security: None · Thread Safety: Safe · Capabilities: DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `id` | `int64` |  | Attribute ID for which to find vertices that use it. |

**Returns:** `Array` — List of vertex IDs which use the given attribute ID.

## Inherited Members

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some