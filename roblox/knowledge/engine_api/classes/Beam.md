---
name: Beam
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Connects two Attachments by drawing a texture between them."
---

# Class: Beam

> Connects two [Attachments](/docs/reference/engine/classes/Attachment.md) by drawing a texture between them.

## Description

A **Beam** object connects two [Attachments](/docs/reference/engine/classes/Attachment.md) by drawing a
texture between them.

To display, a beam must be a descendant of the [Workspace](/docs/reference/engine/classes/Workspace.md) with its
[Attachment0](/docs/reference/engine/classes/Beam.md) and [Attachment1](/docs/reference/engine/classes/Beam.md)
properties set to [Attachments](/docs/reference/engine/classes/Attachment.md) also descending from the
[Workspace](/docs/reference/engine/classes/Workspace.md).

The beam's appearance can be customized using the range of properties outlined
below. Also see the [Beams](/docs/en-us/effects/beams.md) guide for visual
examples.

#### Beam Curvature

Beams are configured to use a cubic Bézier curve formed by four control
points. This means they are not constrained to straight lines and the curve of
the beam can be modified by changing [CurveSize0](/docs/reference/engine/classes/Beam.md),
[CurveSize1](/docs/reference/engine/classes/Beam.md), and the orientation of the beam's
[Attachments](/docs/reference/engine/classes/Attachment.md).

- **P0** — The start of the beam; position of
  [Attachment0](/docs/reference/engine/classes/Beam.md).
- **P1** — [CurveSize0](/docs/reference/engine/classes/Beam.md) studs away from
  [Attachment0](/docs/reference/engine/classes/Beam.md), in the positive **X** direction of
  [Attachment0](/docs/reference/engine/classes/Beam.md).
- **P2** — [CurveSize1](/docs/reference/engine/classes/Beam.md) studs away from
  [Attachment1](/docs/reference/engine/classes/Beam.md), in the negative **X** direction of
  [Attachment1](/docs/reference/engine/classes/Beam.md).
- **P3** — The end of the beam; position of
  [Attachment1](/docs/reference/engine/classes/Beam.md)

![Beam curvature diagram](/assets/engine-api/classes/Beam/Curvature-Diagram.png)

## Code Samples

**Creating a Beam From Scratch**

This code sample demonstrates how a `Beam` effect can be created from scratch
by creating a `Beam`, setting all of its properties and configuring it's
`Attachment`s.

```lua
-- create attachments
local att0 = Instance.new("Attachment")
local att1 = Instance.new("Attachment")

-- parent to terrain (can be part instead)
att0.Parent = workspace.Terrain
att1.Parent = workspace.Terrain

-- position attachments
att0.Position = Vector3.new(0, 10, 0)
att1.Position = Vector3.new(0, 10, 10)

-- create beam
local beam = Instance.new("Beam")
beam.Attachment0 = att0
beam.Attachment1 = att1

-- appearance properties
beam.Color = ColorSequence.new({ -- a color sequence shifting from white to blue
	ColorSequenceKeypoint.new(0, Color3.fromRGB(255, 255, 255)),
	ColorSequenceKeypoint.new(1, Color3.fromRGB(0, 255, 255)),
})
beam.LightEmission = 1 -- use additive blending
beam.LightInfluence = 0 -- beam not influenced by light
beam.Texture = "rbxasset://textures/particles/sparkles_main.dds" -- a built in sparkle texture
beam.TextureMode = Enum.TextureMode.Wrap -- wrap so length can be set by TextureLength
beam.TextureLength = 1 -- repeating texture is 1 stud long
beam.TextureSpeed = 1 -- slow texture speed
beam.Transparency = NumberSequence.new({ -- beam fades out at the end
	NumberSequenceKeypoint.new(0, 0),
	NumberSequenceKeypoint.new(0.8, 0),
	NumberSequenceKeypoint.new(1, 1),
})
beam.ZOffset = 0 -- render at the position of the beam without offset

-- shape properties
beam.CurveSize0 = 2 -- create a curved beam
beam.CurveSize1 = -2 -- create a curved beam
beam.FaceCamera = true -- beam is visible from every angle
beam.Segments = 10 -- default curve resolution
beam.Width0 = 0.2 -- starts small
beam.Width1 = 2 -- ends big

-- parent beam
beam.Enabled = true
beam.Parent = att0
```

## Properties

### Property: Beam.Attachment0

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
  "category": "Shape",
  "capabilities": [
    "Basic"
  ]
}
```

The [Attachment](/docs/reference/engine/classes/Attachment.md) the beam originates from. This attachment is the
first control point on the beam's cubic Bézier curve; its orientation,
alongside the [CurveSize0](/docs/reference/engine/classes/Beam.md) property, determines the
position of the second control point. See
[Beams](/docs/en-us/effects/beams.md#curve) for more details.

For the [Attachment](/docs/reference/engine/classes/Attachment.md) where the beam ends, see
[Attachment1](/docs/reference/engine/classes/Beam.md).

### Property: Beam.Attachment1

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
  "category": "Shape",
  "capabilities": [
    "Basic"
  ]
}
```

The [Attachment](/docs/reference/engine/classes/Attachment.md) the beam ends at. This attachment is the fourth and
final control point on the beam's cubic Bézier curve; its orientation,
alongside the [CurveSize1](/docs/reference/engine/classes/Beam.md) property, determines the
position of the third control point. See
[Beams](/docs/en-us/effects/beams.md#curve) for more details.

For the [Attachment](/docs/reference/engine/classes/Attachment.md) where the beam originates from, see
[Attachment0](/docs/reference/engine/classes/Beam.md).

### Property: Beam.Brightness

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

Scales the light emitted from the beam when
[LightInfluence](/docs/reference/engine/classes/Beam.md) is less than 1. This property
is 1 by default and can set to any number within the range of 0 to 10000.
Increasing the value of [LightInfluence](/docs/reference/engine/classes/Beam.md)
decreases the effect of this property's value.

### Property: Beam.Color

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

Determines the color of the beam across its
[Segments](/docs/reference/engine/classes/Beam.md). If [Texture](/docs/reference/engine/classes/Beam.md) is set,
this color will be applied to the beam's texture. If no
[Texture](/docs/reference/engine/classes/Beam.md) is set, the [Beam](/docs/reference/engine/classes/Beam.md) will appear as a
solid line colored in accordance with this property.

This property is a [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md), allowing the color to be
configured to vary across the length of the beam. Consider the following
[ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md) which, when applied to a beam, would yield the
pictured result.

```lua
local colorSequence = ColorSequence.new({
		ColorSequenceKeypoint.new(0, Color3.fromRGB(255, 0, 0)), -- Red
		ColorSequenceKeypoint.new(0.5, Color3.fromRGB(0, 188, 203)), -- Cyan
		ColorSequenceKeypoint.new(1, Color3.fromRGB(196, 0, 255)), -- Purple
	}
)
```

Note the beam's coloration also depends on the number of
[Segments](/docs/reference/engine/classes/Beam.md) the [Beam](/docs/reference/engine/classes/Beam.md) has. Each segment of the
beam can only show a transition between two colors. Therefore a
[Beam](/docs/reference/engine/classes/Beam.md) will need to have at least `n-1` segments in order for the
color to display correctly, where `n` is the number of
[ColorSequenceKeypoints](/docs/reference/engine/datatypes/ColorSequenceKeypoint.md) in the
[ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md).

### Property: Beam.CurveSize0

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
  "category": "Shape",
  "capabilities": [
    "Basic"
  ]
}
```

Determines, along with [Attachment0](/docs/reference/engine/classes/Beam.md), the position
of the second control point in the beam's Bézier curve. See
[Beams](/docs/en-us/effects/beams.md#curve) for more details.

The position of this point can be determined by the following equation:

**Curve Size0**

Demonstrates [Beam.CurveSize0](/docs/reference/engine/classes/Beam.md).

```lua
local part = Instance.new("Part")
part.Anchored = true
part.Parent = workspace

local attachment0 = Instance.new("Attachment")
attachment0.Parent = part
local attachment1 = Instance.new("Attachment")
attachment1.Parent = part

local Beam = Instance.new("Beam")
Beam.Attachment0 = attachment0
Beam.Attachment1 = attachment1
Beam.Parent = part

local controlPoint2 = Beam.Attachment0.WorldPosition + (Beam.Attachment0.CFrame.RightVector * Beam.CurveSize0)
```

### Property: Beam.CurveSize1

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
  "category": "Shape",
  "capabilities": [
    "Basic"
  ]
}
```

Determines, along with [Attachment1](/docs/reference/engine/classes/Beam.md), the position
of the third control point in the beam's Bézier curve. See
[Beams](/docs/en-us/effects/beams.md#curve) for more details.

The position of this point can be determined by the following equation:

**Curve Size1**

Demonstrates [Beam.CurveSize1](/docs/reference/engine/classes/Beam.md).

```lua
local part = Instance.new("Part")
part.Anchored = true
part.Parent = workspace

local attachment0 = Instance.new("Attachment")
attachment0.Parent = part
local attachment1 = Instance.new("Attachment")
attachment1.Parent = part

local Beam = Instance.new("Beam")
Beam.Attachment0 = attachment0
Beam.Attachment1 = attachment1
Beam.Parent = part

local controlPoint3 = Beam.Attachment1.WorldPosition - (Beam.Attachment1.CFrame.RightVector * Beam.CurveSize1)
```

### Property: Beam.Enabled

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

Determines whether the beam is visible or not.

When this property is set to false, the beam's
[Segments](/docs/reference/engine/classes/Beam.md) will not be displayed.

### Property: Beam.FaceCamera

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
  "category": "Shape",
  "capabilities": [
    "Basic"
  ]
}
```

A [Beam](/docs/reference/engine/classes/Beam.md) is a 2D projection existing in 3D space, meaning that it
may not be visible from every angle. The **FaceCamera** property, when set
to `true`, ensures that the beam always faces the
[CurrentCamera](/docs/reference/engine/classes/Workspace.md), regardless of its
orientation.

### Property: Beam.LightEmission

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

Determines to what degree the colors of the beam are blended with the
colors behind it. It should be set in the range of 0 to 1. A value of 0
uses normal blending modes and a value of 1 uses additive blending.

This property should not be confused with
[LightInfluence](/docs/reference/engine/classes/Beam.md) which determines how the beam
is affected by environmental light.

This property does **not** cause the beam to light the environment.

### Property: Beam.LightInfluence

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

Determines the degree to which the beam is influenced by the environment's
lighting, clamped between 0 and 1. When 0, the beam will be unaffected by
the environment's lighting. When 1, it will be fully affected by lighting
as a [BasePart](/docs/reference/engine/classes/BasePart.md) would be.

See also [LightEmission](/docs/reference/engine/classes/Beam.md) which specifies to what
degree the colors of the beam are blended with the colors behind it.

### Property: Beam.Segments

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
  "category": "Shape",
  "capabilities": [
    "Basic"
  ]
}
```

Rather than being a perfect curve, a beam is made up of straight segments.
The more segments, the higher the resolution of the curve. The
**Segments** property sets how many straight segments the beam is made up
of, with a default value of 10.

Note that the [Color](/docs/reference/engine/classes/Beam.md) and
[Transparency](/docs/reference/engine/classes/Beam.md) properties require a certain number
of segments to display correctly. This is because each segment can only
show a transition between two colors or transparencies. Therefore a
[Beam](/docs/reference/engine/classes/Beam.md) requires at least `n-1` segments to display correctly, where
`n` is the number of keypoint associated with the beam's
[Color](/docs/reference/engine/classes/Beam.md) and [Transparency](/docs/reference/engine/classes/Beam.md).

### Property: Beam.Texture

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

The content ID of the texture to be displayed on the beam. If this
property is not set, the beam will be displayed as a solid line; this also
occurs when the texture is set to an invalid content ID or the image
associated with the texture has not yet loaded.

The appearance of the texture can be further modified by other beam
properties including [Color](/docs/reference/engine/classes/Beam.md) and
[Transparency](/docs/reference/engine/classes/Beam.md).

Scaling of the texture is determined by the
[TextureMode](/docs/reference/engine/classes/Beam.md),
[TextureLength](/docs/reference/engine/classes/Beam.md), [Width0](/docs/reference/engine/classes/Beam.md), and
[Width1](/docs/reference/engine/classes/Beam.md) properties.

### Property: Beam.TextureContent

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

The texture displayed on the beam. Supports
[asset URIs](/docs/en-us/projects/assets.md#asset-uris).

If this property is set to [Content.none](/docs/reference/engine/datatypes/Content.md), the beam displays as a
solid line colored by its [Color](/docs/reference/engine/classes/Beam.md) property. The
appearance of the texture can be further modified by
[Color](/docs/reference/engine/classes/Beam.md), [Transparency](/docs/reference/engine/classes/Beam.md), and
scaling is determined by [TextureMode](/docs/reference/engine/classes/Beam.md),
[TextureLength](/docs/reference/engine/classes/Beam.md), [Width0](/docs/reference/engine/classes/Beam.md), and
[Width1](/docs/reference/engine/classes/Beam.md).

### Property: Beam.TextureLength

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

Sets the length of the beam's texture, dependent on
[TextureMode](/docs/reference/engine/classes/Beam.md).

### Property: Beam.TextureMode

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

This property, alongside [TextureLength](/docs/reference/engine/classes/Beam.md),
determines how a beam's [Texture](/docs/reference/engine/classes/Beam.md) repeats.

When set to [TextureMode.Wrap](/docs/reference/engine/enums/TextureMode.md) or [TextureMode.Static](/docs/reference/engine/enums/TextureMode.md), the
texture repetitions will equal the beam's overall length (in&nbsp;studs)
divided by its [TextureLength](/docs/reference/engine/classes/Beam.md).

![TextureMode diagram with Wrap mode](/assets/engine-api/enums/TextureMode/Wrap-Static.png)

When set to [TextureMode.Stretch](/docs/reference/engine/enums/TextureMode.md), the texture will repeat
[TextureLength](/docs/reference/engine/classes/Beam.md) times across the beam's overall
length.

![TextureMode diagram with Stretch mode](/assets/engine-api/enums/TextureMode/Stretch.png)

### Property: Beam.TextureSpeed

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

Sets the number of texture cycles per second at which the
[Texture](/docs/reference/engine/classes/Beam.md) image moves along the beam, where one cycle
is a full traversal of the texture's UV range. When this property is a
positive value, the beam's texture will move from
[Attachment0](/docs/reference/engine/classes/Beam.md) to
[Attachment1](/docs/reference/engine/classes/Beam.md). This direction can be inverted by
setting this property to a negative number. The default value is `1`.

How far one cycle travels along the beam in studs depends on
[TextureMode](/docs/reference/engine/classes/Beam.md) and
[TextureLength](/docs/reference/engine/classes/Beam.md).

#### Examples

- `-2` — Texture scrolls from [Attachment1](/docs/reference/engine/classes/Beam.md) toward
  [Attachment0](/docs/reference/engine/classes/Beam.md), completing two cycles per second.
- `0` — Texture is static.
- `1` — Texture scrolls from [Attachment0](/docs/reference/engine/classes/Beam.md) toward
  [Attachment1](/docs/reference/engine/classes/Beam.md), completing one cycle per second
  (default).
- `2` — Texture scrolls from [Attachment0](/docs/reference/engine/classes/Beam.md) toward
  [Attachment1](/docs/reference/engine/classes/Beam.md), completing two cycles per second.

### Property: Beam.Transparency

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

Determines the transparency of the beam across its segments. This property
is a [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md), allowing the transparency to be configured
to vary across the length of the beam.

Consider the following [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md) which, when applied to a
beam, would yield the pictured result.

```lua
local numberSequence = NumberSequence.new({
		NumberSequenceKeypoint.new(0, 0), -- Opaque
		NumberSequenceKeypoint.new(0.5, 1), -- Transparent
		NumberSequenceKeypoint.new(1, 0), -- Opaque
	}
)
```

Note that the beam's transparency also depends on the number of
[Segments](/docs/reference/engine/classes/Beam.md). Each segment of the beam can only show a
transition between two transparencies. Therefore a beam will need to have
at least `n-1` segments in order to display correctly, where `n` is the
number of [NumberSequenceKeypoints](/docs/reference/engine/datatypes/NumberSequenceKeypoint.md) in the
[NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md).

### Property: Beam.Width0

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
  "category": "Shape",
  "capabilities": [
    "Basic"
  ]
}
```

The width of the beam at its origin
([Attachment0](/docs/reference/engine/classes/Beam.md)), in studs. The beam's width will
change linearly to [Width1](/docs/reference/engine/classes/Beam.md) studs at its end
([Attachment1](/docs/reference/engine/classes/Beam.md)).

### Property: Beam.Width1

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
  "category": "Shape",
  "capabilities": [
    "Basic"
  ]
}
```

The width of the beam at its end ([Attachment1](/docs/reference/engine/classes/Beam.md)),
in studs. The beam's width will change linearly from
[Width0](/docs/reference/engine/classes/Beam.md) studs at its origin
([Attachment0](/docs/reference/engine/classes/Beam.md)).

### Property: Beam.ZOffset

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

The distance, in studs, the beam display is offset relative to the
[CurrentCamera](/docs/reference/engine/classes/Workspace.md). When 0, the beam will be
displayed in its standard position between
[Attachment0](/docs/reference/engine/classes/Beam.md) and
[Attachment1](/docs/reference/engine/classes/Beam.md). **ZOffset** can be either positive
or negative.

This property is particularly useful to avoid "Z‑fighting" when using
multiple [Beams](/docs/reference/engine/classes/Beam.md) between the same
[Attachments](/docs/reference/engine/classes/Attachment.md).

**Layering Beams**

This code sample uses the [Beam.ZOffset](/docs/reference/engine/classes/Beam.md) property to layer multiple
beams between the same attachments.

```lua
-- Create beams
local beam1 = Instance.new("Beam")
beam1.Color = ColorSequence.new(Color3.new(1, 0, 0))
beam1.FaceCamera = true
beam1.Width0 = 3
beam1.Width1 = 3
local beam2 = Instance.new("Beam")
beam2.Color = ColorSequence.new(Color3.new(0, 1, 0))
beam2.FaceCamera = true
beam2.Width0 = 2
beam2.Width1 = 2
local beam3 = Instance.new("Beam")
beam3.Color = ColorSequence.new(Color3.new(0, 0, 1))
beam3.FaceCamera = true
beam3.Width0 = 1
beam3.Width1 = 1

-- Layer beams
beam1.ZOffset = 0
beam2.ZOffset = 0.01
beam3.ZOffset = 0.02

-- Create attachments
local attachment0 = Instance.new("Attachment")
attachment0.Position = Vector3.new(0, -10, 0)
attachment0.Parent = workspace.Terrain
local attachment1 = Instance.new("Attachment")
attachment1.Position = Vector3.new(0, 10, 0)
attachment1.Parent = workspace.Terrain

-- Connect beams
beam1.Attachment0 = attachment0
beam1.Attachment1 = attachment1
beam2.Attachment0 = attachment0
beam2.Attachment1 = attachment1
beam3.Attachment0 = attachment0
beam3.Attachment1 = attachment1

-- Parent beams
beam1.Parent = workspace
beam2.Parent = workspace
beam3.Parent = workspace
```

### Property: Beam.LocalTransparencyModifier *(hidden)*

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
beam's [Transparency](/docs/reference/engine/classes/Beam.md) that is only visible to the
local client. It does not replicate from client to server and is useful
for when a beam should not render for a specific client.

Uses the same formula as [BasePart.LocalTransparencyModifier](/docs/reference/engine/classes/BasePart.md).

A value of `0` (default) has no effect on the beam's transparency. A value
of `1` makes the beam completely invisible to the local client regardless
of its [Transparency](/docs/reference/engine/classes/Beam.md) value.

## Methods

### Method: Beam:SetTextureOffset

**Signature:** `Beam:SetTextureOffset(offset?: float): ()`

The offset of a beam's texture cycle represents the progress of its
texture animation. This method sets the current offset of the beam's
texture cycle; hence, it can be used to reset the cycle by passing `0` as
the `offset` parameter.

#### Notes

- The given `offset` parameter is expected to be a value between 0 and 1,
  but greater values can be used.
- The texture cycle wraps at 0 and 1, meaning the texture is in the same
  position when the offset is at 0 or 1.
- If the [Texture](/docs/reference/engine/classes/Beam.md) property is not set, this method
  does nothing.
- Increasing the offset will act in the inverse direction to the
  [TextureSpeed](/docs/reference/engine/classes/Beam.md) property, meaning it will move
  the texture in the opposite direction to the direction the texture
  animates when [TextureSpeed](/docs/reference/engine/classes/Beam.md) is greater than 0.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `offset` | `float` | `0` | The desired offset of the texture cycle. |

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