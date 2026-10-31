---
name: CameraSpeedAdjustBinding
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls which input gesture adjusts the Studio camera's fly speed while navigating."
---

# CameraSpeedAdjustBinding

Controls which input gesture adjusts the Studio camera's fly speed while
navigating.

**Type:** enum

## Description

Controls which mouse-and-keyboard gesture is used to adjust the Studio
camera's fly speed while navigating in the 3D viewport. The selected binding
intercepts the mouse scroll wheel (or touchpad pan gesture) when the
designated modifier is active, changing camera speed instead of zooming. This
setting is exposed in Studio's **Camera** preferences as
`Camera Speed Adjust Binding` and defaults to
[CameraSpeedAdjustBinding.RmbScroll](/docs/reference/engine/enums/CameraSpeedAdjustBinding.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | No input gesture is bound to camera speed adjustment; the scroll wheel always zooms. |
| `RmbScroll` | 1 | Scrolling while holding the right mouse button adjusts the camera fly speed instead of zooming. |
| `AltScroll` | 2 | Scrolling while holding Alt adjusts the camera fly speed instead of zooming. |