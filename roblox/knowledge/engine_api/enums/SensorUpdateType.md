---
name: SensorUpdateType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls when a sensor recalculates its output properties."
---

# SensorUpdateType

Controls when a sensor recalculates its output properties.

**Type:** enum

## Description

Controls when a sensor recalculates its output properties. Assign this enum to
the `UpdateType` property on any [SensorBase](/docs/reference/engine/classes/SensorBase.md)‑derived instance
([ControllerSensor](/docs/reference/engine/classes/ControllerSensor.md), [FluidForceSensor](/docs/reference/engine/classes/FluidForceSensor.md), [AtmosphereSensor](/docs/reference/engine/classes/AtmosphereSensor.md))
to choose between automatic lazy evaluation and fully manual control.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `OnRead` | 0 | The sensor lazily recalculates its output the next time an output property is read and the output is marked dirty. |
| `Manual` | 1 | The sensor never automatically recalculates its output; scripts are responsible for driving output updates. |