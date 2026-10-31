---
name: ComputerCameraMovementMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The camera movement mode currently in-use by the client."
---

# ComputerCameraMovementMode

The camera movement mode currently in-use by the client.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | The default camera movement mode is classic. |
| `Classic` | 1 | Camera tracks the player but will not automatically rotate if the player walks left or right. |
| `Follow` | 2 | Camera tracks the player and automatically rotates if the player walks left or right. |
| `Orbital` | 3 | The camera has a fixed Y position, but can be rotated around the player. |
| `CameraToggle` | 4 | The camera toggles between locked and free rotation with the right mouse button. |