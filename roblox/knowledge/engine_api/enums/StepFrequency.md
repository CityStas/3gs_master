---
name: StepFrequency
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Enum used with RunService:BindToSimulation() to indicate the frequency at which the bound function is called."
---

# StepFrequency

Enum used with [RunService:BindToSimulation()](/docs/reference/engine/classes/RunService.md) to indicate the frequency
at which the bound function is called.

**Type:** enum

## Description

Enum used with [RunService:BindToSimulation()](/docs/reference/engine/classes/RunService.md) to indicate the frequency
at which the bound function is called during the simulation step.

The Roblox simulation pipeline runs at 60 Hz. Each `StepFrequency` value
divides that base rate so the bound callback fires at the requested cadence
and receives a `deltaTime` argument representing the simulation-time interval
represented by the invocation. Choosing a lower frequency reduces per-frame
overhead for logic that does not need to run every physics tick, such as
periodic state checks. Because these callbacks run on the simulation step and
can be replayed during client resimulation, avoid using them for actions that
must occur exactly once, such as network replication. The default frequency
for [RunService:BindToSimulation()](/docs/reference/engine/classes/RunService.md) is [StepFrequency.Hz30](/docs/reference/engine/enums/StepFrequency.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Hz60` | 0 | The bound function is called at 60 Hz. |
| `Hz30` | 1 | The bound function is called at 30 Hz. |
| `Hz15` | 2 | The bound function is called at 15 Hz. |
| `Hz10` | 3 | The bound function is called at 10 Hz. |
| `Hz5` | 4 | The bound function is called at 5 Hz. |
| `Hz1` | 5 | The bound function is called at 1 Hz. |