---
title: "Custom particle effects"
url: /docs/en-us/tutorials/use-case-tutorials/vfx/custom-particle-effects
last_updated: 2026-10-30T19:56:01Z
description: "The process for creating a multicolor plume of smoke from an active volcano."
---

# Custom particle effects

Time to look at a more complex example of particle effects. You'll make a multicolored plume of smoke pouring out of an active volcano.

## Starter project

First up, you'll need something like a volcano you can use for the effect. The [Treasure Island example world](https://www.roblox.com/games/6307505882/Treasure-Island) pictured in this tutorial includes a volcano.

![Edit in Studio option from the game's main page](../../../assets/tutorials/custom-particle-effects/Treasure-Island-Edit-Place.png)

A volcano with an orange neon part will be used to emit particles. This part is called **CenterLava** and is parented to the workspace.

1. Locate and select the **CenterLava** part in the workspace.
2. Insert a **ParticleEmitter** onto the part.

## Particle texture

A `Class.ParticleEmitter` has a property called **Texture** that determines the image that will be repeated in the effect. If you want to use your own image, you'll need to upload it to Roblox and get the **Asset ID** to paste into that property. See [Textures and Decals](/docs/en-us/parts/textures-decals.md) for more details.

> **Info:** If you want to make your own texture using image editing software, consider these best practices: - Make your image **grayscale**. This allows you complete control over the final color of the particle with the Color property. - Ensure the **background** is **transparent**. - **Blur** the **edges** of your image to get a more polished, continuous effect.

For a smoke effect, a circle with faded edges works well. A pre-made example of this is provided below. Change the emitter's **Texture** property to `rbxassetid://3845808160`.

## Fading effect

Despite the change of texture, the volcano effect still doesn't look much like smoke. It would look better if the particles faded out over time in the same way that smoke dissipates in the air.

Some emitter properties can be set up to change over time with a **sequence**. Start with **Transparency** which can be used to create a fading effect.

1. Open the sequence window for the emitter's **Transparency** by clicking the three dots next to the property. The sequence window is a graph, with the **time** on the X-axis and the **property value** on the Y-axis. By default, the transparency value is a flat line, with starting and ending **keypoints** at 0, meaning the particles will be opaque for their entire lifetime.
2. Drag the keypoint at the end of the sequence to the top of the graph to create a smooth fade from 0 to 1. Your particles should now slowly fade away as they rise from the volcano.

## Growing smoke

To really look like smoke, the particles should be large enough to overlap with each other and should spread as they rise from the source.

This can be achieved by applying a sequence to the **Size** property. By making the size start at **3** and increase to **10**, the particles will look much more like a cloud of smoke.

1. Open the sequence window for the emitter's **Size** property.
2. Drag the starting keypoint to approximately **3**.
3. Drag the ending keypoint to approximately **10**.

## Color sequences

Sequences aren't just for linear property values - you can even use them to change the color of particles over time.

The window for **color sequences** is slightly different: it shows the color as it changes across the particle's lifetime. By default, the sequence is all white.

If you start your sequence at orange to reflect the lava, then move to darker grey, and then finish at white, you can get a really immersive effect for your smoke.

1. Open the sequence window for the emitter's **Color** property.
2. Click the small square next to **Color** to open a color picker for the keypoint at the start of the sequence. Set the color to **orange**.
3. Click in the middle of the region to create a new keypoint. Set the color at this keypoint to **dark grey**.
4. Set the color at the end of the sequence to **white.**

## Acceleration

For a final touch, you can make the smoke drift away from the volcano as if the wind were blowing it away.

The **Acceleration** property determines how the speed of particles changes over time, measured on the **X**, **Y**, and **Z** axes. Set the **Acceleration** property of the emitter to **2, 2, 0** to achieve a drifting effect.

> **Info:****Acceleration** is the force applied to particles **after** they have been emitted, while **Speed** is the **initial** emission speed.
>
> Understanding how these properties can work together is the key to achieving many effects — for instance, you could simulate water drops falling from a surface to the ground by setting **Speed** to **0** and **Y** acceleration to a negative value.
## Thicker smoke

If the acceleration change has spread the smoke particles out too much, you can increase the **Rate** property to thicken it back up again. A rate of **40** works nicely here. Set the emitter's **Rate** property to **40.**

Your volcano smoke is now complete! With just a few simple changes, your emitter is producing a realistic, immersive smoke effect.

For a complete list of emitter properties you can use to tweak your effects, see the `Class.ParticleEmitter` API page. If you're working with the example world, look for other spots that could benefit from particle effects.
