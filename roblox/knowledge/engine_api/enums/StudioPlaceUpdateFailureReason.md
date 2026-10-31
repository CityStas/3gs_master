---
name: StudioPlaceUpdateFailureReason
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes why a place publish or update operation failed in Roblox Studio."
---

# StudioPlaceUpdateFailureReason

Describes why a place publish or update operation failed in Roblox Studio.

**Type:** enum

## Description

Describes why a place publish or update operation failed in Roblox Studio.
This enum is passed as the `reason` parameter of the `GamePublishFinished`
event when `success` is `false`.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Other` | 0 | The place publish or update failed for an unspecified or generic reason. |
| `TeamCreateConflict` | 1 | The place publish failed because a Team Create server currently holds a lock on the place. |