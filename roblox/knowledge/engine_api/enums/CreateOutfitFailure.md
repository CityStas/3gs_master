---
name: CreateOutfitFailure
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Indicates why a AvatarEditorService:PromptCreateOutfit() call failed."
---

# CreateOutfitFailure

Indicates why a [AvatarEditorService:PromptCreateOutfit()](/docs/reference/engine/classes/AvatarEditorService.md) call failed.

**Type:** enum

## Description

Indicates the reason a [AvatarEditorService:PromptCreateOutfit()](/docs/reference/engine/classes/AvatarEditorService.md) call
did not successfully create an outfit. The failure code is surfaced through
the [AvatarEditorService.PromptCreateOutfitCompleted](/docs/reference/engine/classes/AvatarEditorService.md) event alongside an
[AvatarPromptResult.Failed](/docs/reference/engine/enums/AvatarPromptResult.md) result.

## Code Samples

**Handling Outfit Creation Results**

The example below listens for the result of a PromptCreateOutfit call and
branches on the outcome, using the Enum.CreateOutfitFailure value to explain
why creation failed.

```lua
local AvatarEditorService = game:GetService("AvatarEditorService")

AvatarEditorService.PromptCreateOutfitCompleted:Connect(function(result, failureType)
	if result == Enum.AvatarPromptResult.Success then
		-- Outfit was created
	elseif result == Enum.AvatarPromptResult.PermissionDenied then
		-- User declined the prompt; ignore failureType
	else -- Enum.AvatarPromptResult.Failed
		if failureType == Enum.CreateOutfitFailure.OutfitLimitReached then
			-- Tell the user they hit the outfit cap
		elseif failureType == Enum.CreateOutfitFailure.InvalidName then
			-- Tell the user to pick a different name
		else -- Enum.CreateOutfitFailure.Other
			-- Generic failure; retry or show a generic error
		end
	end
end)
```

## Items

| Name | Value | Description |
|------|-------|-------------|
| `InvalidName` | 1 | The outfit name provided by the player was rejected as invalid. |
| `OutfitLimitReached` | 2 | The player has reached the maximum number of saved outfits. |
| `Other` | 3 | The outfit creation failed for an unspecified or unrecognized reason. |