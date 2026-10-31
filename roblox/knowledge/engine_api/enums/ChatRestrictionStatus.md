---
name: ChatRestrictionStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the chat restriction status that a third-party platform reports for a user."
---

# ChatRestrictionStatus

Describes the chat restriction status that a third-party platform reports for
a user.

**Type:** enum

## Description

The `ChatRestrictionStatus` enum represents whether a user is permitted to
participate in text or voice chat as determined by a third-party platform such
as Xbox or PlayStation. Platform-level restrictions reflect parental controls,
age restrictions, or account-level communication settings that the platform
enforces independently of Roblox. This status is surfaced through properties
such as [Player.ThirdPartyTextChatRestrictionStatus](/docs/reference/engine/classes/Player.md),
`FriendCommunicationRestrictionStatus`, and `VoiceChatRestrictionStatus`, all
of which default to [ChatRestrictionStatus.Unknown](/docs/reference/engine/enums/ChatRestrictionStatus.md) until the platform
reports a definitive value.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Unknown` | 0 | The platform's chat restriction status for the user has not yet been determined; this is the default value for all ChatRestrictionStatus properties. |
| `NotRestricted` | 1 | The third-party platform has confirmed the user has no chat restrictions in effect. |
| `Restricted` | 2 | The third-party platform has reported the user is restricted from chat, typically due to parental controls or platform communication settings. |