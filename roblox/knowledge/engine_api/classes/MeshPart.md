---
name: MeshPart
last_updated: 2026-10-30T19:55:52Z
inherits:
  - TriangleMeshPart
  - BasePart
  - PVInstance
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "A form of BasePart that includes a physically simulated custom mesh."
---

# Class: MeshPart

> A form of [BasePart](/docs/reference/engine/classes/BasePart.md) that includes a physically simulated custom mesh.

## Description

[MeshPart](/docs/reference/engine/classes/MeshPart.md) is a form of [BasePart](/docs/reference/engine/classes/BasePart.md) that includes a physically
simulated custom mesh. Unlike with other mesh classes, such as
[SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md) and [BlockMesh](/docs/reference/engine/classes/BlockMesh.md), they are not parented to a
[BasePart](/docs/reference/engine/classes/BasePart.md) but rather behave as a [BasePart](/docs/reference/engine/classes/BasePart.md) in their own right.

The mesh and texture of a [MeshPart](/docs/reference/engine/classes/MeshPart.md) are determined by the
[MeshId](/docs/reference/engine/classes/MeshPart.md) and [TextureID](/docs/reference/engine/classes/MeshPart.md)
properties. For more information, see [Meshes](/docs/en-us/parts/meshes.md).

## Properties

### Property: MeshPart.DoubleSided

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

This property determines whether to render both faces of polygons in the
mesh. This is useful for meshes that are typically modeled as "cards" such
as a leaf, hair, or cloth.

### Property: MeshPart.MeshContent

```json
{
  "type": "Content",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "NotAccessibleSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

The mesh that is displayed on the [MeshPart](/docs/reference/engine/classes/MeshPart.md). Supports
[asset URIs](/docs/en-us/projects/assets.md#asset-uris) and
[EditableMesh](/docs/reference/engine/classes/EditableMesh.md) objects.

Note that this property cannot be changed directly by scripts, as the
collision geometry of the mesh cannot be recomputed in real time. See
[AssetService:CreateMeshPartAsync()](/docs/reference/engine/classes/AssetService.md) as a method to create a new
[MeshPart](/docs/reference/engine/classes/MeshPart.md) from a given [Content](/docs/reference/engine/datatypes/Content.md) with a specified
[CollisionFidelity](/docs/reference/engine/classes/MeshPart.md).
[MeshPart:ApplyMesh()](/docs/reference/engine/classes/MeshPart.md) can be used to overwrite the
[MeshContent](/docs/reference/engine/classes/MeshPart.md),
[TextureContent](/docs/reference/engine/classes/MeshPart.md), and collision geometry of
an existing [MeshPart](/docs/reference/engine/classes/MeshPart.md).

### Property: MeshPart.MeshId

```json
{
  "type": "ContentId",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "NotAccessibleSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

The [asset URIs](/docs/en-us/projects/assets.md#asset-uris) of the mesh
that is displayed on the [MeshPart](/docs/reference/engine/classes/MeshPart.md). Reads and writes to
[MeshContent](/docs/reference/engine/classes/MeshPart.md).

Note that this property cannot be changed directly by scripts, as the
collision geometry of the mesh cannot be recomputed in real time. See
[AssetService:CreateMeshPartAsync()](/docs/reference/engine/classes/AssetService.md) as a method to create a new
[MeshPart](/docs/reference/engine/classes/MeshPart.md) from a given [Content](/docs/reference/engine/datatypes/Content.md) with a specified
[CollisionFidelity](/docs/reference/engine/classes/MeshPart.md).
[MeshPart:ApplyMesh()](/docs/reference/engine/classes/MeshPart.md) can be used to overwrite the
[MeshContent](/docs/reference/engine/classes/MeshPart.md),
[TextureContent](/docs/reference/engine/classes/MeshPart.md), and collision geometry of
an existing [MeshPart](/docs/reference/engine/classes/MeshPart.md).

### Property: MeshPart.RenderFidelity

```json
{
  "type": "RenderFidelity",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

This property determines the level of detail that the [MeshPart](/docs/reference/engine/classes/MeshPart.md)
will be shown in. It can be set to the possible values of the
[RenderFidelity](/docs/reference/engine/enums/RenderFidelity.md) enum.

The default value is [Automatic](/docs/reference/engine/enums/RenderFidelity.md), meaning
the mesh's detail is based on its distance from the camera as outlined in
the following table.

| Distance From Camera | Render Fidelity | Example |
| --- | --- | --- |
| Less than 250 studs | Highest | |
| 250-500 studs | Medium | |
| 500 or more studs | Lowest | |

### Property: MeshPart.TextureContent

```json
{
  "type": "Content",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

The texture applied to the [MeshPart](/docs/reference/engine/classes/MeshPart.md). Supports
[asset URIs](/docs/en-us/projects/assets.md#asset-uris) and
[EditableImage](/docs/reference/engine/classes/EditableImage.md) objects.

When this property is set to [Content.none](/docs/reference/engine/datatypes/Content.md), no texture will be
applied to the mesh.

```
local Workspace = game:GetService("Workspace")

local meshPart = Workspace.MeshPart
meshPart.TextureContent = Content.none  -- No texture
```

Note that the [MeshContent](/docs/reference/engine/classes/MeshPart.md) property cannot be
directly changed during runtime but the texture can.

##### Changing a Mesh Texture

Using the [TextureContent](/docs/reference/engine/classes/MeshPart.md) property, the
texture of a mesh can be changed without having to re-upload the mesh. To
do this, a new image can be uploaded to Roblox with the desired texture.
The original texture image file can be obtained by exporting the mesh
using the **Export Selection** option in Studio. The image file will be
saved alongside the exported `.obj` file.

The new texture can then be uploaded to Roblox as a decal and its
[asset URI](/docs/en-us/projects/assets.md#asset-uris) can be applied
to the mesh using the [TextureContent](/docs/reference/engine/classes/MeshPart.md) or
[TextureID](/docs/reference/engine/classes/MeshPart.md) property.

[TextureContent](/docs/reference/engine/classes/MeshPart.md) can also be set to
reference an [EditableImage](/docs/reference/engine/classes/EditableImage.md) that has not been published yet.

```
local AssetService = game:GetService("AssetService")
local Workspace = game:GetService("Workspace")

local meshPart = Workspace.MeshPart

local editableImage = AssetService:CreateEditableImageAsync(meshPart.TextureContent)
meshPart.TextureContent = Content.fromObject(editableImage)  -- Live updates
```

When [TextureContent](/docs/reference/engine/classes/MeshPart.md) references an
[EditableImage](/docs/reference/engine/classes/EditableImage.md), the texture will live update with any edits to the
[EditableImage](/docs/reference/engine/classes/EditableImage.md) object.

##### Making a Textured Mesh

A mesh can only be textured if the mesh has been UV mapped, referring to
the practice of projecting a texture map onto a mesh. This cannot be done
using Roblox Studio and must be done using an external 3D modeling
application such as [Blender](https://www.blender.org/).

### Property: MeshPart.TextureID

```json
{
  "type": "ContentId",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

The texture applied to the [MeshPart](/docs/reference/engine/classes/MeshPart.md). Reads and writes to
[TextureContent](/docs/reference/engine/classes/MeshPart.md).

When this property is set to an empty string, no texture will be applied
to the mesh.

```
local Workspace = game:GetService("Workspace")

local meshPart = Workspace.MeshPart
meshPart.TextureID = ""  -- No texture
```

Note that the [MeshPart.MeshId](/docs/reference/engine/classes/MeshPart.md) property cannot be changed during
runtime but the texture can. See
[TextureContent](/docs/reference/engine/classes/MeshPart.md) for details.

### Property: MeshPart.HasJointOffset *(hidden)*

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "NotAccessibleSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

> **Deprecated:** This property is deprecated and should not be used in new work.

Deprecated legacy property associated with a [MeshPart](/docs/reference/engine/classes/MeshPart.md)'s internal
[JointOffset](/docs/reference/engine/classes/MeshPart.md). It is managed by the engine and
cannot be set by scripts. Do not use it in new work.

### Property: MeshPart.HasSkinnedMesh *(hidden)*

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "NotAccessibleSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

Indicates whether the mesh currently applied to the [MeshPart](/docs/reference/engine/classes/MeshPart.md)
contains skinning (bone and joint) data, such as a mesh authored with an
armature for skeletal deformation.

Defaults to `false`. The engine sets this automatically when a mesh is
loaded (`true` when the mesh data includes joints), so scripts cannot set
it.

### Property: MeshPart.JointOffset *(hidden)*

```json
{
  "type": "Vector3",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "NotAccessibleSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

> **Deprecated:** This property is deprecated and should not be used in new work.

Deprecated. A [Vector3](/docs/reference/engine/datatypes/Vector3.md) offset once used to position a skinned
mesh's joints. Defaults to `0, 0, 0` and is reset whenever a new mesh is
applied to the part. Cannot be set by scripts; do not use it in new work.

## Methods

### Method: MeshPart:ApplyMesh

**Signature:** `MeshPart:ApplyMesh(meshPart: Instance): ()`

Overwrites the [MeshContent](/docs/reference/engine/classes/MeshPart.md),
[TextureContent](/docs/reference/engine/classes/MeshPart.md), and collision geometry
properties of this [MeshPart](/docs/reference/engine/classes/MeshPart.md) from the given source `meshPart`.

Most of these properties are read-only and cannot be changed during
runtime on their own directly. To keep
[MeshContent](/docs/reference/engine/classes/MeshPart.md) and physics data in sync, they
must be updated together.

Copies the following properties:

- [MeshPart.MeshContent](/docs/reference/engine/classes/MeshPart.md) (implicitly updates
  [MeshId](/docs/reference/engine/classes/MeshPart.md))
- [MeshPart.TextureContent](/docs/reference/engine/classes/MeshPart.md) (implicitly updates
  [TextureID](/docs/reference/engine/classes/MeshPart.md))
- [MeshPart.RenderFidelity](/docs/reference/engine/classes/MeshPart.md)
- [MeshPart.CollisionFidelity](/docs/reference/engine/classes/MeshPart.md) (with any internal collision
  geometry)
- [MeshPart.FluidFidelity](/docs/reference/engine/classes/MeshPart.md) (with any internal aero geometry)
- [MeshPart.MeshSize](/docs/reference/engine/classes/MeshPart.md)

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `meshPart` | `Instance` |  | The source [MeshPart](/docs/reference/engine/classes/MeshPart.md) whose [MeshContent](/docs/reference/engine/classes/MeshPart.md), [TextureContent](/docs/reference/engine/classes/MeshPart.md), and collision geometry (along with [RenderFidelity](/docs/reference/engine/classes/MeshPart.md), [CollisionFidelity](/docs/reference/engine/classes/MeshPart.md), [FluidFidelity](/docs/reference/engine/classes/MeshPart.md), and [MeshSize](/docs/reference/engine/classes/MeshPart.md)) are copied onto this part. The object must be a [MeshPart](/docs/reference/engine/classes/MeshPart.md), otherwise the call throws an error. |

**Returns:** `()`

## Inherited Members

### From [TriangleMeshPart](/docs/reference/engine/classes/TriangleMeshPart.md)

- **Property `CollisionFidelity`** (`CollisionFidelity`): Determines the level of detail the part's physics will adhere to its mesh.
- **Property `CollisionPrecision`** (`float`): Quantifies how precise or performant a CollisionFidelity.Tunable
- **Property `FluidFidelity`** (`FluidFidelity`): Determines the geometric representation used to compute aerodynamic forces
- **Property `MeshSize`** (`Vector3`): The original size of the part's source mesh geometry, before any scaling

### From [BasePart](/docs/reference/engine/classes/BasePart.md)

- **Property `Anchored`** (`boolean`): Determines whether a part is immovable by physics.
- **Property `AssemblyAngularVelocity`** (`Vector3`): The angular velocity of the part's assembly.
- **Property `AssemblyCenterOfMass`** (`Vector3`): The center of mass of the part's assembly in world space.
- **Property `AssemblyLinearVelocity`** (`Vector3`): The linear velocity of the part's assembly.
- **Property `AssemblyMass`** (`float`): The total mass of the part's assembly.
- **Property `AssemblyRootPart`** (`BasePart`): A reference to the root part of the assembly.
- **Property `AudioCanCollide`** (`boolean`): Determines whether the part will physically interact with audio
- **Property `BackParamA`** (`float`): Determines the first parameter for the SurfaceType on the Back face of a *(deprecated, hidden)*
- **Property `BackParamB`** (`float`): Determines the second parameter for the SurfaceType on the Back face of a *(deprecated, hidden)*
- **Property `BackSurface`** (`SurfaceType`): Determines the type of surface for the back face of a part.
- **Property `BackSurfaceInput`** (`InputType`): Determines the kind of input for the Back face of a part. *(deprecated, hidden)*
- **Property `BottomParamA`** (`float`): Determines the first parameter for the SurfaceType on the Bottom face of a *(deprecated, hidden)*
- **Property `BottomParamB`** (`float`): Determines the second parameter for the SurfaceType on the Bottom face of *(deprecated, hidden)*
- **Property `BottomSurface`** (`SurfaceType`): Determines the type of surface for the bottom face of a part.
- **Property `BottomSurfaceInput`** (`InputType`): Determines the kind of input for the Bottom face of a part. *(deprecated, hidden)*
- **Property `BrickColor`** (`BrickColor`): Determines the color of a part.
- **Property `brickColor`** (`BrickColor`):  *(deprecated)*
- **Property `CanCollide`** (`boolean`): Determines whether a part may collide with other parts.
- **Property `CanQuery`** (`boolean`): Determines whether the part is considered during spatial query operations.
- **Property `CanTouch`** (`boolean`): Determines if Touched and
- **Property `CastShadow`** (`boolean`): Determines whether or not a part casts a shadow.
- **Property `CenterOfMass`** (`Vector3`): Describes the local position of a part's center of mass, relative to its
- **Property `CFrame`** (`CFrame`): Determines the position and orientation of the BasePart in the
- **Property `CollisionGroup`** (`string`): Describes the name of a part's collision group.
- **Property `CollisionGroupId`** (`int`): Describes the automatically set ID number of a part's collision group. *(deprecated)*
- **Property `Color`** (`Color3`): Determines the color of a part.
- **Property `CurrentPhysicalProperties`** (`PhysicalProperties`): Indicates the current physical properties of the part.
- **Property `CustomPhysicalProperties`** (`PhysicalProperties`): Determines several physical properties of a part.
- **Property `Elasticity`** (`float`): Used to control the Elasticity of the part, but it no longer does *(deprecated, hidden)*
- **Property `EnableFluidForces`** (`boolean`): Used to enable or disable aerodynamic forces on parts and assemblies.
- **Property `ExtentsCFrame`** (`CFrame`): The CFrame of the physical extents of the BasePart.
- **Property `ExtentsSize`** (`Vector3`): The actual physical size of the BasePart as regarded by the
- **Property `Friction`** (`float`): Used to control the Friction of the part, but now it no longer does *(deprecated, hidden)*
- **Property `FrontParamA`** (`float`): Determines the first parameter for the SurfaceType on the Front face of a *(deprecated, hidden)*
- **Property `FrontParamB`** (`float`): Determines the second parameter for the SurfaceType on the Front face of a *(deprecated, hidden)*
- **Property `FrontSurface`** (`SurfaceType`): Determines the type of surface for the front face of a part.
- **Property `FrontSurfaceInput`** (`InputType`): Determines the kind of input for the Front face of a part (-Z direction). *(deprecated, hidden)*
- **Property `LeftParamA`** (`float`): Determines the first parameter for the SurfaceType on the Left face of a *(deprecated, hidden)*
- **Property `LeftParamB`** (`float`): Determines the second parameter for the SurfaceType on the Left face of a *(deprecated, hidden)*
- **Property `LeftSurface`** (`SurfaceType`): Determines the type of surface for the left face of a part.
- **Property `LeftSurfaceInput`** (`InputType`): Determines the kind of input for the Left face of a part. *(deprecated, hidden)*
- **Property `LocalTransparencyModifier`** (`float`): Determines a multiplier for BasePart.Transparency that is only *(hidden)*
- **Property `Locked`** (`boolean`): Determines whether a part is selectable in Studio.
- **Property `Mass`** (`float`): Describes the mass of the part, the product of its density and volume.
- **Property `Massless`** (`boolean`): Determines whether the part contributes to the total mass or inertia of
- **Property `Material`** (`Material`): Determines the texture and default physical properties of a part.
- **Property `MaterialVariant`** (`string`): The name of MaterialVariant.
- **Property `Orientation`** (`Vector3`): Describes the rotation of the part in the world. *(hidden)*
- **Property `PivotOffset`** (`CFrame`): Specifies the offset of the part's pivot from its CFrame.
- **Property `Position`** (`Vector3`): Describes the position of the part in the world. *(hidden)*
- **Property `ReceiveAge`** (`float`): Time since last recorded physics update. *(hidden)*
- **Property `Reflectance`** (`float`): Determines how much a part reflects the skybox.
- **Property `ResizeableFaces`** (`Faces`): Describes the faces on which a part may be resized.
- **Property `ResizeIncrement`** (`int`): Describes the smallest change in size allowable by the
- **Property `RightParamA`** (`float`): Determines the first parameter for the SurfaceType on the Right face of a *(deprecated, hidden)*
- **Property `RightParamB`** (`float`): Determines the second parameter for the SurfaceType on the Right face of a *(deprecated, hidden)*
- **Property `RightSurface`** (`SurfaceType`): Determines the type of surface for the right face of a part.
- **Property `RightSurfaceInput`** (`InputType`): Determines the kind of input for the Right face of a part (-X direction). *(deprecated, hidden)*
- **Property `RootPriority`** (`int`): The main rule in determining the root part of an assembly.
- **Property `Rotation`** (`Vector3`): The rotation of the part in degrees for the three axes.
- **Property `RotVelocity`** (`Vector3`): Determines a part's change in orientation over time. *(deprecated, hidden)*
- **Property `Size`** (`Vector3`): Determines the dimensions of a part (length, height, width).
- **Property `SpecificGravity`** (`float`): The ratio of the part's density to the density of water determined by the *(deprecated)*
- **Property `TopParamA`** (`float`): Determines the first parameter for the SurfaceType on the Top face of a *(deprecated, hidden)*
- **Property `TopParamB`** (`float`): Determines the second parameter for the SurfaceType on the Top face of a *(deprecated, hidden)*
- **Property `TopSurface`** (`SurfaceType`): Determines the type of surface for the top face of a part.
- **Property `TopSurfaceInput`** (`InputType`): Determines the kind of input for the Top face of a part (+Y direction). *(deprecated, hidden)*
- **Property `Transparency`** (`float`): Determines how much a part can be seen through (the inverse of part
- **Property `Velocity`** (`Vector3`): Determines a part's change in position over time. *(deprecated, hidden)*
- **Method `AngularAccelerationToTorque(angAcceleration: Vector3, angVelocity?: Vector3): Vector3`**: Returns the torque needed to achieve a given angular acceleration on this
- **Method `ApplyAngularImpulse(impulse: Vector3): ()`**: Apply an angular impulse to the assembly.
- **Method `ApplyImpulse(impulse: Vector3): ()`**: Apply an impulse to the assembly at the assembly's
- **Method `ApplyImpulseAtPosition(impulse: Vector3, position: Vector3): ()`**: Apply an impulse to the assembly at specified position.
- **Method `BindToCollisionSummaries(callback: Function): RBXScriptConnection`**: Subscribes to detailed per-frame contact data for the collisions this part
- **Method `BreakJoints(): ()`**: Breaks any surface connection with any adjacent part, including *(deprecated)*
- **Method `breakJoints(): ()`**:  *(deprecated)*
- **Method `CanCollideWith(part: BasePart): boolean`**: Returns whether the parts can collide with each other.
- **Method `CanSetNetworkOwnership(): Tuple`**: Checks whether you can set a part's network ownership.
- **Method `GetClosestPointOnSurface(position: Vector3): Vector3`**: Returns the closest point on the part's surface to the given point.
- **Method `GetConnectedParts(recursive?: boolean): List<BasePart>`**: Returns a table of parts connected to the object by any kind of rigid
- **Method `GetJoints(): Instances`**: Returns all Joints or Constraints connected to this part that are active
- **Method `GetMass(): float`**: Returns the value of the Mass property.
- **Method `getMass(): float`**:  *(deprecated)*
- **Method `GetNetworkOwner(): Instance`**: Returns the current player who is the network owner of this part, or `nil`
- **Method `GetNetworkOwnershipAuto(): boolean`**: Returns true if the game engine automatically decides the network owner
- **Method `GetNoCollisionConstraints(): Instances`**: Returns the enabled NoCollisionConstraint objects currently
- **Method `GetRenderCFrame(): CFrame`**: OBSOLETE. Returns a CFrame describing where the part is being rendered at. *(deprecated)*
- **Method `GetRootPart(): Instance`**: Returns the base part of an assembly of parts. *(deprecated)*
- **Method `GetTouchingParts(): Instances`**: Returns a table of all BasePart.CanCollide true parts that
- **Method `GetVelocityAtPosition(position: Vector3): Vector3`**: Returns the linear velocity of the part's assembly at the given position
- **Method `IntersectAsync(parts: Instances, collisionfidelity?: CollisionFidelity, renderFidelity?: RenderFidelity): Instance`**: Creates a new IntersectOperation from the overlapping geometry of
- **Method `IsGrounded(): boolean`**: Returns true if the object is connected to a part that will hold it in
- **Method `MakeJoints(): ()`**: Creates a joint on any side of the object that has a surface ID that can *(deprecated)*
- **Method `makeJoints(): ()`**:  *(deprecated)*
- **Method `Resize(normalId: NormalId, deltaAmount: int): boolean`**: Changes the size of an object just like using the Studio resize tool.
- **Method `resize(normalId: NormalId, deltaAmount: int): boolean`**:  *(deprecated)*
- **Method `SetNetworkOwner(playerInstance?: Player): ()`**: Sets the given player as network owner for this and all connected parts.
- **Method `SetNetworkOwnershipAuto(): ()`**: Lets the game engine dynamically decide who will handle the part's physics
- **Method `SubtractAsync(parts: Instances, collisionfidelity?: CollisionFidelity, renderFidelity?: RenderFidelity): Instance`**: Creates a new UnionOperation from the part, minus the geometry
- **Method `TorqueToAngularAcceleration(torque: Vector3, angVelocity?: Vector3): Vector3`**: Returns the angular acceleration that would result from applying a given
- **Method `UnionAsync(parts: Instances, collisionfidelity?: CollisionFidelity, renderFidelity?: RenderFidelity): Instance`**: Creates a new UnionOperation from the part, plus the geometry
- **Event `LocalSimulationTouched`**: Fires on the local client when another part comes in contact with this *(deprecated)*
- **Event `OutfitChanged`**: Fires when the part's appearance changes due to a Shirt. *(deprecated)*
- **Event `StoppedTouching`**: Fires on the local client when a part stops touching another part. *(deprecated)*
- **Event `Touched`**: Fires when a part touches another part as a result of physical movement.
- **Event `TouchEnded`**: Fires when a part stops touching another part as a result of physical

### From [PVInstance](/docs/reference/engine/classes/PVInstance.md)

- **Property `Origin`** (`CFrame`): Editor-only property that reads and sets the world CFrame of
- **Property `Pivot Offset`** (`CFrame`): Editor-only property that displays and edits the pivot's CFrame
- **Method `GetPivot(): CFrame`**: Gets the pivot of a PVInstance.
- **Method `PivotTo(targetCFrame: CFrame): ()`**: Transforms the PVInstance along with all of its descendant

### From [Instance](/docs/reference/engine/classes/Instance.md)

- **Property `Archivable`** (`boolean`): Determines if an Instance and its descendants can be cloned using
- **Property `archivable`** (`boolean`):  *(deprecated, hidden)*
- **Property `Capabilities`** (`SecurityCapabilities`): The set of capabilities allowed to be used for scripts inside this
- **Property `IsInSandbox`** (`boolean`): Indicates whether the instance is inside a sandboxed container.
- **Property `Name`** (`string`): A non-unique identifier of the Instance.
- **Property `Parent`** (`Instance`): Determines the hierarchical parent of the Instance.
- **Property `PredictionMode`** (`PredictionMode`): Reflects the client-side prediction mode applied to the instance under
- **Property `RobloxLocked`** (`boolean`): A deprecated property that used to protect CoreGui objects. *(hidden)*
- **Property `Sandboxed`** (`boolean`): When enabled, the instance can only access abilities in its `Capabilities`
- **Property `UniqueId`** (`UniqueId`): A unique identifier for the instance.
- **Method `AddTag(tag: string): ()`**: Applies a tag to the instance.
- **Method `children(): Instances`**: Returns an array of the object's children. *(deprecated)*
- **Method `ClearAllChildren(): ()`**: This method destroys all of an instance's children.
- **Method `Clone(): Instance`**: Create a copy of an instance and all its descendants, ignoring instances
- **Method `clone(): Instance`**:  *(deprecated)*
- **Method `Destroy(): ()`**: Sets the Instance.Parent property to `nil`, locks the
- **Method `destroy(): ()`**:  *(deprecated)*
- **Method `FindFirstAncestor(name: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorOfClass(className: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorWhichIsA(className: string): Instance?`**: Returns the first ancestor of the Instance for whom
- **Method `FindFirstChild(name: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance found with the given name.
- **Method `findFirstChild(name: string, recursive?: boolean): Instance`**:  *(deprecated)*
- **Method `FindFirstChildOfClass(className: string): Instance?`**: Returns the first child of the Instance whose
- **Method `FindFirstChildWhichIsA(className: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance for whom
- **Method `FindFirstDescendant(name: string): Instance?`**: Returns the first descendant found with the given Instance.Name.
- **Method `GetActor(): Actor?`**: Returns the Actor associated with the Instance, if any.
- **Method `GetAttribute(attribute: string): Variant`**: Returns the value which has been assigned to the given attribute name.
- **Method `GetAttributeChangedSignal(attribute: string): RBXScriptSignal`**: Returns an event that fires when the given attribute changes.
- **Method `GetAttributes(): Dictionary`**: Returns a dictionary of the instance's attributes.
- **Method `GetChildren(): Instances`**: Returns an array containing all of the instance's children.
- **Method `getChildren(): Instances`**:  *(deprecated)*
- **Method `GetDebugId(scopeLength?: int): string`**: Returns a coded string of the debug ID used internally by Roblox.
- **Method `GetDescendants(): Instances`**: Returns an array containing all of the descendants of the instance.
- **Method `GetFullName(): string`**: Returns a string describing the instance's ancestry.
- **Method `GetStyled(name: string, selector: string?): Variant`**: Returns the styled or explicitly modified value of the specified property,
- **Method `GetStyledPropertyChangedSignal(property: string): RBXScriptSignal`**: Returns an event that fires when the given style property changes on the
- **Method `GetTags(): Array`**: Gets an array of all tags applied to the instance.
- **Method `HasTag(tag: string): boolean`**: Check whether the instance has a given tag.
- **Method `IsAncestorOf(descendant: Instance): boolean`**: Returns true if an Instance is an ancestor of the given
- **Method `IsDescendantOf(ancestor: Instance): boolean`**: Returns `true` if an Instance is a descendant of the given
- **Method `isDescendantOf(ancestor: Instance): boolean`**:  *(deprecated)*
- **Method `IsPropertyModified(property: string): boolean`**: Returns `true` if the value stored in the specified property is not equal
- **Method `QueryDescendants(selector: string): Instances`**: Returns an array containing all descendants of the instance that match the
- **Method `Remove(): ()`**: Sets the object's `Parent` to `nil`, and does the same for all its *(deprecated)*
- **Method `remove(): ()`**:  *(deprecated)*
- **Method `RemoveTag(tag: string): ()`**: Removes a tag from the instance.
- **Method `ResetPropertyToDefault(property: string): ()`**: Resets a property to its default value.
- **Method `SetAttribute(attribute: string, value: Variant): ()`**: Sets the attribute with the given name to the given value.
- **Method `WaitForChild(childName: string, timeOut: double): Instance`**: Returns the child of the Instance with the given name. If the
- **Event `AncestryChanged`**: Fires when the Instance.Parent property of this object or one of
- **Event `AttributeChanged`**: Fires whenever an attribute is changed on the Instance.
- **Event `ChildAdded`**: Fires after an object is parented to this Instance.
- **Event `childAdded`**:  *(deprecated)*
- **Event `ChildRemoved`**: Fires after a child is removed from this Instance.
- **Event `DescendantAdded`**: Fires after a descendant is added to the Instance.
- **Event `DescendantRemoving`**: Fires immediately before a descendant of the Instance is removed.
- **Event `Destroying`**: Fires immediately before (or is deferred until after) the instance is
- **Event `StyledPropertiesChanged`**: Fires whenever any style property is changed on the instance, including

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some