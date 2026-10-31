---
name: AudioFilterType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Filter types used for AudioFilter instances."
---

# AudioFilterType

Filter types used for [AudioFilter](/docs/reference/engine/classes/AudioFilter.md) instances.

**Type:** enum

## Description

Families of curves that [AudioFilter](/docs/reference/engine/classes/AudioFilter.md) can use to process incoming audio.
Each filter type is applied at a specified
[Frequency](/docs/reference/engine/classes/AudioFilter.md) and may be shaped by additional
[Gain](/docs/reference/engine/classes/AudioFilter.md) or [Q](/docs/reference/engine/classes/AudioFilter.md) parameters.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Peak` | 0 | Filter that boosts or reduces sound near a specified [Frequency](/docs/reference/engine/classes/AudioFilter.md). |
| `LowShelf` | 1 | Filter that boosts or reduces sound below a specified [Frequency](/docs/reference/engine/classes/AudioFilter.md). |
| `HighShelf` | 2 | Filter that boosts or reduces sound above a specified [Frequency](/docs/reference/engine/classes/AudioFilter.md). |
| `Lowpass12dB` | 3 | Filter that cuts sound above a specified [Frequency](/docs/reference/engine/classes/AudioFilter.md), at a slope of -12dB/octave. |
| `Lowpass24dB` | 4 | Filter that cuts sound above a specified [Frequency](/docs/reference/engine/classes/AudioFilter.md), at a slope of -24dB/octave. |
| `Lowpass48dB` | 5 | Filter that cuts sound above a specified [Frequency](/docs/reference/engine/classes/AudioFilter.md), at a slope of -48dB/octave. |
| `Highpass12dB` | 6 | Filter that cuts sound below a specified [Frequency](/docs/reference/engine/classes/AudioFilter.md), at a slope of -12dB/octave. |
| `Highpass24dB` | 7 | Filter that cuts sound below a specified [Frequency](/docs/reference/engine/classes/AudioFilter.md), at a slope of -24dB/octave. |
| `Highpass48dB` | 8 | Filter that cuts sound below a specified [Frequency](/docs/reference/engine/classes/AudioFilter.md), at a slope of -48dB/octave. |
| `Bandpass` | 9 | Filter that only allows sound near a specified [Frequency](/docs/reference/engine/classes/AudioFilter.md) to be heard. |
| `Notch` | 10 | Filter that cuts sound near a specified [Frequency](/docs/reference/engine/classes/AudioFilter.md). |
| `Lowpass6dB` | 11 | Filter that cuts sound above a specified [Frequency](/docs/reference/engine/classes/AudioFilter.md), at a slope of -6dB/octave. |