---
title: "Particle emitters"
url: /docs/en-us/effects/particle-emitters
last_updated: 2026-10-30T19:55:43Z
description: "Particle emitters emit 2D images to simulate special effects like fire, smoke, and sparks."
---

# Particle emitters

A `Class.ParticleEmitter` is an object that emits customizable 2D images (particles) into the world, useful for simulating special effects like fire, smoke, and sparks.

## Create particle emitters

You can parent a `Class.ParticleEmitter` to an `Class.Attachment` or an object of the `Class.BasePart` class. When parented to a `Class.BasePart`, particles spawn randomly within the part's bounding box or [shape](#shape); when parented to an `Class.Attachment`, particles spawn from the attachment's position.

Additionally, the `Class.ParticleEmitter.EmissionDirection|EmissionDirection` property determines the face (`Enum.NormalId`) of emission when the emitter is parented to a `Class.BasePart`. When you change this property, you consequently change the particle emission direction as well.

> **Info:** When you rotate an emitter's parent `Class.BasePart`, the orientation of its face also changes, altering the direction of particle emission. Alternatively, if you add an emitter to an `Class.Attachment`, you can rotate the attachment itself instead of using `Class.ParticleEmitter.EmissionDirection|EmissionDirection`.

To create a particle emitter on a part or attachment:

1. In the **Explorer** window, hover over the part or attachment and click the ⊕ button. A contextual menu displays.
2. From the menu, insert a **ParticleEmitter**. The particle emitter immediately emits particles within the part's area or from the attachment's position.![ParticleEmitter object as child of MeshPart in Explorer hierarchy](../assets/studio/explorer/MeshPart-ParticleEmitter.png)

## Customize particles

By experimenting with the following properties, you can customize a particle's visual appearance to make unique gameplay elements like bursting volcanos, magical dust, and dust motes.

> **Info:** The visual quality of your particles can change depending on the graphic settings on the player's device. To review your particles across quality levels, it's recommended to open [Studio Settings](/docs/en-us/studio/setup.md#customization), search for **Editor Quality Level**, and set it to the both the lowest and highest level after you finish customizing your particles.
### Texture

The `Class.ParticleEmitter.Texture|Texture` property renders the image that each particle displays. By default, particle emitters have particles with a white sparkle texture, but you can change it to any texture to achieve interesting effects.

_Three similar particle emitters with different `Class.ParticleEmitter.Texture|Texture` assets_

If you're creating an image to use as a particle texture, it's best to use `.png` format with a transparent background. If your texture is grayscale with no alpha channel, try setting the particle emitter's `Class.ParticleEmitter.LightEmission|LightEmission` property to **1** to hide the darker regions.

> **Info:** For steps on how to import an image for use as a particle texture, see [here](/docs/en-us/projects/assets/manager.md#asset-import).

To insert an image into a particle emitter:

1. From Studio's **Window** menu or **Home** tab toolbar, open the [Toolbox](/docs/en-us/projects/assets/toolbox.md).
2. If you want to insert an image that you have previously imported, click the **Inventory** tab. If you want to insert an image from another creator, click the **Creator Store** tab.![Inventory tab indicated in Studio's Toolbox](../assets/studio/toolbox/Inventory-Tab.png)![Creator Store tab indicated in Studio's Toolbox](../assets/studio/toolbox/Creator-Store-Tab.png)
3. Right-click on the image you want to insert into a particle emitter and select **Copy Asset ID**.
4. In the **Explorer** window, select a `Class.ParticleEmitter`.
5. In the **Properties** window, paste the asset ID into the **Texture** property.

### Color

The `Class.ParticleEmitter.Color|Color` property tints each particle's texture to either a specific hue, or to a gradient `Datatype.ColorSequence` across its [lifetime](#lifetime).

#### Constant Color

1. In the **Explorer** window, select the `Class.ParticleEmitter`.
2. In the **Properties** window, select the **Color** property. You can either:
  1. Click on the color square to open the **Colors** pop-up window and select a color.
  2. Input three numbers into the RGB color value field.![Similar particle emitters with different colored particles](../assets/lighting-and-effects/particle-emitter/Color-Examples.jpg)_Similar particle emitters with different colored particles_

#### Color Gradient

1. In the **Explorer** window, select the `Class.ParticleEmitter`.
2. In the **Properties** window, click inside the **Color** property field, then click the **⋯** button.![Button to open color sequence popup](../assets/studio/properties/Color-Open-Sequence.png) In the color sequence popup, each triangle on the bottom axis is a **keypoint** that determines the color value of the property at that point in the particle's lifetime.![Keypoints labeled in color sequence popup](../assets/studio/general/ColorSequence-White-Keypoints-Labeled.png)
3. Click the keypoint at the start of the color sequence, click the small square next to **Color**, and select a color from the popup window.

![Color sequence popup from red to white](../assets/studio/general/ColorSequence-Red-White.png)

1. If you want particles to change their color near the end of their lifetime, click the keypoint at the end of the color sequence, click the small square next to **Color**, and select a color from the popup window.![Color sequence popup from red to purple](../assets/studio/general/ColorSequence-Red-Purple.png)
2. For more customization, you can:
  - Add another keypoint by clicking anywhere on the graph.
  - Make a color change sooner or later within the gradient by dragging an intermediary keypoint to a new position.
  - Delete an intermediary keypoint by selecting it and clicking the **Delete** button.
  - Reset the entire sequence by clicking the **Reset** button.

### Size

The `Class.ParticleEmitter.Size|Size` property sets the size of each particle to a consistent size, or to a `Datatype.NumberSequence` across its [lifetime](#lifetime).

#### Constant Size

1. In the **Explorer** window, select the `Class.ParticleEmitter`.
2. In the **Properties** window, select the **Size** property.
3. Input the size that you want each particle to be.

#### Number Sequence

1. In the **Explorer** window, select the `Class.ParticleEmitter`.
2. In the **Properties** window, click inside the **Size** property field, then click the **⋯** button.![Button to open number sequence popup](../assets/studio/properties/Size-Open-Sequence.png) In the number sequence popup, each square at the start and end of the graph is a **keypoint** that determines the size value of the property at that point in the particle's lifetime. By default, the graph defaults to a straight line and a particle remains the same size throughout its lifetime.![Keypoints labeled in number sequence popup](../assets/studio/general/NumberSequence-0-0-Keypoints-Labeled.png)
3. Perform any of the following actions:
  - To change the size at a point, click on a keypoint and either drag it up or down, or enter a value in the **Value** field.
  - To insert a new keypoint, click on any point in the graph.
  - To delete a keypoint, select it and click the **Delete** button.
  - Reset the entire sequence by clicking the **Reset** button.
  - To add a random range for size, click on any keypoint and drag the **envelope lines** up or down. At that time, particles generate at a random size between the pink envelope.![Envelope lines indicated in number sequence popup](../assets/studio/general/NumberSequence-Envelope.png)_Emitter with large size envelope toward end of its lifetime_

> **Warning:** Particle size can impact performance due to fill-rate. The more pixels particles occupy on a player's screen, the more costly it is on the GPU.
### Transparency

The `Class.ParticleEmitter.Transparency|Transparency` property sets the opacity of each particle as a consistent value, or as a `Datatype.NumberSequence` opacity across its [lifetime](#lifetime). Opacity can range from **0** (totally opaque) to **1** (fully clear). For details on how to set particles to either a specific opacity or to a number sequence, follow the process in customizing [Size](#size) but use the emitter's **Transparency** property field instead.

> **Success:** The `Class.ParticleEmitter.Transparency|Transparency` property is one of the most vital properties of a particle emitter. Fading particles near the start and/or end of their lifetime avoids a popping in/out effect and provides a more realistic effect.

_Static transparency vs. fading in/out_

### Lifetime

The `Class.ParticleEmitter.Lifetime|Lifetime` property sets the lifetime of a particle in seconds. You can set this property either as a consistent value, or provide a **Min** and **Max** range from which a random lifetime will be chosen for each particle.

> **Info:** Particles have a maximum lifetime of 20 seconds. `Class.ParticleEmitter.Lifetime|Lifetime` values higher than this will be internally capped at 20.
### Speed

The `Class.ParticleEmitter.Speed|Speed` property determines a random range of velocities (minimum to maximum) at which new particles will emit, measured in studs per second. Each particle's velocity is chosen upon emission and it applies in the `Class.ParticleEmitter.EmissionDirection|EmissionDirection`. Negative values cause particles to travel in reverse.

Note that changing `Class.ParticleEmitter.Speed|Speed` does not affect active particles and they retain whatever speed they already have. However, `Class.ParticleEmitter.Acceleration|Acceleration`, `Class.ParticleEmitter.Drag|Drag`, and `Class.ParticleEmitter.VelocityInheritance|VelocityInheritance` can be used to affect the speed of active particles over their lifetime.

### Rate

The `Class.ParticleEmitter.Rate|Rate` property sets the number of particles that emit per second. A single particle emitter can create up to 400 particles per second (100 per second on mobile). For best performance, keep the particle rate as low as possible and experiment with [size](#size) and [other properties](#other-properties) to achieve the desired visual effect.

> **Warning:** Particle count can impact performance due to overdraw, especially when particles are overlapping. The more layers of transparent effects on screen, the more costly it is on the GPU.
### Orientation

The `Class.ParticleEmitter.Orientation|Orientation` property determines which orientation mode to use for an emitter's particle geometry.

| Orientation | Particle behavior |
| --- | --- |
| **FacingCamera** | Standard camera-facing billboard quad; default behavior. |
| **FacingCameraWorldUp** | Facing the camera, but rotating only on the vertical upward world **Y** axis. |
| **VelocityParallel** | Aligned parallel to their direction of movement. |
| **VelocityPerpendicular** | Aligned perpendicular to their direction movement. |

_Expected outcome of particle orientation_

### LightEmission

The `Class.ParticleEmitter.LightEmission|LightEmission` property determines the blending of particle `Class.ParticleEmitter.Texture|Texture` colors with the colors behind them. A value of 0 uses normal blending mode while a value of 1 uses additive blending. Higher values can make particles glow even in environments with low lighting.

### SpreadAngle

The `Class.ParticleEmitter.SpreadAngle|SpreadAngle` property has an **X** and a **Y** value which determine the range of angles from which a particle can emit. The range is calculated from both sides around the axes; for example, a value of `(45, 0)` emits particles in a range of 0° to 45° away from the `Class.ParticleEmitter.EmissionDirection|EmissionDirection` across the **X** axis.

### WindAffectsDrag

If you've enabled [global wind](/docs/en-us/environment/global-wind.md) in a game, particles will follow the global wind vector as long as the emitter's `Class.ParticleEmitter.WindAffectsDrag|WindAffectsDrag` property is enabled and its `Class.ParticleEmitter.Drag|Drag` property is greater than 0.

![Drag and WindAffectsDrag properties shown in Properties window of Studio](../assets/studio/properties/ParticleEmitter-WindAffectsDrag.png) ### Shape

The `Class.ParticleEmitter.Shape|Shape` property sets the shape of the particle emitter to either a **Box**, **Sphere**, **Cylinder**, or **Disc**.

![Emitter of Box shape](../assets/lighting-and-effects/particle-emitter/Shape-Box.jpg)_Box_

![Emitter of Sphere shape](../assets/lighting-and-effects/particle-emitter/Shape-Sphere.jpg)_Sphere_

![Emitter of Cylinder shape](../assets/lighting-and-effects/particle-emitter/Shape-Cylinder.jpg)_Cylinder_

![Emitter of Disc shape](../assets/lighting-and-effects/particle-emitter/Shape-Disc.jpg)_Disc_

After you select a shape for your particle emitter, you can experiment with the [ShapeStyle](#shapestyle), [ShapeInOut](#shapeinout), and [ShapePartial](#shapepartial) properties to further customize particle emission.

> **Warning:** If you parent a particle emitter to an `Class.Attachment`, the **Sphere** and **Cylinder** shapes will not display correctly. These shapes should only be used if the emitter is parented to a `Class.BasePart`.
#### ShapeStyle

The `Class.ParticleEmitter.ShapeStyle|ShapeStyle` property sets the emission type to either:

- **Volume** — Particles emit anywhere within the shape.
- **Surface** — Particles only emit from the outside of the shape.

![Emitter of Cylinder shape with Volume shape style](../assets/lighting-and-effects/particle-emitter/Cylinder-Volume.jpg)_Cylinder + Volume_

![Emitter of Cylinder shape with Surface shape style](../assets/lighting-and-effects/particle-emitter/Cylinder-Surface.jpg)_Cylinder + Surface_

#### ShapeInOut

The `Class.ParticleEmitter.ShapeInOut|ShapeInOut` property sets the emission as follows:

- **Inward** — Particles emit toward the shape.
- **Outward** — Particles emit away from the shape.
- **InAndOut** — Particles randomly behave as both **Inward** and **Outward**.

#### ShapePartial

The `Class.ParticleEmitter.ShapePartial|ShapePartial` property is a factor you can use to further modify **Cylinder**, **Disc**, and **Sphere** shapes.

#### Cylinder

For cylinders, `Class.ParticleEmitter.ShapePartial|ShapePartial` multiplies the radius of the cylinder on the side of its **EmissionDirection**.

![Emitter of Cylinder shape with ShapePartial value of 0.5](../assets/lighting-and-effects/particle-emitter/Cylinder-ShapePartial-0.5.jpg)_ShapePartial = 0.5_

![Emitter of Cylinder shape with ShapePartial value of 0](../assets/lighting-and-effects/particle-emitter/Cylinder-ShapePartial-0.jpg)_ShapePartial = 0_

#### Disc

For discs, `Class.ParticleEmitter.ShapePartial|ShapePartial` inversely multiplies the **inner radius** of the disc.

![Emitter of Disc shape with ShapePartial value of 0.5](../assets/lighting-and-effects/particle-emitter/Disc-ShapePartial-0.5.jpg)_ShapePartial = 0.5_

![Emitter of Disc shape with ShapePartial value of 0.1](../assets/lighting-and-effects/particle-emitter/Disc-ShapePartial-0.1.jpg)_ShapePartial = 0.1_

#### Sphere

For spheres, `Class.ParticleEmitter.ShapePartial|ShapePartial` multiplies the **hemispherical angle**.

![Emitter of Sphere shape with ShapePartial value of 1](../assets/lighting-and-effects/particle-emitter/Shape-Sphere.jpg)_ShapePartial = 1_

![Emitter of Sphere shape with ShapePartial value of 0.5](../assets/lighting-and-effects/particle-emitter/Sphere-ShapePartial-0.5.jpg)_ShapePartial = 0.5_

### Squash

The `Class.ParticleEmitter.Squash|Squash` property allows for non-uniform scaling of particles, curve-controlled over their lifetime. Values greater than 0 cause particles to both shrink horizontally and grow vertically, while values less than 0 cause particles to both grow horizontally and shrink vertically. For details on how to set the squash amount to either a constant or to a `Datatype.NumberSequence`, follow the process in customizing [Size](#size) but use the emitter's **Squash** property field instead.

Squash is especially useful for rain. Stretching a particle makes its texture much less recognizable, so even the default sparkle texture can pass as a falling raindrop. For details, see [Simulate rain](#simulate-rain).

### Flipbooks

Particle flipbook textures let you animate a particle's texture over its lifetime.

The flipbook texture can have a frame layout of 2×2, 4×4, 8×8, or custom. For example, the following 1024×1024 image has an 8×8 layout, so it's suitable for a 64‑frame animation.

![Sample texture for particle flipbooks](../assets/lighting-and-effects/particle-emitter/8x8-Explosion.png)
> **Error:** When you create a flipbook texture, include spacing between each of the particle frames. In some cases, mip filtering might require even more spacing. The previous image has transparent spacing around each frame for the flipbook texture.
> **Warning:** Features with custom textures such as flipbooks cost memory to render. If you use many flipbooks with other features that use high memory, then clients automatically deactivate flipbooks when they are low on memory, which is likely for older mobile phones. To reduce the memory usage of flipbooks, use fewer unique animated particle effects or choose a texture of smaller resolution when possible. Reusing textures costs less memory than using unique textures.

Once you've specified a valid flipbook [texture](#texture) for the emitter's `Class.ParticleEmitter.Texture|Texture` property, the `Class.ParticleEmitter.FlipbookLayout|FlipbookLayout` property determines the layout of the texture. It can be any value of the `Enum.ParticleFlipbookLayout` enum:

- `Enum.ParticleFlipbookLayout|None` — Disable flipbook features and use the texture as a single static texture over the particle's lifetime.
- `Enum.ParticleFlipbookLayout|Grid2x2` — 2×2 frames for a 4-frame animation.
- `Enum.ParticleFlipbookLayout|Grid4x4` — 4×4 frames for a 16-frame animation.
- `Enum.ParticleFlipbookLayout|Grid8x8` — 8×8 frames for a 64-frame animation.
- `Enum.ParticleFlipbookLayout|Custom` — A custom grid size defined by `Class.ParticleEmitter.FlipbookSizeX|FlipbookSizeX` and `Class.ParticleEmitter.FlipbookSizeY|FlipbookSizeY`.

To further customize the flipbook behavior, you can adjust the following properties:

#### FlipbookFramerate

The `Class.ParticleEmitter.FlipbookFramerate|FlipbookFramerate` property determines how fast the flipbook texture animates in frames per second. Like `Class.ParticleEmitter.Lifetime|Lifetime`, you can set a minimum and maximum range to randomize the framerate of the flip book, with a maximum of 30 frames per second.

#### FlipbookMode

The `Class.ParticleEmitter.FlipbookMode|FlipbookMode` property determines the type of the flipbook animation. The property can be any value of the `Enum.ParticleFlipbookMode` enum:

- **Loop** — Continuously play through all frames, starting back at the first frame after playing the last.
- **OneShot** — Play through the animation only once across the particle's lifetime. With this setting, the `Class.ParticleEmitter.FlipbookFramerate|FlipbookFramerate` property doesn't apply; instead, the framerate is determined by the particle's `Class.ParticleEmitter.Lifetime|Lifetime` divided evenly by the number of frames in the animation. **OneShot** animations are useful for clear non-repeating animations, such as an explosion that creates a puff of smoke and then fades out.
- **PingPong** — Play from the first to the last frame, then in reverse from the last to the first, repeating throughout the `Class.ParticleEmitter.Lifetime|Lifetime` of the particle.
- **Random** — Play the frames in a random order, blending/crossfading from one frame to the next. This can be useful for organic particle textures at low framerates, such as stars slowly twinkling between subtly different shapes.

#### FlipbookStartRandom

The `Class.ParticleEmitter.FlipbookStartRandom|FlipbookStartRandom` property determines whether each particle begins at a random frame of the animation instead of always starting at the first frame. One use case is to enable this property and also set `Class.ParticleEmitter.FlipbookFramerate|FlipbookFramerate` to zero, causing each emitted particle to be a static frame chosen randomly from the flipbook texture.

### Other properties

To further customize particles, consider the following emitter properties, and click through to the `Class.ParticleEmitter` reference page for more details.

#### Appearance

The following appearance properties are in addition to [color](#color), [light emission](#lightemission), [orientation](#orientation), [size](#size), [texture](#texture), [transparency](#transparency), [squash](#squash), and [flipbooks](#flipbooks).

| Property | Description |
| --- | --- |
| `Class.ParticleEmitter.LightInfluence\|LightInfluence` | Determines how much environmental light affects the color of individual particles. |
| `Class.ParticleEmitter.Brightness\|Brightness` | Scales the light emitted from the emitter when `Class.ParticleEmitter.LightInfluence\|LightInfluence` is 0. |
| `Class.ParticleEmitter.ZOffset\|ZOffset` | Determines the forward-backward render position of particles, in studs, without changing their size on the screen. This allows for multiple emitters to be layered, or to render particles in front of or behind the parent object. |

#### Emission

The following emission properties are in addition to [emission direction](#create-particle-emitters), [lifetime](#lifetime), [speed](#speed), [rate](#rate), [spread angle](#spreadangle), and [shape](#shape).

| Property | Description |
| --- | --- |
| `Class.ParticleEmitter.Enabled\|Enabled` | Determines if particles emit from the emitter. Setting this to `false` stops further particles from spawning, but any existing particles remain active until they expire or the `Class.ParticleEmitter:Clear()\|Clear()` method is called. |
| `Class.ParticleEmitter.Rotation\|Rotation` | Determines the angle of rotation for newly-emitted particles. Single numbers create particles at that angle, while two numbers (minimum, maximum) set a random rotation for each particle. |
| `Class.ParticleEmitter.RotSpeed\|RotSpeed` | Determines the angular speed in degrees per second for particles. This can be a single number or a number range for a randomized speed. Negative values cause particles to rotate counter-clockwise. |

#### Motion

The following motion properties are in addition to [wind influence](#windaffectsdrag).

| Property | Description |
| --- | --- |
| `Class.ParticleEmitter.Acceleration\|Acceleration` | Determines by how much the velocity of particles changes per second. You can use this property to create effects such as particles being affected by gravity. |
| `Class.ParticleEmitter.Drag\|Drag` | Determines the rate in seconds that particles lose half their speed. |
| `Class.ParticleEmitter.LockedToPart\|LockedToPart` | Determines if particles will "stick" to the emission source to which the emitter is parented. |
| `Class.ParticleEmitter.TimeScale\|TimeScale` | A value between 0 and 1 that controls the speed of the particle effect. |
| `Class.ParticleEmitter.VelocityInheritance\|VelocityInheritance` | Determines how much of the parent object's velocity is inherited by particles when they are emitted. |

## Simulate rain

Simulating every raindrop isn't practical, but particle emitters can create a convincing illusion of rain in a 3D world:

1. Insert a `Class.Part` above the area where you want rain to fall. Anchor it, set its **Transparency** to `1`, and disable **CanCollide**.
2. Insert a `Class.ParticleEmitter` into the part and set its `Class.ParticleEmitter.EmissionDirection|EmissionDirection` to **Bottom**.
3. Set [Squash](#squash) to a positive value, such as `3`, to stretch each particle into a streak. Higher values make particles thinner, so you might need to increase [size](#size) as well.
  > **Success:** If you set [Orientation](#orientation) to **VelocityParallel** so that streaks align with their direction of travel, use a negative squash value instead.
4. Darken [Color](#color), increase **LightInfluence** so that the rain reacts to the lighting around it, increase [Speed](#speed), and decrease [Lifetime](#lifetime) so that particles disappear near the ground.
5. To angle the rain, set a small **Rotation** or enable [WindAffectsDrag](#windaffectsdrag) so that particles follow [global wind](/docs/en-us/environment/global-wind.md). Drag slows the fall in addition to applying the wind, so you might need to increase the downward **Acceleration** to keep the rain falling quickly.

A single emitter can create a limited number of particles per second (see [Rate](#rate)), so heavier rain or a larger area requires many parts with emitters. Arrange them in a grid over the desired area.

To show rain landing, place transparent parts on the ground with emitters whose **EmissionDirection** is **Top**. Splash particles aren't stretched like falling rain, so they usually need a custom [texture](#texture) and a [Transparency](#transparency) sequence that makes each splash appear to dissipate. Splashes only look right on surfaces where you've placed them carefully. If you can't place them by hand, low-lying mist is much more forgiving.

### Manage particle limits

Rain that covers a large area reaches particle limits quickly, and mobile devices have much lower limits than desktops. If particles flicker in the distance, reduce how many are on screen at once:

- Place the emitter parts lower in the air and shorten **Lifetime** to match.
- Decrease **Rate** to turn a downpour into a lighter shower.
- Cover a smaller area with fewer emitter parts.

### Rain examples

- For a hand-built example, see [The Mystery of Duvall Drive](/docs/en-us/resources/the-mystery-of-duvall-drive.md). It uses emitters for [rain, mist, splashes, and water dripping from awnings](/docs/en-us/resources/the-mystery-of-duvall-drive/develop-a-moving-world.md#make-storm-debris).
- For a scripted example, see the [weather-island](https://github.com/Roblox/resources/tree/main/experiences/weather-island) project. It schedules storms, transitions [clouds](/docs/en-us/environment/clouds.md) and wind, spawns rain and mist emitters, and performs roof detection.
