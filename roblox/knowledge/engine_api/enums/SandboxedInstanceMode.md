---
name: SandboxedInstanceMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether sandboxed instance mode (script capabilities) is enabled."
---

# SandboxedInstanceMode

Controls whether sandboxed instance mode (script capabilities) is enabled.

**Type:** enum

## Description

Determines whether sandboxed instance mode, which lets you use script
capabilities, is active. This enum is used by
[Workspace.SandboxedInstanceMode](/docs/reference/engine/classes/Workspace.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | Uses the engine-default sandboxed instance state. |
| `Experimental` | 1 | Sandboxed instance mode is enabled. |