---
name: RecommendationPreferenceTargetType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies the kind of entity that a preference signal targets when logged via LogPreferenceEvent()."
---

# RecommendationPreferenceTargetType

Identifies the kind of entity that a preference signal targets when logged via
[LogPreferenceEvent()](/docs/reference/engine/classes/RecommendationService.md).

**Type:** enum

## Description

The kind of entity a preference signal targets when logged via
[LogPreferenceEvent](/docs/reference/engine/classes/RecommendationService.md).
Determines how the `targetId` parameter is interpreted.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `User` | 0 | The target is another Roblox user. The `targetId` is the user key. |
| `Universe` | 1 | The target is a universe. The `targetId` is the universe ID as a string. |
| `CustomTag` | 2 | The target is a custom content tag. The `targetId` is the tag string. |