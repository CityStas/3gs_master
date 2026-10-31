---
title: "Basic particle effects"
url: /docs/en-us/tutorials/use-case-tutorials/vfx/basic-particle-effects
last_updated: 2026-10-30T19:56:01Z
description: "The process of creating particles to elevate the visual effects in your game."
---

# Basic particle effects

**Particles** are used to create a wide range of effects in games, from smoke and fire to splashing water. They can help bring your game to life and can provide valuable visual feedback for your players.

In this tutorial, you will use a `Class.ParticleEmitter` object to create a sparkling effect around a part.

## Particle emitters

The `Class.ParticleEmitter` is a special type of object that will **emit** particles from its position when parented to a part or `Class.Attachment`.

The particles themselves are **2D images** that always face the camera. Particles move or change color according to the emitter's properties. By changing just a few of these, you can make an incredible array of different effects.

The example provided below is a model of a gold nugget. A simple particle effect will be used to make it sparkle.

1. Create a `Class.MeshPart` in the `Class.Workspace` and name it **GoldNugget**.
2. Set the **MeshId** property to `rbxassetid://2903918852`.
3. Set the **Material** property to **Neon** and the **Color** property to `255, 180, 0`.![Color, Material and MeshID properties](../../../assets/tutorials/basic-particle-effects/meshProperties.jpg)
4. Insert a `Class.ParticleEmitter` object into the part.![GoldNugget and ParticleEmitter in the Explorer](../../../assets/tutorials/basic-particle-effects/explorerMeshPart.jpg) Once you add the emitter, white stars will immediately start emitting from the part. The star is the default particle image.![Default particles emitting from the GoldNugget part](../../../assets/tutorials/basic-particle-effects/defaultParticles.jpg)

> **Info:** The pre-made `Class.Fire` and `Class.Smoke` objects can be a convenient way to save time on creating effects, but they are far less customizable than ParticleEmitters.
## Particle emission

Particles are generated randomly throughout the entire volume of a part. They emerge from one **face** of the part according to the **EmissionDirection** property. It defaults to **Top**, meaning the top surface of a part. If you rotate the part, the direction the particles are emitted from will change accordingly.

If you resize the part to be bigger, the particles will be emitted over a wider area.

## Particle properties

### Color

The first thing to change is the emitter color — **gold** would be a much more appropriate color for a sparkle effect.

Change the **Color** property to **255, 200, 50**.

### Lifetime

By default, the particles last for 5 to 10 seconds, which is too long for sparkles. You can change this using the **Lifetime** property.

Lifetime can have either a single value or a **Min** and a **Max** value, with particles lasting for a random amount of time in seconds between the two values.

Change the **Lifetime** property of the emitter to **0.5, 1** to shorten the duration of the particles.

### Rate

The **Rate** property specifies how many particles are emitted per second. The default value is 20 which is fairly high for a sparkle effect. Change the **Rate** property of the emitter to **7**.

### Speed

The **Speed** property determines how fast a particle will travel in studs per second. It can be either a single value or a range of values.

A sparkle effect should be nice and slow — a range of 2 to 3 seconds works nicely. Change the **Speed** property to **2, 3**.

![Particle Speed property](../../../assets/tutorials/basic-particle-effects/particleSpeed.jpg) ### SpreadAngle

The particles are currently emitting straight up from the part. To get an even spread of particles in all directions, change the **SpreadAngle** property.

SpreadAngle has an **X** and a **Y** value which determine the range of angles that a particle can be emitted. This is calculated from both sides around the axes. A value of **180, 0** would emit particles in a flat circle across the X-axis; a value of **180, 180** would emit particles in every direction around the part. Change the **SpreadAngle** property of the emitter to **180, 180**.

### Additional properties

To further improve the sparkle effect, try the following property values.

| Property | Value |
| --- | --- |
| Size | 0.3 |
| LightEmission | 1 |
| Transparency | 0.5 |
| Drag | 1.5 |

With that, your sparkling part is complete. You can try complementing the sparkling effect with a gentle glow by adding a `Class.PointLight` to the part, as shown at the start of the course — check out the [Lighting with Props](/docs/en-us/tutorials/use-case-tutorials/lighting/light-with-props.md) course to learn more about light objects.
