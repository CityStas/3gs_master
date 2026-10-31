---
name: SurfaceAppearance
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "An object that allows developers to override the appearance of a MeshPart with advanced graphics options."
---

# Class: SurfaceAppearance

> An object that allows developers to override the appearance of a MeshPart with
> advanced graphics options.

## Description

**SurfaceAppearance** objects let you override the appearance of a
[MeshPart](/docs/reference/engine/classes/MeshPart.md) with advanced graphics options. Most notably, it can apply a
set of **Physically‑Based Rendering** (PBR) texture images, or maps, on a
single object. Combining multiple texture maps can more accurately simulate
color, roughness, and reflectivity in any lighting environment and can enhance
the visual elements of your assets and environment; see
[PBR Textures](/docs/en-us/art/modeling/surface-appearance.md) for more details.

![A realistic leafy bush](/assets/modeling/surface-appearance/SurfaceAppearance-Example-1.jpg)![A realistic mossy rock](/assets/modeling/surface-appearance/SurfaceAppearance-Example-3.jpg)

Appearance of this object on a [MeshPart](/docs/reference/engine/classes/MeshPart.md) depends on the user's device
and graphics quality level. For best results, you may want to preview your
content with different quality level settings.

Note that most [SurfaceAppearance](/docs/reference/engine/classes/SurfaceAppearance.md) properties cannot be modified by
scripts, as the necessary pre-processing is usually too expensive during
runtime.

## Properties

### Property: SurfaceAppearance.AlphaMode

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
    "Basic"
  ]
}
```

This property determines how the alpha channel of the
[SurfaceAppearance.ColorMap](/docs/reference/engine/classes/SurfaceAppearance.md) is used.

When set to [Transparency](/docs/reference/engine/enums/AlphaMode.md) and the
[MeshPart.Transparency](/docs/reference/engine/classes/MeshPart.md) is set to `0`, opaque pixels in the
[ColorMap](/docs/reference/engine/classes/SurfaceAppearance.md) will render as completely
opaque in the 3D scene. This combination works better with depth-based
effects and occlusion.

When set to [Transparency](/docs/reference/engine/enums/AlphaMode.md) and the
[MeshPart.Transparency](/docs/reference/engine/classes/MeshPart.md) is set to at least `0.02`, a different
blending method is used that can better represent smooth transparency
gradients and soft edges. This combination does not support all effects
and occlusion may not be perfect.

See [here](/docs/en-us/art/modeling/surface-appearance.md#alpha-modes) for
more information.

### Property: SurfaceAppearance.Color

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
    "Basic"
  ]
}
```

Applies a tint to your existing colormap. Set directly with color picker
or programmatically with [Color3](/docs/reference/engine/datatypes/Color3.md).

### Property: SurfaceAppearance.ColorMap

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
    "Basic"
  ]
}
```

This property determines the color and opacity of the surface. This
texture is sometimes called the **albedo** texture. The alpha channel of
this texture controls its opacity, which behaves differently based on the
[SurfaceAppearance.AlphaMode](/docs/reference/engine/classes/SurfaceAppearance.md) setting.

See [here](/docs/en-us/art/modeling/surface-appearance.md#color-albedo) for
more information.

### Property: SurfaceAppearance.ColorMapContent

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
    "Basic"
  ]
}
```

A [Content](/docs/reference/engine/datatypes/Content.md) that determines the color and opacity of the surface
(sometimes called the **albedo** texture). The content can hold an
[asset URI](/docs/en-us/projects/assets.md#asset-uris) or a reference
to an [EditableImage](/docs/reference/engine/classes/EditableImage.md) object.

The alpha channel of the texture controls its opacity, which behaves
differently based on the [SurfaceAppearance.AlphaMode](/docs/reference/engine/classes/SurfaceAppearance.md) setting. It
defaults to an empty content, in which case no color map is applied.
Assigning an [EditableImage](/docs/reference/engine/classes/EditableImage.md) is useful for dynamically generating or
modifying textures at runtime, such as in avatar customization and other
in-experience content creation workflows.

### Property: SurfaceAppearance.EmissiveMaskContent

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
    "Basic"
  ]
}
```

This property determines the apparent emissivity across the surface. An
emissive mask is a grayscale image where black pixels correspond to no
emissivity, and white pixels correspond to full emissivity.

The emissive contribution gets added to total lighting contribution across
the surface, and the sum gets multiplied by the albedo texture, which
would be sampled from [ColorMap](/docs/reference/engine/classes/SurfaceAppearance.md) if
provided.

### Property: SurfaceAppearance.EmissiveStrength

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

This value is a multiplier to control how strong the emissive contribution
is across the surface. If the final contribution of emissives goes beyond
supported dynamic range, it will get clamped; this could result in
emissive contribution appearing all white when using large emissive
strength values. Since this value is a multiplier, the maximum value to
prevent clamping depends on all of the other contributing values,
including [EmissiveTint](/docs/reference/engine/classes/SurfaceAppearance.md),
[ColorMap](/docs/reference/engine/classes/SurfaceAppearance.md) and combined lighting
contribution.

### Property: SurfaceAppearance.EmissiveTint

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
    "Basic"
  ]
}
```

This value is an RGB color for tinting emissive contribution.

### Property: SurfaceAppearance.MetalnessMap

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
    "Basic"
  ]
}
```

This property determines which parts of the surface are metal or
non-metal. The metalness map is a grayscale image where black pixels
correspond to non-metals and white pixels correspond to metals.

Metals only reflect light the same color as the metal, and they reflect
much more light than non-metals. Most pixels in a metalness map will be
either pure black or pure white, while values in between can be used to
simulate dirt or grunge on top of an underlying metal area.

When [Lighting.EnvironmentSpecularScale](/docs/reference/engine/classes/Lighting.md) is 0, metalness has no
effect. For the most realistic reflections, it's recommended to set
[Lighting.EnvironmentSpecularScale](/docs/reference/engine/classes/Lighting.md) and
[Lighting.EnvironmentDiffuseScale](/docs/reference/engine/classes/Lighting.md) to 1, as well as
[Lighting.Ambient](/docs/reference/engine/classes/Lighting.md) and [Lighting.OutdoorAmbient](/docs/reference/engine/classes/Lighting.md) to
`(0, 0, 0)`.

See [here](/docs/en-us/art/modeling/surface-appearance.md#metalness) for more
information.

### Property: SurfaceAppearance.MetalnessMapContent

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
    "Basic"
  ]
}
```

A [Content](/docs/reference/engine/datatypes/Content.md) that determines which parts of the surface are metal
or non-metal. The metalness map is a grayscale image where black pixels
correspond to non-metals and white pixels correspond to metals. The
content can hold an
[asset URI](/docs/en-us/projects/assets.md#asset-uris) or a reference
to an [EditableImage](/docs/reference/engine/classes/EditableImage.md) object.

Metals only reflect light the same color as the metal, and they reflect
much more light than non-metals. Most pixels in a metalness map will be
either pure black or pure white, while values in between can be used to
simulate dirt or grunge on top of an underlying metal area.

When [Lighting.EnvironmentSpecularScale](/docs/reference/engine/classes/Lighting.md) is 0, metalness has no
effect. Defaults to an empty content, in which case no metalness map is
applied.

### Property: SurfaceAppearance.NormalMap

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
    "Basic"
  ]
}
```

This property modifies the lighting of the surface by adding bumps, dents,
cracks, and curves, without adding more polygons. The normal map is an RGB
image that modifies the surface's normal vector used for lighting
calculations. Its **R**, **G**, and **B** channels correspond to the
**X**, **Y**, and **Z** components of the local surface vector
respectively, and byte values of 0 and 255 for each channel correspond
linearly to normal vector components of -1 and 1.016 respectively. This
range is stretched slightly from -1 to 1 so that a byte value of 127 maps
to exactly 0.

The normal vector's **Z** axis is always defined as the direction of the
underlying mesh's normal. A uniform `(127, 127, 255)` image translates to
a completely flat normal map where the normal is everywhere perpendicular
to the mesh surface; this format is referred to as a "tangent space"
normal map. Note that Roblox does not support world space or object space
normal maps.

Incorrectly flipped normal components can make bumps appear like indents.
If you import a normal map and notice the lighting looks off, you may need
to invert the **G** channel of the image. The **X** and **Y** axes of the
tangent space frame correspond to the **X** and **Y** directions in the
image after it's transformed by the mesh UVs. If you view your normal map
in an image editor as if it were displayed on a surface, normals pointing
towards the right side of the screen should appear more red, and normals
pointing towards the top side of your screen should appear more green. The
terms "DirectX format" and "OpenGL format" are sometimes used to describe
whether the **G** channel of the normal map is inverted or not (Roblox
expects the OpenGL format).

Roblox also expects imported meshes to include tangents. Modeling software
may also refer to this as "tangent space" information. If you apply a
normal map and it does not seem to make any visual difference, you may
need to re-export your mesh along with its tangent information from the
modeling software.

See [here](/docs/en-us/art/modeling/surface-appearance.md#normal) for more
information.

### Property: SurfaceAppearance.NormalMapContent

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
    "Basic"
  ]
}
```

A [Content](/docs/reference/engine/datatypes/Content.md) that modifies the lighting of the surface by adding
bumps, dents, cracks, and curves, without adding more polygons. The normal
map is an RGB image that modifies the surface's normal vector used for
lighting calculations, where the **R**, **G**, and **B** channels
correspond to the **X**, **Y**, and **Z** components of the local surface
vector respectively. The content can hold an
[asset URI](/docs/en-us/projects/assets.md#asset-uris) or a reference
to an [EditableImage](/docs/reference/engine/classes/EditableImage.md) object.

Roblox expects tangent-space normal maps in the "OpenGL format" (the **G**
channel is not inverted), and imported meshes must include tangent
information. Defaults to an empty content, in which case no normal map is
applied.

### Property: SurfaceAppearance.ResampleMode

```json
{
  "type": "ResamplerMode",
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

Determines how the surface's texture maps look when they are scaled. When
set to the default [ResamplerMode.Default](/docs/reference/engine/enums/ResamplerMode.md), the textures smooth out
using bilinear filtering when displayed larger or smaller than their size
in texture memory. When set to [Pixelated](/docs/reference/engine/enums/ResamplerMode.md),
the textures preserve the sharp edges of pixels using nearest-neighbor
filtering. Defaults to [ResamplerMode.Default](/docs/reference/engine/enums/ResamplerMode.md).

### Property: SurfaceAppearance.RoughnessMap

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
    "Basic"
  ]
}
```

This property determines the apparent roughness across the surface. The
roughness map is a grayscale image where black pixels correspond to a
maximally smooth surface, and white pixels correspond to a maximally rough
surface.

Note that surface roughness works on a very small scale. Reflections on
smooth surfaces are sharp and concentrated, while reflections on rough
surfaces are more blurry and dispersed.

See [here](/docs/en-us/art/modeling/surface-appearance.md#roughness) for more
information.

### Property: SurfaceAppearance.RoughnessMapContent

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
    "Basic"
  ]
}
```

A [Content](/docs/reference/engine/datatypes/Content.md) that determines the apparent roughness across the
surface. The roughness map is a grayscale image where black pixels
correspond to a maximally smooth surface, and white pixels correspond to a
maximally rough surface. The content can hold an
[asset URI](/docs/en-us/projects/assets.md#asset-uris) or a reference
to an [EditableImage](/docs/reference/engine/classes/EditableImage.md) object.

Surface roughness works on a very small scale. Reflections on smooth
surfaces are sharp and concentrated, while reflections on rough surfaces
are more blurry and dispersed. Defaults to an empty content, in which case
no roughness map is applied.

### Property: SurfaceAppearance.TexturePackContent

```json
{
  "type": "Content",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxEngineSecurity"
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

Managed by the engine and not intended to be set directly. A
[Content](/docs/reference/engine/datatypes/Content.md) that holds the compressed runtime texture data for the
surface appearance. It is the backing storage for
[SurfaceAppearance.TexturePack](/docs/reference/engine/classes/SurfaceAppearance.md): when the object is published, the
engine bakes its individual texture maps into a single texture pack asset
and stores the resulting reference here.

Requires elevated permissions to read (`RobloxScript` security) and is
writable only by the engine (`RobloxEngine` security). Defaults to an
empty content.

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