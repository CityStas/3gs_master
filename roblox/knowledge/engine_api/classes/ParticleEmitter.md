---
name: ParticleEmitter
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "A special object that emits customizable 2D particles into the world."
---

# Class: ParticleEmitter

> A special object that emits customizable 2D particles into the world.

## Description

A **ParticleEmitter** is a special object that emits customizable 2D particles
into the world. To emit and render particles, it must be parented to a
[BasePart](/docs/reference/engine/classes/BasePart.md) or an [Attachment](/docs/reference/engine/classes/Attachment.md) within such a part. When parented to
a [BasePart](/docs/reference/engine/classes/BasePart.md), particles spawn randomly within the part's bounding box or
[shape](/docs/en-us/effects/particle-emitters.md#shape); when parented to an
[Attachment](/docs/reference/engine/classes/Attachment.md), particles spawn from the attachment's position.

Particles emit automatically when the emitter is
[Enabled](/docs/reference/engine/classes/ParticleEmitter.md) with a non-zero
[Rate](/docs/reference/engine/classes/ParticleEmitter.md), or manually when the
[Emit](/docs/reference/engine/classes/ParticleEmitter.md) method is called. With a non-zero
[Speed](/docs/reference/engine/classes/ParticleEmitter.md), particles are set in motion outwards
and/or inwards, depending on the [ShapeInOut](/docs/reference/engine/classes/ParticleEmitter.md)
property.

By default, particles face the camera, but the
[Orientation](/docs/reference/engine/classes/ParticleEmitter.md) can be modified to respect the
particle velocity instead.

During the [Lifetime](/docs/reference/engine/classes/ParticleEmitter.md) of the particles, they
can change appearance according to the [Color](/docs/reference/engine/classes/ParticleEmitter.md) and
[Size](/docs/reference/engine/classes/ParticleEmitter.md). Their motion can change over time according
to the [Drag](/docs/reference/engine/classes/ParticleEmitter.md) and
[Acceleration](/docs/reference/engine/classes/ParticleEmitter.md) properties, and they can
also move as their parent moves when they are
[LockedToPart](/docs/reference/engine/classes/ParticleEmitter.md) or have a non-zero
[VelocityInheritance](/docs/reference/engine/classes/ParticleEmitter.md).

To learn more about creating and customizing particle emitters, see
[Particle Emitters](/docs/en-us/effects/particle-emitters.md).

## Code Samples

**Creating a Particle Emitter from Scratch**

This rather lengthy code sample shows how every property of a
`ParticleEmitter` can be set, including [NumberRange](/docs/reference/engine/datatypes/NumberRange.md),
[NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md) and [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md) properties. Below is
how the ParticleEmitter should look after every property is set. Try playing
around with the different properties to customize how the effect looks!

```lua
local emitter = Instance.new("ParticleEmitter")
-- Number of particles = Rate * Lifetime
emitter.Rate = 5 -- Particles per second
emitter.Lifetime = NumberRange.new(1, 1) -- How long the particles should be alive (min, max)
emitter.Enabled = true

-- Visual properties
emitter.Texture = "rbxassetid://1266170131" -- A transparent image of a white ring
-- For Color, build a ColorSequence using ColorSequenceKeypoint
local colorKeypoints = {
	-- API: ColorSequenceKeypoint.new(time, color)
	ColorSequenceKeypoint.new(0, Color3.new(1, 1, 1)), -- At t=0, White
	ColorSequenceKeypoint.new(0.5, Color3.new(1, 0.5, 0)), -- At t=.5, Orange
	ColorSequenceKeypoint.new(1, Color3.new(1, 0, 0)), -- At t=1, Red
}
emitter.Color = ColorSequence.new(colorKeypoints)
local numberKeypoints = {
	-- API: NumberSequenceKeypoint.new(time, size, envelop)
	NumberSequenceKeypoint.new(0, 1), -- At t=0, fully transparent
	NumberSequenceKeypoint.new(0.1, 0), -- At t=.1, fully opaque
	NumberSequenceKeypoint.new(0.5, 0.25), -- At t=.5, mostly opaque
	NumberSequenceKeypoint.new(1, 1), -- At t=1, fully transparent
}
emitter.Transparency = NumberSequence.new(numberKeypoints)
emitter.LightEmission = 1 -- When particles overlap, multiply their color to be brighter
emitter.LightInfluence = 0 -- Don't be affected by world lighting

-- Speed properties
emitter.EmissionDirection = Enum.NormalId.Front -- Emit forwards
emitter.Speed = NumberRange.new(0, 0) -- Speed of zero
emitter.Drag = 0 -- Apply no drag to particle motion
emitter.VelocitySpread = NumberRange.new(0, 0)
emitter.VelocityInheritance = 0 -- Don't inherit parent velocity
emitter.Acceleration = Vector3.new(0, 0, 0)
emitter.LockedToPart = false -- Don't lock the particles to the parent
emitter.SpreadAngle = Vector2.new(0, 0) -- No spread angle on either axis

-- Simulation properties
local numberKeypoints2 = {
	NumberSequenceKeypoint.new(0, 0), -- At t=0, size of 0
	NumberSequenceKeypoint.new(1, 10), -- At t=1, size of 10
}
emitter.Size = NumberSequence.new(numberKeypoints2)
emitter.ZOffset = -1 -- Render slightly behind the actual position
emitter.Rotation = NumberRange.new(0, 360) -- Start at random rotation
emitter.RotSpeed = NumberRange.new(0) -- Do not rotate during simulation

-- Create an attachment so particles emit from the exact same spot (concentric rings)
local attachment = Instance.new("Attachment")
attachment.Position = Vector3.new(0, 5, 0) -- Move the attachment upwards a little
attachment.Parent = script.Parent
emitter.Parent = attachment
```

**Expected output:** When you run the code sample, you should see particles that look like the provided animation.

## Properties

### Property: ParticleEmitter.Acceleration

```json
{
  "type": "Vector3",
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
  "category": "Motion",
  "capabilities": [
    "Basic"
  ]
}
```

The **Acceleration** property determines how the
[Speed](/docs/reference/engine/classes/ParticleEmitter.md) of particles changes over their
lifetime. It is defined using a [Vector3](/docs/reference/engine/datatypes/Vector3.md) to determine the
acceleration on the global **X**/**Y**/**Z** axes and is measured in studs
per second squared. When changed, this property affects all particles
emitted by the emitter, both current and future.

Acceleration will slow particles down if the vector points in the opposite
[EmissionDirection](/docs/reference/engine/classes/ParticleEmitter.md) in which they
are emitted. Otherwise, it will speed them up.

### Property: ParticleEmitter.Brightness

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

Scales the light emitted from the emitter when
[ParticleEmitter.LightInfluence](/docs/reference/engine/classes/ParticleEmitter.md) is 0.

### Property: ParticleEmitter.Color

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

The **Color** property determines the color of all active particles over
their individual lifetimes. The color applies to the
[Texture](/docs/reference/engine/classes/ParticleEmitter.md) when rendering and it uses the
texture alpha along with the emitter's
[Transparency](/docs/reference/engine/classes/ParticleEmitter.md). If an emitter has a
[LightEmission](/docs/reference/engine/classes/ParticleEmitter.md) value that's greater
than 0, darker colors make particles appear more transparent.

Changing this property affects all particles emitted by the emitter, both
current and future.

When this property uses a gradient [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md), a particle's
present color is determined by linearly interpolating on the sequence
using the particle's age and its total lifetime. For example, if a
particle spawned 2 seconds ago and has a 4 second lifetime, the color will
be whatever is 50% of the way through the [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md).

### Property: ParticleEmitter.Drag

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
  "category": "Particles",
  "capabilities": [
    "Basic"
  ]
}
```

The **Drag** property determines the rate in seconds at which individual
particles will lose half their speed via exponential decay. Drag is
applied by scaling the expected velocity from
[Speed](/docs/reference/engine/classes/ParticleEmitter.md) and any velocity inherited from the
parent from
[VelocityInheritance](/docs/reference/engine/classes/ParticleEmitter.md). Setting
this property to a negative value will cause particles' velocities to grow
exponentially.

### Property: ParticleEmitter.EmissionDirection

```json
{
  "type": "NormalId",
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

The **EmissionDirection** property determines the face ([NormalId](/docs/reference/engine/enums/NormalId.md))
of the parent object that particles emit from. A negative
[Speed](/docs/reference/engine/classes/ParticleEmitter.md) means particles emit in the opposite
direction. [SpreadAngle](/docs/reference/engine/classes/ParticleEmitter.md) further varies
the emission direction.

If you add a [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md) to an [Attachment](/docs/reference/engine/classes/Attachment.md), which has a
direction, you can rotate the attachment itself
([Attachment.Orientation](/docs/reference/engine/classes/Attachment.md)) instead of using this property.

### Property: ParticleEmitter.Enabled

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

The **Enabled** property determines if particles emit from the emitter.
Setting this to `false` stops further particles from spawning, but any
existing particles remain active until they expire. This property is
useful when you have a pre-made particle effect that you want to remain
disabled until you need it to emit particles.

If you want to clear all particles from a disabled emitter, call
[Clear()](/docs/reference/engine/classes/ParticleEmitter.md). Then, if desired, call
[Emit()](/docs/reference/engine/classes/ParticleEmitter.md) on the emitter to emit and render
particles.

### Property: ParticleEmitter.FlipbookBlendFrames

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
  "category": "Flipbook",
  "capabilities": [
    "Basic"
  ]
}
```

The **FlipbookBlendFrames** property determines whether the frames in the
flipbook texture are blended between using a linear crossfade, or swapped
instantly.

### Property: ParticleEmitter.FlipbookFramerate

```json
{
  "type": "NumberRange",
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
  "category": "Flipbook",
  "capabilities": [
    "Basic"
  ]
}
```

The **FlipbookFramerate** property determines how fast the flipbook
texture animates in frames per second. Like
[Lifetime](/docs/reference/engine/classes/ParticleEmitter.md), you can set a minimum and
maximum range to randomize the framerate of the flipbook, with a maximum
of 30 frames per second.

### Property: ParticleEmitter.FlipbookIncompatible

```json
{
  "type": "string",
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
  "category": "Flipbook",
  "capabilities": [
    "Basic"
  ]
}
```

The error message to display if the
[Texture](/docs/reference/engine/classes/ParticleEmitter.md) is incompatible for a flipbook.
The flipbook texture size must be an exact multiple of the flipbook layout
size.

### Property: ParticleEmitter.FlipbookLayout

```json
{
  "type": "ParticleFlipbookLayout",
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
  "category": "Flipbook",
  "capabilities": [
    "Basic"
  ]
}
```

The **FlipbookLayout** property determines the layout of the texture. It
can be any value of the [ParticleFlipbookLayout](/docs/reference/engine/enums/ParticleFlipbookLayout.md) enum:

- **None** &ndash; Disable flipbook features and use the texture as a
  single static texture over the particle's lifetime.
- **Grid2x2** &ndash; 2&times;2 frames for a 4-frame animation.
- **Grid4x4** &ndash; 4&times;4 frames for a 16-frame animation.
- **Grid8x8** &ndash; 8&times;8 frames for a 64-frame animation.
- **Custom** &ndash; A custom grid size defined by
  [FlipbookSizeX](/docs/reference/engine/classes/ParticleEmitter.md) and
  [FlipbookSizeY](/docs/reference/engine/classes/ParticleEmitter.md).

### Property: ParticleEmitter.FlipbookMode

```json
{
  "type": "ParticleFlipbookMode",
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
  "category": "Flipbook",
  "capabilities": [
    "Basic"
  ]
}
```

The **FlipbookMode** property determines the type of the flipbook
animation. It can be any value of the [ParticleFlipbookMode](/docs/reference/engine/enums/ParticleFlipbookMode.md) enum:

- **Loop** &ndash; Continuously play through all frames, starting back at
  the first frame after playing the last.
- **OneShot** &ndash; Play through the animation only once across the
  particle's lifetime. With this setting, the
  [FlipbookFramerate](/docs/reference/engine/classes/ParticleEmitter.md) property
  doesn't apply; instead, the framerate is determined by the particle's
  [Lifetime](/docs/reference/engine/classes/ParticleEmitter.md) divided evenly by the number
  of frames in the animation. **OneShot** animations are useful for clear
  non-repeating animations, such as an explosion that creates a puff of
  smoke and then fades out.
- **PingPong** &ndash; Play from the first to the last frame, then in
  reverse from the last to the first, repeating throughout the
  [Lifetime](/docs/reference/engine/classes/ParticleEmitter.md) of the particle.
- **Random** &ndash; Play the frames in a random order,
  blending/crossfading from one frame to the next. This can be useful for
  organic particle textures at low framerates, such as stars slowly
  twinkling between subtly different shapes.

### Property: ParticleEmitter.FlipbookSizeX

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
  "category": "Flipbook",
  "capabilities": [
    "Basic"
  ]
}
```

The **FlipbookSizeX** property defines the number of horizontal frames
(columns) in a custom flipbook layout. This property only applies when
[FlipbookLayout](/docs/reference/engine/classes/ParticleEmitter.md) is set to
[Custom](/docs/reference/engine/enums/ParticleFlipbookLayout.md).

### Property: ParticleEmitter.FlipbookSizeY

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
  "category": "Flipbook",
  "capabilities": [
    "Basic"
  ]
}
```

The **FlipbookSizeY** property defines the number of vertical frames
(rows) in a custom flipbook layout. This property only applies when
[FlipbookLayout](/docs/reference/engine/classes/ParticleEmitter.md) is set to
[Custom](/docs/reference/engine/enums/ParticleFlipbookLayout.md).

### Property: ParticleEmitter.FlipbookStartRandom

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
  "category": "Flipbook",
  "capabilities": [
    "Basic"
  ]
}
```

The **FlipbookStartRandom** property determines whether each particle
begins at a random frame of the animation instead of always starting at
the first frame. One use case is to enable this property and also set
[FlipbookFramerate](/docs/reference/engine/classes/ParticleEmitter.md) to zero,
causing each emitted particle to be a static frame chosen randomly from
the flipbook texture.

### Property: ParticleEmitter.Lifetime

```json
{
  "type": "NumberRange",
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

The **Lifetime** property defines the maximum and minimum ages for newly
emitted particles. Lifetimes are stored on a per-particle basis, so if
this value is changed, existing particles will stay active until their
randomly chosen lifetime ends. A lifetime of 0 will prevent particles from
emitting at all.

### Property: ParticleEmitter.LightEmission

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

The **LightEmission** property determines the blending of the
[Texture](/docs/reference/engine/classes/ParticleEmitter.md) colors with the colors behind
them. A value of 0 uses normal blending mode while a value of 1 uses
additive blending. When changed, this property instantly affects all
particles owned by the emitter, both current and future.

This property should not be confused with
[LightInfluence](/docs/reference/engine/classes/ParticleEmitter.md) which determines how
particles are affected by environmental light.

This property does **not** cause particles to light the environment around
them. To accomplish that, consider using a [PointLight](/docs/reference/engine/classes/PointLight.md).

### Property: ParticleEmitter.LightInfluence

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

The **LightInfluence** property determines how much environmental light
affects the color of individual particles when they render. It must be in
the range of 0–1; behavior of values outside of this range are not
defined. At 0, particles are not influenced by light at all (they retain
full brightness); at 1, particles are fully influenced by light (in
complete darkness, particles will be black).

By default, this value is 1 if inserted with Studio tools. If inserted
using [Instance.new()](/docs/reference/engine/datatypes/Instance.md), it is 0.

### Property: ParticleEmitter.LockedToPart

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
  "category": "Particles",
  "capabilities": [
    "Basic"
  ]
}
```

The **LockedToPart** property determines if particles "stick" to the
emission source (the [Attachment](/docs/reference/engine/classes/Attachment.md) or [BasePart](/docs/reference/engine/classes/BasePart.md) to which the
[ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md) is parented). If `true`, active particles will
move in lock step if the parent object moves.

Alternatively, consider using the
[VelocityInheritance](/docs/reference/engine/classes/ParticleEmitter.md) property
with a value of 1 which may be more appropriate for some effects.

### Property: ParticleEmitter.Orientation

```json
{
  "type": "ParticleOrientation",
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

The **Orientation** property determines which orientation mode to use for
an emitter's particle geometry.

| Orientation | Particle Behavior |
| --- | --- |
| **FacingCamera** | Standard camera-facing billboard quad; default behavior. |
| **FacingCameraWorldUp** | Facing the camera, but rotating only on the vertical upward world **Y** axis. |
| **VelocityParallel** | Aligned parallel to their direction of movement. |
| **VelocityPerpendicular** | Aligned perpendicular to their direction movement. |

### Property: ParticleEmitter.Rate

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

The **Rate** property determines how many particles are emitted per second
while the emitter is [Enabled](/docs/reference/engine/classes/ParticleEmitter.md). It is the
inverse of frequency, meaning that a rate of 5 emits a particle every 0.2
seconds. When changed, this property has no affect on any active
particles.

### Property: ParticleEmitter.Rotation

```json
{
  "type": "NumberRange",
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

The **Rotation** property determines the range of rotations in degrees for
newly emitted particles, measured in degrees. Positive values are in the
clockwise direction. This property is commonly set to `[0, 360]` to
provide a completely random rotation to new particles.
[RotSpeed](/docs/reference/engine/classes/ParticleEmitter.md) also influences the rotation of
a particle over its lifetime.

Changes to this value only affect new particles; existing particles
maintain the rotation at which they were originally emitted.

### Property: ParticleEmitter.RotSpeed

```json
{
  "type": "NumberRange",
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

The **RotSpeed** property determines a random range of angular speeds for
newly emitted particles, measured in degrees per second. A random angular
speed is chosen upon emission, so changing this property doesn't affect
active particles. This property, along with
[Rotation](/docs/reference/engine/classes/ParticleEmitter.md), affects the angle of the
rendered particle image.

Particles with very high angular speeds can appear to rotate slower or not
at all, since the angle of rotation is synchronized with the software
render speed. For example, if particles rotate at exactly 360 degrees
every frame, there will be no apparent change in rotation.

### Property: ParticleEmitter.Shape

```json
{
  "type": "ParticleEmitterShape",
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
  "category": "EmitterShape",
  "capabilities": [
    "Basic"
  ]
}
```

The **Shape** property sets the shape of the emitter to either a box,
sphere, cylinder, or disc. After you make a selection, you can adjust the
[ShapeStyle](/docs/reference/engine/classes/ParticleEmitter.md),
[ShapeInOut](/docs/reference/engine/classes/ParticleEmitter.md), and
[ShapePartial](/docs/reference/engine/classes/ParticleEmitter.md) properties to further
customize particle emission. For visual examples, see
[here](/docs/en-us/effects/particle-emitters.md#shape).

### Property: ParticleEmitter.ShapeInOut

```json
{
  "type": "ParticleEmitterShapeInOut",
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
  "category": "EmitterShape",
  "capabilities": [
    "Basic"
  ]
}
```

Sets whether particles emit outward only, inward only, or in both
directions. For visual examples, see
[here](/docs/en-us/effects/particle-emitters.md#shape).

### Property: ParticleEmitter.ShapePartial

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
  "category": "EmitterShape",
  "capabilities": [
    "Basic"
  ]
}
```

Depending on the [Shape](/docs/reference/engine/classes/ParticleEmitter.md) value, this property
performs a different action:

- For cylinders, it specifies the top radius proportion. A value of 0
  means the top of the cylinder has zero radius, making it a cone. A value
  of 1 means the cylinder has no deformation.

- For discs, it specifies the inner radius proportion. A value of 0 means
  the disc is fully closed (circle/ellipse), while a value of 1 means
  emission only occurs on the outermost rim of the disc. Values between 0
  and 1 emit from an annulus with a certain thickness.

- For spheres, it specifies the hemispherical angle over which particles
  emit. A value of 1 means particles emit from the entire sphere; a value
  of 0.5 means particles emit from a half-dome; a value of 0 means
  particles only emit from a single point at the north pole.

For visual examples, see
[here](/docs/en-us/effects/particle-emitters.md#shape).

### Property: ParticleEmitter.ShapeStyle

```json
{
  "type": "ParticleEmitterShapeStyle",
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
  "category": "EmitterShape",
  "capabilities": [
    "Basic"
  ]
}
```

Sets particle emission to either volumetric or surface-only emission. For
visual examples, see [here](/docs/en-us/effects/particle-emitters.md#shape).

### Property: ParticleEmitter.Size

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

The **Size** property determines the world size of all active particles
over their individual lifetimes. This property represents the dimensions
of the square [Texture](/docs/reference/engine/classes/ParticleEmitter.md) for each particle.
It is a [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md) that works similarly to
[Transparency](/docs/reference/engine/classes/ParticleEmitter.md).

A particle's present size is determined by linearly interpolating on this
sequence using the particle's age and its total lifetime. For example, if
a particle spawned 2 seconds ago and has a 4 second lifetime, the size
will be whatever is 50% of the way through the [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md).
For any [NumberSequenceKeypoint](/docs/reference/engine/datatypes/NumberSequenceKeypoint.md) with a non-zero envelope value,
a random value in the envelope range is chosen for each keypoint for each
particle when it emits.

### Property: ParticleEmitter.Speed

```json
{
  "type": "NumberRange",
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

The **Speed** property determines a random range of velocities (minimum to
maximum) at which new particles will emit, measured in studs per second.
Each particle's velocity is chosen upon emission and it applies in the
[EmissionDirection](/docs/reference/engine/classes/ParticleEmitter.md). Negative
values cause particles to travel in reverse.

Note that changing [Speed](/docs/reference/engine/classes/ParticleEmitter.md) does not affect
active particles and they retain whatever speed they already have.
However, [Acceleration](/docs/reference/engine/classes/ParticleEmitter.md),
[Drag](/docs/reference/engine/classes/ParticleEmitter.md), and
[VelocityInheritance](/docs/reference/engine/classes/ParticleEmitter.md) can be
used to affect the speed of active particles over their lifetime.

### Property: ParticleEmitter.SpreadAngle

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
  "category": "Emission",
  "capabilities": [
    "Basic"
  ]
}
```

The **SpreadAngle** property determines the random angles at which a
particle may be emitted. For example, if the
[EmissionDirection](/docs/reference/engine/classes/ParticleEmitter.md) is **Top**
(+**Y**), this [Vector2](/docs/reference/engine/datatypes/Vector2.md) describes the size of the random angle
spread on the **X**/**Z** axes, in degrees.

Setting one axis to 360 will cause particles to emit in all direction in a
**circle**. Setting both to 360 will cause particles to emit in all
directions in a **sphere**.

### Property: ParticleEmitter.Squash

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

Allows for non-uniform scaling of particles, curve-controlled over their
lifetime. Values greater than 0 cause particles to both shrink
horizontally and grow vertically, while values less than 0 cause particles
to both grow horizontally and shrink vertically.

### Property: ParticleEmitter.Texture

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

The **Texture** property determines the image rendered on particles. This
image is influenced by [Color](/docs/reference/engine/classes/ParticleEmitter.md),
[Transparency](/docs/reference/engine/classes/ParticleEmitter.md),
[LightInfluence](/docs/reference/engine/classes/ParticleEmitter.md), and
[LightEmission](/docs/reference/engine/classes/ParticleEmitter.md). Textures with
transparent backgrounds work best for particles.

### Property: ParticleEmitter.TextureContent

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

The image rendered on particles. Supports
[asset URIs](/docs/en-us/projects/assets.md#asset-uris).

This property is the [Content](/docs/reference/engine/datatypes/Content.md) equivalent of
[Texture](/docs/reference/engine/classes/ParticleEmitter.md). Assigning `TextureContent`
updates `Texture`. The appearance of the texture is influenced by
[Color](/docs/reference/engine/classes/ParticleEmitter.md),
[Transparency](/docs/reference/engine/classes/ParticleEmitter.md),
[LightInfluence](/docs/reference/engine/classes/ParticleEmitter.md), and
[LightEmission](/docs/reference/engine/classes/ParticleEmitter.md).

### Property: ParticleEmitter.TimeScale

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
  "category": "Particles",
  "capabilities": [
    "Basic"
  ]
}
```

A value between 0 and 1 that controls the speed of the particle effect. At
1, it runs at normal speed; at 0.5 it runs at half speed; at 0 it freezes
in time.

### Property: ParticleEmitter.Transparency

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

The **Transparency** property determines the transparency of all active
particles over their individual lifetimes. It works similar to
[Size](/docs/reference/engine/classes/ParticleEmitter.md) in how it affects particles over time.
In terms of rendering, a value of 0 is completely visible (opaque) and a
value of 1 is completely invisible (not rendered at all).

A particle's present transparency is determined by linearly interpolating
on this sequence using the particle's age and its total lifetime. For
example, if a particle spawned 2 seconds ago and has a 4 second lifetime,
the transparency will be whatever is 50% of the way through the
[NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md). For any [NumberSequenceKeypoint](/docs/reference/engine/datatypes/NumberSequenceKeypoint.md) with
a non-zero envelope value, a random value in the envelope range is chosen
for each keypoint for each particle when it emits.

### Property: ParticleEmitter.VelocityInheritance

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
  "category": "Particles",
  "capabilities": [
    "Basic"
  ]
}
```

The **VelocityInheritance** property determines how much of the parent
part's [Velocity](/docs/reference/engine/classes/BasePart.md) is inherited by particles when
they are emitted. A value of 0 means that no velocity is inherited, while
a value of 1 means the particle will have the exact same speed as the
parent [BasePart](/docs/reference/engine/classes/BasePart.md).

When used in conjunction with [Drag](/docs/reference/engine/classes/ParticleEmitter.md), a
particle emitter can appear to "shed" particles from a moving part.

### Property: ParticleEmitter.WindAffectsDrag

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
  "category": "Particles",
  "capabilities": [
    "Basic"
  ]
}
```

If true, emitted particles follow the [Workspace.GlobalWind](/docs/reference/engine/classes/Workspace.md) vector.
Only applies if the [Drag](/docs/reference/engine/classes/ParticleEmitter.md) property is greater
than 0.

### Property: ParticleEmitter.ZOffset

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

The **ZOffset** property determines the forward-backward render position
of particles, in studs, without changing their size on the screen. When
changed, this property affects both current and future particles. Note
that this property accepts fractional values; it is not like
[GuiObject.ZIndex](/docs/reference/engine/classes/GuiObject.md) (an integer).

Positive values move particles closer to the camera and negative values
move particles away. Sufficiently negative values can cause particles to
render inside or behind the parent part.

### Property: ParticleEmitter.VelocitySpread

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
  "category": "Emission",
  "capabilities": [
    "Basic"
  ]
}
```

> **Deprecated:** This property has been superseded by [ParticleEmitter.SpreadAngle](/docs/reference/engine/classes/ParticleEmitter.md) which should be used in all new work.

This property determines how offset a particle can be fired from the local
emitter direction of its parent. When a particle is created its offset is
picked randomly between 0 and VelocitySpread. This value is measured in
degrees.

### Property: ParticleEmitter.LocalTransparencyModifier *(hidden)*

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
particle emitter's [Transparency](/docs/reference/engine/classes/ParticleEmitter.md) that
is only visible to the local client. It does not replicate from client to
server and is useful for when particles should not render for a specific
client.

Uses the same formula as [BasePart.LocalTransparencyModifier](/docs/reference/engine/classes/BasePart.md):

`1` - ((`1` - [Transparency](/docs/reference/engine/classes/ParticleEmitter.md)) &times;
(`1` - `LocalTransparencyModifier`))

A value of `0` (default) has no effect on the particle transparency. A
value of `1` makes all particles completely invisible to the local client
regardless of their [Transparency](/docs/reference/engine/classes/ParticleEmitter.md)
value.

## Methods

### Method: ParticleEmitter:Clear

**Signature:** `ParticleEmitter:Clear(): ()`

The **Clear** method instantly clears all existing particles that have
been emitted by the [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md) through its natural emission
(non-zero [Rate](/docs/reference/engine/classes/ParticleEmitter.md) on an
[Enabled](/docs/reference/engine/classes/ParticleEmitter.md) emitter) or via
[Emit()](/docs/reference/engine/classes/ParticleEmitter.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `()`

**ParticleEmitter Burst**

This code sample causes a `ParticleEmitter` to [ParticleEmitter:Emit()](/docs/reference/engine/classes/ParticleEmitter.md)
particles in bursts of 10 every 2 seconds. It [ParticleEmitter:Clear()](/docs/reference/engine/classes/ParticleEmitter.md)s
any existing particles before doing so.

```lua
local emitter = script.Parent
while true do
	emitter:Clear()
	emitter:Emit(10)
	task.wait(2)
end
```

**Expected output:** When run, the script should emit a burst of 10 particles every 10 seconds, clearing before each new emission.

### Method: ParticleEmitter:Emit

**Signature:** `ParticleEmitter:Emit(particleCount?: int): ()`

The **Emit** method will cause the [ParticleEmitter](/docs/reference/engine/classes/ParticleEmitter.md) to instantly
emit the given number of particles.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `particleCount` | `int` | `16` | The number of particles to emit. |

**Returns:** `()`

**Emit Particles Over Distance**

This code sample causes a parent `ParticleEmitter` to
[ParticleEmitter:Emit()](/docs/reference/engine/classes/ParticleEmitter.md) particles based on how far the parent
`BasePart` moves.

```lua
local RunService = game:GetService("RunService")

local emitter = script.Parent
local part = emitter.Parent

local PARTICLES_PER_STUD = 3

local lastPosition = part.Position
local distance = 0
local function onStep()
	local displacement = part.Position - lastPosition
	distance = distance + displacement.magnitude

	local n = math.floor(distance * PARTICLES_PER_STUD)
	emitter:Emit(n)
	distance = distance - n / PARTICLES_PER_STUD
	lastPosition = part.Position
end

RunService.Stepped:Connect(onStep)
emitter.Enabled = false
```

**Expected output:** While the script is running, moving the part should cause 3 particles to be emit per stud that the part moves.

**ParticleEmitter Burst**

This code sample causes a `ParticleEmitter` to [ParticleEmitter:Emit()](/docs/reference/engine/classes/ParticleEmitter.md)
particles in bursts of 10 every 2 seconds. It [ParticleEmitter:Clear()](/docs/reference/engine/classes/ParticleEmitter.md)s
any existing particles before doing so.

```lua
local emitter = script.Parent
while true do
	emitter:Clear()
	emitter:Emit(10)
	task.wait(2)
end
```

**Expected output:** When run, the script should emit a burst of 10 particles every 10 seconds, clearing before each new emission.

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