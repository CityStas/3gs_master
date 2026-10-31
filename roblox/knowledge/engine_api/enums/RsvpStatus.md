---
name: RsvpStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates a player's RSVP response to a Roblox experience event."
---

# RsvpStatus

Indicates a player's RSVP response to a Roblox experience event.

**Type:** enum

## Description

Indicates a player's RSVP response to a Roblox experience event.
[SocialService:GetEventRsvpStatusAsync()](/docs/reference/engine/classes/SocialService.md) returns a value of this enum
to reflect whether a player has responded to an event invitation, and
`PromptRsvpToEventCompleted` passes both the new and previous status as
`RsvpStatus` values when a player finishes interacting with the RSVP prompt.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | The player has not yet responded to the event invitation; this is the default RSVP state. |
| `Going` | 1 | The player has accepted the event invitation and confirmed they are going. |
| `NotGoing` | 2 | The player has declined the event invitation and indicated they are not going. |