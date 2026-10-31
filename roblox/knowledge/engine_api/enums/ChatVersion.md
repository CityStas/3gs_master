---
name: ChatVersion
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines whether TextChatService should be fully enabled or to allow the legacy system."
---

# ChatVersion

Determines whether [TextChatService](/docs/reference/engine/classes/TextChatService.md) should be fully enabled or to allow
the legacy system.

**Type:** enum

## Description

Determines whether [TextChatService](/docs/reference/engine/classes/TextChatService.md) should be fully enabled or to allow
the legacy system.

[TextChatService.ChatVersion](/docs/reference/engine/classes/TextChatService.md) is not scriptable and must be set in
Studio.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `LegacyChatService` | 0 | Enables the legacy chat system. |
| `TextChatService` | 1 | Enables [TextChatService](/docs/reference/engine/classes/TextChatService.md) chat and prevents legacy chat system behavior. |