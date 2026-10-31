---
name: Trail
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Used to create a trail effect between two attachments."
---

# Class: Trail

> Used to create a trail effect between two attachments.

## Description

The **Trail** object is used to create a trail effect between two attachments.
As the attachments move through space, a texture is drawn on their defined
plane. This is commonly used to create effects that visualize movements like
tracer trails behind projectiles, footprints, tire tracks, and similar
effects.

See [Trails](/docs/en-us/effects/trails.md) for more information.

## Code Samples

**Creating a Part with a Basic Trail**

This example demos the functionality of [Trails](/docs/reference/engine/classes/Trail.md) by creating a
[BasePart](/docs/reference/engine/classes/BasePart.md) to be the parent of the trail. Two
[Attachments](/docs/reference/engine/classes/Attachment.md) are then parented to the part. The positions of
these two attachments (more importantly the distance between them) determines
where the trail is drawn as the part moves.

For these attachments to create a trail as described, a new [Trail](/docs/reference/engine/classes/Trail.md) is
parented to the part and its [Attachment0](/docs/reference/engine/classes/Trail.md) and
[Attachment1](/docs/reference/engine/classes/Trail.md) are parented to `attachment0` and
`attachment1` respectively. Finally, [TweenService](/docs/reference/engine/classes/TweenService.md) is used to move the
part back and forth, showing how the trail is drawn as the part (and its
attachments) move.

```lua
local TweenService = game:GetService("TweenService")

-- Create a parent part
local part = Instance.new("Part")
part.Material = Enum.Material.SmoothPlastic
part.Size = Vector3.new(4, 1, 2)
part.Position = Vector3.new(0, 5, 0)
part.Anchored = true
part.Parent = workspace

-- Create attachments on part
local attachment0 = Instance.new("Attachment")
attachment0.Name = "Attachment0"
attachment0.Position = Vector3.new(-2, 0, 0)
attachment0.Parent = part
local attachment1 = Instance.new("Attachment")
attachment1.Name = "Attachment1"
attachment1.Position = Vector3.new(2, 0, 0)
attachment1.Parent = part

-- Create a new trail
local trail = Instance.new("Trail")
trail.Attachment0 = attachment0
trail.Attachment1 = attachment1
trail.Parent = part

-- Tween part to display trail
local dir = 15
while true do
	dir *= -1

	local goal = { Position = part.Position + Vector3.new(0, 0, dir) }
	local tweenInfo = TweenInfo.new(3)
	local tween = TweenService:Create(part, tweenInfo, goal)
	tween:Play()

	task.wait(4)
end
```

## Properties

### Property: Trail.Attachment0

```json
{
  "type": "Attachment",
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
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

A [Trail](/docs/reference/engine/classes/Trail.md) starts drawing its segments at the positions of its
**Attachment0** and [Attachment1](/docs/reference/engine/classes/Trail.md). When the trail
is [Enabled](/docs/reference/engine/classes/Trail.md), it records the positions of its
attachments every frame and connects these positions to the attachments'
positions on the previous frame, creating a polygon that is then filled in
by the trail's [Color](/docs/reference/engine/classes/Trail.md) and
[Texture](/docs/reference/engine/classes/Trail.md).

Changing the attachments of a trail while a trail is drawing will remove
all of the segments the trail has already drawn.

### Property: Trail.Attachment1

```json
{
  "type": "Attachment",
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
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

A [Trail](/docs/reference/engine/classes/Trail.md) starts drawing its segments at the positions of its
[Attachment0](/docs/reference/engine/classes/Trail.md) and **Attachment1**. When the trail
is [Enabled](/docs/reference/engine/classes/Trail.md), it records the positions of its
attachments every frame and connects these positions to the attachments'
positions on the previous frame, creating a polygon that is then filled in
by the trail's [Color](/docs/reference/engine/classes/Trail.md) and
[Texture](/docs/reference/engine/classes/Trail.md).

Changing the attachments of a trail while a trail is drawing will remove
all of the segments the trail has already drawn.

### Property: Trail.Brightness

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

Scales the light emitted from the trail when
[LightInfluence](/docs/reference/engine/classes/Trail.md) is less than 1. This property
is 1 by default and can set to any number within the range of 0 to 10000.
Increasing the value of [LightInfluence](/docs/reference/engine/classes/Trail.md)
decreases the effect of this property's value.

### Property: Trail.Color

```json
{
  "type": "ColorSequence",
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

Determines the color of the trail throughout its lifetime. If
[Texture](/docs/reference/engine/classes/Trail.md) is set, this color will tint the texture.

This property is a [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md), allowing the color to be
configured to vary across the length of the trail. If the color changes
after some of the trail segments have been drawn, all of the old segments
will be updated to match the new colors.

**Creating a Trail with a Color Gradient**

This example creates a [Trail](/docs/reference/engine/classes/Trail.md) with a gradient color, meaning that the
color at one end of the trail is different than the color at the opposite end,
and both colors blend together as they get closer to the middle of the trail.

```lua
local TweenService = game:GetService("TweenService")

-- Create a parent part
local part = Instance.new("Part")
part.Material = Enum.Material.SmoothPlastic
part.Size = Vector3.new(4, 1, 2)
part.Position = Vector3.new(0, 5, 0)
part.Anchored = true
part.Parent = workspace

-- Create attachments on part
local attachment0 = Instance.new("Attachment")
attachment0.Name = "Attachment0"
attachment0.Position = Vector3.new(-2, 0, 0)
attachment0.Parent = part
local attachment1 = Instance.new("Attachment")
attachment1.Name = "Attachment1"
attachment1.Position = Vector3.new(2, 0, 0)
attachment1.Parent = part

-- Create a new trail with color gradient
local trail = Instance.new("Trail")
trail.Attachment0 = attachment0
trail.Attachment1 = attachment1
local color1 = Color3.fromRGB(255, 0, 0)
local color2 = Color3.fromRGB(0, 0, 255)
trail.Color = ColorSequence.new(color1, color2)
trail.Parent = part

-- Tween part to display trail
local dir = 15
while true do
	dir *= -1

	local goal = { Position = part.Position + Vector3.new(0, 0, dir) }
	local tweenInfo = TweenInfo.new(3)
	local tween = TweenService:Create(part, tweenInfo, goal)
	tween:Play()

	task.wait(4)
end
```

### Property: Trail.Enabled

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
  "category": "Emission",
  "capabilities": [
    "Basic"
  ]
}
```

This property determines whether the trail will be drawn or not.

If set to `false` while a trail is drawing, no new segments will be drawn,
but any existing segments will be cleaned up naturally when they reach the
end of their [Lifetime](/docs/reference/engine/classes/Trail.md). To forcibly clean up
existing segments, call the [Clear()](/docs/reference/engine/classes/Trail.md) method at the
same time.

### Property: Trail.FaceCamera

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

A [Trail](/docs/reference/engine/classes/Trail.md) is a 2D projection existing in 3D space, meaning that it
may not be visible from every angle. The **FaceCamera** property, when set
to `true`, ensures that the trail always faces the
[CurrentCamera](/docs/reference/engine/classes/Workspace.md), regardless of its
orientation.

Changing this property immediately affects all existing and future trail
segments.

### Property: Trail.Lifetime

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
  "category": "Emission",
  "capabilities": [
    "Basic"
  ]
}
```

The **Lifetime** property determines how long each segment in a trail will
last, in seconds, before it disappears. Defaults to 2 seconds but can be
set anywhere between 0.01 and 20.

The lifetime of a trail is also used by that effect's
[Color](/docs/reference/engine/classes/Trail.md) and [Transparency](/docs/reference/engine/classes/Trail.md)
properties to determine how each segment is drawn. Both of these
properties are sequences, meaning that they define their values at certain
keypoints in the segment's lifetime and then interpolate between the
values as the segment ages.

If a trail's lifetime changes, existing segments will immediately behave
as if they always had the new lifetime, meaning that if they've existed
for longer than the new lifetime, they will be removed immediately.

### Property: Trail.LightEmission

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

Determines to what degree the colors of the trail are blended with the
colors behind it. It should be set in the range of 0 to 1. A value of 0
uses normal blending modes and a value of 1 uses additive blending.

This property should not be confused with
[LightInfluence](/docs/reference/engine/classes/Trail.md) which determines how the trail
is affected by environmental light.

Changing this property immediately affects all existing and future
segments of the trail.

This property does **not** cause the trail to light the environment.

### Property: Trail.LightInfluence

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

Determines the degree to which the trail is influenced by the
environment's lighting, clamped between 0 and 1. When 0, the trail will be
unaffected by the environment's lighting. When 1, it will be fully
affected by lighting as a [BasePart](/docs/reference/engine/classes/BasePart.md) would be.

Changing this property immediately affects all existing and future
segments of the trail.

See also [LightEmission](/docs/reference/engine/classes/Trail.md) which specifies to what
degree the colors of the trail are blended with the colors behind it.

### Property: Trail.MaxLength

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
  "category": "Emission",
  "capabilities": [
    "Basic"
  ]
}
```

This property determines the maximum length of the trail, in studs. Its
value defaults to 0, meaning that the trail will not have a maximum length
and trail segments will expire in their [Lifetime](/docs/reference/engine/classes/Trail.md).

This property can be used alongside the [MinLength](/docs/reference/engine/classes/Trail.md)
property which determines the minimum length a trail must be before it's
drawn.

### Property: Trail.MinLength

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
  "category": "Emission",
  "capabilities": [
    "Basic"
  ]
}
```

This property determines the minimum length of the trail, in studs. If
neither of the trail's attachments have moved at least this value, no new
segments will be created and the endpoints of the current segment will be
moved to the current position of the attachments.

Note that changing this property will only affect **new** segments that
are drawn; any old segments that have already been drawn will maintain
their current length.

This property can be used alongside the [MaxLength](/docs/reference/engine/classes/Trail.md)
property which determines the maximum trail length before its oldest
segments are erased.

### Property: Trail.Texture

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

The content ID of the texture to be displayed on the trail. If this
property is not set, the trail will be displayed as a solid plane; this
also occurs when the texture is set to an invalid content ID or the image
associated with the texture has not yet loaded.

The appearance of the texture can be further modified by other trail
properties including [Color](/docs/reference/engine/classes/Trail.md) and
[Transparency](/docs/reference/engine/classes/Trail.md).

Scaling of the texture is determined by the distance between
[Attachment0](/docs/reference/engine/classes/Trail.md) and
[Attachment1](/docs/reference/engine/classes/Trail.md), as well as the
[TextureMode](/docs/reference/engine/classes/Trail.md),
[TextureLength](/docs/reference/engine/classes/Trail.md), and
[WidthScale](/docs/reference/engine/classes/Trail.md) properties.

**Creating a Trail with a Paw Print Texture**

This example adds a
[paw prints](https://create.roblox.com/store/asset/16178262259/PawPrintTexture)
texture to a trail object. In order for the paw prints to remain "stamped" in
place after rendering, [TextureMode](/docs/reference/engine/classes/Trail.md) is set to
[TextureMode.Static](/docs/reference/engine/enums/TextureMode.md).

```lua
local TweenService = game:GetService("TweenService")

-- Create a parent part
local part = Instance.new("Part")
part.Material = Enum.Material.SmoothPlastic
part.Size = Vector3.new(2, 1, 2)
part.Position = Vector3.new(0, 5, 0)
part.Anchored = true
part.Parent = workspace

-- Create attachments on part
local attachment0 = Instance.new("Attachment")
attachment0.Name = "Attachment0"
attachment0.Position = Vector3.new(-1, 0, 0)
attachment0.Parent = part
local attachment1 = Instance.new("Attachment")
attachment1.Name = "Attachment1"
attachment1.Position = Vector3.new(1, 0, 0)
attachment1.Parent = part

-- Create a new trail with color gradient
local trail = Instance.new("Trail")
trail.Attachment0 = attachment0
trail.Attachment1 = attachment1
trail.Texture = "rbxassetid://16178262222"
trail.TextureMode = Enum.TextureMode.Static
trail.TextureLength = 2
trail.Parent = part

-- Tween part to display trail
local dir = 15
while true do
	dir *= -1

	local goal = { Position = part.Position + Vector3.new(0, 0, dir) }
	local tweenInfo = TweenInfo.new(3)
	local tween = TweenService:Create(part, tweenInfo, goal)
	tween:Play()

	task.wait(4)
end
```

### Property: Trail.TextureContent

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

The texture displayed on the trail. Supports
[asset URIs](/docs/en-us/projects/assets.md#asset-uris).

This property is the [Content](/docs/reference/engine/datatypes/Content.md) equivalent of
[Texture](/docs/reference/engine/classes/Trail.md). Assigning `TextureContent` updates
`Texture`.

If this property is set to [Content.none](/docs/reference/engine/datatypes/Content.md), the trail displays as
a solid plane colored by its [Color](/docs/reference/engine/classes/Trail.md) property. The
appearance of the texture can be further modified by
[Color](/docs/reference/engine/classes/Trail.md) and [Transparency](/docs/reference/engine/classes/Trail.md).
Scaling of the texture is determined by the distance between
[Attachment0](/docs/reference/engine/classes/Trail.md) and
[Attachment1](/docs/reference/engine/classes/Trail.md), as well as
[TextureMode](/docs/reference/engine/classes/Trail.md),
[TextureLength](/docs/reference/engine/classes/Trail.md), and
[WidthScale](/docs/reference/engine/classes/Trail.md).

### Property: Trail.TextureLength

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

Sets the length of the trail's texture, dependent on
[TextureMode](/docs/reference/engine/classes/Trail.md). Changing this property immediately
affects all existing and future trail segments.

### Property: Trail.TextureMode

```json
{
  "type": "TextureMode",
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

This property, alongside [TextureLength](/docs/reference/engine/classes/Trail.md),
determines how a trail's [Texture](/docs/reference/engine/classes/Trail.md) scales, repeats,
and moves along with the trail's attachments. Changing this property
immediately affects all existing and future trail segments.

#### Scale and Repetition

When **TextureMode** is set to [TextureMode.Wrap](/docs/reference/engine/enums/TextureMode.md) or
[TextureMode.Static](/docs/reference/engine/enums/TextureMode.md), the [TextureLength](/docs/reference/engine/classes/Trail.md)
property sets the length of the texture as it repeats across the trail's
length.

![TextureMode diagram with Wrap mode](/assets/engine-api/enums/TextureMode/Wrap-Static.png)

When **TextureMode** is set to [TextureMode.Stretch](/docs/reference/engine/enums/TextureMode.md), the texture
will repeat [TextureLength](/docs/reference/engine/classes/Trail.md) times across the
trail's overall length.

![TextureMode diagram with Stretch mode](/assets/engine-api/enums/TextureMode/Stretch.png)

#### Movement

The **TextureMode** property also affects the **movement** of the trail's
texture as follows:

- If set to [TextureMode.Stretch](/docs/reference/engine/enums/TextureMode.md), the texture will stretch out based
  on the lifetime of the trail, and shrink inwards if the trail's
  attachments stop moving.

- If set to [TextureMode.Wrap](/docs/reference/engine/enums/TextureMode.md), the texture will be tiled as the
  length of the trail changes, but the textures will remain stationary
  relative to their attachments.

- If set to [TextureMode.Static](/docs/reference/engine/enums/TextureMode.md), the texture will be rolled out as
  the attachments move, and they will remain in place until their lifetime
  is met. This setting is ideal for trail textures that should appear
  "stamped" where rendered, such as paw prints or tire tracks.

### Property: Trail.Transparency

```json
{
  "type": "NumberSequence",
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

Sets the transparency of the trail's segments over its
[Lifetime](/docs/reference/engine/classes/Trail.md). This value is a
[NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md), meaning it can be a static value or can change
throughout the lifetime of the trail segments.

### Property: Trail.WidthScale

```json
{
  "type": "NumberSequence",
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
  "category": "Emission",
  "capabilities": [
    "Basic"
  ]
}
```

This property is a [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md) that scales the width of the
trail over the course of its lifetime. Values can range between 0 and 1,
acting as a multiplier on the distance between the trail's attachments.
For example, if the trail's attachments are 2 stud's apart and the value
of this property is 0.5, the trail's width will be 1 stud and the trail
will be centered between the two attachments.

### Property: Trail.LocalTransparencyModifier *(hidden)*

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

The `LocalTransparencyModifier` property is a multiplier applied to the
trail's [Transparency](/docs/reference/engine/classes/Trail.md) that is only visible to
the local client. It does not replicate from client to server and is
useful for when a trail should not render for a specific client.

Uses the same formula as [BasePart.LocalTransparencyModifier](/docs/reference/engine/classes/BasePart.md):

`1` - ((`1` - [Transparency](/docs/reference/engine/classes/Trail.md)) &times; (`1` -
`LocalTransparencyModifier`))

A value of `0` (default) has no effect on the trail's transparency. A
value of `1` makes the trail completely invisible to the local client
regardless of its [Transparency](/docs/reference/engine/classes/Trail.md) value.

## Methods

### Method: Trail:Clear

**Signature:** `Trail:Clear(): ()`

This method immediately clears all segments of the trail and is useful for
cleaning up trails with longer lifetimes or for cases where the trail
should be removed because of a specific action.

Calling this method only affects existing segments. To clear existing
trail segments **and** temporarily prevent new segments from being drawn,
toggle the trail's [Enabled](/docs/reference/engine/classes/Trail.md) property to `false` at
the same time.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

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