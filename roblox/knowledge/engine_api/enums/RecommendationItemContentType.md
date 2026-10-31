---
name: RecommendationItemContentType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the content type of an item registered with RecommendationService."
---

# RecommendationItemContentType

Describes the content type of an item registered with
[RecommendationService](/docs/reference/engine/classes/RecommendationService.md).

**Type:** enum

## Description

This enum describes the content type of the recommendation item. It is
designed to be generic.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Static` | 0 | The item is static, such as an image. |
| `Dynamic` | 1 | The item is dynamic; for example, it is a video. |
| `Interactive` | 2 | The item is interactive, such as a 3D model or a mini-game. |