---
name: MaterialVariant
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Represent a variant of a Material."
---

# Class: MaterialVariant

> Represent a variant of a Material.

## Description

Using MaterialVariant objects can expand the variety of materials in an
experience. MaterialVariant has properties that can define the appearance of a
material. Its name can be set in MaterialService to globally override a
built-in material, or set in the [BasePart.MaterialVariant](/docs/reference/engine/classes/BasePart.md) property to
change certain Parts. MaterialVariant objects only work as descendants of
MaterialService.

## Properties

### Property: MaterialVariant.AlphaMode

```json
{
  "type": "AlphaMode",
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
    "Material"
  ]
}
```

This property determines how the alpha channel of the
[MaterialVariant.ColorMap](/docs/reference/engine/classes/MaterialVariant.md) is used.

When set to [Transparency](/docs/reference/engine/enums/AlphaMode.md) and the
[MeshPart.Transparency](/docs/reference/engine/classes/MeshPart.md) is set to `0`, opaque pixels in the
[ColorMap](/docs/reference/engine/classes/MaterialVariant.md) renders as completely opaque in
the 3D scene. This combination works better with depth-based effects and
occlusion.

When set to [Transparency](/docs/reference/engine/enums/AlphaMode.md) and the
[MeshPart.Transparency](/docs/reference/engine/classes/MeshPart.md) is set to at least `0.02`, a different
blending method is used that can better represent smooth transparency
gradients and soft edges. This combination does not support all effects
and occlusion may not be perfect.

For more information, see
[Alpha modes](/docs/en-us/art/modeling/surface-appearance.md#alpha-modes).

### Property: MaterialVariant.BaseMaterial

```json
{
  "type": "Material",
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
    "Material"
  ]
}
```

Category Material this variant belongs to.

### Property: MaterialVariant.ColorMap

```json
{
  "type": "ContentId",
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
  "category": "Appearance",
  "capabilities": [
    "Material"
  ]
}
```

This property determines the color of the surface. This texture is
sometimes called the albedo texture. The alpha channel is not used.

### Property: MaterialVariant.ColorMapContent

```json
{
  "type": "Content",
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
  "category": "Appearance",
  "capabilities": [
    "Material"
  ]
}
```

This property determines the color of the surface. This texture is
sometimes called the albedo texture. The alpha channel is not used.

### Property: MaterialVariant.CustomPhysicalProperties

```json
{
  "type": "PhysicalProperties",
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
  "category": "Material",
  "capabilities": [
    "Material"
  ]
}
```

Determines the physical properties, such as density, friction, and
elasticity, of parts whose material resolves to this variant.

The assigned [PhysicalProperties](/docs/reference/engine/datatypes/PhysicalProperties.md) apply only when that value was
constructed with explicit values. Otherwise the physical properties are
inherited, falling back first to the base-material override configured on
the parent [MaterialService](/docs/reference/engine/classes/MaterialService.md), and if none is set, to the default
physical properties of the variant's
[BaseMaterial](/docs/reference/engine/classes/MaterialVariant.md) category.

The default value is a [PhysicalProperties](/docs/reference/engine/datatypes/PhysicalProperties.md) constructed without
explicit values, so an unmodified variant inherits its base material's
physical properties.

### Property: MaterialVariant.EmissiveMaskContent

```json
{
  "type": "Content",
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
  "category": "Appearance",
  "capabilities": [
    "Material"
  ]
}
```

This property determines the apparent emissivity across the surface. An
emissive mask is a grayscale image where black pixels correspond to no
emissivity, and white pixels correspond to full emissivity.

The emissive contribution gets added to total lighting contribution across
the surface, and the sum gets multiplied by the albedo texture, which
would be sampled from [ColorMap](/docs/reference/engine/classes/MaterialVariant.md) if
provided.

### Property: MaterialVariant.EmissiveStrength

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
    "Material"
  ]
}
```

This value is a multiplier to control how strong the emissive contribution
is across the surface. If the final contribution of emissives goes beyond
supported dynamic range, it will get clamped; this could result in
emissive contribution appearing all white when using large emissive
strength values. Since this value is a multiplier, the maximum value to
prevent clamping depends on all of the other contributing values,
including [EmissiveTint](/docs/reference/engine/classes/MaterialVariant.md),
[ColorMap](/docs/reference/engine/classes/MaterialVariant.md) and combined lighting
contribution.

### Property: MaterialVariant.EmissiveTint

```json
{
  "type": "Color3",
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
    "Material"
  ]
}
```

This value is an RGB color for tinting emissive contribution.

### Property: MaterialVariant.MaterialPattern

```json
{
  "type": "MaterialPattern",
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
    "Material"
  ]
}
```

Determines texture tiling method.

### Property: MaterialVariant.MetalnessMap

```json
{
  "type": "ContentId",
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
  "category": "Appearance",
  "capabilities": [
    "Material"
  ]
}
```

This property determines which parts of the surface are metal and are
non-metal. A metalness map is a grayscale image where black pixels
correspond to non-metals and white pixels correspond to metals.

Metals only reflect light the same color as the metal, and they reflect
much more light than non-metals. Most materials in the real world can be
categorized either metals or non-metals. For this reason, most pixels in a
metalness map will be either pure black or pure white. Values in between
are typically used to simulate dirt or grunge on top of an underlying
metal area.

When [Lighting.EnvironmentSpecularScale](/docs/reference/engine/classes/Lighting.md) is 0, metalness has no
effect. For the most realistic reflections, setting
EnvironmentSpecularScale and [Lighting.EnvironmentDiffuseScale](/docs/reference/engine/classes/Lighting.md) to
1, and [Lighting.Ambient](/docs/reference/engine/classes/Lighting.md) and [Lighting.OutdoorAmbient](/docs/reference/engine/classes/Lighting.md) to
(0,0,0) is recommended.

### Property: MaterialVariant.MetalnessMapContent

```json
{
  "type": "Content",
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
  "category": "Appearance",
  "capabilities": [
    "Material"
  ]
}
```

This property determines which parts of the surface are metal and are
non-metal. A metalness map is a grayscale image where black pixels
correspond to non-metals and white pixels correspond to metals.

Metals only reflect light the same color as the metal, and they reflect
much more light than non-metals. Most materials in the real world can be
categorized either metals or non-metals. For this reason, most pixels in a
metalness map will be either pure black or pure white. Values in between
are typically used to simulate dirt or grunge on top of an underlying
metal area.

When [Lighting.EnvironmentSpecularScale](/docs/reference/engine/classes/Lighting.md) is 0, metalness has no
effect. For the most realistic reflections, setting
EnvironmentSpecularScale and [Lighting.EnvironmentDiffuseScale](/docs/reference/engine/classes/Lighting.md) to
1, and [Lighting.Ambient](/docs/reference/engine/classes/Lighting.md) and [Lighting.OutdoorAmbient](/docs/reference/engine/classes/Lighting.md) to
(0,0,0) is recommended.

### Property: MaterialVariant.NormalMap

```json
{
  "type": "ContentId",
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
  "category": "Appearance",
  "capabilities": [
    "Material"
  ]
}
```

This property modifies the lighting of the surface by adding bumps, dents,
cracks, and curves without adding more polygons.

Normal maps are RGB images that modify the surface's normal vector used
for lighting calculations. The R, G, and B channels of the NormalMap
correspond to the X, Y, and Z components of the local surface vector
respectively, and byte values of 0 and 255 for each channel correspond
linearly to normal vector components of -1 and 1.016 respectively. This
range is stretched slightly from -1 to 1 so that a byte value of 127 maps
to exactly 0. The normal vector's Z axis is always defined as the
direction of the underlying mesh's normal. A uniform (127,127,255) image
translates to a completely flat normal map where the normal is everywhere
perpendicular to the mesh surface. This format is called "tangent space"
normal maps. Roblox does not support world space or object space normal
maps.

Incorrectly flipped normal components can make bumps appear like indents.
If you import a normal map and notice the lighting looks off, you may need
to invert the G channel of the image. The X and Y axes of the tangent
space frame correspond to the X and Y directions in the image after it's
transformed by the mesh UVs. If you view your normal map in an image
editor as if it were displayed on a surface, normals pointing towards the
right side of the screen should appear more red, and normals pointing
towards the top side of your screen should appear more green.

The terms "DirectX format" and "OpenGL format" are sometimes used to
describe whether the G channel of the normal map is inverted or not.
Roblox expects the OpenGL format.

Roblox expects imported meshes to include tangents. Modeling software may
also refer to this as "tangent space" information. If you apply a normal
map and it does not seem to make any visual difference, you may need to
re-export your mesh along with its tangent information from modeling
software.

### Property: MaterialVariant.NormalMapContent

```json
{
  "type": "Content",
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
  "category": "Appearance",
  "capabilities": [
    "Material"
  ]
}
```

This property modifies the lighting of the surface by adding bumps, dents,
cracks, and curves without adding more polygons.

Normal maps are RGB images that modify the surface's normal vector used
for lighting calculations. The R, G, and B channels of the NormalMap
correspond to the X, Y, and Z components of the local surface vector
respectively, and byte values of 0 and 255 for each channel correspond
linearly to normal vector components of -1 and 1.016 respectively. This
range is stretched slightly from -1 to 1 so that a byte value of 127 maps
to exactly 0. The normal vector's Z axis is always defined as the
direction of the underlying mesh's normal. A uniform (127,127,255) image
translates to a completely flat normal map where the normal is everywhere
perpendicular to the mesh surface. This format is called "tangent space"
normal maps. Roblox does not support world space or object space normal
maps.

Incorrectly flipped normal components can make bumps appear like indents.
If you import a normal map and notice the lighting looks off, you may need
to invert the G channel of the image. The X and Y axes of the tangent
space frame correspond to the X and Y directions in the image after it's
transformed by the mesh UVs. If you view your normal map in an image
editor as if it were displayed on a surface, normals pointing towards the
right side of the screen should appear more red, and normals pointing
towards the top side of your screen should appear more green.

The terms "DirectX format" and "OpenGL format" are sometimes used to
describe whether the G channel of the normal map is inverted or not.
Roblox expects the OpenGL format.

Roblox expects imported meshes to include tangents. Modeling software may
also refer to this as "tangent space" information. If you apply a normal
map and it does not seem to make any visual difference, you may need to
re-export your mesh along with its tangent information from modeling
software.

### Property: MaterialVariant.RoughnessMap

```json
{
  "type": "ContentId",
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
  "category": "Appearance",
  "capabilities": [
    "Material"
  ]
}
```

This property determines the apparent roughness across the surface. A
roughness map is a grayscale image where black pixels correspond to a
maximally smooth surface, and white pixels correspond to a maximally rough
surface.

Roughness refers to how much variation the surface has on a very small
scale. Reflections on smooth surfaces are sharp and concentrated.
Reflections on rough surfaces are more blurry and dispersed.

### Property: MaterialVariant.RoughnessMapContent

```json
{
  "type": "Content",
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
  "category": "Appearance",
  "capabilities": [
    "Material"
  ]
}
```

This property determines the apparent roughness across the surface. A
roughness map is a grayscale image where black pixels correspond to a
maximally smooth surface, and white pixels correspond to a maximally rough
surface.

Roughness refers to how much variation the surface has on a very small
scale. Reflections on smooth surfaces are sharp and concentrated.
Reflections on rough surfaces are more blurry and dispersed.

### Property: MaterialVariant.StudsPerTile

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
    "Material"
  ]
}
```

Determines the scale of textures. Larger values for this property will
lead to the textures appearing larger, and repeating less frequently.

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