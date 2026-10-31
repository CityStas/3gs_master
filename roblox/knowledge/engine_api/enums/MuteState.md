---
name: MuteState
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes whether a voice chat participant's microphone is actively transmitting audio."
---

# MuteState

Describes whether a voice chat participant's microphone is actively
transmitting audio.

**Type:** enum

## Description

[MuteState](/docs/reference/engine/enums/MuteState.md) is the microphone mute status of a local player in a voice
chat session. It is passed in [VoiceChatService](/docs/reference/engine/classes/VoiceChatService.md) events such as
`VoiceChatPlayerMuteStateChangedClientToServer` and
`VoiceChatPlayerMuteStateChangedServerToClient`. Defaults to
[MuteState.Unmuted](/docs/reference/engine/enums/MuteState.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unmuted` | 0 | The participant's microphone is active and transmitting audio. |
| `Muted` | 1 | The participant's microphone is muted and not transmitting audio. |