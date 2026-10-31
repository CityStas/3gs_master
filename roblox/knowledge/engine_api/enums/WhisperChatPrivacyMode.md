---
name: WhisperChatPrivacyMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes which other players a player allows to initiate a whisper (direct) chat with them in an experience."
---

# WhisperChatPrivacyMode

Describes which other players a player allows to initiate a whisper (direct)
chat with them in an experience.

**Type:** enum

## Description

Describes which other players a player allows to initiate a whisper (direct)
chat with them in an experience. A whisper chat is only permitted when
**both** the sender and the recipient have
[WhisperChatPrivacyMode.AllUsers](/docs/reference/engine/enums/WhisperChatPrivacyMode.md); if either player's mode is
[WhisperChatPrivacyMode.NoOne](/docs/reference/engine/enums/WhisperChatPrivacyMode.md), the private chat is blocked. The setting
comes from the player's account privacy configuration and is applied when the
[Player](/docs/reference/engine/classes/Player.md) object is created. Defaults to
[WhisperChatPrivacyMode.NoOne](/docs/reference/engine/enums/WhisperChatPrivacyMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `AllUsers` | 0 | The player allows any other player in the experience to initiate a whisper chat with them. |
| `NoOne` | 1 | The player does not allow any other player to initiate a whisper chat with them. |