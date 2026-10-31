---
name: PlayerChatType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the style of a chat message."
---

# PlayerChatType

Determines the style of a chat message.

**Type:** enum

## Description

Used by Roblox's Chat to determine the style of a chat message. If you want to
check for this kind of stuff, see [Player.Chatted](/docs/reference/engine/classes/Player.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `All` | 0 | A global message that everyone can receive. |
| `Team` | 1 | A team message only players in the same team can receive. |
| `Whisper` | 2 | A whispered message only the person it's whispered to can receive. |