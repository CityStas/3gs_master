---
name: UICaptureMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used to determine what UI elements should be captured with CaptureService."
---

# UICaptureMode

Used to determine what UI elements should be captured with
[CaptureService](/docs/reference/engine/classes/CaptureService.md).

**Type:** enum

## Description

Controls which UI layers are composited into screenshots and video captures
taken by [CaptureService](/docs/reference/engine/classes/CaptureService.md). When [UICaptureMode.All](/docs/reference/engine/enums/UICaptureMode.md), both
[CoreGui](/docs/reference/engine/classes/CoreGui.md) and [PlayerGui](/docs/reference/engine/classes/PlayerGui.md) elements are rendered into the output.
When [UICaptureMode.None](/docs/reference/engine/enums/UICaptureMode.md), no UI is included and the capture shows only
the 3D scene.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `All` | 0 | Capture all UI elements. |
| `None` | 1 | Capture no UI elements. |