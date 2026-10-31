---
name: SwipeDirection
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The direction that a user is swiping on their touch screen."
---

# SwipeDirection

The direction that a user is swiping on their touch screen.

**Type:** enum

## Description

The SwipeDirection Enum represents the direction in which a user swipes on a
[UserInputService.TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device.

The [GuiObject.TouchSwipe](/docs/reference/engine/classes/GuiObject.md) and [UserInputService.TouchSwipe](/docs/reference/engine/classes/UserInputService.md)
events pass this enum as an argument.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Right` | 0 | The user swiped right. |
| `Left` | 1 | The user swiped left. |
| `Up` | 2 | The user swiped up. |
| `Down` | 3 | The user swiped down. |
| `None` | 4 | The user did not swipe in a certain direction. |