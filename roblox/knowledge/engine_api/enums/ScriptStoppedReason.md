---
name: ScriptStoppedReason
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes why the debugger paused execution."
---

# ScriptStoppedReason

Describes why the debugger paused execution.

**Type:** enum

## Description

Passed in the [ScriptDebugStopped](/docs/reference/engine/datatypes/ScriptDebugStopped.md) payload to the
[ScriptDebuggerService.OnStopped](/docs/reference/engine/classes/ScriptDebuggerService.md) callback, indicating what triggered
the pause.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Breakpoint` | 0 | Execution stopped because a user-defined breakpoint was hit. |
| `Exception` | 1 | Execution stopped because an exception was thrown (governed by the current [DebugBreakModeType](/docs/reference/engine/enums/DebugBreakModeType.md)). |
| `Pause` | 2 | Execution stopped because [ScriptDebuggerService:Pause()](/docs/reference/engine/classes/ScriptDebuggerService.md) was called. |
| `Step` | 3 | Execution stopped after completing a step operation. |
| `Entry` | 4 | Execution stopped at a script's entry point. |