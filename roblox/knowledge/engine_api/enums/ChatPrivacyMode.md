---
name: ChatPrivacyMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes which other users a player is permitted to exchange in-game chat messages with."
---

# ChatPrivacyMode

Describes which other users a player is permitted to exchange in-game chat
messages with.

**Type:** enum

## Description

Internally controls the user's chat privacy settings.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `AllUsers` | 0 | A player can chat with all users in a game. |
| `NoOne` | 1 | A player cannot chat with any other users in a game. |
| `Friends` | 2 | A player can only chat with users in a game that are on their friends list. |