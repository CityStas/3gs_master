---
name: WrapLayer
last_updated: 2026-10-30T19:55:53Z
inherits:
  - BaseWrap
  - Instance
  - Object
type: class
memory_category: Instances
summary: "The WrapLayer object defines a 3D accessory's inner and outer surfaces and other properties related to layering accessories. These surfaces, or the Inner Cage and Outer Cage, are similar to collision boxes, and describe the surfaces of which other 3D accessories can be placed without clipping or breaking."
---

# Class: WrapLayer

> The WrapLayer object defines a 3D accessory's inner and outer surfaces and
> other properties related to layering accessories. These surfaces, or the Inner
> Cage and Outer Cage, are similar to collision boxes, and describe the surfaces
> of which other 3D accessories can be placed without clipping or breaking.

## Description

The WrapLayer object defines a 3D accessory's inner and outer surfaces and
other properties related to layering accessories. These surfaces, or the Inner
Cage and Outer Cage, are similar to collision boxes, and describe the surfaces
of which other 3D accessories can be placed without clipping or breaking.

Internally, WrapLayer also uses the UV layout of the Inner and Outer cages to
match coordinates to another 3D object's cage. This powers the deformation of
objects around differently shaped avatars and underlying accessories.

## Properties

### Property: WrapLayer.AutoSkin

```json
{
  "type": "WrapLayerAutoSkin",
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
  "category": "Behavior",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

Determines whether this WrapLayer automatically transfers skinning data
from the underlying body mesh to the clothing mesh. When set to
[EnabledOverride](/docs/reference/engine/enums/WrapLayerAutoSkin.md), skinning is
applied regardless of whether the clothing mesh already has skinning data.
When set to [EnabledPreserve](/docs/reference/engine/enums/WrapLayerAutoSkin.md),
skinning is only applied if the mesh does not already have skinning data.

This property requires [StarterPlayer.LoadCharacterLayeredClothing](/docs/reference/engine/classes/StarterPlayer.md)
to be set to `Enabled` (or `Default`) in order to function. When layered
clothing is disabled, the auto-skinning pipeline does not run and this
property has no effect.

For more information, see
[Automatic Skinning Transfer](/docs/en-us/avatar/automatic-skinning-transfer.md).

### Property: WrapLayer.BindOffset

```json
{
  "type": "CFrame",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Tuning",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

This property is intended for fine-tuning purposes and is highly optional.

[CFrame](/docs/reference/engine/datatypes/CFrame.md) to adjust a binding point for a clothing item mesh.
Allows for fine-tuning of clothing items (slight adjustment of
position/rotation to get a unique look) in contexts such as community-made
avatar editors.

### Property: WrapLayer.Color

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

### Property: WrapLayer.DebugMode

```json
{
  "type": "WrapLayerDebugMode",
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

### Property: WrapLayer.Enabled

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
  "category": "Behavior",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

Allows for disabling of the [WrapLayer](/docs/reference/engine/classes/WrapLayer.md) object as if it does not
exist.

### Property: WrapLayer.Order

```json
{
  "type": "int",
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

Controls the composition order for layered clothing. Clothing items with
higher order will appear on top of clothing items with lower order. If two
items have the same order, the deformer composition order is ambiguous and
depends on serialization order. Default value is 1.

### Property: WrapLayer.ReferenceMeshContent

```json
{
  "type": "Content",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "PluginSecurity"
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

The reference mesh that defines the inner cage of a [WrapLayer](/docs/reference/engine/classes/WrapLayer.md),
stored as a [Content](/docs/reference/engine/datatypes/Content.md) value. Together with the outer cage from
[CageMeshContent](/docs/reference/engine/classes/BaseWrap.md), the inner cage describes
the surfaces used to fit and deform the accessory around an avatar and
underlying accessories without clipping. A [WrapLayer](/docs/reference/engine/classes/WrapLayer.md) is only
considered valid once both its cage mesh and its reference mesh are set.

The reference mesh establishes the standard topology and UV coordinates
used for index matching. It is expected that for all catalog avatars this
points to one of the 15 standard reference meshes provided by Roblox, but
for some NPCs or a custom avatar system it might point to a different
mesh. This property is normally set up automatically by the Importer.

This [Content](/docs/reference/engine/datatypes/Content.md)-typed property is the successor to
[WrapLayer.ReferenceMeshId](/docs/reference/engine/classes/WrapLayer.md) and reads and writes the same underlying
storage. Defaults to an empty [Content](/docs/reference/engine/datatypes/Content.md).

### Property: WrapLayer.ReferenceMeshId

```json
{
  "type": "ContentId",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "PluginSecurity"
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

AssetID for reference mesh used to define Inner Cage of a 3D object

Reference mesh is used to define standard topology and UV coordinates for
index matching. It is expected that for all catalog avatars, this will
point to one of 15 standard reference meshes provided by Roblox. But for
some NPCs or a custom avatar system, this might point to other meshes.

Note: this property is set up automatically by the FBX importer

### Property: WrapLayer.ReferenceOrigin

```json
{
  "type": "CFrame",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "PluginSecurity"
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

Reference mesh offset relative to parent MeshPart (in the parent MeshPart
space)

Note: this property is set up automatically by the FBX importer

### Property: WrapLayer.ReferenceOriginWorld

```json
{
  "type": "CFrame",
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
  "category": "Data",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

Reference mesh offset relative to parent MeshPart (in the world space)

Note: this property is set up automatically by the FBX importer

### Property: WrapLayer.Puffiness

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
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

Controls how much underlying clothing items inflate the current clothing
item.

Valid range is -1 to 1. A value of -1 compresses the clothing, body, and
all underlying layers such that the clothing itself takes the shape of the
body. A value of 0 makes the clothing item fit as if it was the only piece
of clothing being worn, compressing all underlying layers. A value of 1
(default) never compresses anything and infinitely inflates over
underlying clothing items.

### Property: WrapLayer.ShrinkFactor

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
  "category": "Tuning",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

This property is intended for fine-tuning purposes and is highly optional.

Allows slight shrinking/expanding of the resulting render mesh, without
affecting any other layers. This is useful in rare cases when the clothing
mesh does not precisely fit the underlying clothing layers (the cage is
usually slightly overestimated atop the real shape to avoid layer
interpenetration). Even slight overestimation has the tendency to
accumulate, especially when there are a lot of layers. While this is
usually not critical, some items like backpacks may be problematic.

Valid range is -1 to 1. A value of -1 will maximally expand while a value
of 1 will maximally shrink. A value of 0 (default) has no effect.

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