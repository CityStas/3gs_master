---
name: WrapTarget
last_updated: 2026-10-30T19:55:53Z
inherits:
  - BaseWrap
  - Instance
  - Object
type: class
memory_category: Instances
summary: "The WrapTarget object defines a target. A target is the 3D body with only an outer surface, or an Outer Cage."
---

# Class: WrapTarget

> The WrapTarget object defines a target. A target is the 3D body with only an
> outer surface, or an Outer Cage.

## Description

The WrapTarget object defines a target. A target is the 3D body with only an
outer surface, or an Outer Cage.

This target, often an Avatar, is what 3D accessories (using WrapLayer) will be
applied to, allowing multiple accessories items to naturally layer over the
source target.

## Properties

### Property: WrapTarget.Color

```json
{
  "type": "Color3",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Debug",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

Sets color used for the debug rendering. See [WrapTarget.DebugMode](/docs/reference/engine/classes/WrapTarget.md)

### Property: WrapTarget.DebugMode

```json
{
  "type": "WrapTargetDebugMode",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Debug",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

Allows switching between different debugging visualization modes for cage
meshes.

### Property: WrapTarget.Stiffness

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

Defines how much the body mesh can be compressed by clothing. Super tight
clothing may lead to an intersection between the clothing mesh and body
mesh. To solve this visual artifact, the deformer can compress the body
mesh slightly to solve possible intersections.

Valid range is 0 to 1. A value of 0 will compress the body mesh as much as
necessary to ensure that the intersections are eliminated (visible body
parts might look a little bit deformed). A value of 1 will prevent the
body mesh from being compressed (may lead to visible intersections or
Z-fighting). A value of 0.9 (default) is a reasonable default that solves
most of the intersections without introducing any significant body
deformation.

## Methods

### Method: WrapTarget:CreateTextureInCageSpaceAsync

**Signature:** `WrapTarget:CreateTextureInCageSpaceAsync(texture: EditableImage, options: Dictionary?): EditableImage`

Creates a new [EditableImage](/docs/reference/engine/classes/EditableImage.md) by transferring `texture` from the UV
space of this [WrapTarget](/docs/reference/engine/classes/WrapTarget.md)'s parent [MeshPart](/docs/reference/engine/classes/MeshPart.md) into the UV
space of the WrapTarget's cage. This method yields until the transfer is
complete and does not modify the input image.

For example, after a player paints makeup onto a head mesh in an
in-experience creation tool, use this method to transfer the texture into
cage UV space before uploading it for use with
[WrapTextureTransfer](/docs/reference/engine/classes/WrapTextureTransfer.md). This method also supports cage-space texture
transfers unrelated to makeup. To transfer a texture in the opposite
direction, use [WrapTarget:CreateTextureInTargetSpaceAsync()](/docs/reference/engine/classes/WrapTarget.md).

Use `options` to specify a region of cage UV space. Each supplied bound
must be a finite [Vector2](/docs/reference/engine/datatypes/Vector2.md). If both bounds are supplied,
`MaxUVBounds` must be greater than `MinUVBounds` on both axes.
Unrecognized option keys raise an error.

This method requires the WrapTarget to be parented to a [MeshPart](/docs/reference/engine/classes/MeshPart.md)
with valid mesh and cage data. It raises an error if the input or options
are invalid, required mesh data cannot be loaded, or the transfer fails.
If the device-specific editable memory budget is exhausted, it returns
`nil`. See [EditableImage](/docs/reference/engine/classes/EditableImage.md) for additional usage requirements.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance, DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `texture` | `EditableImage` |  | The [EditableImage](/docs/reference/engine/classes/EditableImage.md) in the UV space of this [WrapTarget](/docs/reference/engine/classes/WrapTarget.md)'s parent [MeshPart](/docs/reference/engine/classes/MeshPart.md). |
| `options` | `Dictionary?` |  | Optional dictionary containing controls for the transfer:  - `MinUVBounds` – A [Vector2](/docs/reference/engine/datatypes/Vector2.md) specifying the minimum cage UV   bound. - `MaxUVBounds` – A [Vector2](/docs/reference/engine/datatypes/Vector2.md) specifying the maximum cage UV   bound.  Each omitted bound is calculated from the cage mesh. If neither is specified, the bounds include the entire cage. |

**Returns:** `EditableImage` — A new [EditableImage](/docs/reference/engine/classes/EditableImage.md) in cage UV space, or `nil` if the
device-specific editable memory budget is exhausted.

### Method: WrapTarget:CreateTextureInTargetSpaceAsync

**Signature:** `WrapTarget:CreateTextureInTargetSpaceAsync(texture: EditableImage, wrapTextureTransfer: WrapTextureTransfer): EditableImage`

Creates a new [EditableImage](/docs/reference/engine/classes/EditableImage.md) by transferring `texture` from cage UV
space into the UV space of this [WrapTarget](/docs/reference/engine/classes/WrapTarget.md)'s parent
[MeshPart](/docs/reference/engine/classes/MeshPart.md). This method yields until the transfer is complete and
does not modify the input image.

The `wrapTextureTransfer` supplies the optional reference cage through
[WrapTextureTransfer.ReferenceCageMeshContent](/docs/reference/engine/classes/WrapTextureTransfer.md) and the cage UV
bounds through [WrapTextureTransfer.UVMinBound](/docs/reference/engine/classes/WrapTextureTransfer.md) and
[WrapTextureTransfer.UVMaxBound](/docs/reference/engine/classes/WrapTextureTransfer.md). Use a WrapTextureTransfer under a
[Decal](/docs/reference/engine/classes/Decal.md) on the same MeshPart as the WrapTarget.

For example, use this method to transfer a makeup texture you own into a
head mesh's UV space so players can edit it directly on the head in an
in-experience creation tool. This method also supports target-space
texture transfers unrelated to makeup. To transfer the edited texture back
into cage UV space, use
[WrapTarget:CreateTextureInCageSpaceAsync()](/docs/reference/engine/classes/WrapTarget.md).

This method requires the WrapTarget to be parented to a [MeshPart](/docs/reference/engine/classes/MeshPart.md)
with valid mesh and cage data. It raises an error if either input is
invalid, required mesh data cannot be loaded, or the transfer fails. If
the device-specific editable memory budget is exhausted, it returns `nil`.
See [EditableImage](/docs/reference/engine/classes/EditableImage.md) for additional usage requirements.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance, DynamicGeneration*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `texture` | `EditableImage` |  | The [EditableImage](/docs/reference/engine/classes/EditableImage.md) in cage UV space. |
| `wrapTextureTransfer` | `WrapTextureTransfer` |  | The [WrapTextureTransfer](/docs/reference/engine/classes/WrapTextureTransfer.md) associated with the same parent [MeshPart](/docs/reference/engine/classes/MeshPart.md) as this [WrapTarget](/docs/reference/engine/classes/WrapTarget.md). |

**Returns:** `EditableImage` — A new [EditableImage](/docs/reference/engine/classes/EditableImage.md) in the parent [MeshPart](/docs/reference/engine/classes/MeshPart.md)'s UV space,
or `nil` if the device-specific editable memory budget is exhausted.

## Inherited Members

### From [BaseWrap](/docs/reference/engine/classes/BaseWrap.md)

- **Property `CageMeshContent`** (`Content`): The cage mesh this wrap uses to deform geometry, stored as a
- **Property `CageMeshId`** (`ContentId`): Asset ID for cage mesh.
- **Property `CageOrigin`** (`CFrame`): Cage mesh offset relative to parent MeshPart.
- **Property `CageOriginWorld`** (`CFrame`): Cage mesh offset in world space.
- **Property `HSRAssetId`** (`ContentId`): Asset ID for the hidden surface removal (HSR) data used by layered
- **Property `HSRContent`** (`Content`): The hidden surface removal data for this wrap, stored as a
- **Property `ImportOrigin`** (`CFrame`): Describes where a global zero was while authoring the cage mesh in an
- **Property `ImportOriginWorld`** (`CFrame`): Describes where the origin (in world space) was while authoring the cage

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