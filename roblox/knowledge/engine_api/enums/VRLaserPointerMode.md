---
name: VRLaserPointerMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the display mode of the VR laser pointer used to interact with the user interface."
---

# VRLaserPointerMode

Specifies the display mode of the VR laser pointer used to interact with the
user interface.

**Type:** enum

## Description

Specifies the display mode of the laser pointer that a VR player uses to
interact with the user interface. This enum is the type of
[VRService.LaserPointer](/docs/reference/engine/classes/VRService.md), which defaults to
[Pointer](/docs/reference/engine/enums/VRLaserPointerMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Disabled` | 0 | The laser pointer is hidden and no pointer is rendered for any VR hand. |
| `Pointer` | 1 | A single laser pointer is shown for the primary VR hand; this is the default value of [VRService.LaserPointer](/docs/reference/engine/classes/VRService.md). |
| `DualPointer` | 2 | A laser pointer is shown for each VR hand simultaneously. |