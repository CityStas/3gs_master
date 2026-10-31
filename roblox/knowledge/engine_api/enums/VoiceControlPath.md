---
name: VoiceControlPath
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies which leg of a voice chat control-plane operation is being reported."
---

# VoiceControlPath

Identifies which leg of a voice chat control-plane operation is being
reported.

**Type:** enum

## Description

Identifies which voice control-plane path triggered a [VoiceChatService](/docs/reference/engine/classes/VoiceChatService.md)
event such as `RelayCandidatesGathered` or `VoiceSetupFailed`:
[VoiceControlPath.Join](/docs/reference/engine/enums/VoiceControlPath.md) (enter a voice room),
[VoiceControlPath.Publish](/docs/reference/engine/enums/VoiceControlPath.md) (send local microphone audio), or
[VoiceControlPath.Subscribe](/docs/reference/engine/enums/VoiceControlPath.md) (receive remote audio).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Publish` | 0 | Represents the outbound audio path, through which a client sends local microphone audio to the room. |
| `Subscribe` | 1 | Represents the inbound audio path, through which a client receives remote participants' audio streams. |
| `Join` | 2 | Represents the room-join path, through which a client establishes membership in a voice room. |