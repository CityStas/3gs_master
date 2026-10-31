---
name: BreakpointRemoveReason
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Reason that a breakpoint was removed."
---

# BreakpointRemoveReason

Reason that a breakpoint was removed.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Requested` | 0 | Breakpoint removal was requested by user or a command. |
| `ScriptChanged` | 1 | Script that contained the breakpoint has changed. |
| `ScriptRemoved` | 2 | Script that contained the breakpoint was removed. |