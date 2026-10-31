---
title: "Use particles for actions"
url: /docs/en-us/education/build-it-play-it-mansion-of-wonder/using-particles-for-actions
last_updated: 2026-10-30T19:55:42Z
description: "Learn how to use particle effects to give players feedback to their actions, and learn several techniques to further customize your particles in Roblox Studio. Part of the Build It Play It Mansion of Wonder series."
---

# Use particles for actions

With arrows finished, first-time players can follow the path to their goal, making their initial introduction clearer and less likely that they get lost and quit. To further enhance the user experience, let players know they've successfully completed their task with an appealing particle effect.

In the example below, a celebratory burst of ticket-shaped particles emits whenever players interact with the booths.

> **Info:** Giving **multiple forms** of feedback is also another way of improving a player's user experience. A player with the sound down or one who is hearing impaired may rely more on visual cues. Other players may be low vision and paying more attention to sound.
## Create particles

When creating a particle, it needs to be inserted into a part or attachment. In this example, you'll place particles in the TestPlayer object used earlier.

1. In **TestPlayer**, create a **ParticleEmitter** named **Burst**. Default particles will start emitting from the TestPlayer object. You'll customize the emitter to create a burst effect. An example is shown below.
  > **Warning:** Particles must be named exactly since a script will be looking for the name later.
2. With **Burst** selected, go to the **Properties** window and find the **Texture** property. Copy and paste one of the texture IDs supplied below, or use your own, into the texture field and press `Enter`._6772766862__6772766551__5857851618__6803084085__6772783963__6703369286__6749057157__6772766413_ If using the ticket texture, it will look like below.
  > **Info:** Custom textures can be any image that you have. Learn to upload them in the [Asset Manager](/docs/en-us/projects/assets/manager.md) article.
3. In the **Explorer** window, select **TestPlayer**, then in the **Properties** window, find and change the **Color** and **Size** properties to something appropriate for your game. For example, the following image includes particles with the following settings:
  - **Color** = `255, 178, 44`
  - **Size** = `0.6`

## Create a burst effect

Different properties can be changed so that the particles look more like a quick burst rather than a gentle stream. After designing the particle, you'll disable the emitter so that it only plays when activated by a script.

## Make particles spread

The ParticleEmitter sends out particles along two planes controlled by the property, **SpreadAngle**.

1. To make the particles fly out in all directions like the example, set the **SpreadAngle X** and **Y** to **360**.

## Different burst properties

After adding the recommended values under the video, the particles will look like they are quickly bursting from the player like a firework.

1. To get a burst motion, set the following properties to these values to make the particles explode and then quickly fade out. | Property | Value | Rationale |
| --- | --- | --- | | **LightEmission** | 0.4 | Adds a faint glow. Note the maximum is 1. | | **Drag** | 8 | More drag causes the particles to quickly lose speed. | | **Lifetime** | 0.6, 1 | Makes particles exist for between .6 and 1 seconds. | | **Rate** | 50 | How many particles are emitted per second. | | **Speed** | 40 | How fast the particles are going when first emitted. |
  > **Info:** Try adding some randomized numbers to make particles feel less repetitive. Some properties, such as **Lifetime** and **Rotation** add randomization by allowing for a minimum and a maximum value.
2. Lastly, the particle should only play when the script (which you'll see in the next lesson) tells it to. Find the **Enabled** property and toggle it **off**.
  > **Info:** This page only covered a few properties. For more, see the [Particle Emitters](/docs/en-us/effects/particle-emitters.md) reference article.
