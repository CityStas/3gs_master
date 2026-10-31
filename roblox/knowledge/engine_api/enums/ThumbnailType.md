---
name: ThumbnailType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the type of user thumbnail returned by Players:GetUserThumbnailAsync()."
---

# ThumbnailType

Describes the type of user thumbnail returned by
[Players:GetUserThumbnailAsync()](/docs/reference/engine/classes/Players.md).

**Type:** enum

## Description

Describes the type of user thumbnail that should be returned by
GetUserThumbnailAsync.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `HeadShot` | 0 | The returned thumbnail shows just the headshot (head and up) of the user's avatar. |
| `AvatarBust` | 1 | The returned thumbnail shows the bust (chest up) of the user's avatar. |
| `AvatarThumbnail` | 2 | The returned thumbnail shows the entire body of the user's avatar. |