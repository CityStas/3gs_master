---
name: Lighting
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "The `Lighting` service controls global lighting in an experience. It includes a range of adjustable properties that you can use to change how lighting appears and interacts with other objects."
---

# Class: Lighting

> The `Lighting` service controls global lighting in an experience. It includes
> a range of adjustable properties that you can use to change how lighting
> appears and interacts with other objects.

## Description

The `Lighting` service controls global lighting in an experience. It includes
a range of adjustable properties that you can use to change how lighting
appears and interacts with other objects, as summarized in
[Lighting Properties](/docs/en-us/environment/lighting.md).

`Lighting` may also contain an [Atmosphere](/docs/reference/engine/classes/Atmosphere.md) object to render realistic
atmospheric effects, including particle density, haze, glare, and color. See
[Atmospheric Effects](/docs/en-us/environment/atmosphere.md) for details.

In addition, `Lighting` (along with [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md)) may
contain
[post‑processing effects](/docs/en-us/environment/post-processing-effects.md)
such as [SunRaysEffect](/docs/reference/engine/classes/SunRaysEffect.md) and [BlurEffect](/docs/reference/engine/classes/BlurEffect.md).

## Properties

### Property: Lighting.Ambient

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
    "Environment"
  ]
}
```

`Ambient` is the lighting hue applied to areas that are occluded from the
sky, such as indoor areas.

`Ambient` defaults to `[0, 0, 0]` (black). As long as the red, green, and
blue channels of this property do not exceed the corresponding channels in
[OutdoorAmbient](/docs/reference/engine/classes/Lighting.md), the change in hue will be
reserved for areas occluded from the sun/moon.

Note that when [GlobalShadows](/docs/reference/engine/classes/Lighting.md) is disabled,
there is no distinction between areas occluded from the sky and
non‑occluded areas. In this case,
[OutdoorAmbient](/docs/reference/engine/classes/Lighting.md) will be ignored and the hue
from the `Ambient` property will be applied everywhere.

### Property: Lighting.Brightness

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
    "Environment"
  ]
}
```

The intensity of illumination in the place.

Changing this value will influence the impact of the light source (sun or
moon) on the place's lighting. Note that [Ambient](/docs/reference/engine/classes/Lighting.md)
and [OutdoorAmbient](/docs/reference/engine/classes/Lighting.md) can also be used to
influence how bright a place appears. For example, setting
[OutdoorAmbient](/docs/reference/engine/classes/Lighting.md) to <Typography
noWrap>`[255, 255, 255]`</Typography> will make the place appear brighter
than its default value of <Typography noWrap>`127, 127, 127`</Typography>
(as it is more white).

### Property: Lighting.ClockTime

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
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Environment"
  ]
}
```

A numerical representation (in hours) of the current time of day used by
`Lighting`. Note that this property does not correspond with the actual
time of day and will not change during gameplay unless it has been changed
by a script.

For a measure of `Lighting` time formatted as a 24-hour string, use
[TimeOfDay](/docs/reference/engine/classes/Lighting.md). Changing
[TimeOfDay](/docs/reference/engine/classes/Lighting.md) or using
[SetMinutesAfterMidnight()](/docs/reference/engine/classes/Lighting.md) will
also change this property.

### Property: Lighting.ColorShift_Bottom

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
    "Environment"
  ]
}
```

The hue represented in light reflected in the opposite surfaces to those
facing the sun or moon.

The surfaces of a [BasePart](/docs/reference/engine/classes/BasePart.md) influenced by `ColorShift_Bottom`
depends on the position and orientation of the [BasePart](/docs/reference/engine/classes/BasePart.md) relative
to the sun or moon's position. Where the sun is directly overhead a
[BasePart](/docs/reference/engine/classes/BasePart.md), the shift in color will only apply to the bottom
surface.

This effect can be increased or reduced by altering
[Brightness](/docs/reference/engine/classes/Lighting.md).

Note that [ColorShift_Top](/docs/reference/engine/classes/Lighting.md) and
`ColorShift_Bottom` will interact with the
[Ambient](/docs/reference/engine/classes/Lighting.md) and
[OutdoorAmbient](/docs/reference/engine/classes/Lighting.md) properties if they are
greater than <Typography noWrap>`[0, 0, 0]`</Typography>. Also note that
the influence of `ColorShift_Bottom` can be very hard to identify when
[GlobalShadows](/docs/reference/engine/classes/Lighting.md) is enabled (default).

### Property: Lighting.ColorShift_Top

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
    "Environment"
  ]
}
```

The hue represented in light reflected from surfaces facing the sun or
moon.

The surfaces of a [BasePart](/docs/reference/engine/classes/BasePart.md) influenced by `ColorShift_Top` depends
on the position and orientation of the [BasePart](/docs/reference/engine/classes/BasePart.md) relative to the
sun or moon's position. Where the sun is directly overhead a
[BasePart](/docs/reference/engine/classes/BasePart.md), the shift in color will only apply to the top surface.

This effect can be increased or reduced by altering
[Brightness](/docs/reference/engine/classes/Lighting.md).

Note that `ColorShift_Top` and
[ColorShift_Bottom](/docs/reference/engine/classes/Lighting.md) will interact with
the [Ambient](/docs/reference/engine/classes/Lighting.md) and
[OutdoorAmbient](/docs/reference/engine/classes/Lighting.md) properties if they are
greater than <Typography noWrap>`[0, 0, 0]`</Typography>.

### Property: Lighting.EnvironmentDiffuseScale

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
    "Environment"
  ]
}
```

Ambient light that is derived from the environment with a default of `0`.
This property is similar to [Ambient](/docs/reference/engine/classes/Lighting.md) and
[OutdoorAmbient](/docs/reference/engine/classes/Lighting.md) but it's dynamic and can
change according to the sky and time of day. When this property is
increased, it's recommended to decrease [Ambient](/docs/reference/engine/classes/Lighting.md)
and [OutdoorAmbient](/docs/reference/engine/classes/Lighting.md) accordingly.

### Property: Lighting.EnvironmentSpecularScale

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
    "Environment"
  ]
}
```

Specular light derived from environment with a default of `0`. This
property will make smooth objects reflect the environment and it is
especially important to make metal look more realistic.

### Property: Lighting.ExposureCompensation

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
  "category": "Exposure",
  "capabilities": [
    "Environment"
  ]
}
```

This property determines the exposure compensation amount which applies a
bias to the exposure level of the scene prior to the tonemap step.
Defaults to `0` (no exposure compensation) and has a range from `-5` to
`5`. A value of `1` indicates twice as much exposure and `-1` means half
as much exposure.

### Property: Lighting.ExtendLightRangeTo120

```json
{
  "type": "RolloutState",
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
    "Environment"
  ]
}
```

Unused. The maximum [Range](/docs/reference/engine/classes/PointLight.md) of [PointLight](/docs/reference/engine/classes/PointLight.md),
[SpotLight](/docs/reference/engine/classes/SpotLight.md), and [SurfaceLight](/docs/reference/engine/classes/SurfaceLight.md) objects is always 120 studs;
this property does not change that clamp.

This property is typed as [RolloutState](/docs/reference/engine/enums/RolloutState.md). It is non-scriptable and
hidden in the Studio Properties window.

### Property: Lighting.FogColor

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
  "category": "Fog",
  "capabilities": [
    "Environment"
  ]
}
```

A [Color3](/docs/reference/engine/datatypes/Color3.md) value giving the hue of `Lighting` fog. Note that fog
properties are hidden when `Lighting` contains an [Atmosphere](/docs/reference/engine/classes/Atmosphere.md)
object.

### Property: Lighting.FogEnd

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
  "category": "Fog",
  "capabilities": [
    "Environment"
  ]
}
```

The depth from the [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md), in studs, at which fog
will be completely opaque. Note that fog properties are hidden when
`Lighting` contains an [Atmosphere](/docs/reference/engine/classes/Atmosphere.md) object.

### Property: Lighting.FogStart

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
  "category": "Fog",
  "capabilities": [
    "Environment"
  ]
}
```

The depth from the [Workspace.CurrentCamera](/docs/reference/engine/classes/Workspace.md), in studs, at which fog
begins to show. Note that fog properties are hidden when `Lighting`
contains an [Atmosphere](/docs/reference/engine/classes/Atmosphere.md) object.

### Property: Lighting.GeographicLatitude

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
  "category": "Data",
  "capabilities": [
    "Environment"
  ]
}
```

The geographic latitude, in degrees, of the scene, influencing the result
of `Lighting` time on the position of the sun and moon. When calculating
the position of the sun, the earth's tilt is also taken into account.

Changing `GeographicLatitude` will alter the position of the sun at every
[TimeOfDay](/docs/reference/engine/classes/Lighting.md). If you're looking to obtain the sun
or moon's position, use
[GetSunDirection()](/docs/reference/engine/classes/Lighting.md) or
[GetMoonDirection()](/docs/reference/engine/classes/Lighting.md).

### Property: Lighting.GlobalShadows

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
    "Environment"
  ]
}
```

Toggles voxel-based dynamic lighting in the place. When set to `true`,
shadows are rendered in sheltered areas depending on the position of the
sun and moon. The lighting hue applied to these sheltered areas is
determined by the [Ambient](/docs/reference/engine/classes/Lighting.md) property while the
lighting hue in all other areas is determined by the
[OutdoorAmbient](/docs/reference/engine/classes/Lighting.md) property.

When `false`, shadows are not drawn and no distinction is made between
indoor and outdoor areas. As a result, the
[Ambient](/docs/reference/engine/classes/Lighting.md) property determines the lighting hue and
[OutdoorAmbient](/docs/reference/engine/classes/Lighting.md) will do nothing.

Shadows are calculated using a voxel system and each lighting voxel is
4&times;4&times;4 studs. This means objects need to be larger than
4&times;4&times;4 studs to display a realistic shadow. Shadows are also
recalculated when [BaseParts](/docs/reference/engine/classes/BasePart.md) are moving.

### Property: Lighting.LightingStyle

```json
{
  "type": "LightingStyle",
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
    "Environment"
  ]
}
```

`LightingStyle` indicates the artistic intent behind lighting in the
experience, as an [LightingStyle](/docs/reference/engine/enums/LightingStyle.md) option. [LightingStyle.Soft](/docs/reference/engine/enums/LightingStyle.md)
is the stylized look; [LightingStyle.Realistic](/docs/reference/engine/enums/LightingStyle.md) is the naturalistic
look. The actual shadowing path also depends on
[PrioritizeLightingQuality](/docs/reference/engine/classes/Lighting.md) (for
example, Soft with that property enabled uses shadow maps rather than
voxel lighting).

### Property: Lighting.OutdoorAmbient

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
    "Environment"
  ]
}
```

`OutdoorAmbient` is the lighting hue applied to outdoor areas.

`OutdoorAmbient` defaults to `[127, 127, 127]`. As long as the red, green,
and blue channels of [Ambient](/docs/reference/engine/classes/Lighting.md) do not exceed the
corresponding channels in `OutdoorAmbient`, the hue of the lighting in
outdoor areas will be determined by this property.

The effective `OutdoorAmbient` value is clamped to be greater than or
equal to [Ambient](/docs/reference/engine/classes/Lighting.md) in all channels, meaning that if
a channel of [Ambient](/docs/reference/engine/classes/Lighting.md) exceeds its corresponding
`OutdoorAmbient` channel, the hue of [Ambient](/docs/reference/engine/classes/Lighting.md) will
begin to apply to outdoor areas.

Note that when [GlobalShadows](/docs/reference/engine/classes/Lighting.md) is disabled,
there is no distinction between areas occluded from the sky and
non‑occluded areas. In this case, `OutdoorAmbient` will be ignored and the
hue from the [Ambient](/docs/reference/engine/classes/Lighting.md) property will be applied
everywhere.

### Property: Lighting.PrioritizeLightingQuality

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
    "Environment"
  ]
}
```

This property indicates whether you prefer lighting/shading quality or
view distance to scale down first. As the rendering quality level reduces,
a setting of `true` prioritizes features such as advanced shadows and
high‑quality shaders at closer distances, while a setting of `false`
prioritizes view distance.

### Property: Lighting.ShadowSoftness

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
    "Environment"
  ]
}
```

Controls how blurry the shadows are with a default of `0.2`. This property
only works when [Technology](/docs/reference/engine/classes/Lighting.md) mode is
[ShadowMap](/docs/reference/engine/enums/Technology.md) or [Future](/docs/reference/engine/enums/Technology.md) and the device is
capable of rendering shadow maps.

### Property: Lighting.TimeOfDay

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
  "category": "Data",
  "capabilities": [
    "Environment"
  ]
}
```

A 24-hour string representation of the current time of day used by
`Lighting`. For example:

```lua
local Lighting = game:GetService("Lighting")

Lighting.TimeOfDay = "11:00" -- Set time of day to 11:00 AM
Lighting.TimeOfDay = "21:30" -- Set time of day to 9:30 PM
```

Note that this property does not correspond with the real-world time of
day and will not change during gameplay unless it has been changed by a
script.

For a numeric measure of `Lighting` time, use
[ClockTime](/docs/reference/engine/classes/Lighting.md). Changing
[ClockTime](/docs/reference/engine/classes/Lighting.md) or using
[SetMinutesAfterMidnight()](/docs/reference/engine/classes/Lighting.md) will
also change this property.

### Property: Lighting.Outlines

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

> **Deprecated:** This item is no longer supported as the outlines feature was removed from the Roblox platform.

This property determines whether outlines are enabled or disabled in a
place.

Outlines can be disabled on a global basis, using this `Lighting`
property, or alternatively on a surface-by-surface basis for
[BaseParts](/docs/reference/engine/classes/BasePart.md) using [SurfaceType](/docs/reference/engine/enums/SurfaceType.md).

Although this property can be set by scripts, it recommended this property
is set in Roblox Studio prior to publishing the place.

### Property: Lighting.ShadowColor

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
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

> **Deprecated:** This item is deprecated and has no current functionality. Do not use it for new work.

This is supposed to change the color of player shadows, but currently
doesn't do anything.

### Property: Lighting.Technology

```json
{
  "type": "Technology",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "Environment"
  ]
}
```

> **Deprecated:** This property has been superseded by [LightingStyle](/docs/reference/engine/classes/Lighting.md) which determines the artistic intent behind lighting, and [PrioritizeLightingQuality](/docs/reference/engine/classes/Lighting.md) which indicates whether you prefer lighting/shading quality or view distance to scale down first.

Determines the lighting system for rendering the 3D world. This property
is non‑scriptable and only modifiable in Studio.

## Methods

### Method: Lighting:GetMinutesAfterMidnight

**Signature:** `Lighting:GetMinutesAfterMidnight(): double`

Returns the number of minutes that have passed after midnight for the
purposes of lighting. This number will be nearly identical to
[ClockTime](/docs/reference/engine/classes/Lighting.md) multiplied by `60`.

Note that this number will not always be equal to the value given in
[SetMinutesAfterMidnight()](/docs/reference/engine/classes/Lighting.md) as it
returns minutes after midnight in the current day.

*Security: None · Thread Safety: Safe · Capabilities: Environment*

**Returns:** `double` — The number of minutes after midnight.

### Method: Lighting:GetMoonDirection

**Signature:** `Lighting:GetMoonDirection(): Vector3`

Returns a [Vector3](/docs/reference/engine/datatypes/Vector3.md) representing the direction of the moon from
the position <Typography noWrap>`(0, 0, 0)`</Typography>. Note that when
the moon has "set" and is no longer visible, the [Vector3](/docs/reference/engine/datatypes/Vector3.md)
returned by this method will continue to point towards the moon below the
horizon.

[GetSunDirection()](/docs/reference/engine/classes/Lighting.md) is a variant of this
method for obtaining the direction of the sun.

*Security: None · Thread Safety: Safe · Capabilities: Environment*

**Returns:** `Vector3` — [Vector3](/docs/reference/engine/datatypes/Vector3.md) representing the direction of the moon.

### Method: Lighting:GetMoonPhase

**Signature:** `Lighting:GetMoonPhase(): float`

Returns the moon's current phase. There is no way to change the moon's
phase so this will always return `0.75`.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Returns:** `float`

### Method: Lighting:GetSunDirection

**Signature:** `Lighting:GetSunDirection(): Vector3`

Returns a [Vector3](/docs/reference/engine/datatypes/Vector3.md) representing the direction of the sun from
the position <Typography noWrap>`(0, 0, 0)`</Typography>. Note that when
the sun has "set" and is no longer visible, the [Vector3](/docs/reference/engine/datatypes/Vector3.md)
returned by this method will continue to point towards the sun below the
horizon.

[GetMoonDirection()](/docs/reference/engine/classes/Lighting.md) is a variant of
this method for obtaining the direction of the moon.

*Security: None · Thread Safety: Safe · Capabilities: Environment*

**Returns:** `Vector3` — [Vector3](/docs/reference/engine/datatypes/Vector3.md) representing the direction of the sun.

### Method: Lighting:SetMinutesAfterMidnight

**Signature:** `Lighting:SetMinutesAfterMidnight(minutes: double): ()`

Sets [TimeOfDay](/docs/reference/engine/classes/Lighting.md) and
[ClockTime](/docs/reference/engine/classes/Lighting.md) to the given number of minutes after
midnight.

This method allows a numerical value to be used, for example in a
day/night cycle [Script](/docs/reference/engine/classes/Script.md), without the need to convert to a string in
the format required by [TimeOfDay](/docs/reference/engine/classes/Lighting.md). It also
allows values greater than 24 hours to be given that correspond to times
in the next day.

The following code sample includes a simple day/night cycle script. The
speed of time and the initial time can be changed using the `TIME_SPEED`
and `START_TIME` parameters.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `minutes` | `double` |  | The number of minutes after midnight. |

**Returns:** `()`

**Set Minutes After Midnight**

Demonstrates [Lighting:SetMinutesAfterMidnight()](/docs/reference/engine/classes/Lighting.md).

```lua
local Lighting = game:GetService("Lighting")

local TIME_SPEED = 60  -- 1 min = 1 hour
local START_TIME = 9  -- 9 AM

local minutesAfterMidnight = START_TIME * 60
local waitTime = 60 / TIME_SPEED

while true do
	minutesAfterMidnight = minutesAfterMidnight + 1

	Lighting:SetMinutesAfterMidnight(minutesAfterMidnight)

	task.wait(waitTime)
end
```

### Method: Lighting:getMinutesAfterMidnight

**Signature:** `Lighting:getMinutesAfterMidnight(): double`

> **Deprecated:** This method is a deprecated variant of [Lighting:GetMinutesAfterMidnight()](/docs/reference/engine/classes/Lighting.md) which should be used instead.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Returns:** `double`

### Method: Lighting:setMinutesAfterMidnight

**Signature:** `Lighting:setMinutesAfterMidnight(minutes: double): ()`

> **Deprecated:** This method is a deprecated variant of [Lighting:SetMinutesAfterMidnight()](/docs/reference/engine/classes/Lighting.md) which should be used instead.

*Security: None · Thread Safety: Unsafe · Capabilities: Environment*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `minutes` | `double` |  |  |

**Returns:** `()`

## Events

### Event: Lighting.LightingChanged

**Signature:** `Lighting.LightingChanged(skyChanged: boolean)`

This event fires when a `Lighting` property is changed or a [Sky](/docs/reference/engine/classes/Sky.md) is
added or removed from `Lighting`. See the `skyChanged` parameter for when
that flag is `true` versus `false`. Some Lighting property changes never
fire this event:

- Changing [GlobalShadows](/docs/reference/engine/classes/Lighting.md) will not fire this
  event.
- Changing fog properties [FogColor](/docs/reference/engine/classes/Lighting.md),
  [FogStart](/docs/reference/engine/classes/Lighting.md), or [FogEnd](/docs/reference/engine/classes/Lighting.md)
  will not fire this event.

In cases where this behavior is not desired, the [Object.Changed](/docs/reference/engine/classes/Object.md)
event or [Object:GetPropertyChangedSignal()](/docs/reference/engine/classes/Object.md) method can be used.

*Security: None · Capabilities: Environment*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `skyChanged` | `boolean` | `true` when a [Sky](/docs/reference/engine/classes/Sky.md) is added or removed, or when a Sky property other than [Sky.SkyboxOrientation](/docs/reference/engine/classes/Sky.md) changes. `false` for Lighting property changes, Atmosphere property changes, and SkyboxOrientation changes. |

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