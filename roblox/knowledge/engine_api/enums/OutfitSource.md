---
name: OutfitSource
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Filters which outfits are returned by AvatarEditorService:GetOutfitsAsync() based on how they were obtained."
---

# OutfitSource

Filters which outfits are returned by
[AvatarEditorService:GetOutfitsAsync()](/docs/reference/engine/classes/AvatarEditorService.md) based on how they were obtained.

**Type:** enum

## Description

Specifies whether [AvatarEditorService:GetOutfitsAsync()](/docs/reference/engine/classes/AvatarEditorService.md) should return
all of a user's outfits, only outfits the user created themselves, or only
outfits the user purchased. Pass this value as the `outfitSource` parameter of
[AvatarEditorService:GetOutfitsAsync()](/docs/reference/engine/classes/AvatarEditorService.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `All` | 1 | Return all outfits regardless of whether they were created or purchased. |
| `Created` | 2 | Return only outfits that the user created themselves (editable outfits). |
| `Purchased` | 3 | Return only outfits that the user purchased (non-editable outfits). |