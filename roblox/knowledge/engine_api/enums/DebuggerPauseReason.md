---
name: DebuggerPauseReason
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Reason that the DataModel was paused."
---

# DebuggerPauseReason

Reason that the DataModel was paused.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | Pausing for a reason not covered by other values. |
| `Requested` | 1 | Pause was requested by user. |
| `Breakpoint` | 2 | Pausing on a user breakpoint. |
| `Exception` | 3 | Pausing on error hit in the code. |
| `SingleStep` | 4 | Pausing on an internal breakpoint set by debugger command: e.g. step over, step into, step out of. |
| `Entrypoint` | 5 | Pausing at the entry on the script. |