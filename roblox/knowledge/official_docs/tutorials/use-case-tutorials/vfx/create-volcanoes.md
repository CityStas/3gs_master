---
title: "Create volcanic eruptions with VFX"
url: /docs/en-us/tutorials/use-case-tutorials/vfx/create-volcanoes
last_updated: 2026-10-30T19:56:01Z
description: "The process of creating volcanoes to elevate your visual and gameplay requirements."
---

# Create volcanic eruptions with VFX

A **volcano** is a crater within the earth's crust that spews lava and smoke due to internal pressure from magma and dissolved gasses. Games often include volcanoes within challenging gameplay areas, such as locations where players must balance the danger of lava and molten rock hazards with the reward of valuable resources, boss battle arenas, or environments that dynamically change as the volcano cyclically erupts.

Using the [Volcano Island - Start](https://create.roblox.com/dashboard/creations/experiences/5825677169/overview) `.rbxl` file as a starting place and [Volcano Island - Complete](https://www.roblox.com/games/17374256579/Volcano-Island-Complete) as a reference, this tutorial shows you how to transform the environment into a volcanic eruption with custom lighting and VFX objects that represent real-world physical behavior, including guidance on:

- Breaking down referential material into individual components with distinct visual and behavioral characteristics.
- Configuring surface ripples to emulate hot fluid rising to the surface and disrupting the surface of the caldera.
- Configuring embers to emulate pieces of molten rock quickly cooling as they rise into the atmosphere.
- Configuring lava that splashes and flows from the caldera to emulate various types of lava viscosity states.
- Configuring a smoke plume to emulate harsh impurities rising into the sky that catch players' attention.

> **Info:** You can create your own textures in third-party texture creation tools and follow along with your own design. For information on importing textures for use in Studio, see [Asset Manager](/docs/en-us/projects/assets/manager.md).

![The starting volcano terrain you can use to complete this tutorial.](../../../assets/tutorials/creating-volcanoes/Volcano-Start.jpg)_Volcano Island - Start_

![The complete volcano with VFX objects you will create by the end of this tutorial.](../../../assets/tutorials/creating-volcanoes/Volcano-Complete.jpg)_Volcano Island - Complete_

## Break down reference

To create credible volcanoes, it's important to reference real-world volcanic eruptions in the design process because it allows you to break down the subject matter into individual components with distinct visual and behavioral characteristics. For example, the sample [Volcano Island - Complete](https://www.roblox.com/games/17374256579/Volcano-Island-Complete) game references the volcanic eruption in Iceland to inform all texture and VFX design decisions relating to the caldera and its surrounding terrain.

![A far out view of an Iceland volcanic eruption.](../../../assets/tutorials/creating-volcanoes/Volcano-NoComponents.jpg)

It's useful to break down a volcano that's erupting into individual components so that you can plan how to utilize different VFX objects to mimic their real-world counterparts. To demonstrate, this tutorial breaks the sample volcano into five unique components:

- **Surface Ripples** – The small waves of lava on the surface of the caldera.
- **Embers** – The small, light pieces of molten rock that rise to the sky from the caldera.
- **Lava Splashes** – The thin molten rock that bursts out from the caldera due to internal pressure within the volcano.
- **Lava Flow** – The viscous molten rock that oozes away from the caldera.
- **Smoke Plume** – The warm, billowing gas that rises into the sky from the caldera.

![The volcanic eruption reference with all five components highlighted.](../../../assets/tutorials/creating-volcanoes/Volcano-Components.jpg)

![The sample volcanic eruption with the same five components highlighted to compare the reference image with the final result.](../../../assets/tutorials/creating-volcanoes/Sample-Components.jpg)

The following sections provide an in-depth analysis of the different design decisions and techniques you can use to recreate each of these components. As you review these decisions and experiment with various lighting, `Class.ParticleEmitter`, and `Class.Beam` properties, you will learn how to utilize lighting and VFX to solve the unique environmental requirements for your own games.

## Configure lighting

To make an environmental element a point of interest within your game, it's important to increase its contrast against the overall environment so that it stands out as something that players should explore. For example, to draw players into the caldera, you can configure your lighting sources so that the volcano's lava appears to glow as the only light source within an otherwise dark environment.

Studio provides two high-level types of lighting sources you can use for this technique:

- **Global lighting** - Produces lighting for the entire outdoor environment.
- **Local lighting** - Produces lighting around where you place them within your game.

This section of the tutorial teaches you how to utilize both types of lighting sources to make your volcanic eruption the most significant point of interest within your scene, as well as create a dramatic effect for your environmental storytelling. To illustrate, review how the same final volcano without custom lighting feels like an unobtrusive hazard in an otherwise cheerful environment while the volcano with custom lighting feels like a dangerous presence in a dark, melancholic environment.

![The complete version of the sample volcanic eruption with default light sources.](../../../assets/tutorials/creating-volcanoes/Default-Lighting.jpg)_With default light sources_

![The complete version of the sample volcanic eruption with custom light sources.](../../../assets/tutorials/creating-volcanoes/Custom-Lighting.jpg)_With custom light sources_

### Local lighting

Local lighting is the luminescence from local [light sources](/docs/en-us/effects/light-sources.md) in your game, such as `Class.SpotLight`, `Class.SurfaceLight`, and `Class.PointLight` objects. Local lighting is important to add to your volcano because while you can apply brightness to your `Class.ParticleEmitter` and `Class.Beam` textures, they cannot fill the canyon with enough light alone to realistically simulate how the caldera and its flowing lava would illuminate the environment in the real world.

![The complete version of the sample volcanic eruption without local lighting.](../../../assets/tutorials/creating-volcanoes/Without-LocalLighting.jpg)_Without local lighting_

![The complete version of the sample volcanic eruption with local lighting.](../../../assets/tutorials/creating-volcanoes/With-LocalLighting.jpg)_With local lighting_

It's helpful to configure your local lighting before your global lighting for this tutorial because without the local light sources, you cannot see the 3D space to configure your VFX objects. However, common workflows require you to iterate on both local and global lighting concurrently to see the effects of your changes on VFX objects, so it's important to be flexible to design requirements of your own games.

To recreate the local lighting for the volcano in the sample [Volcano Island - Complete](https://www.roblox.com/games/17374256579/Volcano-Island-Complete) place file:

1. In the **Explorer** window, create a **Folder** in the **Workspace** to contain all local light source objects, then rename the folder **LocalLighting**.
2. Insert three **block** parts into the **LocalLighting** folder, then rename them **LightCaldera**, **LightMagma**, and **LightOutflow**, respectively.
3. Move the parts to a position where they can light the entirety of the volcano.
  1. Move **LightCaldera** to the center of the space between the caldera and the cliff.
  2. Move **LightMagma** to the center of the crevice between the caldera and the magma outflow.
  3. Move **LightOutflow** to slightly above where the outflow forks into two streams.![A front view of the volcano with three block parts positioned throughout the volcano's valley.](../../../assets/tutorials/creating-volcanoes/LL-3.jpg)
4. Insert a **Pointlight** into each part.![A front view of the volcano with three block parts with point light visual aids.](../../../assets/tutorials/creating-volcanoes/LL-4.jpg)
5. Select the **PointLight** child of **LightCaldera**, then in the **Properties** window,
  1. Set **Brightness** to `15` to make the light source much brighter.
  2. Set **Color** to `255, 85, 0` to tint the light to a dark orange hue.
  3. Set **Range** to `60` to illuminate the entire caldera area.![A front view of the volcano with three block parts. The block part nearest the caldera emits orange light.](../../../assets/tutorials/creating-volcanoes/LL-5.jpg)
6. Select the **PointLight** children of **LightMagma** and **LightOutflow**, then in the **Properties** window,
  1. Set **Brightness** to `2` to make the light source slightly brighter.
  2. Set **Color** to `255, 81, 0` to tint the light to an orange hue.
  3. Set **Range** to `50` to illuminate the crevice and outflow areas.![A front view of the volcano with three block parts that are all emitting orange light.](../../../assets/tutorials/creating-volcanoes/LL-6.jpg)
7. In the **Explorer** window, select all block parts in the **LocalLighting** folder, then in the **Properties** window, set **Transparency** to `1` to make the blocks invisible.![A front view of the volcano that has orange lighting throughout the volcano's valley.](../../../assets/tutorials/creating-volcanoes/LL-7.jpg)

### Global lighting

Global lighting is the luminescence from either the sun or moon in a game. By adjusting a couple of key default properties in the `Class.Lighting` service and its child post-processing effects objects, you can dramatically change how global light appears to players, as well as how it interacts with any other object you place in the game, including `Class.ParticleEmitter` and `Class.Beam` textures.

For example, to ensure that the `Class.Beam` textures that produce a flowing lava effect later in the tutorial are able to glow, you must configure `Class.BloomEffect` properties to exaggerate the lighting like a camera viewing a bright light. Similarly, to simulate more realistic colors at night, you must also adjust the effect's properties to desaturate the overall environment.

![The complete version of the sample volcanic eruption without bloom.](../../../assets/tutorials/creating-volcanoes/Without-Bloom.jpg)_Without bloom_

![The complete version of the sample volcanic eruption with bloom.](../../../assets/tutorials/creating-volcanoes/With-Bloom.jpg)_With bloom_

To recreate the global lighting in the sample [Volcano Island - Complete](https://www.roblox.com/games/17374256579/Volcano-Island-Complete) place file:

1. In the **Explorer** window, select the **Lighting** service, then in the **Properties** window,
  1. Set **Ambient** to `133, 152, 176` to set a light gray hue over the entire outdoor environment.
  2. Set **Brightness** to `2` to make the global light source slightly dimmer.
  3. Set **ColorShift_Top** to `207, 178, 72` to set a yellow hue to the light that reflects from surfaces facing the global light source.
  4. Set **LightingStyle** to **Realistic** to utilize Roblox's most advanced lighting technology.
  5. Set **ClockTime** to `4.3` to set the time of day about a quarter after 4am.
  6. Set **GeographicLatitude** to `199` to modify the position of the moon.
  7. Set **ExposureCompensation** to `-1` to expose the environment to half of the exposure from the moon.![A front view of the volcano with darkened outdoor lighting.](../../../assets/tutorials/creating-volcanoes/GL-1.jpg)
2. In the **Explorer** window, select **Bloom** child of the **Lighting** service, then in the **Properties** window,
  1. Set **Intensity** to `0.75` to slightly dim all colors within the environment.
  2. Set **Size** to `80` to create a wider bloom effect.
  3. Set **Threshold** to `0.85` to allow more colors in the environment to glow.![A front view of the volcano with darkened outdoor lighting and local lighting that glows orange.](../../../assets/tutorials/creating-volcanoes/GL-2.jpg)
3. In the **Explorer** window, insert a **ColorCorrection** object into the **Lighting** service, then in the **Properties** window,
  1. Set **Brightness** to `0.017` to slightly shift the color of your pixels.
  2. Set **Contrast** to `0.25` to make a sharper contrast between light and dark colors in the environment.
  3. Set **Saturation** to `-0.15` to desaturate colors in the environment.
  4. Set **TintColor** to `255, 214, 143` to tint pixels with a light yellow hue.![A front view of the volcano with pitch black outdoor lighting and local lighting that glows orange.](../../../assets/tutorials/creating-volcanoes/GL-3.jpg)
4. **OPTIONAL** Provide indirect light with clouds in the sky.
  1. In the **Explorer** window, insert a **Clouds** object into the **Terrain** service.
  2. Select the **Clouds** object, then in the **Properties** window,
    1. Set **Cover** to `1` to provide full cloud cover to the sky.
    2. Set **Density** to `0.08` to make the cloud cover less dense.
    3. Set **Color** to `136, 143, 152` to set a light gray hue to the cloud cover.![A front view of the volcano with pitch black outdoor lighting, gray clouds, and local lighting that glows orange.](../../../assets/tutorials/creating-volcanoes/GL-4.jpg)

## Configure volcano

Now that your local and global lighting configuration is complete, it's time to configure all of the VFX objects relating to the actual volcano and its surrounding terrain. As you follow these instructions that exactly recreate the final environment within the sample [Volcano Island](https://www.roblox.com/games/17374256579/Volcano-Island-Complete) `.rbxl` file, observe how each step works together to add character, movement, and illuminance to the environment.

### Surface ripples

**Surface ripples** are the small lava waves that flow across the surface of the caldera as a result of internal magma and pressurized gasses moving upward from beneath the earth's crust. This visual phenomenon conveys the real-world physical process of convection, or the movement within a fluid when hotter fluid rises to the surface, and it adds to the realism of your scene.

Surface ripples provide valuable insight for players into the state of the volcanic eruption. For example, if magma and gas are moving upward with enough force to disrupt the state of the lava on top of the caldera and cause it to churn, players can deduce that the volcano is actively erupting with boiling magma, so they should exercise caution around this gameplay area.

![A top-down view of the caldera without surface ripples.](../../../assets/tutorials/creating-volcanoes/Without-SurfaceRipples.jpg)_Without surface ripples_

_With surface ripples_

To demonstrate this process, the sample uses a `Class.ParticleEmitter` object slightly below the base of the caldera to emit flat, bright particles that slowly expand and contract on top of a dark backdrop. This allows the particles to emulate the behavior of lava smoothly and continuously churning in a way that's similar to the realistic way elements move in nature.

![The 2D texture that represents surface ripples that result from churning lava.](../../../assets/tutorials/creating-waterfalls/Foam-Texture.png)_Foam Ripples Texture = rbxassetid://16811365086_

To recreate the surface ripples on top of the caldera in the sample [Volcano Island - Complete](https://www.roblox.com/games/17374256579/Volcano-Island-Complete) place file:

1. In the **Explorer** window, create a **Folder** in the **Workspace** to contain all caldera objects, then rename the folder **Caldera**.
2. Create a backdrop to provide a high contrast background for the surface ripples.
  1. Insert a **block** part into the **Caldera** folder, then rename it **Backdrop**.
  2. Position and scale **Backdrop** to slightly beyond the full surface area of the caldera. The part appears as though it's glowing because of its close proximity to the caldera's local light source.![A top-down view of the caldera with a highlighted block part that's glowing yellow.](../../../assets/tutorials/creating-volcanoes/Ripples-2B.jpg)
3. Select **Backdrop**, the in the **Properties** window,
  1. Set **Color** to `0, 0, 0` to make the block black.
  2. Set **Material** to **Foil** to provide texture to the backdrop.![A top-down view of the caldera with a block part that's black with some rough texture.](../../../assets/tutorials/creating-volcanoes/Ripples-2C.jpg)
4. Create the ripple effect.
  1. Duplicate **Backdrop**, rename it **MagmaRipples**, then scale it slightly down to the surface area of the caldera.
  2. Select **MagmaRipples**, then in the **Properties** window, set **Transparency** to `1` to make the block invisible.
  3. Insert a **ParticleEmitter** into **MagmaRipples**, then rename the emitter **Ripples**.
  4. Select **Ripples**, then in the **Properties** window,
    1. Set **Texture** to `rbxassetid://16829556885` to render particles that look like foam ripples.
    2. Set **Orientation** to **VelocityPerpendicular** to emit particles perpendicular to the direction of their movement.
    3. Set **Color** to a color sequence in which particles are brown, become bright red, then turn maroon.
      1. Click the **Color** property, then click the **⋯** button. A color sequence pop-up displays.![A close up view of Studio's Properties window with the Color property's ellipsis button highlighted.](../../../assets/tutorials/creating-waterfalls/Cascades-1G1.png) Each triangle on the bottom axis of the color sequence is a **keypoint** that determines the color value of the property at that point of the particle's lifetime.
      1. Set the following time and value properties throughout the color sequence:
      - **Time** = `0`, **RGB Value** = `130, 53, 2`
      - **Time** = `0.5`, **RGB Value** = `224, 37, 0`
      - **Time** = `1`, **RGB Value** = `147, 5, 0`
    4. Set **Size** to a number sequence in which particles increase in size toward the middle of their lifetime before returning to their original size with a small window of variation.
      1. Click the **Size** property, then click the **⋯** button. A number sequence pop-up displays. By default, the graph is a straight line and the image remains the same size from left to right.![A close up view of the Size number sequence graph.](../../../assets/tutorials/creating-waterfalls/Cascades-1H1.png) Each square at the start and end of the number sequence is a **keypoint** that determines the size value of the property at that point of the texture from left to right.
      1. Set the following time and value properties throughout the number sequence:
      - **Time** = `0`, **Value** = `4.81`, **Envelope** = `0.438`
      - **Time** = `0.341`, **Value** = `8.75`, **Envelope** = `0.48`
      - **Time** = `0.497`, **Value** = `9.38`, **Envelope** = `0.5`
      - **Time** = `0.644`, **Value** = `8.75`, **Envelope** = `0.48`
      - **Time** = `1`, **Value** = `4.81`, **Envelope** = `0.438`
    5. Set **Transparency** to a number sequence in which particles start as transparent, become more opaque toward the middle of their lifetime, then become transparent again at the end of their lifetime.
      1. Click the **Transparency** property, then click the **⋯** button.
      2. Set the following time and value properties throughout the number sequence:
      - **Time** = `0`, **Value** = `1`, **Envelope** = `0`
      - **Time** = `0.3`, **Value** = `0.387`, **Envelope** = `0.0375`
      - **Time** = `0.5`, **Value** = `0.269`, **Envelope** = `0.0812`
      - **Time** = `0.7`, **Value** = `0.381`, **Envelope** = `0.05`
      - **Time** = `0`, **Value** = `1`, **Envelope** = `0`
    6. Set **ZOffset** to `-2` to offset the texture to be slightly away from the caldera.
    7. Set **Lifetime** to `5, 8` to randomly set each particle's lifetime between 5 and 8 seconds.
    8. Set **Rate** to `12` to emit 12 particles per second.
    9. Set **Rotation** to `-360, 360` to randomly orient each particle in a circle.
    10. Set **Speed** to `0.01` to emit each particle one tenth of a stud per second.
    11. Set **LightEmission** to `1` to significantly brighten the particles.
    12. Set **LightInfluence** to `0` to prevent the environmental light from affecting the color of the particles.
    13. Set **Brightness** to `15` to scale the light emitted from the emitter.

### Embers

**Embers** are the small, light pieces of molten rock that burst out of the caldera, rapidly expelling heat as they rise into the atmosphere. Similar to surface ripples, embers reveal that internal pressure below the earth's crust is pressing upwards, causing hot elements to break the lava's surface tension to release pressure.

The sample emulates this process by using a `Class.ParticleEmitter` object to emit particles with motion blur that's baked into the texture. As the particles rise and reach the end of their lifetime, the emitter squashes the particles into a 1:1 ratio to reform the particles into circles. This technique allows the particles to seem as though they are rapidly moving as they exit the caldera, then slow down as they dissipate into the sky.

![The 2D texture that represents embers bursting from the caldera.](../../../assets/tutorials/creating-volcanoes/Embers-Texture.jpg)_Embers Texture = rbxassetid://17581858560_

In addition, as particles rise, they change their color, opacity, and size to reflect their changing temperature. For example, they begin their lifetime as large, brown particles, but quickly transform into small orange, then maroon particles. This strategy also has the benefit of subtly reflecting the lighting throughout the canyon, increasing a player's immersion within the environment.

To recreate the glowing embers from the surface of the caldera in the sample [Volcano Island - Complete](https://www.roblox.com/games/17374256579/Volcano-Island-Complete) place file:

1. Insert a **cylinder** part into the **Caldera** folder, then rename it **GlowingEmbers**.
2. Position **GlowingEmbers** so that it is on top of the surface ripples, then scale it until it fills the interior of the caldera. The part appears as though it's glowing because of its close proximity to the caldera's local light source.![A close front view of the caldera with a cylinder part that's glowing yellow.](../../../assets/tutorials/creating-volcanoes/Embers-2.jpg)
3. Select **GlowingEmbers**, then in the **Properties** window, set **Transparency** to `1` to make the cylinder invisible.
4. Insert a **ParticleEmitter** into **GlowingEmbers**, then rename the emitter **Embers**.
5. Select **Embers**, then in the **Properties** window,
  1. Set **Texture** to `rbxassetid://17581858560` to render particles that look like an elongated oval horizontally and vertically.
  2. Set **Orientation** to **VelocityParallel** to emit particles parallel to their direction of movement.
  3. Set **Color** to a color sequence in which particles are brown, become orange, then turn maroon.
  - **Time** = `0`, **RGB Value** = `130, 53, 2`
  - **Time** = `0.5`, **RGB Value** = `224, 82, 0`
  - **Time** = `1`, **RGB Value** = `147, 5, 0`
  1. Set **Size** to a number sequence in which particles slowly decrease in size across their lifetime.
  - **Time** = `0`, **Value** = `0.313`, **Envelope** = `0.1`
  - **Time** = `1`, **Value** = `0`, **Envelope** = `0`
  1. Set **Squash** to a number sequence in which particles slightly elongate about midway through their lifetime.
  - **Time** = `0`, **Value** = `-3`, **Envelope** = `0`
  - **Time** = `0.323`, **Value** = `-0.188`, **Envelope** = `0`
  - **Time** = `1`, **Value** = `-0.5`, **Envelope** = `0`
  1. Set **Transparency** to a number sequence in which particles randomly change their opacity to simulate embers glowing as they rise. The actual values are not important, just that they change a lot during the course of their lifetimes.
  1. Set **ZOffset** to `1` to offset the texture to be slightly away from the caldera.
  2. Set **Lifetime** to `1, 5` to randomly set each particle's lifetime between 1 and 5 seconds.
  3. Set **Speed** to `5, 8` to randomly emit each particle between 5 and 8 studs per second.
  4. Set **SpreadAngle** to `180, 180` to emit particles in an angle along the X and Z axis.
  5. Set **Acceleration** to `0, 10, 0` to simulate upward force and pull particles to the sky.
  6. Set **Drag** to `0.8` to have particles lose their speed with exponential decay.
  7. Set **LightEmission** to `1` to significantly brighten the particles.
  8. Set **LightInfluence** to `0` to prevent the environmental light from affecting the color of the particles.
  9. Set **Brightness** to `20` to scale the light emitted from the emitter.

### Lava splashes

**Lava splashes** are bursts of thin molten rock that erupt upward from the volcano as a result of internal magma and pressurized gasses applying enough force to break the surface tension of the lava on top of the caldera. This core component of a volcano is one of the most common signs in determining that a volcano is no longer dormant and is actively erupting.

The sample represents this process with two `Class.ParticleEmitter` objects that utilize [flipbooks](/docs/en-us/effects/particle-emitters.md#flipbooks) to animate each particle's texture over their lifetime. The first particle emitter emits particles that look like dense, high-viscosity splashes that are heavy and thick, causing them to rise and fall slowly back down into the volcano. Conversely, the second particle emitter emits particles that look like webby, low-viscosity splashes that are light and thin, causing them to rise and fall quickly.

![The 2D texture that represents a dense splash texture.](../../../assets/tutorials/creating-volcanoes/DenseSplash-Texture.jpg)_Dense Splash Texture = rbxassetid:/17363669906_

![The 2D texture that represents a webby splash texture.](../../../assets/tutorials/creating-volcanoes/WebbySplash-Texture.jpg)_Webby Splash Texture = rbxassetid://17363668312_

Each particle emitter animates their texture over 64 frames to emulate smooth, lifelike physical behavior. While you could use only one particle emitter, the repetition of the animation would become apparent and break the immersion for your players because they would see the exact same animation every time. However, when two particles animate flipbooks with slightly different custom properties, it is much more difficult to spot the repetition.

The sample also provides a `Class.ParticleEmitter` object that emits particles that look like aerated splashes to represent even lighter webby splashes. This technique fills the space with dynamic movement and further hides the repetition of the flipbook animations. As an extra bonus, if your game also includes the waterfall from [Creating Waterfalls](/docs/en-us/tutorials/use-case-tutorials/vfx/create-waterfalls.md), you're able to reuse the same texture twice for different gameplay areas, saving you memory and improving performance on low-end devices.

![The 2D texture that represents aerated splashes.](../../../assets/tutorials/creating-waterfalls/Splashes-Droplets.png)_Webby Texture = rbxassetid://17082061238_

To recreate the splashing lava from the surface of the caldera in the sample [Volcano Island - Complete](https://www.roblox.com/games/17374256579/Volcano-Island-Complete) place file:

1. Insert a **cylinder** part into the **Caldera** folder, then rename it **SplashingLava**.
2. Position **SplashingLava**. so that it is on top of the surface ripples, then scale it until it covers the middle of the caldera where you want the lava to splash. The part appears as though it's glowing because of its close proximity to the caldera's local light source.![A close front view of the caldera with a cylinder part that's glowing yellow.](../../../assets/tutorials/creating-volcanoes/Splashes-2.jpg)
3. Select **SplashingLava**, then in the **Properties** window, set **Transparency** to `1` to make the cylinder invisible.
4. Insert a **ParticleEmitter** into **SplashingLava**, then rename the emitter **WebbySplashes**.
5. Select **WebbySplashes**, then in the **Properties** window,
  1. Set **Texture** to **rbxassetid://17363668312** to render particles that look like webby splashes.
  2. Set **Orientation** to **FacingCameraWorldUp** to emit particles facing the camera, but rotating only on the vertical upward world Y axis.
  3. Set **Color** to `255, 152, 79` to tint the particles to a light orange hue.
  4. Set **Size** to a number sequence in which particles increase in size across their lifetime with a window of variation.
  - **Time** = `0`, **Value** = `4.31`, **Envelope** = `0.762`
  - **Time** = `1`, **Value** = `6.2`, **Envelope** = `0.875`
  1. Set **Squash** to a number sequence in which particles slightly elongate throughout their lifetime with a window of variation.
  - **Time** = `0`, **Value** = `-0.075`, **Envelope** = `0.263`
  - **Time** = `1`, **Value** = `-0.413`, **Envelope** = `0.412`
  1. Set **ZOffset** to `1` to offset the texture to be slightly away from the caldera.
  2. Set **Lifetime** to `1.5, 2` to randomly set each particle's lifetime between 1.5 and 2 seconds.
  3. Set **Rate** to `0.37` to emit a particle about every 3 seconds.
  4. Set **RotSpeed** to `-20, 20` to randomly emit each particle between -20 and 20 degrees per second.
  5. Set **Speed** to `2` to emit each particle 2 studs per second.
  6. Set **SpreadAngle** to `5, 5` to emit particles in a small angle along the X and Z axis.
  7. Set **FlipbookLayout** to **Grid8x8** to animate the texture over a 64-frame duration.
  8. Set **FlipbookMode** to **Oneshot** to ensure the animation only plays once during its lifetime.
  9. Set **Drag** to `0.5` to have particles lose their speed with exponential decay.
  10. Set **LightEmission** to `0.1` to slightly brighten the particles.
  11. Set **LightInfluence** to `0.25` to significantly reduce how much the environmental light affects the color of particles.
6. Duplicate **DenseSplashes**, then in the **Properties** window, modify the following properties to provide variation to the additional lava splashes.
  1. Set **Name** to **DenseSplashes**.
  2. Set **Texture** to **rbxassetid://17363669906** to render particles that look like dense splashes.
  3. Set **Size** to a number sequence in which particles increase in size across their lifetime with a window of variation.
  - **Time** = `0`, **Value** = `5.75`, **Envelope** = `0.762`
  - **Time** = `1`, **Value** = `7.37`, **Envelope** = `0.875`
  1. Set **Squash** to a number sequence in which particles slightly elongate throughout their lifetime with a window of variation.
  - **Time** = `0`, **Value** = `0`, **Envelope** = `0.225`
  - **Time** = `1`, **Value** = `-0.262`, **Envelope** = `0.15`
  1. Set **Rate** to `0.289` to emit a particle nearly every fourth of a second.
7. Fill the caldera with additional splashes.
  1. Insert a **ParticleEmitter** into **SplashingLava**, then rename the emitter **SplashFill**.
  2. Select **SplashFill**, then in the **Properties** window,
    1. Set **Texture** to **rbxassetid://17082061238** to render particles that look like lighter webby splashes
    2. Set **Orientation** to **FacingCameraWorldUp** to emit particles facing the camera, but rotating only on the vertical upward world Y axis.
    3. Set **Color** to `255, 152, 33` to tint the particles to an orange hue.
    4. Set **Size** to a number sequence in which particles increase in size across their lifetime with a window of variation.
    - **Time** = `0`, **Value** = `1.25`, **Envelope** = `0.388`
    - **Time** = `1`, **Value** = `6.38`, **Envelope** = `0.563`
    1. Set **Transparency** to a number sequence in which particles start as transparent, become opaque, then become transparent again toward the end of their lifetime.
    - **Time** = `0`, **Value** = `1`, **Envelope** = `0`
    - **Time** = `0.19`, **Value** = `0`, **Envelope** = `0`
    - **Time** = `0.795`, **Value** = `0`, **Envelope** = `0`
    - **Time** = `1`, **Value** = `1`, **Envelope** = `0`
    1. Set **ZOffset** to `1` to offset the texture to be slightly away from the caldera.
    2. Set **Lifetime** to `1.5` to set each particle's lifetime to 1.5 seconds.
    3. Set **Rate** to `8` to emit a particle every 8 seconds.
    4. Set **Rotation** to `0, 360` to randomly orient each particle in a half circle.
    5. Set **RotSpeed** to `-50, 50` to randomly emit each particle between -50 and 50 degrees per second.
    6. Set **Speed** to `12, 20` to randomly emit each particle between 12 and 20 studs per second.
    7. Set **SpreadAngle** to `45, 45` to emit particles in an angle along the X and Z axis.
    8. Set **Acceleration** to `0, -25, 0` to simulate gravity and pull particles back down.
    9. Set **Drag** to `1` to have particles lose their speed with exponential decay.
    10. Set **LightEmission** to `1` to significantly brighten the particles.
    11. Set **LightInfluence** to `0` to prevent the environmental light from affecting the color of the particles.
    12. Set **Brightness** to `8` to scale the light emitted from the emitter.

> **Warning:** Features with custom textures such as flipbooks cost memory to render. If you use many flipbooks with other features that use high memory, then clients automatically deactivate flipbooks when they are low on memory, which is likely for older mobile phones. To reduce the memory usage of flipbooks, use fewer unique animated particle effects or choose a texture of smaller resolution.
### Lava flow

A **lava flow** is a mass of lava that erupts and oozes away from the caldera and across the earth's surface during a volcanic eruption. As the lava cools due to its exposure to air, it solidifies and transforms into solid rock, creating new land mass.

To simulate this process, the sample layers multiple `Class.Beam` objects on top of each other with seamless textures and property configurations that emulate the behavioral characteristics of lava cooling as it travels further away from the caldera:

- The **bottom layer** renders a flat color that transforms from a warm to a cool color to communicate that the lava is beginning to drop in temperature, such as bright red to a dark maroon.
- The **middle layer** renders a black texture that looks like dark crust with holes that reveal the glowing lava underneath.
- The **top layer** renders the same texture as the middle layer at a slower rate, flipped attachments, and opposite property configurations. This ensures that the textures never have the opportunity to fully line up with each other while rendering in the same direction, which would allow players to easily detect the unrealistic texture repetition.

_Bottom layer_

_Middle Layer_

_Top Layer_

Layering three `Class.Beam` objects creates an illusion of parallax to make the lava seem like it has a sense of depth and volume where the lava is flowing at different rates, even though they are only three 2D images. This lets players know that there is a sense of turbulence within the canyon, both on and below the lava's surface.

![The 2D texture that represents the crust on top of the flowing lava.](../../../assets/tutorials/creating-volcanoes/Crust-Texture.jpg)_Crust Texture = rbxassetid://17023930265_

To recreate the flowing magma from the caldera in the sample [Volcano Island - Complete](https://www.roblox.com/games/17374256579/Volcano-Island-Complete) place file:

1. In the **Explorer** window, create a **Folder** in the **Workspace** to contain all flowing magma objects, then rename the folder **FlowingMagma**.
2. Insert a **block** part into the **FlowingMagma** folder, then rename it **MagmaRiverBeam**.
3. Move **MagmaRiverBeam** to slightly under the edge of the caldera.![An angled top down view of the volcano with a block part highlighted.](../../../assets/tutorials/creating-volcanoes/LavaFlow-3.jpg)
4. Configure attachments for all flowing magma beams from the caldera to use to render their textures.
  1. Insert an attachment into **MagmaRiverBeam**, then rotate the attachment until the yellow visual aid points toward the caldera.
  2. Insert another attachment into **MagmaRiverBeam**, position it toward the fork in the crevice, then rotate the attachment until the yellow visual aid points down into the ground.![An angled top down view of the volcano with two attachment visual aids highlighted.](../../../assets/tutorials/creating-volcanoes/LavaFlow-4.jpg)
5. Insert a **Beam** into **MagmaRiverBeam**, then rename it **Magma**.
6. Assign the part's attachments to **Magma**.
  1. In the **Explorer** window, select **Magma**.
  2. In the **Properties** window,
    1. Set **Attachment0** to the attachment at the edge of the caldera.
    2. Set **Attachment1** to the attachment at the fork in the crevice. The beam renders its default texture between the two attachments.![An angled top down view of the volcano with two block parts rendering the default beam texture between the attachments.](../../../assets/tutorials/creating-volcanoes/LavaFlow-6.jpg)
7. Customize the beam's visual appearance so it looks like flowing magma.
  1. In the **Explorer** window, verify **Magma** is still selected.
  2. In the **Properties** window,
    1. Set **Width0** to `50` to widen the texture from the axis that it starts to render.
    2. Set **Width1** to `50` to widen the texture as it meets the fork in the crevice.
    3. Set **CurveSize0** to `-50` to curve the texture away from the crevice's floor.
    4. Set **CurveSize1** to `5` to curve the texture into the fork in the crevice.
    5. Set **Color** to a color sequence that starts bright red and becomes dark red over the beam's lifetime to simulate the magma cooling.
    - **Time** = `0`, **RGB Value** = `255, 51, 0`
    - **Time** = `0.5`, **RGB Value** = `211, 39, 0`
    - **Time** = `1`, **RGB Value** = `118, 24, 0`
    1. Set **Transparency** to a number sequence that allows the magma to be more vibrant between the attachment points.
    - **Time** = `0`, **Value** = `1`
    - **Time** = `0.0916`, **Value** = `0`
    - **Time** = `0.867`, **Value** = `0`
    - **Time** = `0.941`, **Value** = `0.725`
    - **Time** = `1`, **Value** = `1`
    1. Set **LightEmission** to `1` to significantly brighten the beam.
    2. Set **LightInfluence** to `0` to prevent the environmental light from affecting the color of the beam.
    3. Set **Brightness** to `8` to scale the light emitted from the beam.
8. Insert another **Beam** into **MagmaRiverBeam**, rename it **Crust1**, then attach the part's attachments to **Crust1** using the same process in step 6.
9. Customize the beam's visual appearance so it looks like crust on top of the magma.
  1. In the **Explorer** window, verify **Crust1** is still selected.
  2. In the **Properties** window,
    1. Set **Texture** to **rbxassetid://17023930265** to render a new texture that looks like flowing crust.
    2. Set **Width0** to `35` to widen the texture from the axis that it starts to render.
    3. Set **Width1** to `25` to widen the texture as it meets the fork in the crevice.
    4. Set **TextureSpeed** to `0.01` to significantly slow down the flow of the texture.
    5. Set **TextureLength** to `3` to slightly stretch the texture's length.
    6. Set **CurveSize0** to `-50` to curve the texture away from the crevice's floor.
    7. Set **CurveSize1** to `5` to curve the texture into the fork in the crevice.
    8. Set Color to `83, 83, 83` to tint the beam gray.
    9. Set **Transparency** to a number sequence that allows the crust to be more vibrant between the attachment points.
    - **Time** = `0`, **Value** = `1`
    - **Time** = `0.22`, **Value** = `0`
    - **Time** = `0.85`, **Value** = `0`
    - **Time** = `1`, **Value** = `1`
    1. Set **ZOffset** to `1` to offset the texture to be slightly away from the caldera.
10. Duplicate **Crust1**, rename it **Crust2**, then in the **Properties** window,
  1. Set **Attachment0** to the attachment at the fork in the crevice.
  2. Set **Attachment1** to the attachment at the edge of the caldera.
  3. Set **Width0** to `25` to widen the texture from the axis that it starts to render.
  4. Set **Width1** to `35` to widen the texture as it meets the fork in the crevice.
  5. Set **TextureSpeed** to `-0.008` to significantly slow down the flow of the texture.
  6. Set **TextureLength** to `2` to slightly unstretch the texture's length.
  7. Set **CurveSize0** to `-5` to curve the texture away from the crevice's floor.
  8. Set **CurveSize1** to `50` to curve the texture into the fork in the crevice.
  9. Set **ZOffset** to `2` to offset the texture from the other crust.
11. **OPTIONAL** Using this same process, create more beams around the fork in the crevice to offshoot the magma. Be sure to adjust the properties to slow the textures and simulate magma that's darker in color as it cools in temperature.

### Smoke plume

A **smoke plume** from the caldera emits warm pressurized gas, steam, and volcanic ash into the atmosphere. This mixture of volcanic emission can be seen for miles in the real world, so volcano designs often incorporate large smoke plumes to be a significant point of interest in the 3D space.

Rather than emitting thick, pyroclastic smoke that one would see immediately following an explosive eruption, the sample uses a `Class.ParticleEmitter` object to emit particles that look like thin smoke vapors that change color as they rise upwards. This technique accomplishes two goals:

- It breaks up the silhouette of the background crater, creating more visual interest around the volcanic eruption.
- It allows the smoke to look like it accepts light from the environment while still emitting a dark presence as though the smoke is burning impurities into the air before turning gray like the night sky.

![The 2D texture that represents the smoke rising out of the caldera.](../../../assets/tutorials/creating-waterfalls/Mist-Texture.png)_Smoke Texture = rbxassetid://16830667309_

To recreate the smoke plume from the caldera in the sample [Volcano Island - Complete](https://www.roblox.com/games/17374256579/Volcano-Island-Complete) place file:

1. Insert a **block** part into the **Caldera** folder, then rename it **SmokePlume**.
2. Position **SmokePlume** underneath the caldera, then scale it to roughly the size of the caldera's surface area.![An angled side view of the volcano with a block part highlighted underneath the caldera.](../../../assets/tutorials/creating-volcanoes/Plume-2.jpg)
3. Insert a **ParticleEmitter** into **SmokePlume**, then rename the emitter **Smoke**.
4. Select **Smoke**, then in the **Properties** window,
  1. Set **Texture** to **rbxassetid://16830673704** to render particles that look like thick smoke.
  2. Set **Color** to a color sequence in which particles simulate lighting in the environment from the caldera to the sky by starting black, becoming a light peach, then gray.
  - **Time** = `0`, **RGB Value** = `0, 0, 0`
  - **Time** = `0.374`, **RGB Value** = `195, 104, 76`
  - **Time** = `0.469`, **RGB Value** = `225, 121, 86`
  - **Time** = `0.709`, **RGB Value** = `111, 111, 111`
  - **Time** = `1`, **RGB Value** = `113, 113, 113`
  1. Set **Transparency** to a number sequence in which particles start as transparent, become fully opaque early into their lifetime, then become transparent again near the end of their lifetime.
  - **Time** = `0`, **Value** = `1`
  - **Time** = `0.0622`, **Value** = `0`
  - **Time** = `0.845`, **Value** = `0`
  - **Time** = `0`, **Value** = `1`
  1. Set **ZOffset** to `-10` to offset the texture to be closer to the top of the caldera.
  2. Set **Lifetime** to `50, 60` to randomly set each particle's lifetime between 50 and 60 seconds.
  3. Set **Rate** to `0.3` to emit a particle about every 3 seconds.
  4. Set **Rotation** to `-360, 360` to randomly orient each particle in a circle.
  5. Set **RotSpeed** to `-5, 5` to randomly emit each particle between -5 and 5 degrees per second.
  6. Set **SpreadAngle** to `5, 5` to emit particles in a small angle along the X and Z axis.
  7. Set **Acceleration** to `0, 7, 0` to simulate upward force and pull particles to the sky.
  8. Set **Drag** to `1` to have particles lose their speed with exponential decay.
  9. Enable **WindAffectsDrag** to have the wind in the environment push the smoke around.
  10. Set **LightEmission** to `0.1` to slightly brighten the particles.
  11. Set **LightInfluence** to `0.06` to significantly reduce how much the environmental light affects the color of particles.
5. In the **Command Bar**, input the following string to increase each particle's size from 40 to 100 studs across their lifetime with a small window of variation:```lua
workspace.Caldera.SmokePlume.Smoke.Size = NumberSequence.new{NumberSequenceKeypoint.new(0,40,5), NumberSequenceKeypoint.new(1,100,15)}
```
