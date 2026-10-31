---
name: RenderingCacheOptimizationMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls rendering cache optimization behavior."
---

# RenderingCacheOptimizationMode

Controls rendering cache optimization behavior.

**Type:** enum

## Description

Determines whether the renderer caches per-object rendering state to avoid
redundant per-frame work. This enum is used by
[Workspace.RenderingCacheOptimizations](/docs/reference/engine/classes/Workspace.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Uses the engine-default rendering cache state. |
| `Disabled` | 1 | Rendering cache optimizations are disabled. |
| `Enabled` | 2 | Rendering cache optimizations are enabled. |