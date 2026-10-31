---
name: TextChatMessageStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates the status of a TextChatMessage."
---

# TextChatMessageStatus

Indicates the status of a [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md).

**Type:** enum

## Description

Indicates the status of a [TextChatMessage](/docs/reference/engine/classes/TextChatMessage.md). The
[TextChatMessage.Status](/docs/reference/engine/classes/TextChatMessage.md) property is set by
[TextChannel:SendAsync()](/docs/reference/engine/classes/TextChannel.md) to report the outcome of an attempted send. A
status of [TextChatMessageStatus.Success](/docs/reference/engine/enums/TextChatMessageStatus.md) means the message passed all
server-side checks; any other value identifies the reason the message was
blocked or has not yet completed delivery.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 1 | Generic failed status for any other [TextChannel:SendAsync()](/docs/reference/engine/classes/TextChannel.md) failures. |
| `Success` | 2 | Message has no issues. |
| `Sending` | 3 | Message is sending. |
| `TextFilterFailed` | 4 | Text filter failed to process the message. |
| `Floodchecked` | 5 | Message is from a user sending messages too frequently. |
| `InvalidPrivacySettings` | 6 | Message can't be sent because of the user's chat privacy settings. |
| `InvalidTextChannelPermissions` | 7 | Message's [TextSource](/docs/reference/engine/classes/TextSource.md) is either not in the intended [TextChannel](/docs/reference/engine/classes/TextChannel.md) or [TextSource.CanSend](/docs/reference/engine/classes/TextSource.md) is `false`. |
| `MessageTooLong` | 8 | Message is too long. |
| `ModerationTimeout` | 9 | Message can't be sent because the user has an active moderation timeout on chat. |