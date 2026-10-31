---
name: ParticleFlipbookMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the type of the flipbook animation."
---

# ParticleFlipbookMode

Determines the type of the flipbook animation.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Loop` | 0 | Continuously play through all frames, starting back at the first frame after playing the last. |
| `OneShot` | 1 | Play through the animation only once across the particle's lifetime. With this setting, the [ParticleEmitter.FlipbookFramerate](/docs/reference/engine/classes/ParticleEmitter.md) property doesn't apply; instead, the framerate is determined by the particle's [ParticleEmitter.Lifetime](/docs/reference/engine/classes/ParticleEmitter.md) divided evenly by the number of frames in the animation. **OneShot** animations are useful for clear non-repeating animations, such as an explosion that creates a puff of smoke and then fades out. |
| `PingPong` | 2 | Play from the first to the last frame, then in reverse from the last to the first, repeating throughout the [ParticleEmitter.Lifetime](/docs/reference/engine/classes/ParticleEmitter.md) of the particle. |
| `Random` | 3 | Play the frames in a random order, blending/crossfading from one frame to the next. This can be useful for organic particle textures at low framerates, such as stars slowly twinkling between subtly different shapes. |