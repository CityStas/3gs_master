---
title: "Light sources"
url: /docs/en-us/effects/light-sources
last_updated: 2026-10-30T19:55:43Z
description: "Light sources simulate realistic lighting from objects such as torches, spotlights, and screens."
---

# Light sources

Local light sources simulate realistic lighting from objects such as lamps, torches, spotlights, and TV screens. By using the different types of light sources instead of just general global lighting through the `Class.Lighting` service, you can create immersive environments such as cyberpunk cities, traditional light festivals, and moody detective scenes.

![A far out view of a diner bulding in the middle of a nighttime city. The diner is utilizing several local light sources.](../assets/lighting-and-effects/light-sources/Showcase.jpg)
> **Info:** The `Class.Lighting.LightingStyle|LightingStyle` property, modifiable only in the [Properties](/docs/en-us/studio/properties.md) window for the global `Class.Lighting` object, sets your game's lighting style. For more information, see [Appearance](/docs/en-us/environment/lighting.md#appearance).
> **Success:** To view **light guides** that indicate the color and field of effect from light sources, such as the angle of light emission from the cone's apex of a `Class.SpotLight`, open [Studio Settings](/docs/en-us/studio/setup.md#customization) and toggle on **Show Light Guides**.
## Light types

Local light sources include [PointLight](#pointlight), [SpotLight](#spotlight), and [SurfaceLight](#surfacelight). Each [shares various properties](#shared-properties) from the `Class.Light` class, including `Class.Light.Color|Color`, `Class.Light.Brightness|Brightness`, and `Class.Light.Shadows|Shadows`.

### PointLight

A `Class.PointLight` emits light spherically from a single point. This object is ideal for **non-directional** lights like bulbs, torches, and fireballs.

To create a point light in Studio, insert a `Class.PointLight` into an `Class.Attachment` or a `Class.BasePart` (`Class.Attachment` is recommended for point‑specific light emission). Then adjust the object's `Class.PointLight.Range|Range` as well as [shared properties](#shared-properties) like `Class.PointLight.Brightness|Brightness` and `Class.PointLight.Color|Color`.

#### Range

A point light's `Class.PointLight.Range|Range` property defines the radial distance of illumination from the light's position, measured in studs.

#### 8

![A street lamp point light with a small range.](../assets/lighting-and-effects/light-sources/PointLight-Range-8.jpg)

#### 12

![The same street lamp point light with a larger range.](../assets/lighting-and-effects/light-sources/PointLight-Range-12.jpg)

### SpotLight

A `Class.SpotLight` emits light in the shape of a cone with a spherical base. This object is ideal for directional lights like street lamps, flashlights, and headlights.

To create a spotlight in Studio, insert a `Class.SpotLight` into an `Class.Attachment` or a `Class.BasePart` and set its `Class.SpotLight.Face|Face` property to specify which direction light emits from. Then adjust the `Class.SpotLight.Angle|Angle` and `Class.SpotLight.Range|Range`, as well as [shared properties](#shared-properties) like `Class.SpotLight.Brightness|Brightness` and `Class.SpotLight.Color|Color`.

#### Face

A spotlight's `Class.SpotLight.Face|Face` property determines which face/axis light emits from, as shown from the following streetlamp's glowing light part:

#### Bottom

![A street lamp spotlight that emits light from its bottom face.](../assets/lighting-and-effects/light-sources/SpotLight-Face-Bottom.jpg)

#### Left

![A street lamp spotlight that emits light from its left face.](../assets/lighting-and-effects/light-sources/SpotLight-Face-Left.jpg)

#### Angle

A spotlight's `Class.SpotLight.Angle|Angle` property defines the angle of light emission from the cone's apex. The maximum value is `180` which illuminates a full half sphere from the apex.

#### 30

![A street lamp spotlight with a 30 degree angle of emission.](../assets/lighting-and-effects/light-sources/SpotLight-Angle-30.jpg)

#### 75

![The same street lamp spotlight with a 75 degree angle of emission.](../assets/lighting-and-effects/light-sources/SpotLight-Angle-75.jpg)

### SurfaceLight

A `Class.SurfaceLight` emits light from the face of a `Class.BasePart`. This object is ideal for lighting from computer screens, billboards, signs, and fluorescent panels.

To create a surface light in Studio, insert a `Class.SurfaceLight` into a `Class.BasePart` and set its `Class.SurfaceLight.Face|Face` property to specify which surface light emits from. Then adjust the `Class.SurfaceLight.Angle|Angle` and `Class.SurfaceLight.Range|Range`, as well as [shared properties](#shared-properties) like `Class.SurfaceLight.Brightness|Brightness` and `Class.SurfaceLight.Color|Color`.

#### Face

A surface light's `Class.SurfaceLight.Face|Face` property determines the face of the `Class.BasePart` from which light emanates. Notice that light emits from the entire surface, not just a point on the surface.

#### Bottom

![A sign surface light that emits light from its bottom face.](../assets/lighting-and-effects/light-sources/SurfaceLight-Face-Bottom.jpg)

#### Right

![A sign surface light that emits light from its right face.](../assets/lighting-and-effects/light-sources/SurfaceLight-Face-Right.jpg)

#### Angle

A surface light's `Class.SurfaceLight.Angle|Angle` property defines the angle of light emission from the part's surface. An angle of `0` means that light travels directly outward from the surface while an angle of `180` means light travels outward perpendicular to the surface.

#### 0

![A sign surface light with a 0 degree angle of emission.](../assets/lighting-and-effects/light-sources/SurfaceLight-Angle-0.jpg)

#### 60

![A sign surface light with a 60 degree angle of emission.](../assets/lighting-and-effects/light-sources/SurfaceLight-Face-Right.jpg)

## Shared properties

All light sources share various properties from the `Class.Light` class, including [color](#color), [brightness](#brightness), and [shadows](#shadows).

### Color

The `Class.Light.Color|Color` property sets the `Datatype.Color3` value of the emitted light.

#### [255, 100, 50]

![A torch that emits red light.](../assets/lighting-and-effects/light-sources/Light-Color-255-100-50.jpg)

#### [0, 255, 125]

![A torch that emits green light.](../assets/lighting-and-effects/light-sources/Light-Color-0-255-125.jpg)

#### [75, 150, 255]

![A torch that emits blue light.](../assets/lighting-and-effects/light-sources/Light-Color-75-150-255.jpg)

### Brightness

The `Class.Light.Brightness|Brightness` property sets the light's brightness with maximum effect at the center of the light. Note that `Class.Light.Brightness|Brightness` is still limited to the light's defined range, so a higher `Class.Light.Brightness|Brightness` value doesn't light up a larger region around the light.

#### 2

![A torch that emits low light.](../assets/lighting-and-effects/light-sources/Light-Brightness-2.jpg)

#### 10

![A torch that emits medium light.](../assets/lighting-and-effects/light-sources/Light-Brightness-10.jpg)

#### 50

![A torch that emits bright light.](../assets/lighting-and-effects/light-sources/Light-Brightness-50.jpg)

### Shadows

The `Class.Light.Shadows|Shadows` property projects shadows where light is blocked by an obstacle.

#### Enabled

![A corner view of the diner with shadows enabled.](../assets/lighting-and-effects/light-sources/Light-Shadows-True.jpg)

#### Disabled

![A corner view of the diner with shadows disabled.](../assets/lighting-and-effects/light-sources/Light-Shadows-False.jpg)
