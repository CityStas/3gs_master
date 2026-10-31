---
name: AudioSimulationFidelity
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Enum which determines how detailed audio simulation should be for AudioEmitters and AudioListeners."
---

# AudioSimulationFidelity

Enum which determines how detailed audio simulation should be for
[AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md) and [AudioListeners](/docs/reference/engine/classes/AudioListener.md).

**Type:** enum

## Description

This enum, used with [AudioEmitter.SimulationFidelity](/docs/reference/engine/classes/AudioEmitter.md) and
[AudioListener.SimulationFidelity](/docs/reference/engine/classes/AudioListener.md), determines how detailed audio
simulation should be.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | No acoustic simulation occurs; only direction and distance are taken into account. |
| `Automatic` | 1 | The audio engine simulates transmission, diffraction, and reflections at a level of detail suitable to most devices. |