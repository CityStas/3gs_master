---
name: DebugBreakModeType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls when the debugger pauses on exceptions."
---

# DebugBreakModeType

Controls when the debugger pauses on exceptions.

**Type:** enum

## Description

Used with [ScriptDebuggerService:SetExceptionBreakMode()](/docs/reference/engine/classes/ScriptDebuggerService.md) to control
when the debugger pauses on exceptions. The mode applies to all
[DataModels](/docs/reference/engine/classes/DataModel.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Never` | 0 | Never break on exceptions. |
| `Always` | 1 | Break on all exceptions. |
| `Unhandled` | 2 | Break only on unhandled exceptions. |