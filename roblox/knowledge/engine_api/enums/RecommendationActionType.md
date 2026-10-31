---
name: RecommendationActionType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the type of action a user took on a recommended item, used when logging action events via RecommendationService:LogActionEvent()."
---

# RecommendationActionType

Describes the type of action a user took on a recommended item, used when
logging action events via [RecommendationService:LogActionEvent()](/docs/reference/engine/classes/RecommendationService.md).

**Type:** enum

## Description

Action a user performed on a recommended item. Pass as the first argument to
[RecommendationService:LogActionEvent()](/docs/reference/engine/classes/RecommendationService.md) to record interaction signals
used for personalization.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `AddReaction` | 0 | The user added a reaction to the item, such as a "like". |
| `RemoveReaction` | 1 | The user removed a reaction from the item. |
| `Share` | 2 | The user shared the item. |
| `Report` | 3 | The user created an abuse report of the item. |
| `Comment` | 4 | The user commented on the item. |
| `Play` | 5 | The user joined an experience through the item, or played a mini-game associated with the item. |
| `Purchase` | 6 | The user made a purchase from the item. |