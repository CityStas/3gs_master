---
name: TickCountSampleMethod
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls the precision and performance trade-off used when sampling the current time."
---

# TickCountSampleMethod

Controls the precision and performance trade-off used when sampling the
current time.

**Type:** enum

## Description

Controls the precision and performance trade-off used when sampling the
current time via [DebugSettings.TickCountPreciseOverride](/docs/reference/engine/classes/DebugSettings.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Fast` | 0 | Compute time using a faster, but less precise method. |
| `Benchmark` | 1 | Dynamically decide between using `Fast` and `Precise` depending on the value of `DebugSettings.TickCountPreciseOverride`. |
| `Precise` | 2 | Compute time using a precise method. |