---
title: "Missions package"
url: /docs/en-us/resources/feature-packages/missions
last_updated: 2026-10-30T19:55:55Z
description: "Learn about the missions feature package."
---

# Missions package

> **Warning:** This feature package is in beta.

The **Missions** feature package offers out-of-the-box functionality to create missions that players can complete to achieve rewards and progress in your game. All missions must have an ID, category, and a list of tasks that players must complete to finish the mission. However, the tasks list can be empty, allowing the mission's rewards to be claimed immediately.

Using the package's customization options, you can personalize all missions to meet your unique gameplay requirements, such as:

- Creating missions that [onboard](/docs/en-us/production/game-design/onboarding.md) new players into your game and improve [D1 retention](/docs/en-us/production/game-design/analytics-essentials.md#retention-metrics).
- Targetting [D7 and D30 retention](/docs/en-us/production/game-design/analytics-essentials.md#retention-metrics) by adding mid- to long-term goals and a sense of progression.
- Increasing [engagement](/docs/en-us/production/game-design/analytics-essentials.md#engagement-metrics) by surfacing the various systems in your game and rewarding players for interacting with them.

> **Info:** For information on how to provide players with fresh goals and incentives so that they're motivated to play longer and increase their engagement, see [Introduction to Quest Design](/docs/en-us/production/game-design/introduction-to-quest-design.md).
## Get package

The **Creator Store** is a tab of the **Toolbox** that you can use to find all assets that are made by Roblox and the Roblox community for use within your projects, including model, image, mesh, audio, plugin, video, and font assets. You can use the Creator Store to add one or more assets directly into an open game, including feature packages!

Every feature package requires the **Core** feature package to function properly. Once the **Core** and **Missions** feature package assets are within your inventory, you can reuse them in any project on the platform.

To get the packages from your inventory into your game:

1. Add the **Core** and **Missions** to your inventory within Studio by clicking the **Add to Inventory** link in the following set of components. #### Core Feature Package The Core feature package offers shared data store logic for all feature packages. #### Missions Feature Package The Missions Feature Package offers functionality to create missions that players can complete to achieve rewards and progress in your game.
2. From Studio's **Window** menu or **Home** tab toolbar, open the [Toolbox](/docs/en-us/projects/assets/toolbox.md).
3. In the **Toolbox** window, click the **Inventory** tab. The **My Models** sort displays.![Studio's Toolbox window with the Inventory tab highlighted.](../../assets/studio/toolbox/Inventory-Tab.png)
4. Click the **Feature Package Core** tile, then the **Missions Feature Package** tile. Both package folders display in the **Explorer** window.
5. Drag the package folders into `Class.ReplicatedStorage`.

## Define missions

Each completeable mission includes a set of tasks that must be finished to complete the mission, configuration options, and optional display metadata, all of which can be defined within `ReplicatedStorage.Missions.Configs.Missions`, with types exported from the `Types` script in the same folder.

### Required fields

The following fields are required for each mission.

| Name | Type | Description |
| --- | --- | --- |
| `missionId` | `string` | The main Missions table key. All missions are identified by their own unique string. |
| `categoryId` | `string` | Missions must belong to a category, and are grouped by category in the UI. |
| `tasks` | `table` | A list of tasks that the player must finish to complete the mission. |

### Unlock conditions

By default, missions are unlocked for players automatically and can be completed exactly once. However, you can use the following **optional** configuration options to alter this behavior.

| Name | Type | Description |
| --- | --- | --- |
| `prerequisites` | `table` | A list of other missionIds that must be completed before the mission can be unlocked. |
| `manualOnly` | `bool` | Disables the automatic unlocking of the mission. Instead, a function must be called to unlock the mission. Any other unlock conditions must still be met as well. |
| `availableAfterUtc` | `bool` | The mission cannot be unlocked before the specified time in UTC. |
| `availableBeforeUtc` | `bool` | The mission cannot be unlocked after the specified time in UTC. If it is unlocked but not completed before this time, the mission will be failed. |
| `repeatable` | `bool` | The mission becomes unlocked again after it is completed. |
| `repeatLimit` | `number` | If the mission is repeatable, it cannot be repeated more than this many times. |
| `repeatCooldownSeconds` | `number` | If the mission is repeatable, there is a delay before it becomes unlocked. |
| `expireSeconds` | `number` | If the mission is unlocked and not completed within the specified number of seconds, then it will fail instead. |
| `expireCountOffline` | `bool` | If the mission has `expireSeconds` and `expireCountOffline` is set to true, time while the player is not actually in the game will count toward mission expiration. |

### Metadata

Missions have metadata that specifies how they will be displayed in the Missions user interface. You can use the following **optional** fields to customize its metadata.

| Name | Type | Description |
| --- | --- | --- |
| `displayName` | `string` | A name to display for the mission in the user interface instead of the `missionId`. |
| `description` | `string` | A longer block of text that provides additional information or context about the mission. |
| `visibleAfterComplete` | `bool` | If set to true, the mission will show up in the list of missions even after it is completed but marked as completed. |
| `visibleAfterFailed` | `bool` | If set to true, the mission will show up in the list of missions even after it is failed but marked as failed. |
| `visibleBeforeUnlocked` | `bool` | If set to true, the mission will be visible but locked in the list of missions before being available for completion. |
| `invisibleWhileActive` | `bool` | If set to true, the mission will be invisible even while actively in progress. |
| `rewards` | `table` | A list of reward display information.<br><ul><li>`assetID` (`number`) - The image ID that displays in the missions UI under the rewards for a quest. This is required if a reward is present.</li><li>`displayName` (`string`) - The name that displays in the missions UI under the icon.</li></ul> |

## Define tasks

Each mission can have zero or more tasks. If a mission has zero tasks, it is claimable immediately after it's unlocked; if a mission has one or more tasks, once the tasks are complete, the player can collect any rewards associated with the mission. Each task has a `taskId`, which is the key associated with the task for a given mission.

Tasks come in two types:

- **Timed Tasks** - Lets you start and stop the task at different points in time. A certain amount of time must pass while the task's timer is running, then the task is complete.
- **Count Tasks** - Lets you add to or set the task's progress. When the progress reaches a set value, the task is complete.

Both task types share the following fields:

| Name | Type | Description |
| --- | --- | --- |
| `taskType` | `string` | Specifies if the task type is count or timed. |
| `counter` | `object` | (Optional) The counter this task tracks. Counters are player-specific persistent storage for a number or a timer. Multiple tasks can track a single counter; for example, if more than one task tracks how many coins a player has collected, then they all can share the same “coins” counter. These tasks can independently track new coins collected, starting from zero, or continue counting from the counter value (all coins already collected).<br><ul><li>`counterId` (`string`) - The ID of the counter to be tracked. Use this ID to get or set the value of the counter.</li><li>`continueFromCounter` (Optional `bool`) - If set to true, the task progress will directly match the value of the counter rather than the amount it has increased.</li></ul> |
| `metadata` | `object` | (Optional) Information about how the task displays in the UI.<br><ul><li>`displayName` (`string`) - Name of the task, used when shown in the UI.</li><li>`numericType` (Optional `string`) - how the progress number in the task should be displayed.<ul><li>Fraction, ex. 5/10 or 5k/50k</li><li>Percentage, ex. 50% or 10%</li><li>LongFraction, ex. 5/10 or 5000/50000</li><li>Boolean, ex. Incomplete</li></ul></li></ul> |
| `callToAction` | `object` | (Optional) A button that triggers a callback function.<br><ul><li>`callback` (`function`) - Function triggered by the `callToAction` button.</li><li>`buttonText` (`string`) - The text that is displayed in the button UI.</li></ul> |

### Count tasks fields

Count tasks have a required value. When the task progress meets this amount, the task is complete.

| Name | Type | Description |
| --- | --- | --- |
| `goalCount` | `number` | (Optional) The progress required to complete the task. |

### Time tasks fields

Time tasks have a target amount of time spent, and are started and stopped. When the target amount of time is met, the task is complete.

| Name | Type | Description |
| --- | --- | --- |
| `goalSeconds` | `number` | The number of seconds that must pass to complete the task. |
| `startImmediately` | `bool` | If the task should start counting time as soon as it is unlocked, rather than only after it is started. |
| `includesOfflineTime` | `bool` | If the task should include time spent while the player is not actively in the game. |

## Configure categories

Categories do not have to be explicitly defined to be used, as the category for a mission has default values that will be used. However, you can configure these values in `ReplicatedStorage.Missions.Configs.Categories` to add additional effects to the category. Categories are identified by unique `CategoryIds`, the same ones referenced in the missions config.

| Name | Type | Description |
| --- | --- | --- |
| `repeatDelaySeconds` | `number` | (Optional) If set, all missions in the category are reset every time the specified amount of time passes, and may be unlocked, completed, and their rewards claimed again. This is separate from repeatable missions, which are repeatable within a given category repeat. |

## Integrate server logic

Take a look at `ReplicatedStorage.Missions.Server.Examples.MissionsExample`, which shows how your server will interact with the **Missions** feature package.

You mainly need to hook up four things once dragging the **Missions** feature package into your game:

1. Define missions in your missions config.
2. Add logic to your game to update task progress or the counters the progress is tied to.```lua
-- Increases progress on a mission Jumping with a Jumps task
Missions.addProgressToTask(player, "Jumping", "Jumps", 1)

-- Starts the timer on a mission BattlingTime with a TimeInBattle task
Missions.startTimedTask(player, "BattlingTime", "TimeInBattle")

-- Stops the timer on a mission BattlingTime with a TimeInBattle task
Missions.stopTimedTask(player, "BattlingTime", "TimeInBattle")

-- Increases the progress on all tasks tied to the Jumps counter
CounterSystem.addCounter(player, "Jumps", 1)

-- Starts the timer on all timed tasks tied to the TimeInBattle timer counter
CounterSystem.startTimer(player, "TimeInBattle")

-- Stops the timer on all timed tasks tied to the TimeInBattle timer counter
CounterSystem.stopTimer(player, "TimeInBattle")
```
3. Set mission completion handlers, and optionally unlock or fail handlers. Use the completion handler to award the rewards from the mission in your game.```lua
local function completeHandler(player: Player, missionId: Types.MissionId)
     print(\`{player} completed mission {missionId}\`)
     -- Award player their rewards.
 end

Missions.setCompletionHandler(missionId, completeHandler)
```
4. Unlock missions that are not unlocked automatically. **Missions** feature package logic ensures that all mission requirements are met before the mission is complete, and its rewards are collectible.```lua
 Missions.unlockMission(player, "Manual")
```

## Configure constants

Constants for the **Core** feature package live in two spots:

- Shared constants live in `ReplicatedStorage.FeaturePackagesCore.Configs.SharedConstants`.
- Package-specific constants, in this case the **Missions** feature package, live in `ReplicatedStorage.Missions.Configs.Constants`.

Additionally, you can find strings for translation broken out into one location: `ReplicatedStorage.FeaturePackagesCore.Configs.TranslationStrings`.

## Customize UI components

By modifying the package objects, such as colors, font, and transparency, you can adjust the visual presentation of your missions UI. For example, in `ReplicatedStorage.Missions.Configs.Constants`, you can enable `SingleTaskMode` to display a progress bar for a task directly on the mission itself for missions that only have a single task.

> **Warning:** If you move any of the objects around hierarchically, the code will not be able to find them, and you'll need to make adjustments in **MissionsUI**.

In addition, if your game already has an existing UI that you would like to integrate with the **Missions** feature package, the client `Class.ModuleScript` `MissionsClient` contains all the functions necessary to get the information about a player's missions sent from the server.
