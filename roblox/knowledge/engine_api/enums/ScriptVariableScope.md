---
name: ScriptVariableScope
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates the scope category of a variable returned by the debugger."
---

# ScriptVariableScope

Indicates the scope category of a variable returned by the debugger.

**Type:** enum

## Description

Used in [ScriptVariable](/docs/reference/engine/datatypes/ScriptVariable.md) to classify the scope of a variable returned
by [ScriptDebuggerService:GetRootVariables()](/docs/reference/engine/classes/ScriptDebuggerService.md) or
[ScriptDebuggerService:GetVariables()](/docs/reference/engine/classes/ScriptDebuggerService.md). Children of a variable inherit
the parent's scope.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Local` | 0 | A local variable declared in the current function scope. |
| `Upvalue` | 1 | A variable captured from an enclosing function scope. |
| `Global` | 2 | A global variable. |