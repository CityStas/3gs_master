---
name: DebuggerExceptionBreakMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls when the Luau debugger pauses script execution in response to a runtime exception."
---

# DebuggerExceptionBreakMode

Controls when the Luau debugger pauses script execution in response to a
runtime exception.

**Type:** enum

## Description

Controls when the Luau debugger pauses script execution in response to a
runtime exception. This enum is used as the `breakMode` argument to
`DebuggerConnection:SetExceptionBreakMode()`.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Never` | 0 | The debugger never pauses due to a runtime exception; execution continues normally regardless of whether the exception is caught or uncaught. |
| `Always` | 1 | The debugger pauses on every runtime exception, including those caught by `pcall` or `xpcall`. |
| `Unhandled` | 2 | The debugger pauses only on runtime exceptions that propagate without being caught by `pcall` or `xpcall`. |