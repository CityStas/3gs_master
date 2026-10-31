---
title: "Attributes and signals"
url: /docs/en-us/matchmaking/attributes-and-signals
last_updated: 2026-10-30T19:55:45Z
description: "Attributes and signals define the player and server data used in matchmaking, including both Roblox-provided signals and custom signals you can create."
---

# Attributes and signals

## Existing attributes

The default Roblox matchmaking configuration uses signals based on existing attributes like player location, age group, and latency.

To use data for matchmaking that Roblox doesn't automatically include in its default configuration, you need to create [custom attributes](#custom-attributes) and [custom signals](#custom-signals).

| **Attribute** | **Type** | **Description** |
| --- | --- | --- |
| **Estimated Player Latency** | Numerical | The estimated latency of a player in a server. |
| **Has Friends** | Categorical | Whether a server has a friend or another player of the same IP address as the joining player. |
| **Is Voice Chat Enabled** | Categorical | Whether a player has voice chat enabled. |
| **Player Age** | Numerical | The player’s age. |
| **Player Device Type** | Categorical | The player’s device type. Can be a mobile device, a computer, a tablet, a console, or a VR device. |
| **Player Language** | Categorical | The player’s language. |
| **Player Play History** | Numerical | The log-10 number of minutes a player has played in a universe in the past 28 days. |
| **Server Occupancy** | Numerical | The number of players in a server. |
| **Player Text Chat Group** | Categorical | The player's text chat group where they can text chat together. |

## Existing signals

The following are Roblox-defined signals derived based on Roblox attributes:

| **Signal** | **Description** |
| --- | --- |
| [**Age**](#age) | The difference between the average age of players in the server and the joining player’s age, with a maximum relevant difference of 25. |
| [**Device Type**](#device-type) | The ratio of players in the server with the same device type as the joining player. |
| [**Friends**](#friends) | The number of people in the server who are friends with the joining player or who share an IP address with the joining player. 1 if there is a preferred player, 0 otherwise. |
| [**Latency**](#latency) | The joining player's delta ping for a server, which is the estimated ping above the lowest ping the player could achieve on their best reachable datacenter, with a max relevant value of 100. |
| [**Language**](#language) | The ratio of players in the server with the same language as the joining player |
| [**Occupancy**](#occupancy) | The ratio of players in the server compared to the capacity of the server. |
| [**Play History**](#play-history) | The difference between the average play history in the server and the joining player’s play history, with a maximum relevant difference of 4.6. |
| [**Voice Chat**](#voice-chat) | The ratio of players in the server with voice chat enabled. |
| [**Text Chat**](#text-chat) | The ratio of players in the server who can text chat with the joining player together. |

### Age

A numerical signal that compares the average ages of players on a server to the joining player's age. This signal has a max relevant difference of 25. The signal score is inversely related to the age difference, meaning lower age differences have higher scores.

ageDifferenceSignalScore = 1 − min ⁡ ( 25, ageDifference) / 25 \text{ageDifferenceSignalScore} = 1 - \min(25, \text{ageDifference}) / 25ageDifferenceSignalScore=1−min(25,ageDifference)/25

where

ageDifference = ∣ avgServerAge − joiningPlayerAge ∣ \text{ageDifference} = |\text{avgServerAge} - \text{joiningPlayerAge}|ageDifference=∣avgServerAge−joiningPlayerAge∣

### Device Type

A categorical signal that measures the ratio of players on the server with the same device type as the joining player. Device types include: Computer, mobile device, tablet, console, and VR device.

deviceTypeSignalScore = # players with same device as joining player / # players on the server \text{deviceTypeSignalScore} = \text{\# players with same device as joining player} / \text{\# players on the server}deviceTypeSignalScore=# players with same device as joining player/# players on the server

### Friends

A preferred player is a player who is either friends with the joining player or who shares the same IP address as the joining player. The Friends signal is a categorical signal with a score of 1 when there is a preferred player in the server and a score of 0 when there are no preferred players on the server.

friendsSignalScore = hasFriends ?   1: 0 \text{friendsSignalScore} = \text{hasFriends} \ {?} \ 1 : 0friendsSignalScore=hasFriends ? 1:0

The Friends signal can also be considered a numerical signal with a maximum relevant value of 1.

friendsSignalScore = min ⁡ ( # preferred players in server, 1) / 1 \text{friendsSignalScore} = \min(\text{\# preferred players in server}, 1) / 1friendsSignalScore=min(# preferred players in server,1)/1

### Language

A categorical signal that measures the ratio of players on the server who share the same language setting as the joining player.

languageSignalScore = # players with same language setting as joining player / # players on the server \text{languageSignalScore} = \text{\# players with same language setting as joining player} / \text{\# players on the server}languageSignalScore=# players with same language setting as joining player/# players on the server

### Latency

A numerical signal that measures the joining player's delta ping in milliseconds if they were to play on a server, which is the estimated ping above the lowest ping the player could achieve on their best reachable datacenter. This signal has a max relevant value of 100 milliseconds. The signal score is inversely related to the delta ping, meaning lower delta ping values have higher scores.

latencySignalScore = 1 − min ⁡ ( 100, deltaPingMs) / 100 \text{latencySignalScore} = 1 - \min(100, \text{deltaPingMs}) / 100latencySignalScore=1−min(100,deltaPingMs)/100

### Occupancy

A numerical signal that measures the ratio of players on the server to the capacity of the server.

occupancySignalScore = # players in server / serverCapacity \text{occupancySignalScore} = \text{\# players in server} / \text{serverCapacity}occupancySignalScore=# players in server/serverCapacity

### Play History

The Play History attribute value is the log-10 number of minutes a player has played in a universe in the past 28 days. This numerical signal compares the average log-10 Play History value of players in the server to the joining player's Play History value. This signal has a max relevant difference of 4.6. The signal score is inversely related to the play history difference, meaning lower play history differences have higher scores.

playHistorySignalScore = 1 − min ⁡ ( 4.6, playHistoryDifference / 4.6) \text{playHistorySignalScore} = 1 - \min(4.6, \text{playHistoryDifference} / 4.6)playHistorySignalScore=1−min(4.6,playHistoryDifference/4.6), where

playHistoryDifference = ∣ avgServerPlayHistory − joiningPlayerPlayHistory ∣ \text{playHistoryDifference} = |\text{avgServerPlayHistory} - \text{joiningPlayerPlayHistory}|playHistoryDifference=∣avgServerPlayHistory−joiningPlayerPlayHistory∣

### Voice Chat

A player can have voice chat enabled or disabled. The Voice Chat signal is a categorical signal that measures the ratio of players with the same voice chat setting as the joining player to the number of players in the server.

If a place has voice chat disabled, the Voice Chat signal's weight is 0.

voiceChatSignalScore = # players with same voice chat setting as joining player / # players on the server \text{voiceChatSignalScore} = \text{\# players with same voice chat setting as joining player} / \text{\# players on the server}voiceChatSignalScore=# players with same voice chat setting as joining player/# players on the server

### Text Chat

A categorical signal that measures the ratio of players on the server who can text chat with the joining player together in common.

textChatSignalScore = # players can text with the joining player in common  / # players on the server \text{textChatSignalScore} = \text{\# players can text with the joining player in common } / \text{\# players on the server}textChatSignalScore=# players can text with the joining player in common /# players on the server

## Custom attributes

Custom attributes give custom signals access to player and server data. For more information about creating your own custom attributes, see [Create a custom attribute](/docs/en-us/matchmaking/customize-matchmaking.md#create-a-custom-attribute). For more information about existing Roblox attributes, see [Existing attributes](#existing-attributes).

| **Attribute** | **Characteristics** |
| --- | --- |
| **Player** | Persistent <br><br> Custom player data that persists in data stores, like a player's level or score inside the game <br><br> Managed using the `Class.DataStore\|DataStore` APIs |
| **Server** | Not persistent and only last as long as the server is active <br><br> Server-specific data like the server level or game mode <br><br> Managed using the `Class.MatchmakingService\|MatchmakingService` API |

```lua
local DataStoreService = game:GetService("DataStoreService")

local eloStore = DataStoreService:GetDataStore("PlayerElo")

function onMatchEnded(players: {Player}, winners: {Player}, losers: {Player})
	for _, player in players do
		local updatedElo = CalculateUpdatedElo(player, winners, losers)
		local success, errorMessage = pcall(function()
			eloStore:SetAsync(player.UserId, updatedElo)
		end)
	end
end
```

```lua
local MatchmakingService = game:GetService("MatchmakingService")
local RunService = game:GetService("RunService")

if RunService:IsStudio() then
	-- Sets up initial attributes and schema for testing
	MatchmakingService:InitializeServerAttributesForStudio({
		Level = "Advanced",
		Elo = 123.456,
		TrainingMode = true
	})
end

-- Retrieves the Level attribute
local currentLevel, errorMessage = MatchmakingService:GetServerAttribute("Level")
if errorMessage then
	warn(errorMessage)
else
	print("Current level: " .. currentLevel)
end

-- Updates the Level attribute value to Advanced
local success, errorMessage = MatchmakingService:SetServerAttribute("Level", "Advanced")
if not success then
	warn("Failed to update server attribute [Level] to [Advanced] due to error: " .. errorMessage)
else
	print("Successfully set [Level] to [Advanced]")
end
```

## Custom signals

Custom signals are created and defined by you and can be numerical or categorical:

- Numerical signals are numbers. They compare the difference between the joining player's attribute and the server's aggregated value, with larger differences lowering or increasing the score. For example, the closer the skill level of a player is to the average skill level of the server, the higher the numerical signal's score is. This score is then multiplied by the signal's weight.
- Categorical signals are strings or booleans. They're based on how common the joining player's attribute is when compared to the other players in the server. For example, if a high percentage of the players inside a server have the same preferred language as the joining player, the score increases. This score is then also multiplied by the signal's weight.

For more information about creating your own custom signals, see [Create a custom signal](/docs/en-us/matchmaking/customize-matchmaking.md#create-a-custom-signal). For more information about existing Roblox signals, see [Existing signals](#existing-signals).

### Player numerical

##### Joining player

Minimizes the difference between the server's average player attribute and the joining player's attribute. Differences beyond 1000 return a signal score of 0.

```lua
local diff = math.abs(server_{aggregation_function}_{attribute_name} - joining_player_{attribute_name})
local score = 1 - math.min(diff / max_relevant_difference, 1)
return score
```

```lua
local server_average_Elo = 2000
local joining_player_Elo = 1000
local max_relevant_difference = 1500

local diff = math.abs(server_average_Elo - joining_player_Elo)
local score = 1 - math.min(diff / max_relevant_difference, 1)
return score
```

##### Constant value

Minimizes the difference between the server's average player attribute and a constant value of 500. Differences beyond 1000 return a signal score of 0.

```lua
local diff = math.abs(server_sum_{attribute_name} + joining_player_{attribute_name} - constant_value)
local score = 1 - math.min(diff / max_relevant_difference, 1)
return score
```

```lua
local server_sum_PowerLevel = 4500
local joining_player_PowerLevel = 9901
local max_relevant_difference = 1500
local constant_value = 5000

local diff = math.abs(server_sum_PowerLevel + joining_player_PowerLevel - constant_value)
local score = 1 - math.min(diff / max_relevant_difference, 1)
```

### Player categorical

##### Clustering

Maximizes the ratio of players in the server who have the same attribute as the joining player's attribute.

```lua
local score = num_players_same_{attribute_name} / occupancy
return score
```

```lua
local num_players_same_Guild = 15
local occupancy = 19

local score = num_players_same_Guild / occupancy
return score
```

##### Diversifying

Maximizes the ratio of players in the server who have a different attribute than the joining player's attribute.

```lua
local score = num_players_same_{attribute_name} / occupancy
return 1 - score
```

```lua
local num_players_same_RpgClass = 15
local occupancy = 19

local score = num_players_same_RpgClass / occupancy
return score
```

### Server numerical

##### Joining player

Minimizes the difference between the server's attribute and the joining player's attribute. Differences beyond 1000 return a signal score of 0.

```lua
local diff = math.abs(server_{attribute_name} - joining_player_{attribute_name})
local score = 1 - math.min(diff / max_relevant_difference, 1)
return score
```

```lua
local server_Level = 4500
local joining_player_Level = 9000
local max_relevant_difference = 1500

local diff = math.abs(server_Level - joining_player_Level)
local score = 1 - math.min(diff / max_relevant_difference, 1)
```

##### Constant value

Minimizes the difference between the server's attribute value and a constant value. Differences beyond this constant value return a signal score of 0.

```lua
local diff = math.abs(server_{attribute_name} - constant_value)
local score = math.min(diff / max_relevant_difference, 1)
return score
```

```lua
local server_GameTime = 500
local max_relevant_difference = 1000
local constant_value = 1000

local diff = math.abs(server_GameTime - constant_value)
local score = math.min(diff / max_relevant_difference, 1)
```

### Server categorical

##### Compare to joining player

The score is 1 when the server's attribute value (for example, Game Mode) is equal to the player's attribute value (for example, Preferred Game Mode). Otherwise, the signal score is 0.

```lua
if server_{attribute_name} == joining_player_{attribute_name} then
	return 1
else
	return 0
end
```

```lua
local server_GameMode = "Survival"
local joining_player_GameMode = "Survival"

if server_GameMode == joining_player_GameMode then
	return 1
else
	return 0
end
```

##### Compare to constant value

The score is 1 when the server's attribute value is equal to a constant value of true. Otherwise, the signal score is 0.

```lua
if server_{attribute_name} == constant_value then
	return 1
else
	return 0
end
```

```lua
local server_GameNotStarted = true

if server_GameNotStarted == true then
	return 1
else
	return 0
end
```
