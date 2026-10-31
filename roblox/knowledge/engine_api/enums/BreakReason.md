---
name: BreakReason
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Reason for the breakpoint hit."
---

# BreakReason

Reason for the breakpoint hit.

**Type:** enum

## Description

Value for the reason the [ScriptDebugger.EncounteredBreak](/docs/reference/engine/classes/ScriptDebugger.md) signal fired.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Other` | 0 | Pausing for a reason not covered by other values, for example if the user hit "Pause" button. |
| `Error` | 1 | Pausing on error hit in the code. |
| `SpecialBreakpoint` | 2 | Pausing on an internal breakpoint set by debugger command: e.g. step over, step into, step out of. |
| `UserBreakpoint` | 3 | Pausing on a user breakpoint. |