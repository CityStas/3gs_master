---
name: DebuggerResumeType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies how the debugger should resume execution after a pause."
---

# DebuggerResumeType

Specifies how the debugger should resume execution after a pause.

**Type:** enum

## Description

Returned from the [ScriptDebuggerService.OnStopped](/docs/reference/engine/classes/ScriptDebuggerService.md) callback (via
[ScriptResumeAction](/docs/reference/engine/datatypes/ScriptResumeAction.md)) to control how execution resumes after a
debugger pause.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `StepInto` | 0 | Step into the next function call on the specified thread. |
| `StepOut` | 1 | Step out of the current function on the specified thread. |
| `StepOver` | 2 | Step over the current line on the specified thread. |
| `Resume` | 3 | Resume execution normally without stepping. |