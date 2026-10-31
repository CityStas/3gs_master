---
name: VRSessionState
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The lifecycle state of the active VR session, as reported by the `VRSessionState` property of VRService."
---

# VRSessionState

The lifecycle state of the active VR session, as reported by the
`VRSessionState` property of [VRService](/docs/reference/engine/classes/VRService.md).

**Type:** enum

## Description

Represents the current state of the VR session managed by [VRService](/docs/reference/engine/classes/VRService.md).
The engine updates `VRSessionState` each frame from the active session.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Undefined` | 0 | The VR session state is unknown or has not yet been established; the default value of `VRSessionState`. |
| `Idle` | 1 | The VR headset is connected and ready but is not yet presenting frames to the user. |
| `Visible` | 2 | The VR session is rendering frames visible to the user but does not yet have XR input focus; haptic feedback is available. |
| `Focused` | 3 | The VR session has full XR input focus and is rendering visible frames; haptic feedback is available. |
| `Stopping` | 4 | The VR session is in the process of stopping and will transition to an inactive state. |