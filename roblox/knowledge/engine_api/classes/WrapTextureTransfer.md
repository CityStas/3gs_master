---
name: WrapTextureTransfer
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "WrapTextureTransfer allows a parent Decal to be wrapped around its parent MeshPart based on the cage of its WrapTarget."
---

# Class: WrapTextureTransfer

> [WrapTextureTransfer](/docs/reference/engine/classes/WrapTextureTransfer.md) allows a parent [Decal](/docs/reference/engine/classes/Decal.md) to be wrapped around
> its parent [MeshPart](/docs/reference/engine/classes/MeshPart.md) based on the cage of its [WrapTarget](/docs/reference/engine/classes/WrapTarget.md).

## Description

WrapTextureTransfer provides an alternative projection mode for [Decal](/docs/reference/engine/classes/Decal.md)
where this [Decal](/docs/reference/engine/classes/Decal.md) is fit to the parent [MeshPart](/docs/reference/engine/classes/MeshPart.md) based on it's
CageMesh provided in [WrapTarget](/docs/reference/engine/classes/WrapTarget.md).

This is useful as it allows fitting of Decals to a wide variety of differently
shaped MeshParts that share a similar WrapTarget CageMesh topology. By
authoring textures that are in the WrapTarget UV space, these textures can be
reused across many different MeshParts with different texture layouts.

- DataModel Structure
  - [MeshPart](/docs/reference/engine/classes/MeshPart.md)
    - [WrapTarget](/docs/reference/engine/classes/WrapTarget.md)
    - [Decal](/docs/reference/engine/classes/Decal.md)
      - [WrapTextureTransfer](/docs/reference/engine/classes/WrapTextureTransfer.md)

A way to visualize how this works is to imagine the Decals textures on the
WrapTarget CageMesh, which is wrapped around the MeshPart. These textures are
then projected from the CageMesh onto the MeshPart surface. Geometry that is
internal to the MeshPart, or that is not covered by the CageMesh, will not
receive any projected decal textures. Segmented regions of the target
[MeshPart](/docs/reference/engine/classes/MeshPart.md) are used to improve projection quality near holes or
boundaries in the CageMesh.

## Properties

### Property: WrapTextureTransfer.ReferenceCageMeshContent

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
    "AvatarAppearance"
  ]
}
```

The reference cage mesh is the cage mesh that the texture was authored
for. This target cage mesh defined in [WrapTarget](/docs/reference/engine/classes/WrapTarget.md) is pruned against
this `ReferenceCageMeshContent`. If the target cage mesh contains vertices
or faces that are not present in the reference cage mesh, these vertices
and faces are removed from the target cage mesh before performing the
texture transfer. If there are no shared UVs between
`ReferenceCageMeshContent` and cage mesh defined in [WrapTarget](/docs/reference/engine/classes/WrapTarget.md),
the texture transfer fails.

When not defined, the cage in [WrapTarget](/docs/reference/engine/classes/WrapTarget.md) in ancestor
[MeshPart](/docs/reference/engine/classes/MeshPart.md) is used for transfer without any pruning or validation.

### Property: WrapTextureTransfer.UVMaxBound

```json
{
  "type": "Vector2",
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
    "AvatarAppearance"
  ]
}
```

Determines the maximum bound of the UV space to include in the transfer.
Areas of the cage mesh with UV values greater than the maximum bound
aren't included when applying the texture.

The Decal textures apply to the parent [MeshPart](/docs/reference/engine/classes/MeshPart.md) with the textures
scaling linearly between UVMinBound and UVMaxBound.

When set to default -inf, the maximum UV value is used from WrapTarget's
cage.

### Property: WrapTextureTransfer.UVMinBound

```json
{
  "type": "Vector2",
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
    "AvatarAppearance"
  ]
}
```

Determines the minimum bound of the UV space to include in the transfer.
Areas of the cage mesh with UV values smaller than the minimum bound
aren't included when applying the texture.

The Decal textures apply to the parent [MeshPart](/docs/reference/engine/classes/MeshPart.md) with the textures
scaling linearly between UVMinBound and UVMaxBound.

When set to default inf, uses the minimum UV value from WrapTarget's cage.

## Methods

### Method: WrapTextureTransfer:PrepareProjectionMeshDataAsync

**Signature:** `WrapTextureTransfer:PrepareProjectionMeshDataAsync(): ()`

Prepares this [WrapTextureTransfer](/docs/reference/engine/classes/WrapTextureTransfer.md) for use as the
`projectionSource` in [EditableImage:DrawImageProjected()](/docs/reference/engine/classes/EditableImage.md) and
[EditableImage:SampleImageProjected()](/docs/reference/engine/classes/EditableImage.md). This method takes no
parameters, yields until preparation completes, and returns no value.

This allows projected texture editing, such as painting makeup on a
player's current head, without creating an [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) from the
target asset or requiring permission to create one. The prepared data is
cached internally; it is not returned to scripts and cannot be inspected,
converted to [Content](/docs/reference/engine/datatypes/Content.md), or published.

The [WrapTextureTransfer](/docs/reference/engine/classes/WrapTextureTransfer.md) must be parented to a [Decal](/docs/reference/engine/classes/Decal.md) whose
parent is a [MeshPart](/docs/reference/engine/classes/MeshPart.md) with mesh content and a valid
[WrapTarget](/docs/reference/engine/classes/WrapTarget.md) child. This hierarchy must be in the data model.
Configure [WrapTextureTransfer.ReferenceCageMeshContent](/docs/reference/engine/classes/WrapTextureTransfer.md),
[WrapTextureTransfer.UVMinBound](/docs/reference/engine/classes/WrapTextureTransfer.md), and
[WrapTextureTransfer.UVMaxBound](/docs/reference/engine/classes/WrapTextureTransfer.md) as needed before calling this
method.

The prepared data combines the target mesh's positions, normals, and
triangle connectivity within the region covered by the transfer with the
transferred UVs computed from the current cage configuration and UV
bounds. The geometry is scaled to match the target [MeshPart](/docs/reference/engine/classes/MeshPart.md)'s
current [BasePart.Size](/docs/reference/engine/classes/BasePart.md). Projection positions and directions use the
target MeshPart's local space.

Preparation is reused across projected image operations while the data
remains valid. Changes to the target mesh or its size, cage configuration,
UV bounds, or hierarchy invalidate the cached data. Call this method again
after such a change. Both projection methods raise an error if preparation
has not completed successfully or the cached data has been invalidated.
Passing an [EditableMesh](/docs/reference/engine/classes/EditableMesh.md) to those methods does not require this
preparation.

Use `pcall()` to handle preparation errors, including invalid hierarchy,
unavailable mesh or cage data, failed UV transfer, or inputs changing
during preparation. Only perform projected image operations after the call
succeeds.

For example, with the head, decal, images, reference cage content, UV
bounds, and brush configurations already defined:

```lua
local projectionTransfer = Instance.new("WrapTextureTransfer")
projectionTransfer.ReferenceCageMeshContent = referenceCageContent
projectionTransfer.UVMinBound = makeupUVMin
projectionTransfer.UVMaxBound = makeupUVMax
projectionTransfer.Parent = makeupDecal
makeupDecal.Parent = playerHead

local success, errorMessage = pcall(function()
    projectionTransfer:PrepareProjectionMeshDataAsync()
end)

if not success then
    warn("Failed to prepare makeup projection: " .. tostring(errorMessage))
    return
end

makeupTexture:DrawImageProjected(projectionTransfer, projection, brushConfig)
sampledBrush:SampleImageProjected(
    projectionTransfer,
    makeupTexture,
    projection,
    sampleBrushConfig
)
```

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance, DynamicGeneration*

**Returns:** `()`

## Inherited Members

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