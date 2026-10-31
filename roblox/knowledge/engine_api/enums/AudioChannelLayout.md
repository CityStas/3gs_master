---
name: AudioChannelLayout
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the channel layout of an audio stream."
---

# AudioChannelLayout

Describes the channel layout of an audio stream.

**Type:** enum

## Description

The `AudioChannelLayout` enum describes the channel layout of an audio stream.
Audio streams contain one or more channels that are intended to be rendered
simultaneously with a particular arrangement of speakers. In general, more
channels impact performance but provide higher spatial quality.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Mono` | 0 | Monaural audio streams contain only one **Center** channel.  ![Diagram showing position of channels for Mono layout.](/assets/engine-api/enums/AudioChannelLayout/Mono.jpg) |
| `Stereo` | 1 | Stereophonic audio streams consist of two channels: **Left** and **Right**.  ![Diagram showing position of channels for Stereo layout.](/assets/engine-api/enums/AudioChannelLayout/Stereo.jpg) |
| `Quad` | 2 | Quadrophonic audio streams consist of four channels: **Left**, **Right**, **BackLeft**, and **BackRight**. Quadrophonic streams can encode forward/backward spatial information that stereo streams might struggle with.  ![Diagram showing position of channels for Quad layout.](/assets/engine-api/enums/AudioChannelLayout/Quad.jpg) |
| `Surround_5` | 3 | Surround sound audio streams consist of five channels: **Left**, **Right**, **Center**, **BackLeft**, and **BackRight**. Surround sound streams encode spatial information with better resolution front and center.  ![Diagram showing position of channels for Surround 5 layout.](/assets/engine-api/enums/AudioChannelLayout/Surround_5.jpg) |
| `Surround_5_1` | 4 | 5.1 surround sound consists of six channels: **Left**, **Right**, **Center**, **BackLeft**, **BackRight**, and a **Sub** (subsonic) low‑frequency channel. 5.1 surround sound benefits from low frequencies being less directional in order to encode higher resolution spatial information versus simple 5‑channel surround sound.  ![Diagram showing position of channels for Surround 5.1 layout.](/assets/engine-api/enums/AudioChannelLayout/Surround_5_1.jpg) |
| `Surround_7_1` | 5 | 7.1 surround sound consists of eight channels: **Left**, **Right**, **Center**, **SurroundLeft**, **SurroundRight**, **BackLeft**, **BackRight**, and a **Sub** (subsonic) low‑frequency channel. 7.1 surround sound is an improvement over 5.1 surround sound, offering better spatial resolution directly to the left and right as well.  ![Diagram showing position of channels for Surround 7.1 layout.](/assets/engine-api/enums/AudioChannelLayout/Surround_7_1.jpg) |
| `Surround_7_1_4` | 6 | 7.1.4 surround sound consists of twelve channels: **Left**, **Right**, **Center**, **SurroundLeft**, **SurroundRight**, **BackLeft**, **BackRight**, **Sub**, **TopLeft**, **TopRight**, **TopBackLeft**, and **TopBackRight**. 7.1.4 is the only currently supported channel layout that encodes height information.  ![Diagram showing position of channels for Surround 7.1.4 layout.](/assets/engine-api/enums/AudioChannelLayout/Surround_7_1_4.jpg) |