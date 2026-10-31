---
name: ActuatorType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The active physics component of the constraint."
---

# ActuatorType

The active physics component of the constraint.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | The motor and servo components are both disabled. |
| `Motor` | 1 | The motor component is enabled. Motor properties are active and the actuator will apply continuous force. |
| `Servo` | 2 | The servo component is enabled. Servo properties are active and the actuator will apply force to approach the servo's target. |