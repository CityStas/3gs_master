---
name: AnalyticsService
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "Collection of methods that allows you to track how users interact with your experiences."
---

# Class: AnalyticsService

> Collection of methods that allows you to track how users interact with your
> experiences.

## Description

`AnalyticsService` is a collection of methods that allows you to track how
users interact with your experiences, specifically player progression,
in-experience economy, funnels, and custom events. For more information on
using this service, see
[Event types](/docs/en-us/production/analytics/event-types.md).

## Properties

### Property: AnalyticsService.ApiKey

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "LocalUserSecurity",
    "write": "LocalUserSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Basic"
  ]
}
```

> **Deprecated:** This property is deprecated. Do not use it for new work.

This property contains the game's PlayFab API key. It must be set and
valid in order to use [FireEvent](/docs/reference/engine/classes/AnalyticsService.md).

## Methods

### Method: AnalyticsService:GetPlayerSegmentsAsync

**Signature:** `AnalyticsService:GetPlayerSegmentsAsync(player: Player): Dictionary`

This server-only method returns coarse segment buckets for a player in the
current experience. Use these buckets at runtime to personalize content or
gate features for specific player groups. If a cached result is not
already available, the method may yield while the engine fetches the
segment data. Successfully fetched results are cached per player for the
lifetime of the server session.

If segment data is unavailable, this method does not throw. Instead, it
returns `HasData = false` and all enum fields are set to `Unknown`.

This method throws only when called from the client or when the `player`
argument is invalid.

The returned dictionary has the following structure:

| Name | Type | Description |
| --- | --- | --- |
| `HasData` | bool | Whether segment data was successfully retrieved for the player. |
| `ActivePayerStatus` | [ActivePayerStatus](/docs/reference/engine/enums/ActivePayerStatus.md) | The player's current payer status bucket for this experience. |
| `WhenUserFirstPlayed` | [WhenUserFirstPlayed](/docs/reference/engine/enums/WhenUserFirstPlayed.md) | When the player first played this experience, represented as a bucket. |
| `PlatformSpenderStatus` | [PlayerPlatformSpenderStatus](/docs/reference/engine/enums/PlayerPlatformSpenderStatus.md) | The player's platform-wide spender status bucket, including whether the player falls outside the active spender bucket. |
| `ExperienceActivationStatus` | [ExperienceActivationStatus](/docs/reference/engine/enums/ExperienceActivationStatus.md) | Whether the player is new, active, lapsed, or reactivated in this experience, based on the last 30 days. |
| `EngagementLevel` | [EngagementLevel](/docs/reference/engine/enums/EngagementLevel.md) | How many days the player played this experience in the last 7 days, represented as a bucket. |
| `PlatformActivationStatus` | [PlayerPlatformActivationStatus](/docs/reference/engine/enums/PlayerPlatformActivationStatus.md) | Whether the player is new, active, lapsed, or reactivated on Roblox, based on the last 60 days. |
| `UserNewReturningStatus` | [UserNewReturningStatus](/docs/reference/engine/enums/UserNewReturningStatus.md) | Whether the player is new to this experience or has played it before. |
| `UserAcquisitionSource` | [UserAcquisitionSource](/docs/reference/engine/enums/UserAcquisitionSource.md) | How the player first found this experience. |

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The player whose segment buckets should be returned. |

**Returns:** `Dictionary` — A dictionary containing coarse player segment buckets for the current
experience.

**Configure server-side experiences with player segments**

This server-side sample retrieves runtime player segments when a player joins
and uses them to choose onboarding and offer behavior.

```lua
local Players = game:GetService("Players")
local AnalyticsService = game:GetService("AnalyticsService")

local function configurePlayerExperience(player)
	local segments = AnalyticsService:GetPlayerSegmentsAsync(player)

	if not segments.HasData then
		return
	end

	if segments.WhenUserFirstPlayed == Enum.WhenUserFirstPlayed.Days0To30 then
		print("Show additional onboarding for", player.Name)
	end

	if segments.ActivePayerStatus == Enum.ActivePayerStatus.Top15Percent then
		print("Show high-value offer to", player.Name)
	end
end

Players.PlayerAdded:Connect(configurePlayerExperience)
```

### Method: AnalyticsService:LogCustomEvent

**Signature:** `AnalyticsService:LogCustomEvent(player: Player, eventName: string, value?: double, customFields?: Dictionary): ()`

Logs an event used to track custom metrics of a user in experience. For
more information, see
[Custom events](/docs/en-us/production/analytics/custom-events.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The user who triggered the event. |
| `eventName` | `string` |  | The name of the custom event. |
| `value` | `double` | `1` | The value of the event that will be used in aggregation. |
| `customFields` | `Dictionary` | `nil` | Optional dictionary of custom fields that will provide breakdowns in Roblox-provided charts. Only specific keys, provided by [AnalyticsCustomFieldKeys](/docs/reference/engine/enums/AnalyticsCustomFieldKeys.md), will be used for these breakdowns. Limited to 8,000 unique combinations of values across the three custom fields per experience. |

**Returns:** `()`

**Log Custom Event**

This example uses [AnalyticsService:LogCustomEvent](/docs/reference/engine/classes/AnalyticsService.md) to log two custom
events: `MissionStarted` and `MissionCompletedDuration`.

```lua
local AnalyticsService = game:GetService("AnalyticsService")

-- Log when the mission starts
AnalyticsService:LogCustomEvent(
	player,
	"MissionStarted" -- Custom event name
)

-- Log when the mission is completed with the time it took
AnalyticsService:LogCustomEvent(
	player,
	"MissionCompletedDuration", -- Custom event name
	120 -- Event value used in aggregation
)
```

### Method: AnalyticsService:LogEconomyEvent

**Signature:** `AnalyticsService:LogEconomyEvent(player: Player, flowType: AnalyticsEconomyFlowType, currencyType: string, amount: float, endingBalance: float, transactionType: string, itemSku: string, customFields?: Dictionary): ()`

Logs an event used to track player actions related in experience. For more
information, see
[Economy events](/docs/en-us/production/analytics/economy-events.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The user who triggered the event. |
| `flowType` | `AnalyticsEconomyFlowType` |  | Should specify the direction that currency is flowing using [AnalyticsEconomyFlowType](/docs/reference/engine/enums/AnalyticsEconomyFlowType.md). |
| `currencyType` | `string` |  | The name of the currency being added or removed, for example `"gold"`, `"gems"`, or `"energy"`. Limited to 5 unique currency types per experience. |
| `amount` | `float` |  | The amount of currency being added or removed. This value should always be positive. |
| `endingBalance` | `float` |  | The user's balance after the currency has been added or removed. This value should always be greater than or equal to `0`. |
| `transactionType` | `string` |  | The type of transaction that occurred. While you're free to use any transaction type, it's recommended to use the provided types from [AnalyticsEconomyTransactionType](/docs/reference/engine/enums/AnalyticsEconomyTransactionType.md) such as `"IAP"` or `"ContextualPurchase"` to enable future insights from Roblox tools and charts.  Because this field type is a string, you'll need to pass the `Name` value of the enum. For example [Enum.AnalyticsEconomyTransactionType.IAP.Name](/docs/reference/engine/enums/AnalyticsEconomyTransactionType.md).  Limited to 20 unique types per experience. |
| `itemSku` | `string` |  | Optional SKU of the item or bundle being purchased. This is a unique identifier for the item being purchased. Limited to 100 unique SKUs per experience. |
| `customFields` | `Dictionary` | `nil` | Optional dictionary of custom fields that will provide breakdowns in Roblox-provided charts. Only specific keys, provided by [AnalyticsCustomFieldKeys](/docs/reference/engine/enums/AnalyticsCustomFieldKeys.md), will be used for these breakdowns. Limited to 8,000 unique combinations of values across the three custom fields per experience. |

**Returns:** `()`

**Tracking an in-app purchase**

The following sample tracks a Robux purchase of a 1000-coin bundle, using the
IAP (in-app purchase) transaction type. Note the item name provided as an
optional parameter when compared to the previous sample.

```lua
local AnalyticsService = game:GetService("AnalyticsService")

AnalyticsService:LogEconomyEvent(
	player,
	Enum.AnalyticsEconomyFlowType.Source,
	"Coins",
	1000, -- How many coins are in the bundle
	1020, -- balance after transaction
	Enum.AnalyticsEconomyTransactionType.IAP.Name,
	"1000CoinBundle" -- Unique identifier of the coin bundle
)
```

### Method: AnalyticsService:LogFunnelStepEvent

**Signature:** `AnalyticsService:LogFunnelStepEvent(player: Player, funnelName: string, funnelSessionId: string, step?: int, stepName: string, customFields?: Dictionary): ()`

Logs an event used to track user actions stepping through a pre-planned
funnel. Funnel breakdowns only consider the user and event values from the
first step in a funnel session. See
[Funnel events](/docs/en-us/production/analytics/funnel-events.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The user who triggered the event. |
| `funnelName` | `string` |  | The name of the funnel. This should be the same for all steps in the funnel. Limited to 10 unique funnels per experience. |
| `funnelSessionId` | `string` |  | Optional unique identifier for the funnel session. This should be the same for all steps in the funnel.  Note that this field is only necessary for **recurring** funnels, for example a purchase flow funnel or an item upgrade funnel. If you don't have a natural funnel session identifier, it's recommended to use [HttpService:GenerateGUID()](/docs/reference/engine/classes/HttpService.md). |
| `step` | `int` | `1` | The step number in the funnel. This should be unique for each step in the funnel. All funnels start at step 1. Limited to steps 1-100.  Repeated steps by the same user in the same funnel session, or when `funnelSessionId` is `nil` will be ignored.  Note that if any steps are skipped, the intermediate steps will be considered completed. |
| `stepName` | `string` |  | Optional name of the step in the funnel. This field is only used for display purposes in Roblox-provided charts. |
| `customFields` | `Dictionary` | `nil` | Optional dictionary of custom fields that will provide breakdowns in Roblox-provided charts. Only specific keys, provided by [AnalyticsCustomFieldKeys](/docs/reference/engine/enums/AnalyticsCustomFieldKeys.md), will be used for these breakdowns. Limited to 8,000 unique combinations of values across the three custom fields per experience. |

**Returns:** `()`

**Tracking Shop steps**

The following sample tracks some basic events for each user beginning the
process to buy an item from an "armory" shop. Note the funnelSessionId used to
distinguish between different sessions of the same user opening the shop.

```lua
local AnalyticsService = game:GetService("AnalyticsService")
local HttpService = game:GetService("HttpService")

funnelSessionId = HttpService:GenerateGUID()

-- Log when the user opens the store
AnalyticsService:LogFunnelStepEvent(
	player,
	"ArmoryCheckout", -- Funnel name used to group steps together
	funnelSessionId, -- Funnel session ID for this unique checkout session
	1, -- Step number
	"Opened Store" -- Step name
)

-- Log when the user views an item
AnalyticsService:LogFunnelStepEvent(
	player,
	"ArmoryCheckout", -- Funnel name used to group steps together
	funnelSessionId, -- Funnel session ID for this unique checkout session
	2, -- Step number
	"Viewed Item" -- Step name
)

-- Log when the user views adds to cart
AnalyticsService:LogFunnelStepEvent(
	player,
	"ArmoryCheckout", -- Funnel name used to group steps together
	funnelSessionId, -- Funnel session ID for this unique checkout session
	3, -- Step number
	"Added to Cart" -- Step name
)
```

### Method: AnalyticsService:LogOnboardingFunnelStepEvent

**Signature:** `AnalyticsService:LogOnboardingFunnelStepEvent(player: Player, step: int, stepName: string, customFields?: Dictionary): ()`

Logs an event used to track user actions stepping through an onboarding
funnel. Funnel breakdowns only consider the user and event values from the
first step in a funnel session. See
[Funnel events](/docs/en-us/production/analytics/funnel-events.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The user who triggered the event. |
| `step` | `int` |  | The step number in the funnel. This should be unique for each step in the funnel. All funnels start at step 1. Limited to steps 1-100.  Note that if any steps are skipped, the intermediate steps will be considered completed. |
| `stepName` | `string` |  | Optional name of the step in the funnel. This field is only used for display purposes in Roblox-provided charts. |
| `customFields` | `Dictionary` | `nil` | Optional dictionary of custom fields that will provide breakdowns in Roblox-provided charts. Only specific keys, provided by [AnalyticsCustomFieldKeys](/docs/reference/engine/enums/AnalyticsCustomFieldKeys.md), will be used for these breakdowns. Limited to 8,000 unique combinations of values across the three custom fields per experience. |

**Returns:** `()`

**Tracking onboarding steps**

The following sample demonstrates how to log two steps of an onboarding
funnel. An onboarding funnel typically introduces players to the game's core
loop.

```lua
local AnalyticsService = game:GetService("AnalyticsService")

-- Log the first step of the FTUE
AnalyticsService:LogOnboardingFunnelStepEvent(
	player,
	1, -- Step number
	"Joined Game" -- Step name
)

-- Log the second step of the FTUE
AnalyticsService:LogOnboardingFunnelStepEvent(
	player,
	2, -- Step number
	"Choose Class" -- Step name
)
```

### Method: AnalyticsService:LogProgressionCompleteEvent

**Signature:** `AnalyticsService:LogProgressionCompleteEvent(player: Player, progressionPathName: string, level: int, levelName: string, customFields?: Dictionary): ()`

Logs an event for when a user has completed a level attempt. This event
does not currently display in any Roblox-provided charts.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The player who triggered the event. |
| `progressionPathName` | `string` |  | The name of the progression path this event belongs to, such as a world, chapter, or level group. This groups related progression events together. Cannot be empty and cannot contain a comma `,`, double quote `"`, single quote `'`, or newline character. |
| `level` | `int` |  | The numeric level the player is progressing through within the progression path. |
| `levelName` | `string` |  | The name of the level associated with this event. This field is used for display purposes in Roblox-provided charts. |
| `customFields` | `Dictionary` | `nil` | Optional dictionary of custom fields that will provide breakdowns in Roblox-provided charts. Only specific keys, provided by [AnalyticsCustomFieldKeys](/docs/reference/engine/enums/AnalyticsCustomFieldKeys.md), will be used for these breakdowns. Limited to 8,000 unique combinations of values across the three custom fields per experience. |

**Returns:** `()`

### Method: AnalyticsService:LogProgressionEvent

**Signature:** `AnalyticsService:LogProgressionEvent(player: Player, progressionPathName: string, status: AnalyticsProgressionType, level: int, levelName: string, customFields?: Dictionary): ()`

Logs an event for when a user has started, completed, or failed a level
attempt. This event does not currently display in any Roblox-provided
charts.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The player who triggered the event. |
| `progressionPathName` | `string` |  | The name of the progression path this event belongs to, such as a world, chapter, or level group. This groups related progression events together. Cannot be empty and cannot contain a comma `,`, double quote `"`, single quote `'`, or newline character. |
| `status` | `AnalyticsProgressionType` |  | The progression status to record, provided as an [AnalyticsProgressionType](/docs/reference/engine/enums/AnalyticsProgressionType.md) value such as `Start`, `Complete`, or `Fail`. The [AnalyticsService:LogProgressionStartEvent()](/docs/reference/engine/classes/AnalyticsService.md), [AnalyticsService:LogProgressionCompleteEvent()](/docs/reference/engine/classes/AnalyticsService.md), and [AnalyticsService:LogProgressionFailEvent()](/docs/reference/engine/classes/AnalyticsService.md) methods are shortcuts that set this status for you. |
| `level` | `int` |  | The numeric level the player is progressing through within the progression path. |
| `levelName` | `string` |  | The name of the level associated with this event. This field is used for display purposes in Roblox-provided charts. |
| `customFields` | `Dictionary` | `nil` | Optional dictionary of custom fields that will provide breakdowns in Roblox-provided charts. Only specific keys, provided by [AnalyticsCustomFieldKeys](/docs/reference/engine/enums/AnalyticsCustomFieldKeys.md), will be used for these breakdowns. Limited to 8,000 unique combinations of values across the three custom fields per experience. |

**Returns:** `()`

### Method: AnalyticsService:LogProgressionFailEvent

**Signature:** `AnalyticsService:LogProgressionFailEvent(player: Player, progressionPathName: string, level: int, levelName: string, customFields?: Dictionary): ()`

Logs an event for when a user has failed a level attempt. This event does
not currently display in any Roblox-provided charts.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The user who triggered the event. |
| `progressionPathName` | `string` |  | The name of the progression path this event belongs to, such as a world, chapter, or level group. This groups related progression events together. Cannot be empty and cannot contain a comma `,`, double quote `"`, single quote `'`, or newline character. |
| `level` | `int` |  | The numeric level the player is progressing through within the progression path. |
| `levelName` | `string` |  | The name of the level associated with this event. This field is used for display purposes in Roblox-provided charts. |
| `customFields` | `Dictionary` | `nil` | Optional dictionary of custom fields that will provide breakdowns in Roblox-provided charts. Only specific keys, provided by [AnalyticsCustomFieldKeys](/docs/reference/engine/enums/AnalyticsCustomFieldKeys.md), will be used for these breakdowns. Limited to 8,000 unique combinations of values across the three custom fields per experience. |

**Returns:** `()`

### Method: AnalyticsService:LogProgressionStartEvent

**Signature:** `AnalyticsService:LogProgressionStartEvent(player: Player, progressionPathName: string, level: int, levelName: string, customFields?: Dictionary): ()`

Logs an event for when a user has started a level attempt. This event does
not currently display in any Roblox-provided charts.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The player who triggered the event. |
| `progressionPathName` | `string` |  | The name of the progression path this event belongs to, such as a world, chapter, or level group. This groups related progression events together. Cannot be empty and cannot contain a comma `,`, double quote `"`, single quote `'`, or newline character. |
| `level` | `int` |  | The numeric level the player is progressing through within the progression path. |
| `levelName` | `string` |  | The name of the level associated with this event. This field is used for display purposes in Roblox-provided charts. |
| `customFields` | `Dictionary` | `nil` | Optional dictionary of custom fields that will provide breakdowns in Roblox-provided charts. Only specific keys, provided by [AnalyticsCustomFieldKeys](/docs/reference/engine/enums/AnalyticsCustomFieldKeys.md), will be used for these breakdowns. Limited to 8,000 unique combinations of values across the three custom fields per experience. |

**Returns:** `()`

### Method: AnalyticsService:FireCustomEvent

**Signature:** `AnalyticsService:FireCustomEvent(player: Instance, eventCategory: string, customData: Variant): ()`

> **Deprecated:** This deprecated function is a variant of [AnalyticsService:LogCustomEvent()](/docs/reference/engine/classes/AnalyticsService.md) which should be used instead.

This function triggers a custom event with a custom event name data.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The player who triggered the custom event. `nil` if not player related. |
| `eventCategory` | `string` |  | User defined category. This should be the name of the event. |
| `customData` | `Variant` |  | Optional. User defined data, could be a string, a number or a table. |

**Returns:** `()`

**Analytics Event - Custom**

The code sample below demonstrates one possible usage for the
[FireCustomEvent()](/docs/reference/engine/classes/AnalyticsService.md) function, which
can be used to fire a custom event for the `AnalyticsService`. In this
example, the custom function is used to report that a new server has started,
which would allow the developer to track data such as how many servers are
started for their game.

```lua
local AnalyticsService = game:GetService("AnalyticsService")
local Players = game:GetService("Players")

-- server event, report a new server started
local serverInfo = {
	Time = os.time(),
	PlaceId = game.PlaceId,
}

AnalyticsService:FireCustomEvent(nil, "ServerStart", serverInfo)

Players.PlayerAdded:Connect(function(player)
	player.Chatted:Connect(function(message)
		local customData = {
			Time = os.time(),
			Message = message,
		}
		AnalyticsService:FireCustomEvent(player, "PlayerChatted", customData)
	end)
end)
```

### Method: AnalyticsService:FireEvent

**Signature:** `AnalyticsService:FireEvent(category: string, value: Variant): ()`

> **Deprecated:** This function has been deprecated in favor of more descriptive methods, including [AnalyticsService:LogCustomEvent()](/docs/reference/engine/classes/AnalyticsService.md), [AnalyticsService:LogEconomyEvent()](/docs/reference/engine/classes/AnalyticsService.md), and [AnalyticsService:LogProgressionEvent()](/docs/reference/engine/classes/AnalyticsService.md).

This function reports a custom event to PlayFab. The event is reported
using a **category** and **value**, where the category is a string and the
value can be a string or table. In order to use PlayFab, you must have a
valid [ApiKey](/docs/reference/engine/classes/AnalyticsService.md) set.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `category` | `string` |  | 'The category of event to report. Cannot contain the following characters: comma `,`, double quote `"` or newline characters `\r\n`'. |
| `value` | `Variant` |  | A value to be serialized and reported. Serialized length must not exceed 1 KiB, or 1024 bytes. |

**Returns:** `()`

### Method: AnalyticsService:FireInGameEconomyEvent

**Signature:** `AnalyticsService:FireInGameEconomyEvent(player: Instance, itemName: string, economyAction: AnalyticsEconomyAction, itemCategory: string, amount: int, currency: string, location: Variant, customData: Variant): ()`

> **Deprecated:** This deprecated function is a variant of [AnalyticsService:LogEconomyEvent()](/docs/reference/engine/classes/AnalyticsService.md) which should be used instead.

This function triggers an event used to track player actions pertaining to
the in-game economy. For example, it should be called to track when
players acquire or spend virtual items within the economy like currency.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The player who triggered the economy event. |
| `itemName` | `string` |  | The name of the item. |
| `economyAction` | `AnalyticsEconomyAction` |  | Indicates the acquisition or spending of an in game resource. |
| `itemCategory` | `string` |  | A user defined category for items such as "Vehicle," "Weapon.". |
| `amount` | `int` |  | The amount of the currency. |
| `currency` | `string` |  | The currency used. Examples: 'gold', 'gems', 'life.'. |
| `location` | `Variant` |  | The event location. A dictionary that each key-value represents an entry of location data. The key-value is a string-string pair. With this you can query which are the most popular "stores" then maybe you want to increase/lower the price for the stores.  See the example below:  ```lua local location = {     ["placeDesc"] = "Dungeon1",     ["levelDesc"] = "level2",     ["mapDesc"] = "LeftChamberMap",     ["storeName"] = "DarkSmith",     ["userDefinedKey"] = "0005" } ``` |
| `customData` | `Variant` |  | Optional. User defined data, could be a string, a number or a table. |

**Returns:** `()` — No return.

**Analytics Event - Economy**

The event below demonstrates one possible usage for the
`AnalyticsService:FireInGameEconomyEvent` function. It uses the function to
invoke an analytics economy event when the parented gold `Part` is touched by
a player.

```lua
local AnalyticsService = game:GetService("AnalyticsService")

local gold = script.Parent

gold.Touched:Connect(function(otherPart)
	local player = game.Players:GetPlayerFromCharacter(otherPart.Parent)
	if player == nil then
		return
	end

	local location = {
		["Map"] = "someMap",
		["Position"] = tostring(gold.Position),
	}

	AnalyticsService:FireInGameEconomyEvent(
		player,
		"Sword", -- item name
		Enum.AnalyticsEconomyAction.Spend,
		"Weapon", -- itemCategory
		2020, -- amount of Gold
		"Gold", -- currency
		location,
		{ SomeCustomKey = "SomeCustomValue" }
	) -- optional customData
end)
```

### Method: AnalyticsService:FireLogEvent

**Signature:** `AnalyticsService:FireLogEvent(player: Instance, logLevel: AnalyticsLogLevel, message: string, debugInfo: Variant, customData: Variant): ()`

> **Deprecated:** This method is deprecated. Do not use it for new work.

This function triggers an event used to track errors and warnings
experienced by players. For example, it could be called to indicate when a
function call fails, such as a datastore save or
[TeleportService:Teleport()](/docs/reference/engine/classes/TeleportService.md). See the example below.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The player who triggered the error event, `nil` if not player related. |
| `logLevel` | `AnalyticsLogLevel` |  | The specified log level (e.g. Debug, Error). |
| `message` | `string` |  | User defined message. |
| `debugInfo` | `Variant` |  | Optional. A dictionary which contains predefined keys including "errorCode" and "stackTrace". Both keys values are strings. stackTrace is a traceback of the current function call stack. |
| `customData` | `Variant` |  | Optional. User defined data, could be a string, a number or a table. |

**Returns:** `()` — No return.

**Analytics Event - Log**

The code sample below demonstrates how to use the
[AnalyticsService:FireLogEvent()](/docs/reference/engine/classes/AnalyticsService.md) function to track log events using the
`AnalyticsService`. The example uses the function to report when a
[TeleportService:Teleport()](/docs/reference/engine/classes/TeleportService.md) call fails.

```lua
local Players = game:GetService("Players")
local TeleportService = game:GetService("TeleportService")
local AnalyticsService = game:GetService("AnalyticsService")

local placeId = game.PlaceId

local player = Players:GetPlayerByUserId(123)

xpcall(function()
	TeleportService:Teleport(placeId, player)
end, function(errorMessage)
	local debugInfo = {
		errorCode = "TeleportFailed",
		stackTrace = debug.traceback(), -- the function call stack
	}
	AnalyticsService:FireLogEvent(
		player,
		Enum.AnalyticsLogLevel.Error, -- log level
		errorMessage, -- message
		debugInfo, -- optional
		{
			PlayerId = player.UserId,
			PlaceId = placeId,
		}
	) -- customData optional
end)
```

### Method: AnalyticsService:FirePlayerProgressionEvent

**Signature:** `AnalyticsService:FirePlayerProgressionEvent(player: Instance, category: string, progressionStatus: AnalyticsProgressionStatus, location: Variant, statistics: Variant, customData: Variant): ()`

> **Deprecated:** This deprecated function is a variant of [AnalyticsService:LogProgressionEvent()](/docs/reference/engine/classes/AnalyticsService.md) which should be used instead.

This function triggers an event used to track player progression through
the game. For example, it should be called when a player starts an in-game
tutorial and again that player finishes the tutorial.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The player who triggered the event. |
| `category` | `string` |  | A user defined category for progression. |
| `progressionStatus` | `AnalyticsProgressionStatus` |  | Indicates the status of the progression. |
| `location` | `Variant` |  | The event location. A dictionary that each key-value represents an entry of location data. The key-value is a string-string pair. With this developers can query where is the most frequent location for a specific progression event category. For example, the category could be "LevelUp". |
| `statistics` | `Variant` |  | Optional. A dictionary that each key-value represents an entry of statistics data that allows developers to track any specific data that they want to collect as players progress through their game. Key-Value is a string-number pair. |
| `customData` | `Variant` |  | Optional. User defined data, could be a string, a number or a table. |

**Returns:** `()` — No return.

**Analytics Event - Progression**

This example demonstrates how to use the
`AnalyticsService:FirePlayerProgressionEvent` function to trigger an analytics
progression event. When a player touches the parent `Part`, a _wisdomStone_,
the function is fired as a _LevelUp_ event.

```lua
local AnalyticsService = game:GetService("AnalyticsService")
local Players = game:GetService("Players")

local wisdomStone = script.Parent

wisdomStone.Touched:Connect(function(otherPart)
	local player = Players:GetPlayerFromCharacter(otherPart.Parent)
	if player == nil then
		return
	end

	local location = {
		["placeDesc"] = "Dungeon1",
		["mapDesc"] = "LeftChamberMap",
	}

	local statistics = {
		["amountOfExp"] = 1337,
		["amountOfGold"] = 1337,
		["kills"] = 1337,
	}

	AnalyticsService:FirePlayerProgressionEvent(
		player,
		Enum.AnalyticsProgressionStatus.Complete, -- progressionStatus
		"LevelUp", -- category
		location,
		statistics, -- optional
		{ AcquireType = "PickUp" }
	) -- customData optional
end)
```

## Inherited Members

### From [Instance](/docs/reference/engine/classes/Instance.md)

- **Property `Archivable`** (`boolean`): Determines if an Instance and its descendants can be cloned using
- **Property `archivable`** (`boolean`):  *(deprecated, hidden)*
- **Property `Capabilities`** (`SecurityCapabilities`): The set of capabilities allowed to be used for scripts inside this
- **Property `IsInSandbox`** (`boolean`): Indicates whether the instance is inside a sandboxed container.
- **Property `Name`** (`string`): A non-unique identifier of the Instance.
- **Property `Parent`** (`Instance`): Determines the hierarchical parent of the Instance.
- **Property `PredictionMode`** (`PredictionMode`): Reflects the client-side prediction mode applied to the instance under
- **Property `RobloxLocked`** (`boolean`): A deprecated property that used to protect CoreGui objects. *(hidden)*
- **Property `Sandboxed`** (`boolean`): When enabled, the instance can only access abilities in its `Capabilities`
- **Property `UniqueId`** (`UniqueId`): A unique identifier for the instance.
- **Method `AddTag(tag: string): ()`**: Applies a tag to the instance.
- **Method `children(): Instances`**: Returns an array of the object's children. *(deprecated)*
- **Method `ClearAllChildren(): ()`**: This method destroys all of an instance's children.
- **Method `Clone(): Instance`**: Create a copy of an instance and all its descendants, ignoring instances
- **Method `clone(): Instance`**:  *(deprecated)*
- **Method `Destroy(): ()`**: Sets the Instance.Parent property to `nil`, locks the
- **Method `destroy(): ()`**:  *(deprecated)*
- **Method `FindFirstAncestor(name: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorOfClass(className: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorWhichIsA(className: string): Instance?`**: Returns the first ancestor of the Instance for whom
- **Method `FindFirstChild(name: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance found with the given name.
- **Method `findFirstChild(name: string, recursive?: boolean): Instance`**:  *(deprecated)*
- **Method `FindFirstChildOfClass(className: string): Instance?`**: Returns the first child of the Instance whose
- **Method `FindFirstChildWhichIsA(className: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance for whom
- **Method `FindFirstDescendant(name: string): Instance?`**: Returns the first descendant found with the given Instance.Name.
- **Method `GetActor(): Actor?`**: Returns the Actor associated with the Instance, if any.
- **Method `GetAttribute(attribute: string): Variant`**: Returns the value which has been assigned to the given attribute name.
- **Method `GetAttributeChangedSignal(attribute: string): RBXScriptSignal`**: Returns an event that fires when the given attribute changes.
- **Method `GetAttributes(): Dictionary`**: Returns a dictionary of the instance's attributes.
- **Method `GetChildren(): Instances`**: Returns an array containing all of the instance's children.
- **Method `getChildren(): Instances`**:  *(deprecated)*
- **Method `GetDebugId(scopeLength?: int): string`**: Returns a coded string of the debug ID used internally by Roblox.
- **Method `GetDescendants(): Instances`**: Returns an array containing all of the descendants of the instance.
- **Method `GetFullName(): string`**: Returns a string describing the instance's ancestry.
- **Method `GetStyled(name: string, selector: string?): Variant`**: Returns the styled or explicitly modified value of the specified property,
- **Method `GetStyledPropertyChangedSignal(property: string): RBXScriptSignal`**: Returns an event that fires when the given style property changes on the
- **Method `GetTags(): Array`**: Gets an array of all tags applied to the instance.
- **Method `HasTag(tag: string): boolean`**: Check whether the instance has a given tag.
- **Method `IsAncestorOf(descendant: Instance): boolean`**: Returns true if an Instance is an ancestor of the given
- **Method `IsDescendantOf(ancestor: Instance): boolean`**: Returns `true` if an Instance is a descendant of the given
- **Method `isDescendantOf(ancestor: Instance): boolean`**:  *(deprecated)*
- **Method `IsPropertyModified(property: string): boolean`**: Returns `true` if the value stored in the specified property is not equal
- **Method `QueryDescendants(selector: string): Instances`**: Returns an array containing all descendants of the instance that match the
- **Method `Remove(): ()`**: Sets the object's `Parent` to `nil`, and does the same for all its *(deprecated)*
- **Method `remove(): ()`**:  *(deprecated)*
- **Method `RemoveTag(tag: string): ()`**: Removes a tag from the instance.
- **Method `ResetPropertyToDefault(property: string): ()`**: Resets a property to its default value.
- **Method `SetAttribute(attribute: string, value: Variant): ()`**: Sets the attribute with the given name to the given value.
- **Method `WaitForChild(childName: string, timeOut: double): Instance`**: Returns the child of the Instance with the given name. If the
- **Event `AncestryChanged`**: Fires when the Instance.Parent property of this object or one of
- **Event `AttributeChanged`**: Fires whenever an attribute is changed on the Instance.
- **Event `ChildAdded`**: Fires after an object is parented to this Instance.
- **Event `childAdded`**:  *(deprecated)*
- **Event `ChildRemoved`**: Fires after a child is removed from this Instance.
- **Event `DescendantAdded`**: Fires after a descendant is added to the Instance.
- **Event `DescendantRemoving`**: Fires immediately before a descendant of the Instance is removed.
- **Event `Destroying`**: Fires immediately before (or is deferred until after) the instance is
- **Event `StyledPropertiesChanged`**: Fires whenever any style property is changed on the instance, including

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some