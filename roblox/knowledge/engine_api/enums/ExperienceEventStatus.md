---
name: ExperienceEventStatus
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the lifecycle state of a Roblox experience event as returned by SocialService."
---

# ExperienceEventStatus

Describes the lifecycle state of a Roblox experience event as returned by
[SocialService](/docs/reference/engine/classes/SocialService.md).

**Type:** enum

## Description

Describes the lifecycle state of a Roblox experience event.
[SocialService:GetExperienceEventAsync()](/docs/reference/engine/classes/SocialService.md) and
[SocialService:GetUpcomingExperienceEventsAsync()](/docs/reference/engine/classes/SocialService.md) return event
dictionaries whose `Status` field is a value of this enum, derived from the
`eventStatus` field in the virtual-events API response.
`GetUpcomingExperienceEventsAsync()` filters out events whose status is
`Cancelled`, `Moderated`, or `Unpublished`, so only `Active` events appear in
that list.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Active` | 0 | The event is currently published and available. |
| `Cancelled` | 1 | The event has been cancelled and will not occur. |
| `Moderated` | 2 | The event has been removed by moderation. |
| `Unpublished` | 3 | The event has been unpublished by the creator. |
| `Unknown` | 4 | The event status could not be determined. |