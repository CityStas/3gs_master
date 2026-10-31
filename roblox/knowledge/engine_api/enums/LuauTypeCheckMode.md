---
name: LuauTypeCheckMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The Luau type checking mode for scripts in the experience."
---

# LuauTypeCheckMode

The Luau type checking mode for scripts in the experience.

**Type:** enum

## Description

Determines how strictly the Luau type checker analyzes scripts in the
experience. This enum is used by [Workspace.LuauTypeCheckMode](/docs/reference/engine/classes/Workspace.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Uses the engine-default type checking mode. |
| `NoCheck` | 1 | Scripts are not type-checked. |
| `Nonstrict` | 2 | Scripts are type-checked in nonstrict mode. |
| `Strict` | 3 | Scripts are type-checked in strict mode. |