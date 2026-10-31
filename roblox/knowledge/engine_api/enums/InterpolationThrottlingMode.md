---
name: InterpolationThrottlingMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether the engine reduces the physics interpolation update rate for distant assemblies when the client is under load. Used by the deprecated Workspace.InterpolationThrottling property."
---

# InterpolationThrottlingMode

Controls whether the engine reduces the physics interpolation update rate for
distant assemblies when the client is under load. Used by the deprecated
[Workspace.InterpolationThrottling](/docs/reference/engine/classes/Workspace.md) property.

**Type:** enum

## Description

Controls whether the engine reduces the physics interpolation update rate for
distant assemblies when the client is under load. This enum is consumed by the
deprecated [Workspace.InterpolationThrottling](/docs/reference/engine/classes/Workspace.md) property, which is no
longer exposed in Studio or recommended for use in new experiences.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | The engine automatically throttles physics interpolation for distant assemblies when client frame time is high. |
| `Disabled` | 1 | Physics interpolation throttling is unconditionally disabled; all assemblies interpolate at the full rate regardless of client load. |
| `Enabled` | 2 | Physics interpolation throttling is unconditionally enabled; distant assemblies have their interpolation update rate reduced even when the client is not under load. |