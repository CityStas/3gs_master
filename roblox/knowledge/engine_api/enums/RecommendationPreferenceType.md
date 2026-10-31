---
name: RecommendationPreferenceType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies the type of preference action (follow, unfollow, mute, or unmute) passed to LogPreferenceEvent()."
---

# RecommendationPreferenceType

Identifies the type of preference action (follow, unfollow, mute, or unmute)
passed to
[LogPreferenceEvent()](/docs/reference/engine/classes/RecommendationService.md).

**Type:** enum

## Description

The type of preference signal logged via
[LogPreferenceEvent](/docs/reference/engine/classes/RecommendationService.md).
Preference signals capture follow, unfollow, mute, and unmute actions toward
another user, a universe, or a custom content tag, and are used by the
recommendation engine to personalize future results.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `AddFollow` | 0 | The user started following the target. |
| `RemoveFollow` | 1 | The user stopped following the target. |
| `AddMute` | 2 | The user muted the target. |
| `RemoveMute` | 3 | The user unmuted a previously muted target. |