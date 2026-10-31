---
title: "Dynamic effects"
url: /docs/en-us/sound/dynamic-effects
last_updated: 2026-10-30T19:55:56Z
description: "Legacy effects that modify or enhance Sound objects in your games."
---

# Dynamic effects

> **Warning:** There is a newer set of audio effects that offer more control and address robust use cases. For more information, see [Audio effects](/docs/en-us/audio/effects.md).

Dynamic effects modify or enhance the audio of individual `Class.Sound` objects or an entire `Class.SoundGroup`. You can apply these effects to make your audio more immersive within your game, such as using `Class.ReverbSoundEffect` in large rooms to make them feel massive.

## Apply dynamic effects

Each dynamic effect you apply has additional properties you can adjust until you achieve the type of sound you desire. For more information on these properties, see each dynamic effect's API page.

To apply a dynamic effect:

1. In the **Explorer** window, insert a new dynamic effect into a `Class.Sound` or `Class.SoundGroup` object.
  1. Hover over the object and click the ⊕ button. A contextual menu displays.
  2. From the menu, insert a **dynamic effect**.
2. **OPTIONAL** In the **Properties** window, select the new dynamic effect and adjust its properties.

## Types

### Equalizer

The `Class.EqualizerSoundEffect` allows for control of the volume of various frequency ranges. This dynamic effect is useful to highlight or minimize particular elements of audio, such as muffling all audio in your game when a player goes underwater.

|  | |
| --- | --- |
| Audio without effect | Audio with equalizer |

### Compressor

The `Class.CompressorSoundEffect` reduces the dynamic range of audio by lowering the volume of the highest parts of a source while at the same time raising the overall volume. This dynamic effect is useful to set a consistent volume for users to hear even if you record audio while whispering or speaking loudly. You can also use this dynamic effect to prioritize sounds from one `Class.SoundGroup` over another through the process of ducking. For more information, see [Ducking](/docs/en-us/sound/groups.md#ducking).

|  | |
| --- | --- |
| Audio without effect | Audio with compressor |

### Reverb

The `Class.ReverbSoundEffect` simulates the effect of sounds bouncing off of several surfaces. This dynamic effect is useful to simulate more realistic reflections of sounds in interior spaces, such as bouncing a basketball inside a gymnasium, or playing rock music in a stadium.

|  | |
| --- | --- |
| Audio without effect | Audio with reverb |

### Chorus

The `Class.ChorusSoundEffect` simulates the effect of multiple vocals or instruments playing simultaneously by taking the original sound and overlaying copies, each with slight variations in pitch. This dynamic effect is useful for simulating a robotic or futuristic quality to your audio.

|  | |
| --- | --- |
| Audio without effect | Audio with chorus |

### Distortion

The `Class.DistortionSoundEffect` simulates the effect that would occur when overdriving older style audio equipment. This dynamic effect causes clipping in the sound and adds a general "fuzziness", which is useful for either adding intensity and character to musical instruments.

|  | |
| --- | --- |
| Audio without effect | Audio with distortion |

### Echo

The `Class.EchoSoundEffect` causes a sound to repeat on a delay with diminishing volume, simulating the real effect of an echo that bounces off of hard surfaces, such as walls and caves.

|  | |
| --- | --- |
| Audio without effect | Audio with echo |

### Flange

The `Class.FlangeSoundEffect` creates a sweeping or whooshing effect by copying the original audio signal and playing it slightly offset and modulated on top of the original. This dynamic effect is useful for adding strange, otherworldly digital quality to your audio. For example, you can use it on an air conditioner recording to make a sci-fi spaceship engine rumble.

|  | |
| --- | --- |
| Audio without effect | Audio with flange |

### Pitch Shift

The `Class.PitchShiftSoundEffect` raises or lowers pitch without changing the playback speed. This dynamic effect is useful for changing the scale of your sounds. You can use it to make small sounds feel huge by pitching them down or conversely pitch sounds up to make an explosion sound more like a balloon pop.

|  | |
| --- | --- |
| Audio without effect | Audio with pitch shift |

### Tremolo

The `Class.TremoloSoundEffect` creates a trembling effect on a sound by varying its volume up and down. This dynamic effect is useful to transform instrument sounds into a wavy, dreamlike quality, or to create swells and dips in weather-related audio.

|  | |
| --- | --- |
| Audio without effect | Audio with tremolo |
