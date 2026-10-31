---
name: Decal
last_updated: 2026-10-30T19:55:52Z
inherits:
  - FaceInstance
  - Instance
  - Object
type: class
memory_category: GraphicsTexture
summary: "Applies an image texture to a face of a parent BasePart."
---

# Class: Decal

> Applies an image texture to a face of a parent [BasePart](/docs/reference/engine/classes/BasePart.md).

## Description

The [Decal](/docs/reference/engine/classes/Decal.md) object applies an image texture to a face of a parent
[BasePart](/docs/reference/engine/classes/BasePart.md). The affected face is dependent on the
[Face](/docs/reference/engine/classes/Decal.md) property, and the size of the decal is dependent on
the size of the face.

The applied image texture is determined by its
[ColorMapContent](/docs/reference/engine/classes/Decal.md) property. For details on how to
upload images, see
[asset management](/docs/en-us/projects/assets.md#asset-management).

For more information, review
[textures and decals](/docs/en-us/parts/textures-decals.md). See also:

- [Texture](/docs/reference/engine/classes/Texture.md) for repeating surface images.
- [MeshPart.TextureContent](/docs/reference/engine/classes/MeshPart.md) to apply an image texture to a
  [MeshPart](/docs/reference/engine/classes/MeshPart.md).
- [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) to apply an [ImageLabel](/docs/reference/engine/classes/ImageLabel.md) or [ImageButton](/docs/reference/engine/classes/ImageButton.md) to
  an in-experience 3D object.

## Code Samples

**Changing Decal Texture**

The following code will create a `Part` on the ground with a `Decal` applied
to its top face. When something hits the part, such as when a player walks
over it, the texture applied to the decal will change and a sound will play.

```lua
-- create part
local part = Instance.new("Part")
part.Size = Vector3.new(5, 1, 5)
part.Position = Vector3.new(0, 0.5, 0)
part.Anchored = true
part.TopSurface = Enum.SurfaceType.Smooth
part.BrickColor = BrickColor.new("Toothpaste")

-- create decal
local decal = Instance.new("Decal")
decal.Face = Enum.NormalId.Top
decal.Parent = part

-- define faces
local happyFace = Content.fromUri("http://www.roblox.com/asset/?id=26424652")
local sadFace = Content.fromUri("http://www.roblox.com/asset/?id=147144198")

decal.ColorMapContent = happyFace

-- touched event
local cooldown = false
part.Touched:Connect(function(hit)
	if not cooldown then
		if hit and hit.Parent then
			cooldown = true
			sound:Play()
			decal.ColorMapContent = sadFace
			task.wait(1)
			decal.ColorMapContent = happyFace
			task.wait(0.2)
			cooldown = false
		end
	end
end)

-- add to workspace
part.Parent = workspace
```

**Expected output:** A part will be created in the workspace with a smug face Decal applied to the top surface. When the player, or anything, hits the part the image will temporarily change to a distressed face and a sound will play.

**Fading Decal**

The code below will create a transparent `Part` with a decal that will fade in
and out using `TweenService` and [Decal.Transparency](/docs/reference/engine/classes/Decal.md).

```lua
local TweenService = game:GetService("TweenService")

local part = Instance.new("Part")
part.Size = Vector3.new(10, 10, 1)
part.Position = Vector3.new(0, 5, 0)
part.Anchored = true
part.Transparency = 1

local decal = Instance.new("Decal")
decal.Face = Enum.NormalId.Front
decal.ColorMapContent = Content.fromUri("http://www.roblox.com/asset/?id=699259085") -- roblox logo
decal.Parent = part

part.Parent = workspace

local tween = TweenService:Create(
	decal,
	TweenInfo.new(1, Enum.EasingStyle.Linear, Enum.EasingDirection.Out, -1, true),
	{ Transparency = 1 }
)

tween:Play()
```

**Expected output:** A part will be created in the Workspace with the Roblox logo applied to it. This logo will fade in and out repeatedly.

## Properties

### Property: Decal.AutoLocalize

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
  "category": "Localization",
  "capabilities": [
    "Basic"
  ]
}
```

When set to `true`, the decal's image asset is eligible for automatic
localization through the Automatic Asset Capture system. The
[LocalizationService](/docs/reference/engine/classes/LocalizationService.md) uses this property to determine whether the
decal's [ColorMapContent](/docs/reference/engine/classes/Decal.md) should be captured
and potentially replaced with a localized version.

This property only applies to non-PBR decals. If any PBR maps
([NormalMapContent](/docs/reference/engine/classes/Decal.md),
[RoughnessMapContent](/docs/reference/engine/classes/Decal.md),
[MetalnessMapContent](/docs/reference/engine/classes/Decal.md), or
[EmissiveMaskContent](/docs/reference/engine/classes/Decal.md)) are set, automatic
localization capture is suppressed to avoid inconsistent rendering.

### Property: Decal.Color3

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

The [Color3](/docs/reference/engine/datatypes/Color3.md) tint of the [Decal](/docs/reference/engine/classes/Decal.md). Note that this property
only sets the **tint** of the decal rather than the color; unless the
image associated with the [Decal](/docs/reference/engine/classes/Decal.md) was originally pure white, then
the color cannot be freely changed using this property.

**Decal Color3**

This code sample creates a `Decal` in the workspace and changes its
[Decal.Color3](/docs/reference/engine/classes/Decal.md) property on a loop using [TweenService](/docs/reference/engine/classes/TweenService.md).

```lua
local TweenService = game:GetService("TweenService")

local part = Instance.new("Part")
part.Size = Vector3.new(10, 10, 1)
part.Position = Vector3.new(0, 5, 0)
part.Anchored = true
part.Transparency = 1

local decal = Instance.new("Decal")
decal.Face = Enum.NormalId.Front
decal.ColorMapContent = Content.fromUri("http://www.roblox.com/asset/?id=1145367640")
decal.Parent = part

part.Parent = workspace

local redTween = TweenService:Create(
	decal,
	TweenInfo.new(1, Enum.EasingStyle.Linear, Enum.EasingDirection.Out),
	{ Color3 = Color3.new(1, 0, 0) }
)
local greenTween = TweenService:Create(
	decal,
	TweenInfo.new(1, Enum.EasingStyle.Linear, Enum.EasingDirection.Out),
	{ Color3 = Color3.new(0, 1, 0) }
)
local blueTween = TweenService:Create(
	decal,
	TweenInfo.new(1, Enum.EasingStyle.Linear, Enum.EasingDirection.Out),
	{ Color3 = Color3.new(0, 0, 1) }
)

while true do
	redTween:Play()
	redTween.Completed:Wait()
	greenTween:Play()
	greenTween.Completed:Wait()
	blueTween:Play()
	blueTween.Completed:Wait()
end
```

### Property: Decal.ColorMap

```json
{
  "type": "ContentId",
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
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

This property takes a content ID to determine the color and opacity of the
surface. This texture is sometimes called the **albedo** texture.

### Property: Decal.ColorMapContent

```json
{
  "type": "Content",
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
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

This property takes a [Content](/docs/reference/engine/datatypes/Content.md) object to determine the color and
opacity of the surface. This texture is sometimes called the **albedo**
texture.

### Property: Decal.EmissiveMaskContent

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

This property takes a [Content](/docs/reference/engine/datatypes/Content.md) object that determines the
apparent emissivity across the surface. An emissive mask is a grayscale
image where black pixels correspond to no emissivity and white pixels
correspond to full emissivity. It defaults to an empty content, in which
case the decal doesn't glow.

The emissive contribution is added to the total lighting contribution
across the surface, and the sum is multiplied by the albedo texture from
[ColorMapContent](/docs/reference/engine/classes/Decal.md), if provided. Use
[EmissiveStrength](/docs/reference/engine/classes/Decal.md) and
[EmissiveTint](/docs/reference/engine/classes/Decal.md) to control how bright the glow is
and what color it has.

Assigning an emissive mask makes the [Decal](/docs/reference/engine/classes/Decal.md) a physically based
rendering (PBR) surface.

### Property: Decal.EmissiveStrength

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

This value is a multiplier that controls how strong the emissive
contribution from [EmissiveMaskContent](/docs/reference/engine/classes/Decal.md) is
across the surface. Defaults to `1`. Negative values are treated as `0`,
and a value of `0` turns off the glow.

If the final emissive contribution goes beyond the supported dynamic
range, it's clamped, which can make the emissive areas appear fully white
at large strength values. Since this value is a multiplier, the maximum
value that avoids clamping depends on the other contributing values,
including [EmissiveTint](/docs/reference/engine/classes/Decal.md),
[ColorMapContent](/docs/reference/engine/classes/Decal.md), and the combined lighting
contribution.

### Property: Decal.EmissiveTint

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

This value is a [Color3](/docs/reference/engine/datatypes/Color3.md) that tints the emissive contribution
from [EmissiveMaskContent](/docs/reference/engine/classes/Decal.md). Defaults to
white, which leaves the emissive color unchanged. Each component is
clamped between `0` and `1`, and black turns off the glow.

### Property: Decal.MetalnessMapContent

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

This property takes a [Content](/docs/reference/engine/datatypes/Content.md) object that determines the
metalness map applied to the surface. A metalness map controls how
metallic the surface appears at each point, blending between a dielectric
(non-metal) and a metallic response to light. It defaults to an empty
content, in which case no metalness map is applied.

Assigning a normal, roughness, metalness, or emissive map makes the
[Decal](/docs/reference/engine/classes/Decal.md) a physically based rendering (PBR) surface.

### Property: Decal.NormalMapContent

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

This property takes a [Content](/docs/reference/engine/datatypes/Content.md) object that determines the normal
map applied to the surface. A normal map perturbs the surface normals used
in lighting calculations, adding the appearance of fine detail such as
bumps and grooves without changing the underlying geometry. It defaults to
an empty content, in which case no normal map is applied.

Assigning a normal, roughness, metalness, or emissive map makes the
[Decal](/docs/reference/engine/classes/Decal.md) a physically based rendering (PBR) surface.

### Property: Decal.Rotation

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

This property controls the rotation angle of the decal texture in degrees.
Rotation is applied to the UV coordinates in the clockwise direction.

### Property: Decal.RoughnessMapContent

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

This property takes a [Content](/docs/reference/engine/datatypes/Content.md) object that determines the
roughness map applied to the surface. A roughness map controls how rough
or smooth the surface appears at each point, which in turn determines how
sharp or blurry its reflections are. It defaults to an empty content, in
which case no roughness map is applied.

Assigning a normal, roughness, metalness, or emissive map makes the
[Decal](/docs/reference/engine/classes/Decal.md) a physically based rendering (PBR) surface.

### Property: Decal.Texture

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

The content ID of the image to be applied by the [Decal](/docs/reference/engine/classes/Decal.md).

### Property: Decal.TextureContent

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

The texture content displayed by the [Decal](/docs/reference/engine/classes/Decal.md). Supports
[asset URIs](/docs/en-us/projects/assets.md#asset-uris) and
[EditableImage](/docs/reference/engine/classes/EditableImage.md) objects.

### Property: Decal.TexturePackContent

```json
{
  "type": "Content",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
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

Managed by the engine and not accessible from scripts. A
[Content](/docs/reference/engine/datatypes/Content.md) that holds the decal's compressed runtime texture data.
When the [Decal](/docs/reference/engine/classes/Decal.md) is a physically based rendering (PBR) surface, the
engine packs its color, normal, roughness, metalness, and emissive maps
into a single texture-pack asset and references it here. Defaults to an
empty content.

### Property: Decal.Transparency

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

Determines the transparency of the [Decal](/docs/reference/engine/classes/Decal.md) with `0` being completely
opaque and `1` completely transparent.

Note that
[LocalTransparencyModifier](/docs/reference/engine/classes/Decal.md) acts as
a **multiplier** for this transparency level and should be used when the
transparency of the decal is likely to be changed by another script.

### Property: Decal.UVOffset

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
    "Basic"
  ]
}
```

This property controls the UV coordinate translation. The
[X](/docs/reference/engine/datatypes/Vector2.md) value (**U**&nbsp;offset) and
[Y](/docs/reference/engine/datatypes/Vector2.md) value (**V**&nbsp;offset) are added to every
corresponding UV coordinate during texture mapping.

### Property: Decal.UVScale

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
    "Basic"
  ]
}
```

This property controls the scale applied to the horizontal and vertical
coordinates. The [X](/docs/reference/engine/datatypes/Vector2.md) value (**U**&nbsp;scale) and
[Y](/docs/reference/engine/datatypes/Vector2.md) value (**V**&nbsp;scale) are multiplied by every
corresponding UV coordinate during texture mapping.

### Property: Decal.ZIndex

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
    "Basic"
  ]
}
```

This property determines the order in which decals on the same
[Face](/docs/reference/engine/classes/Decal.md) of a [BasePart](/docs/reference/engine/classes/BasePart.md) are rendered. Lower values
are rendered first, so a decal with a higher `ZIndex` renders on top of
those with a lower `ZIndex`.

If you're unsure whether you'll need to layer a decal between two
already-existing decals in the future, use larger separations between
`ZIndex` values such as `10` or `100` to ensure space for future decals
between.

### Property: Decal.Shiny

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
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

> **Deprecated:** This non-functional property is deprecated and should not be used in new work.

This property dictates how shiny the decal is. It takes a value between
`0` and `1`, where `1` is "fully shiny."

### Property: Decal.Specular

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
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

> **Deprecated:** This property no longer functions correctly and is deprecated. It should not be used in new work.

Sets the specularity, which is how the surface responds to light being
shined on it.

### Property: Decal.LocalTransparencyModifier *(hidden)*

```json
{
  "type": "float",
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
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

Acts as a multiplier for the decal's
[Transparency](/docs/reference/engine/classes/Decal.md) property. The effect is only
visible to the [LocalPlayer](/docs/reference/engine/classes/Players.md) and will not
replicate to the server.

When this property is set to `1`, the [Decal](/docs/reference/engine/classes/Decal.md) will be completely
invisible regardless of its original transparency. When it is set to `0`,
the decal's rendered transparency will match the
[Transparency](/docs/reference/engine/classes/Decal.md) value.

### Property: Decal.MetalnessMap *(hidden)*

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

This property takes a content ID that determines the metalness map applied
to the surface. A metalness map controls how metallic the surface appears
at each point, blending between a dielectric (non-metal) and a metallic
response to light. It defaults to an empty content, in which case no
metalness map is applied.

Assigning a normal, roughness, metalness, or emissive map makes the
[Decal](/docs/reference/engine/classes/Decal.md) a physically based rendering (PBR) surface. To assign this
map from a [Content](/docs/reference/engine/datatypes/Content.md) object, use
[MetalnessMapContent](/docs/reference/engine/classes/Decal.md).

### Property: Decal.NormalMap *(hidden)*

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

This property takes a content ID that determines the normal map applied to
the surface. A normal map perturbs the surface normals used in lighting
calculations, adding the appearance of fine detail such as bumps and
grooves without changing the underlying geometry. It defaults to an empty
content, in which case no normal map is applied.

Assigning a normal, roughness, metalness, or emissive map makes the
[Decal](/docs/reference/engine/classes/Decal.md) a physically based rendering (PBR) surface. To assign this
map from a [Content](/docs/reference/engine/datatypes/Content.md) object, use
[NormalMapContent](/docs/reference/engine/classes/Decal.md).

### Property: Decal.RoughnessMap *(hidden)*

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

This property takes a content ID that determines the roughness map applied
to the surface. A roughness map controls how rough or smooth the surface
appears at each point, which in turn determines how sharp or blurry its
reflections are. It defaults to an empty content, in which case no
roughness map is applied.

Assigning a normal, roughness, metalness, or emissive map makes the
[Decal](/docs/reference/engine/classes/Decal.md) a physically based rendering (PBR) surface. To assign this
map from a [Content](/docs/reference/engine/datatypes/Content.md) object, use
[RoughnessMapContent](/docs/reference/engine/classes/Decal.md).

## Inherited Members

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