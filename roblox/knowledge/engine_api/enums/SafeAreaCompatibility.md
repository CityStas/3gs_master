---
name: SafeAreaCompatibility
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes how descendants of a ScreenGui adapt to screens with cutouts."
---

# SafeAreaCompatibility

Describes how descendants of a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) adapt to screens with
cutouts.

**Type:** enum

## Description

This enum describes the automatic compatibility transformations that apply to
descendant "fullscreen" [GuiObjects](/docs/reference/engine/classes/GuiObject.md) of a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) on
displays with screen cutouts.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | Do not apply compatibility transformations to any descendants of the [ScreenGui](/docs/reference/engine/classes/ScreenGui.md). |
| `FullscreenExtension` | 1 | If the total area of any descendant [GuiObject](/docs/reference/engine/classes/GuiObject.md) within the [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) (including any applied border or [UIStroke](/docs/reference/engine/classes/UIStroke.md)) covers the device's safe area both horizontally and vertically, its background area will be expanded to cover the fullscreen area. This expansion does **not** affect the size or position of the descendant's **content**, except in the case of [ImageLabel](/docs/reference/engine/classes/ImageLabel.md), [ImageButton](/docs/reference/engine/classes/ImageButton.md), or [VideoFrame](/docs/reference/engine/classes/VideoFrame.md) where the image/video is considered part of the background and will be expanded to fullscreen.  Note that this option is intended to automatically improve the appearance of UI that was authored for screens without any cutouts. However, it's recommended that you avoid fullscreen extensions for new work; instead, use the [ScreenInsets](/docs/reference/engine/classes/ScreenGui.md) property to specify which insets should be respected for different [ScreenGuis](/docs/reference/engine/classes/ScreenGui.md). |