---
name: SignalBehavior
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines when the engine resumes event handlers."
---

# SignalBehavior

Determines when the engine resumes event handlers.

**Type:** enum

## Description

Determines when the engine resumes event handlers. At some future point, the
default mode will be `Deferred` but opt-out will still be possible through use
of `Immediate`.

For more information, see
[Deferred Events](/docs/en-us/scripting/events/deferred.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Default` | 0 | The default behavior; currently equivalent to `Immediate` but this will eventually change to `Deferred`. |
| `Immediate` | 1 | Event handlers are resumed immediately when the event occurs. |
| `Deferred` | 2 | All events are deferred and their handlers resumed at specific resumptions points each frame. |
| `AncestryDeferred` | 3 | Equivalent to `Deferred` but only for events triggered by changes in ancestry. |