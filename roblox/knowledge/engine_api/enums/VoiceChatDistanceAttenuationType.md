---
name: VoiceChatDistanceAttenuationType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Enum used for preset distance attenuation curve options in the default voice chat setup."
---

# VoiceChatDistanceAttenuationType

Enum used for preset distance attenuation curve options in the default voice
chat setup.

**Type:** enum

## Description

Each value in this enum represents a distance attenuation curve that can be
used by [VoiceChatService](/docs/reference/engine/classes/VoiceChatService.md) when creating the default voice chat setup
using [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) and [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) objects.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Inverse` | 0 | Represents a distance attenuation curve that follows the inverse-squared law. This is identical to the default distance attenuation of an [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) instance. |
| `Legacy` | 1 | Represents a linear-squared distance attenuation curve with a minimum distance of `7` and a maximum distance of `80`. This is identical to the distance attenuation used in the internal-only default voice setup that does not use [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) and [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) objects. |