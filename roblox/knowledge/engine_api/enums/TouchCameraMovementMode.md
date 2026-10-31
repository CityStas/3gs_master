---
name: TouchCameraMovementMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Changes the touch camera movement mode currently in-use by the client using a TouchEnabled device."
---

# TouchCameraMovementMode

Changes the touch camera movement mode currently in-use by the client using a
TouchEnabled device.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Default mode used by Roblox core scripts. |
| `Classic` | 1 | Default mode used by Roblox core scripts. |
| `Follow` | 2 | Camera moves with the subject and rotates to keep the subject in the center. |
| `Orbital` | 3 | The camera locks at a certain angle. Once it's set, players can rotate the camera, but it will always maintain a consistent angle to the ground. |