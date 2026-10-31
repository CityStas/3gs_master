---
name: VRTouchpadMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used to identify the behavior of a specified VR touchpad."
---

# VRTouchpadMode

Used to identify the behavior of a specified VR touchpad.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Touch` | 0 | The touchpad is treated as ButtonB if it is the left touchpad, or ButtonA if it is the right touchpad. |
| `VirtualThumbstick` | 1 | The touchpad will function as a gamepad joystick. |
| `ABXY` | 2 | The touchpad will function as a means of inputting the standard ABXY gamepad input, dividing it up into 4 diagonal pie slices. |