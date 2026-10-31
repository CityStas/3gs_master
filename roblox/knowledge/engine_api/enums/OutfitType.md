---
name: OutfitType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Categorizes a saved player outfit by its content type, used to filter or specify outfit type in AvatarEditorService methods."
---

# OutfitType

Categorizes a saved player outfit by its content type, used to filter or
specify outfit type in [AvatarEditorService](/docs/reference/engine/classes/AvatarEditorService.md) methods.

**Type:** enum

## Description

`OutfitType` is an enum used with [AvatarEditorService](/docs/reference/engine/classes/AvatarEditorService.md) to distinguish
saved player outfits by their content. It is accepted by
[AvatarEditorService:GetOutfitsAsync()](/docs/reference/engine/classes/AvatarEditorService.md) and
[AvatarEditorService:GetOutfits()](/docs/reference/engine/classes/AvatarEditorService.md) as a filter.

The most common values are [OutfitType.Avatar](/docs/reference/engine/enums/OutfitType.md) (a full-body outfit) and
[OutfitType.Makeup](/docs/reference/engine/enums/OutfitType.md) (a makeup-only configuration). Passing
[OutfitType.All](/docs/reference/engine/enums/OutfitType.md) to a query method returns outfits of every type with no
filtering applied.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `All` | 1 | Returns outfits of every type, with no filtering applied. |
| `Avatar` | 2 | A full-body avatar outfit. |
| `DynamicHead` | 3 | An outfit containing a dynamic head. |
| `Shoes` | 4 | An outfit consisting of a pair of shoes. |
| `Makeup` | 5 | An outfit consisting of makeup items applied to the avatar's face. |