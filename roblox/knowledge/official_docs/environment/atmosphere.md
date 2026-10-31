---
title: "Atmospheric effects"
url: /docs/en-us/environment/atmosphere
last_updated: 2026-10-30T19:55:43Z
description: "Atmospheric effects simulate realistic environments by scattering sunlight in unique ways."
---

# Atmospheric effects

**Atmospheric effects** simulate realistic environments by scattering sunlight in unique ways based on properties that control air particles. Using the `Class.Atmosphere` object, you can:

- Control particle density.
- Create a silhouette or blend distant objects with an offset.
- Simulate a haze or glare.
- Set an atmosphere's color or decay.

![Atmospheric effects used to render a brilliant sunset scene](../assets/lighting-and-effects/atmosphere/Sahara-Sunset.jpg) ## Atmosphere properties

Every property of the `Class.Atmosphere` object inside the `Class.Lighting` service works together to support the overall vision, themes, and mood of your game.

![Atmosphere object shown in Explorer window of Studio](../assets/studio/explorer/Lighting-Atmosphere.png) ### Density

The `Class.Atmosphere.Density|Density` property controls how many particles exist in the air of your game; the higher the density, the more particles, which obstruct a player's view of objects and terrain.

#### 0

![Atmosphere with Density value of 0](../assets/lighting-and-effects/atmosphere/Density-A.jpg)

#### 0.35

![Atmosphere with Density value of 0.35](../assets/lighting-and-effects/atmosphere/Density-B.jpg)

> **Info:** Density only **directly** affects objects and terrain; however, since you view a [skybox](/docs/en-us/environment/skybox.md) through those objects and terrain, the visibility of a skybox is also affected.
### Offset

The `Class.Atmosphere.Offset|Offset` property controls how light transmits between the camera and the sky background. When you increase this value, it creates a horizon silhouette; when you decrease this value, it blends distant objects into the sky for a seemingly endless and seamless open world.

#### 0

![Atmosphere with Offset value of 0](../assets/lighting-and-effects/atmosphere/Offset-A.jpg)

#### 1

![Atmosphere with Offset value of 1](../assets/lighting-and-effects/atmosphere/Offset-B.jpg)

> **Warning:** Carefully balance the `Class.Atmosphere.Offset|Offset` property with the `Class.Atmosphere.Density|Density` property. A low offset value may cause the [skybox](/docs/en-us/environment/skybox.md) to be seen through objects and terrain, and a high offset value may cause distant objects and terrain to have too much detail for your desired lighting effect.
### Haze

The `Class.Atmosphere.Haze|Haze` property controls the haziness of the atmosphere to create a visible effect both above the horizon and far into the distance from the camera. To create environmental moods, like a smoky tint for a polluted alien planet or a foggy blue tint for a somber game, combine this property with the [Color](#color) property.

#### 1

![Atmosphere with Haze value of 1](../assets/lighting-and-effects/atmosphere/Haze-A.jpg)

#### 2.8

![Atmosphere with Haze value of 2.8](../assets/lighting-and-effects/atmosphere/Haze-B.jpg)

### Color

The `Class.Atmosphere.Color|Color` property sets the hue of the atmosphere for subtle environmental moods and themes. To expand this property's visible effect, combine it with a high [Haze](#haze) property value.

#### [255, 255, 255]

![Atmosphere with Color value of [255, 255, 255]](../assets/lighting-and-effects/atmosphere/Color-A.jpg)

#### [255, 200, 255]

![Atmosphere with Color value of [255, 200, 255]](../assets/lighting-and-effects/atmosphere/Color-B.jpg)

### Glare

The `Class.Atmosphere.Glare|Glare` property sets an atmospheric glare around the sun. A high value results in an increased effect of sunlight cast onto the sky and game. To see this property's visible effect, you **must** combine a glare with a [Haze](#haze) value higher than 0.

#### 0

![Atmosphere with Glare value of 0](../assets/lighting-and-effects/atmosphere/Glare-A.jpg)

#### 1

![Atmosphere with Glare value of 1](../assets/lighting-and-effects/atmosphere/Glare-B.jpg)

### Decay

The `Class.Atmosphere.Decay|Decay` property sets the hue of the atmosphere away from the sun, gradually falling off from [Color](#color) toward this value. To see this property's visible effect, you **must** combine a glare with [Haze](#haze) and [Glare](#glare) values higher than 0.

#### [255, 255, 255]

![Atmosphere with Decay value of [255, 255, 255]](../assets/lighting-and-effects/atmosphere/Decay-A.jpg)

#### [255, 90, 80]

![Atmosphere with Decay value of [255, 90, 80]](../assets/lighting-and-effects/atmosphere/Decay-B.jpg)
