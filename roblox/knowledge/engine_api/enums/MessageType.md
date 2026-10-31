---
name: MessageType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Message category and severity level."
---

# MessageType

Message category and severity level.

**Type:** enum

## Description

A message can be a simple diagnostic or a sign of a system instability or
failure. The channel that the message appears in indicates its severity. The
MessageType indicates which channel the message displays in.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `MessageOutput` | 0 | The message is from the standard output channel. |
| `MessageInfo` | 1 | The message is from the information channel. |
| `MessageWarning` | 2 | The message is from the warning channel. |
| `MessageError` | 3 | The message is from the error channel. |