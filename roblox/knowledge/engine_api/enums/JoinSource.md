---
name: JoinSource
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies the context in which a player joined an experience via a deeplink."
---

# JoinSource

Identifies the context in which a player joined an experience via a deeplink.

**Type:** enum

## Description

Identifies the context in which a player joined an experience via a deeplink.
The value is available as the `JoinSource` key in the `GameJoinContext` table
returned by [Player:GetJoinData()](/docs/reference/engine/classes/Player.md). Experiences can inspect this value
on [Players.PlayerAdded](/docs/reference/engine/classes/Players.md) to customize the player's starting state
depending on how they arrived.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `CreatedItemAttribution` | 1 | The player joined by following an attribution link for an item created inside an experience. |