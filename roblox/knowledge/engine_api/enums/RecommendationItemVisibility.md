---
name: RecommendationItemVisibility
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls whether a registered recommendation item is publicly discoverable or restricted to private access."
---

# RecommendationItemVisibility

Controls whether a registered recommendation item is publicly discoverable or
restricted to private access.

**Type:** enum

## Description

Controls whether a recommendation item registered via
[RecommendationService:RegisterItemAsync()](/docs/reference/engine/classes/RecommendationService.md) or updated via
[RecommendationService:UpdateItemAsync()](/docs/reference/engine/classes/RecommendationService.md) is publicly discoverable by
the recommendation system or kept private. Pass the desired value in the
`Visibility` field of the request dictionary.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Private` | 0 | The recommendation item is not surfaced to other players by the recommendation system. |
| `Public` | 1 | The recommendation item is discoverable and may be surfaced to other players by the recommendation system. |