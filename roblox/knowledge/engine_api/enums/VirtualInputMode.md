---
name: VirtualInputMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the current operational state of a VirtualInputManager."
---

# VirtualInputMode

Describes the current operational state of a [VirtualInputManager](/docs/reference/engine/classes/VirtualInputManager.md).

**Type:** enum

## Description

Describes the current operational state of a [VirtualInputManager](/docs/reference/engine/classes/VirtualInputManager.md). The
service reports a value from this enum to indicate whether it is idle,
actively capturing input events, or replaying a previously captured sequence.
Transitions are driven by calls to `StartRecording()`, `StopRecording()`,
`StartPlaying()`, and `StopPlaying()`.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | The [VirtualInputManager](/docs/reference/engine/classes/VirtualInputManager.md) is idle and neither recording nor playing back input. |
| `Recording` | 1 | The [VirtualInputManager](/docs/reference/engine/classes/VirtualInputManager.md) is actively capturing input events into a sequence. |
| `Playing` | 2 | The [VirtualInputManager](/docs/reference/engine/classes/VirtualInputManager.md) is replaying a previously recorded input sequence. |