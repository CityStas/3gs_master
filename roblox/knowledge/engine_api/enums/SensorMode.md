---
name: SensorMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies whether a ControllerPartSensor targets floor or ladder geometry, and which detection algorithm to use."
---

# SensorMode

Specifies whether a [ControllerPartSensor](/docs/reference/engine/classes/ControllerPartSensor.md) targets floor or ladder
geometry, and which detection algorithm to use.

**Type:** enum

## Description

The [SensorMode](/docs/reference/engine/enums/SensorMode.md) enum controls both the type of geometry a
[ControllerPartSensor](/docs/reference/engine/classes/ControllerPartSensor.md) targets (floor surfaces or ladder rungs) and the
detection algorithm it applies. [SensorMode.Floor](/docs/reference/engine/enums/SensorMode.md) and
[SensorMode.Ladder](/docs/reference/engine/enums/SensorMode.md) use the current sensing algorithms, while
[SensorMode.ClassicFloor](/docs/reference/engine/enums/SensorMode.md) and [SensorMode.ClassicLadder](/docs/reference/engine/enums/SensorMode.md) preserve
legacy behavior. The default value of [ControllerPartSensor.SensorMode](/docs/reference/engine/classes/ControllerPartSensor.md)
is [SensorMode.Floor](/docs/reference/engine/enums/SensorMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Floor` | 0 | Detects floor surfaces below the part using the modern detection algorithm; the default value of [ControllerPartSensor.SensorMode](/docs/reference/engine/classes/ControllerPartSensor.md). |
| `Ladder` | 1 | Detects ladder surfaces adjacent to the part using the modern piercing-based detection algorithm. |
| `ClassicFloor` | 2 | Detects floor surfaces below the part using the legacy raycast-based algorithm. |
| `ClassicLadder` | 3 | Detects ladder surfaces adjacent to the part using the legacy ladder detection algorithm. |