---
title: "Customize global lighting"
url: /docs/en-us/tutorials/curriculums/core/building/customize-global-lighting
last_updated: 2026-10-30T19:55:58Z
description: "Explains how to use global lighting settings to refine the look and feel of your game."
---

# Customize global lighting

**Global lighting** controls the overall look and atmosphere of your game. By adjusting a few properties on the `Class.Lighting` service, you can change the color, shadows, time of day, and atmospheric effects of a scene.

In this section, you'll update the lighting to match the [Island Jump - Final](https://www.roblox.com/games/14238807008/Island-Jump-Completed-Sample) sample.

> **Info:** Lighting is mostly configured through property values, making it a great fit for Assistant. After applying the prompt, spend some time in the viewport adjusting **Ambient**, **ClockTime**, and **Density** until the scene looks the way you want. For an overview of every lighting object Studio offers, see [Lighting and effects](/docs/en-us/environment.md).
## Set lighting properties

The `Class.Lighting` service controls how light behaves in your game. The sample game adjusts properties such as ambient color, lighting technology, shadow settings, and sun position to create a cooler ocean palette, sharper shadows, and stronger directional lighting.

#### Build with Assistant

```text
On the Lighting service, set the following properties:
- Ambient: Color3.fromRGB(16, 16, 16)
- ColorShift_Top: Color3.fromRGB(196, 222, 255)
- OutdoorAmbient: Color3.fromRGB(134, 158, 190)
- ShadowSoftness: 0
- LightingStyle: Realistic
- ClockTime: 9
- GeographicLatitude: 78
```

After it runs, the world picks up a cooler blue-grey tone, shadows get hard edges, and the sun shifts to mid-morning over to the right of your sea stacks.

#### Build it Yourself

In the **Properties** window of **Lighting**:

1. **Tint the ambient and reflective light.** `Class.Lighting.Ambient` colors light in shaded areas (like the inside of your tunnel), `Class.Lighting.OutdoorAmbient` colors light where the sky is visible, and `Class.Lighting.ColorShift_Top` tints surfaces facing the sun. Together they pull the whole world toward a cool blue-grey ocean tone.
  1. Set **Ambient** to `16, 16, 16`.
  2. Set **ColorShift_Top** to `196, 222, 255`.
  3. Set **OutdoorAmbient** to `134, 158, 190`.**A comparison between the sample Island Jump game's default and custom ambient lighting**![The sample Island Jump game with default ambient lighting visuals.](../../../../assets/tutorials/core-building-and-scripting/Default-Color.jpg)_Default Properties_![The sample Island Jump game with custom ambient lighting visuals.](../../../../assets/tutorials/core-building-and-scripting/Custom-Color.jpg)_Custom Properties_
2. **Switch to realistic lighting.** Studio defaults to `Enum.LightingStyle|Soft`, which produces a flatter look. Set **LightingStyle** to `Enum.LightingStyle|Realistic` so local light sources cast precise shadows and illumination. Your flare will start dropping a real shadow on the platform beneath it.![The sample Island Jump game with Soft lighting style.](../../../../assets/tutorials/core-building-and-scripting/LightingStyle-Soft.jpg)_`Enum.LightingStyle|Soft`_![The sample Island Jump game with Realistic lighting produces more prominent lighting from the flare.](../../../../assets/tutorials/core-building-and-scripting/LightingStyle-Realistic.jpg)_`Enum.LightingStyle|Realistic`_
3. **Harden shadows.** Set **ShadowSoftness** to `0` to give shadows crisp edges. This makes the moment players step from outside into the tunnel feel more dramatic.![The sample Island Jump game with default shadow visuals that produce fuzzy shadows.](../../../../assets/tutorials/core-building-and-scripting/Default-Shadows.jpg)_Default Shadows_![The sample Island Jump game with custom shadow visuals that produce sharp shadows.](../../../../assets/tutorials/core-building-and-scripting/Custom-Shadows.jpg)_Custom Shadows_
4. **Move the sun.** `Class.Lighting.ClockTime|ClockTime` is the time of day on a 0-24 hour scale, and `Class.Lighting.GeographicLatitude|GeographicLatitude` rotates the world to position the sun at a different angle. The values below drop the sun toward the right of the sea stacks for longer, more directional shadows.
  1. Set **ClockTime** to `9`.
  2. Set **GeographicLatitude** to `78`.
  > **Info:****ClockTime** and **TimeOfDay** are linked. Changing one updates the other, so you only need to set one.![The sample Island Jump game with the default sun position high in the sky.](../../../../assets/tutorials/core-building-and-scripting/Default-SunPosition.jpg)_Default sun position_![The sample Island Jump game with a custom sun position approaching the horizon.](../../../../assets/tutorials/core-building-and-scripting/Custom-SunPosition.jpg)_Custom sun position_

For an overview of the rest of the `Class.Lighting` properties, see [Global lighting](/docs/en-us/environment/lighting.md).

## Atmosphere properties

The `Class.Atmosphere` object is a child of the `Class.Lighting` service. It adds depth by simulating particles in the air and blending distant scenery into the sky. The two most important properties are `Density`, which controls the thickness of the atmosphere, and `Offset`, which controls where that blending begins.

#### Build with Assistant

```text
On the Atmosphere object inside the Lighting service, set:
- Density: 0.375
- Offset: 0.17
```

#### Build it Yourself

1. In the **Explorer**, expand the **Lighting** service and select its child **Atmosphere** object. In the **Properties** window:
  1. Set **Density** to `0.375` to thicken the air. This obscures the edge of your water terrain, so players don't see where the world ends.![The sample Island Jump game with the default air particle density that produces a clear background.](../../../../assets/tutorials/core-building-and-scripting/Custom-SunPosition.jpg)_Default air particle density_![The sample Island Jump game with custom air particle density that produces a hazy background.](../../../../assets/tutorials/core-building-and-scripting/Custom-AirParticleDensity.jpg)_Custom air particle density_
  1. Set **Offset** to `0.17`. Lower offset values blend distant objects into the sky, which is good for endless-feeling worlds. Higher values keep a clear silhouette. This middle value keeps the mountains you'll add next chapter visible while still giving you a hint of distant fog.![The sample Island Jump game with default Offset values that keep the background visible.](../../../../assets/tutorials/core-building-and-scripting/Custom-AirParticleDensity.jpg)_Default `Class.Atmosphere.Offset`_![The sample Island Jump game with custom Offset values that hide the edges of the background.](../../../../assets/tutorials/core-building-and-scripting/Custom-Offset.jpg)_Custom `Class.Atmosphere.Offset`_

For more information about Atmosphere, see [Atmospheric Effects](/docs/en-us/environment/atmosphere.md).

Now that you've configured the game's lighting, the next section shows you how to replace the greybox layout with polished assets.

#### Pre-Customization

![The sample Island Jump game's lighting visuals before the customization from this page.](../../../../assets/tutorials/core-building-and-scripting/Lighting-Pre-Customization.jpg)

#### Customized Visual Effects

![The sample Island Jump game's lighting visuals after the customization from this page.](../../../../assets/tutorials/core-building-and-scripting/Lighting-Post-Customization.jpg)
