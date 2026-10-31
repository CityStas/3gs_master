---
name: Texture
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Decal
  - FaceInstance
  - Instance
  - Object
type: class
memory_category: GraphicsTexture
summary: "Applies a repeating image texture to the face of a parent BasePart."
---

# Class: Texture

> Applies a repeating image texture to the face of a parent [BasePart](/docs/reference/engine/classes/BasePart.md).

## Description

A [Texture](/docs/reference/engine/classes/Texture.md) object applies a repeating image texture to the face of a
parent [BasePart](/docs/reference/engine/classes/BasePart.md). The affected face is dependent on the
[Face](/docs/reference/engine/classes/Texture.md) property. Unlike [Decals](/docs/reference/engine/classes/Decal.md), the texture
applied by a [Texture](/docs/reference/engine/classes/Texture.md) will repeat when the parent [BasePart](/docs/reference/engine/classes/BasePart.md) is
resized, with the size of the repeating textures determined by the
[StudsPerTileU](/docs/reference/engine/classes/Texture.md) and
[StudsPerTileV](/docs/reference/engine/classes/Texture.md) properties.

The applied image texture is determined by its
[ColorMapContent](/docs/reference/engine/classes/Texture.md) property. For details on how
to upload images, see
[asset management](/docs/en-us/projects/assets.md#asset-management).

For more information, review
[textures and decals](/docs/en-us/parts/textures-decals.md). See also:

- [Decal](/docs/reference/engine/classes/Decal.md) for non-repeating surface images.
- [MeshPart.TextureContent](/docs/reference/engine/classes/MeshPart.md) to apply an image texture to a
  [MeshPart](/docs/reference/engine/classes/MeshPart.md).
- [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) to apply an [ImageLabel](/docs/reference/engine/classes/ImageLabel.md) or [ImageButton](/docs/reference/engine/classes/ImageButton.md) to
  an in-experience 3D object.

## Properties

### Property: Texture.OffsetStudsU

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
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

This property determines how far the rendered texture is offset on the
horizontal axis, in studs, as visualized
[here](/docs/en-us/parts/textures-decals.md#offset-textures).

See also [OffsetStudsV](/docs/reference/engine/classes/Texture.md).

### Property: Texture.OffsetStudsV

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
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

This property determines how far the rendered texture is offset on the
vertical axis, in studs, as visualized
[here](/docs/en-us/parts/textures-decals.md#offset-textures).

See also [OffsetStudsU](/docs/reference/engine/classes/Texture.md).

### Property: Texture.StudsPerTileU

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
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

Sets the horizontal size, in studs, of the tiled image applied by the
[Texture](/docs/reference/engine/classes/Texture.md).

Larger values for this property will lead to the [Texture](/docs/reference/engine/classes/Texture.md) appearing
larger, and repeating less frequently. Unlike with [Decals](/docs/reference/engine/classes/Decal.md),
the size of the repeated image is unaffected by the dimensions of the
[BasePart](/docs/reference/engine/classes/BasePart.md). Instead, resizing the [BasePart](/docs/reference/engine/classes/BasePart.md) only increases
the number of times the texture repeats.

Note that this property can be set to very low values, but not zero. Also
note that the horizontal/vertical distinction is relative to the parent
[BasePart](/docs/reference/engine/classes/BasePart.md) axis; therefore the [Texture](/docs/reference/engine/classes/Texture.md) will rotate along
with the [BasePart](/docs/reference/engine/classes/BasePart.md).

See also [StudsPerTileV](/docs/reference/engine/classes/Texture.md).

### Property: Texture.StudsPerTileV

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
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

Sets the vertical size, in studs, of the tiled image applied by the
[Texture](/docs/reference/engine/classes/Texture.md).

Larger values for this property will lead to the [Texture](/docs/reference/engine/classes/Texture.md) appearing
larger, and repeating less frequently. Unlike with [Decals](/docs/reference/engine/classes/Decal.md),
the size of the repeated image is unaffected by the dimensions of the
[BasePart](/docs/reference/engine/classes/BasePart.md). Instead, resizing the [BasePart](/docs/reference/engine/classes/BasePart.md) only increases
the number of times the texture repeats.

Note that this property can be set to very low values, but not zero. Also
note that the horizontal/vertical distinction is relative to the parent
[BasePart](/docs/reference/engine/classes/BasePart.md) axis; therefore the [Texture](/docs/reference/engine/classes/Texture.md) will rotate along
with the [BasePart](/docs/reference/engine/classes/BasePart.md).

See also [StudsPerTileU](/docs/reference/engine/classes/Texture.md).

## Inherited Members

### From [Decal](/docs/reference/engine/classes/Decal.md)

- **Property `AutoLocalize`** (`boolean`): When set to `true`, the decal's image asset is eligible for automatic
- **Property `Color3`** (`Color3`): The Color3 tint of the Decal.
- **Property `ColorMap`** (`ContentId`): Content ID that determines the color and opacity of the surface.
- **Property `ColorMapContent`** (`Content`): Content object that determines the color and opacity of the
- **Property `EmissiveMaskContent`** (`Content`): Content object that determines the emissivity across the
- **Property `EmissiveStrength`** (`float`): Determines the strength of the emissive contribution.
- **Property `EmissiveTint`** (`Color3`): Determines the tinting color for the emissive contribution.
- **Property `LocalTransparencyModifier`** (`float`): Acts as a multiplier for the decal's *(hidden)*
- **Property `MetalnessMap`** (`ContentId`): Content ID that determines the metalness map of the surface. *(hidden)*
- **Property `MetalnessMapContent`** (`Content`): Content object that determines the metalness map of the
- **Property `NormalMap`** (`ContentId`): Content ID that determines the normal map of the surface. *(hidden)*
- **Property `NormalMapContent`** (`Content`): Content object that determines the normal map of the surface.
- **Property `Rotation`** (`float`): Rotates the decal texture.
- **Property `RoughnessMap`** (`ContentId`): Content ID that determines the roughness map of the surface. *(hidden)*
- **Property `RoughnessMapContent`** (`Content`): Content object that determines the roughness map of the
- **Property `Shiny`** (`float`): Deprecated property that previously set the shininess of the decal. *(deprecated)*
- **Property `Specular`** (`float`): Deprecated property that previously set the specularity of the decal. *(deprecated)*
- **Property `Texture`** (`ContentId`): The content ID of the image to be applied by the Decal.
- **Property `TextureContent`** (`Content`): The texture content displayed by the Decal.
- **Property `TexturePackContent`** (`Content`): Engine-managed Content that stores the compressed runtime
- **Property `Transparency`** (`float`): Determines the transparency of the Decal.
- **Property `UVOffset`** (`Vector2`): Shifts the UV coordinates by adding an offset before texture mapping.
- **Property `UVScale`** (`Vector2`): Stretches or compresses the UV coordinates by multiplying a scale factor.
- **Property `ZIndex`** (`int`): Determines the rendering order when multiple decals are assigned the same

### From [FaceInstance](/docs/reference/engine/classes/FaceInstance.md)

- **Property `Face`** (`NormalId`): Sets which face of the parent BasePart the object appears on.

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