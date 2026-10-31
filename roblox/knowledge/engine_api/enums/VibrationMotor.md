---
name: VibrationMotor
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes various types of haptic motor sizes and locations."
---

# VibrationMotor

Describes various types of haptic motor sizes and locations.

**Type:** enum

## Description

Describes various types of haptic motor sizes and locations. Most devices have
two motors, one that's small and another that's large. For devices with a
single motor, such as mobile devices, only the large motor is implemented.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Large` | 0 | Large motor. |
| `Small` | 1 | Small motor. |
| `LeftTrigger` | 2 | Left trigger motor. |
| `RightTrigger` | 3 | Right trigger motor. |
| `LeftHand` | 4 | Left hand motor for VR devices. |
| `RightHand` | 5 | Right hand motor for VR devices. |