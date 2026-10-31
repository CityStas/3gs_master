---
name: SelfViewPosition
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Defines the screen location of the current player's self view."
---

# SelfViewPosition

Defines the screen location of the current player's self view.

**Type:** enum

## Description

This enum defines the screen location of the current player's self view, used
in conjunction with [SocialService:ShowSelfView()](/docs/reference/engine/classes/SocialService.md) for example.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `LastPosition` | 0 | The position of the self view when it was last closed. |
| `TopLeft` | 1 | Top-left corner of the screen, with slight padding from the top and left edges. |
| `TopRight` | 2 | Top-right corner of the screen, with slight padding from the top and right edges. |
| `BottomLeft` | 3 | Bottom-left corner of the screen, with slight padding from the bottom and left edges. |
| `BottomRight` | 4 | Bottom-right corner of the screen, with slight padding from the bottom and right edges. |