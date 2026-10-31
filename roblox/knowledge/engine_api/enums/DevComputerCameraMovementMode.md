---
name: DevComputerCameraMovementMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Overwrites the player's camera movement mode setting on a computer."
---

# DevComputerCameraMovementMode

Overwrites the player's camera movement mode setting on a computer.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `UserChoice` | 0 | The camera will move based on the player's settings. |
| `Classic` | 1 | Camera tracks the player but will not automatically rotate if the player walks left or right. |
| `Follow` | 2 | Camera tracks the player and automatically rotates if the player walks left or right. |
| `Orbital` | 3 | The camera has a fixed Y position, but can be rotated around the player. |
| `CameraToggle` | 4 | The camera toggles between locked and free rotation with the right mouse button. |