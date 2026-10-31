---
name: GroupMembershipStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Defines the possible outcomes of the GroupService:PromptJoinAsync() method."
---

# GroupMembershipStatus

Defines the possible outcomes of the [GroupService:PromptJoinAsync()](/docs/reference/engine/classes/GroupService.md)
method.

**Type:** enum

## Description

`GroupMembershipStatus` is an enumeration that represents the result of a
player's interaction with the [GroupService:PromptJoinAsync()](/docs/reference/engine/classes/GroupService.md) method.
It conveys the player's group membership status after the prompt.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | The player chose not to join, cancelled the prompt, or was not eligible to join the group. |
| `Joined` | 1 | The player successfully joined the group during the prompt. |
| `JoinRequestPending` | 2 | The player submitted a request to join the group, or already had a pending join request prior to prompting. |
| `AlreadyMember` | 3 | The player was already a member of the group. |