---
name: RenderSettings
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
  - NotBrowsable
summary: "A singleton settings class that exposes rendering configuration for graphics quality, framerate management, and debug visualization in Roblox Studio."
---

# Class: RenderSettings

> A singleton settings class that exposes rendering configuration for graphics
> quality, framerate management, and debug visualization in Roblox Studio.

## Description

`RenderSettings` is a singleton class which lets developers debug components
of Roblox's graphics engine. It can be found in Roblox Studio's settings under
the **Rendering** tab.

## Properties

### Property: RenderSettings.AutoFRMLevel

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Debug"
}
```

Sets the starting quality level of the framerate manager when
[EnableFRM](/docs/reference/engine/classes/RenderSettings.md) is set to `true`.

### Property: RenderSettings.EagerBulkExecution

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Performance"
}
```

When set to `true`, all scene updates will be given an unlimited budget,
regardless of how computationally expensive it may be. This ensures each
frame will look as it should, at the cost of a more unstable frame rate.

### Property: RenderSettings.EditQualityLevel

```json
{
  "type": "QualityLevel",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Performance"
}
```

Sets the graphics quality level in Roblox Studio when
[EnableFRM](/docs/reference/engine/classes/RenderSettings.md) is set to `false`.

### Property: RenderSettings.Enable VR Mode

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "General"
}
```

When set to `true`, virtual reality (VR) mode is enabled. This property
reflects the same underlying setting as
[UserGameSettings.VREnabled](/docs/reference/engine/classes/UserGameSettings.md), so reading or writing it reads or
writes that shared value. Defaults to `false`.

### Property: RenderSettings.ExportMergeByMaterial

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "General"
}
```

Controls how materials are written during `.obj` export from Studio. When
set to `true`, parts that share the same material appearance are merged
into shared material definitions in the exported `.obj` file, reducing
material count. When set to `false`, each part receives its own
independent material definition. Defaults to `false`.

### Property: RenderSettings.FrameRateManager

```json
{
  "type": "FramerateManagerMode",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "General"
}
```

Determines how the framerate manager (FRM) manages rendering quality using
a [FramerateManagerMode](/docs/reference/engine/enums/FramerateManagerMode.md) value. When set to
[FramerateManagerMode.Automatic](/docs/reference/engine/enums/FramerateManagerMode.md), the engine decides whether to
enable FRM quality adjustment based on context (typically enabled during
gameplay). When set to [FramerateManagerMode.On](/docs/reference/engine/enums/FramerateManagerMode.md), the FRM is always
active. When set to [FramerateManagerMode.Off](/docs/reference/engine/enums/FramerateManagerMode.md), the FRM does not
adjust quality and block culling is forced to the lowest-quality distance
setting. Defaults to [FramerateManagerMode.Automatic](/docs/reference/engine/enums/FramerateManagerMode.md).

### Property: RenderSettings.GraphicsMode

```json
{
  "type": "GraphicsMode",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "General"
}
```

Determines which graphics rendering API Roblox uses on startup, specified
as a [GraphicsMode](/docs/reference/engine/enums/GraphicsMode.md) value. When set to [GraphicsMode.Automatic](/docs/reference/engine/enums/GraphicsMode.md),
the engine selects the best available backend for the current platform.
Available options are platform-dependent; for example,
[GraphicsMode.Metal](/docs/reference/engine/enums/GraphicsMode.md) is only available on macOS and
[GraphicsMode.Direct3D11](/docs/reference/engine/enums/GraphicsMode.md) is only available on Windows. If an
unsupported mode is selected, the engine silently falls back to
[GraphicsMode.Automatic](/docs/reference/engine/enums/GraphicsMode.md). Defaults to [GraphicsMode.Automatic](/docs/reference/engine/enums/GraphicsMode.md).

Because the graphics API is initialized at startup, changing this property
only takes effect after restarting Roblox Studio.

### Property: RenderSettings.MeshCacheSize

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Cache"
}
```

The size in bytes of the mesh cache. Defaults to 32 MiB.

### Property: RenderSettings.MeshPartDetailLevel

```json
{
  "type": "MeshPartDetailLevel",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Debug"
}
```

Determines the mode for the selection of detail levels for mesh parts. For
a good balance between performance and fidelity, this should be set to
[MeshPartDetailLevel.DistanceBased](/docs/reference/engine/enums/MeshPartDetailLevel.md) (default), which is what the
client uses.

Note that the [MeshPart.RenderFidelity](/docs/reference/engine/classes/MeshPart.md) needs to be set to
[RenderFidelity.Automatic](/docs/reference/engine/enums/RenderFidelity.md) for this to work. If you set it to
[RenderFidelity.Precise](/docs/reference/engine/enums/RenderFidelity.md), you will always see the higher resolution
version and the [MeshPartDetailLevel](/docs/reference/engine/enums/MeshPartDetailLevel.md) value will be ignored for that
[MeshPart](/docs/reference/engine/classes/MeshPart.md).

### Property: RenderSettings.QualityLevel

```json
{
  "type": "QualityLevel",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Performance"
}
```

If [EnableFRM](/docs/reference/engine/classes/RenderSettings.md) is set to `true`, this
property controls the quality level in Roblox Studio.

### Property: RenderSettings.ReloadAssets

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Debug"
}
```

When set to `true`, Roblox Studio will automatically reload changes that
are made to files in Roblox's `content` folder.

### Property: RenderSettings.RenderCSGTrianglesDebug

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Debug"
}
```

When set to `true`, a wireframe of polygons will be shown on all
[PartOperation](/docs/reference/engine/classes/PartOperation.md) objects.

### Property: RenderSettings.ShowBoundingBoxes

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Debug"
}
```

If set to `true`, renders bounding boxes around each individual rendered
entity in the scene.

### Property: RenderSettings.ViewMode

```json
{
  "type": "ViewMode",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Debug"
}
```

Studio only. Determines which debug rendering visualization is drawn over
the viewport, using a value of [ViewMode](/docs/reference/engine/enums/ViewMode.md). Defaults to
[ViewMode.None](/docs/reference/engine/enums/ViewMode.md), which disables the overlay. Other values enable
overdraw visualizations for geometry complexity, transparency, or decals.

### Property: RenderSettings.EnableFRM *(hidden)*

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Debug"
}
```

When set to `true`, the framerate manager (FRM) dynamically adjusts the
rendering quality level during gameplay to maintain a stable framerate.
When set to `false`, the quality level is fixed at
[RenderSettings.EditQualityLevel](/docs/reference/engine/classes/RenderSettings.md) and no automatic adjustment
occurs. Defaults to `true`.

The [AutoFRMLevel](/docs/reference/engine/classes/RenderSettings.md) property reports the
current quality level that the FRM has assigned when this property is
enabled.

## Methods

### Method: RenderSettings:GetMaxQualityLevel

**Signature:** `RenderSettings:GetMaxQualityLevel(): int`

Returns the total number of quality levels available in the rendering
quality system. Quality levels are numbered from
[QualityLevel.Automatic](/docs/reference/engine/enums/QualityLevel.md) (0) through [QualityLevel.Level21](/docs/reference/engine/enums/QualityLevel.md)
(21), so this method returns 22. Use `GetMaxQualityLevel() - 1` to obtain
the highest numeric quality level.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `int` — The total number of quality levels available in the rendering system.

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