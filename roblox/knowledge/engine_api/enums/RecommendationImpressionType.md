---
name: RecommendationImpressionType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Specifies the outcome of rendering a recommended item, passed to RecommendationService:LogImpressionEvent() to indicate whether the item was shown to the user."
---

# RecommendationImpressionType

Specifies the outcome of rendering a recommended item, passed to
[RecommendationService:LogImpressionEvent()](/docs/reference/engine/classes/RecommendationService.md) to indicate whether the
item was shown to the user.

**Type:** enum

## Description

`RecommendationImpressionType` is used as the `impressionType` argument to
[RecommendationService:LogImpressionEvent()](/docs/reference/engine/classes/RecommendationService.md). It tells the Roblox
recommendation backend whether a given item was successfully rendered on the
client ([RecommendationImpressionType.View](/docs/reference/engine/enums/RecommendationImpressionType.md)) or whether a rendering error
prevented the user from seeing it
([RecommendationImpressionType.NotViewable](/docs/reference/engine/enums/RecommendationImpressionType.md)). The backend uses
`NotViewable` as a negative signal when ranking future recommendations.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `View` | 0 | A complete view of the item. |
| `NotViewable` | 1 | The item has failed to render. |