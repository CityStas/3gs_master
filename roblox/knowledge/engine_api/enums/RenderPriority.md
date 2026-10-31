---
name: RenderPriority
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "A list of standard reserved values in BindToRenderStep."
---

# RenderPriority

A list of standard reserved values in BindToRenderStep.

**Type:** enum

## Description

A list of standard reserved values in BindToRenderStep.

See [RunService:BindToRenderStep()](/docs/reference/engine/classes/RunService.md) for the proper usage, as the enum
itself isn't used.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `First` | 0 | The lowest reserved priority level; callbacks run before all other standard priorities. |
| `Input` | 100 | Runs after `First`; intended for input-processing callbacks. |
| `Camera` | 200 | Runs after `Input`; intended for camera-update callbacks. |
| `Character` | 300 | Runs after `Camera`; intended for character-response callbacks. |
| `Last` | 2000 | The highest reserved priority level; callbacks run after all other standard priorities. |