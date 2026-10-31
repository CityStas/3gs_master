---
name: ListenerPositionType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Defines where and how an AudioListener is positioned when receiving spatial audio."
---

# ListenerPositionType

Defines where and how an [AudioListener](/docs/reference/engine/classes/AudioListener.md) is positioned when receiving
spatial audio.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Parent` | 0 | Uses the position and orientation of the [AudioListener](/docs/reference/engine/classes/AudioListener.md)'s parent [Instance](/docs/reference/engine/classes/Instance.md). |
| `Instance` | 1 | Uses the position and orientation of the [Instance](/docs/reference/engine/classes/Instance.md) specified by [AudioListener.PositionInstance](/docs/reference/engine/classes/AudioListener.md). |