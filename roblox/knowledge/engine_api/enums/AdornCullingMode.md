---
name: AdornCullingMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Culling method used for adornments."
---

# AdornCullingMode

Culling method used for adornments.

**Type:** enum

## Description

Used by [HandleAdornment](/docs/reference/engine/classes/HandleAdornment.md) to determine how it is culled.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Automatic` | 0 | Automatically culls adornment based on distance. |
| `Never` | 1 | Never culls adornment. Adornment is always visible. |