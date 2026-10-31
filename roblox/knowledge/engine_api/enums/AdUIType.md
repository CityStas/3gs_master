---
name: AdUIType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the type of ad creative currently rendered by an AdGui."
---

# AdUIType

Describes the type of ad creative currently rendered by an [AdGui](/docs/reference/engine/classes/AdGui.md).

**Type:** enum

## Description

Describes the type of ad creative that an [AdGui](/docs/reference/engine/classes/AdGui.md) is currently rendering
on its surface. Managed by the engine based on the creative asset served to
the ad slot.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | The [AdGui](/docs/reference/engine/classes/AdGui.md) has no ad creative loaded and is not rendering ad content. |
| `Image` | 1 | The [AdGui](/docs/reference/engine/classes/AdGui.md) is rendering a static image ad creative. |
| `Video` | 2 | The [AdGui](/docs/reference/engine/classes/AdGui.md) is rendering a video ad creative. |