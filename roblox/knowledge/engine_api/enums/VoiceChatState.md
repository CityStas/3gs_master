---
name: VoiceChatState
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the connection state of a local player's voice chat session."
---

# VoiceChatState

Describes the connection state of a local player's voice chat session.

**Type:** enum

## Description

Describes the connection state of a local player's voice chat session. The
session progresses through the [VoiceChatState](/docs/reference/engine/enums/VoiceChatState.md) items from idle, through
joining, to joined, and then to leaving, ended, or failed when the session
concludes.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Idle` | 0 | The player is not connected to voice chat and no join attempt is in progress. |
| `Joining` | 1 | A voice chat join attempt is in progress for the first time. |
| `JoiningRetry` | 2 | A voice chat join is being retried after a previous attempt did not succeed. |
| `Joined` | 3 | The player has successfully joined the voice chat session and is actively connected. |
| `Leaving` | 4 | The player is in the process of disconnecting from the voice chat session. |
| `Ended` | 5 | The voice chat session has ended normally. |
| `Failed` | 6 | The voice chat session ended due to an error, such as a failure to join or a mid-session error. |