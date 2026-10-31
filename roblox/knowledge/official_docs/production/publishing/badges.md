---
title: "Badges"
url: /docs/en-us/production/publishing/badges
last_updated: 2026-10-30T19:55:50Z
description: "Badges are a special award you can gift users when they meet a goal within your game."
---

# Badges

A **badge** is a special award you can gift players when they meet a goal within your game, such as completing a difficult objective or playing for a certain amount of time. As soon as a player receives a badge, it displays within the **Badges** category of their inventory.

![Example badges in a player's inventory](../../assets/publishing/badges/Badges-Inventory.png)_Example badges in a player's inventory_

## Create badges

You can create up to 5 badges for free in a 24‑hour period (GMT) for each game you own. If you want to create more within the 24‑hour period, each additional badge costs 100 Robux.

To create a badge:

1. Navigate to the [Creator Dashboard](https://create.roblox.com/dashboard/creations).
2. Hover over a game's thumbnail, click the **⋯** button, and select **Create Badge**.
3. On the create page, click the **Upload Image** button and then select/confirm the image you want to use as the badge's icon. When creating an image to use for a badge, consider the following:
  - Use a template of **512×512 pixels**.
  - The upload process trims and crops the badge image into a circular icon, so avoid putting important details outside of the circular boundaries.![Good circular trimming](../../assets/publishing/badges/Circular-Trimming-Good.png)_
    > **Success:** Main content included_![Bad circular trimming](../../assets/publishing/badges/Circular-Trimming-Bad.png)_
    > **Error:** Text content cropped_
4. Complete the following fields:
  - **Name** — A title for the badge.
  - **Description** — A description of what the player can do to earn the badge.
  - **Badge is Enabled** — Whether or not the badge will be enabled when it is created. Disabled badges are not shown under the **Badges** section of the game's main page and cannot be earned by players.
5. Click the **Create Badge** button. The new badge displays within the **Engagement** ⟩ **Badges** section on the [Creator Dashboard](https://create.roblox.com/dashboard/creations). If the new badge is enabled, it will also be shown under the **Badges** section of the game's main page._Badge on game's main page_

## Reorder badges

When a badge is first created, it is placed at the end of the badge list. You can reorder up to 50 badges at once using the drag‑and‑drop interface.

To reorder badges:

1. Navigate to the associated game.
2. In the side panel under the **Engagement** header, navigate to the **Badges** page.
3. Select **Reorder** to navigate to the reordering page.![Badge reorder button](../../assets/publishing/badges/Reorder-Button.png)
4. On the reordering page, drag and drop badges into their preferred order.![Badge drag-and-drop to reorder](../../assets/publishing/badges/Reordering.png)
5. Select **Save** to save this order. The specified order should now appear on the game details page.

## Script badges

Common badge scripting workflows include [awarding badges](#award-badges), checking if a player has previously [earned](#check-earned-badges) a badge in your game, and [getting badge information](#get-badge-info).

### Locate badge IDs

A badge's ID is its unique identifier. You'll need this ID when implementing workflows such as [awarding the badge](#award-badges) to a player.

1. On the [Creator Dashboard](https://create.roblox.com/dashboard/creations), navigate to the associated game's **Badges** section under **Engagement**.
2. Hover over a badge's thumbnail, click the **⋯** button, and select **Copy Asset ID** from the context menu.

### Award badges

You can award badges to players throughout your game by calling the `Class.BadgeService:AwardBadgeAsync()` method in a server-side `Class.Script`. `Class.BadgeService:GetBadgeInfoAsync()` returns properties of the badge, including `IsEnabled` which confirms whether or not the badge can be awarded to a player. You can enable or disable a badge from the **Configure Badge** form on the [Creator Dashboard](https://create.roblox.com/dashboard/creations).

The following is an example of a safe function for awarding badges to players.

```lua
local BadgeService = game:GetService("BadgeService")

local function awardBadge(player, badgeId)
	-- Fetch badge information
	local success, badgeInfo = pcall(function()
		return BadgeService:GetBadgeInfoAsync(badgeId)
	end)

	if success then
		-- Confirm that badge can be awarded
		if badgeInfo.IsEnabled then
			-- Award badge
			local awarded, errorMessage = pcall(BadgeService.AwardBadgeAsync, BadgeService, player.UserId, badgeId)
			if not awarded then
				warn("Error while awarding badge:", errorMessage)
			end
		end
	else
		warn("Error while fetching badge info: " .. badgeInfo)
	end
end
```

### Check earned badges

The following script checks when any player enters the game, then uses the `Class.BadgeService:UserHasBadgeAsync()` method to verify if that player owns the badge with the [matching ID](#locate-badge-ids) set in the variable `BADGE_ID`. You can also verify badge ownership in batches using the `Class.BadgeService:GetUserBadgesAsync()` method.

```lua
local BadgeService = game:GetService("BadgeService")
local Players = game:GetService("Players")

local BADGE_ID = 00000000  -- Change this to your badge ID

local function onPlayerAdded(player)
  -- Check if the player has the badge
	local success, hasBadge = pcall(BadgeService.UserHasBadgeAsync, BadgeService, player.UserId, BADGE_ID)

  -- If there's an error, issue a warning and exit the function
	if not success then
		warn("Error while checking if player has badge")
		return
	end

	if hasBadge then
		-- Handle player's badge ownership as needed
	end
end

-- Connect "PlayerAdded" events to the "onPlayerAdded()" function
Players.PlayerAdded:Connect(onPlayerAdded)
```

### Get badge info

To get information about a badge, such as its description or icon asset ID, call the `Class.BadgeService:GetBadgeInfoAsync()` method with a [badge ID](#locate-badge-ids). For example:

```lua
local BadgeService = game:GetService("BadgeService")

local BADGE_ID = 00000000  -- Change this to your badge ID

-- Fetch badge information
local success, result = pcall(BadgeService.GetBadgeInfoAsync, BadgeService, BADGE_ID)

-- Output the information
if success then
	print("Badge:", result.Name)
	print("Enabled:", result.IsEnabled)
	print("Description:", result.Description)
	print("Icon:", "rbxassetid://" .. result.IconImageId)
else
	warn("Error while fetching badge info:", result)
end
```
