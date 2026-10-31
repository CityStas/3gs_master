---
name: RecommendationService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "A service that provides an interface for you to manage and display personalized content recommendations."
---

# Class: RecommendationService

> A service that provides an interface for you to manage and display
> personalized content recommendations.

## Description

`RecommendationService` provides an interface for you to manage and display
personalized content recommendations. It supports creating, retrieving,
updating, and deleting recommendation items, as well as generating lists of
recommended content for users. Additionally, it includes functionality for
logging user interactions, such as views and actions, to help refine and
improve recommendation quality. Once set up, you can monitor analytics in the
Creator Dashboard under the **Engagement** section for an experience.

## Methods

### Method: RecommendationService:GenerateItemListAsync

**Signature:** `RecommendationService:GenerateItemListAsync(generateRecommendationItemListRequest: Dictionary): RecommendationPages`

This function returns a paginated list of recommended items based on a
given request. The request can specify criteria such as configuration
name, location, and page size to tailor the recommendations. It returns a
[RecommendationPages](/docs/reference/engine/classes/RecommendationPages.md) object that can be used to iterate through the
list of items.

The `ConfigName` parameter determines how the recommendation engine ranks
and returns items. For example, you can have configurations that optimize
for views, likes, or purchases. For the ranking to be effective, you must
ensure that you are logging the corresponding user interactions using
[LogImpressionEvent](/docs/reference/engine/classes/RecommendationService.md) and
[LogActionEvent](/docs/reference/engine/classes/RecommendationService.md).

Supported `ConfigName` are:

- `MaximizeTimespent`: Optimizes recommendations to prioritize content
  that engages users for longer periods.
- `MaximizeReactions`: Optimizes recommendations to highlight content that
  generates the most user reactions, such as likes and favorites.
- `MaximizePlays`: Optimizes recommendations to prioritize content that
  generates the most `Play` actions. To use this configuration
  effectively, you must log both impressions and `Play` actions. It's
  recommended to filter for "quality" plays (for example play duration
  greater than 60 seconds) before logging to reduce noise and improve the
  system's learning accuracy.
- `MaximizeEngagement`: Optimizes recommendations through a balanced
  approach that considers multiple engagement signals, including quality
  views and reactions. This config is designed to highlight content that
  performs well across different engagement areas.
- `PlayerSpecific`: Returns public items created by the player specified
  in the request and sorted by the most recent creation time. To use this
  config, you must pass the `UserId` in the `CustomContexts`.
- `RecentlyAdded`: Returns items sorted by how recent they are, and
  displays the most recently added public content first.
- `MaximizeJoins`: Optimizes recommendations to prioritize game joins.
  This configuration is exclusive to Roblox Moments and focuses on
  maximizing interactions leading to a teleport. In contrast,
  `MaximizePlays` is purely optimizing `Play` actions.
- `PlayerOwnedItems`: Displays the user's own creations sorted by creation
  time. This config requires user authentication because it displays
  private items. This config is only available on the **client**.

This function can be called from both the **server** and the **client**.
When called from the server, you must pass the `UserId` in the
`CustomContexts`.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `generateRecommendationItemListRequest` | `Dictionary` |  | A dictionary containing the following fields:  - `ConfigName` &mdash; A unique ID for the specific configuration.   This determines how the candidates are ranked. - `LocationId` &mdash; A developer-defined string that specifies the   location where the recommendation is used, such as `"For_you"` or   `"Lobby"`. This parameter will not affect the items returned, and it   can help you track the performance of multiple recommendation   features within your experience. Recommendation metrics for each   individual location will be displayed in the Creator Hub.   `LocationId` **must** be a string and cannot be `"Other"` or   `"other"` as these values are reserved by the Creator Hub. - `PageSize` &mdash; The number of items returned for each page. - `BoostCustomTags` &mdash; A list of string tags. Any item with this   tag will be boosted in ranking. Supports boosting one tag. - `CustomContexts` &mdash; A table of key-value pairs used to pass in   additional context data for ranking. For example, `UserId` for a   Server script. |

**Returns:** `RecommendationPages` — A `RecommendationPages` object containing the paginated list of
recommended items for the given request configuration.

**Generate a list of recommended items**

This code snippet demonstrates how to generate a list of recommended items
using RecommendationService.

```lua
local RecommendationService = game:GetService("RecommendationService")

-- Define the request for generating a recommendation list
local request: GenerateRecommendationItemListRequest = {
	ConfigName = "MaximizeEngagement",
	LocationId = "Lobby",
	PageSize = 10
    -- NOTE: Uncomment and set CustomContexts.UserId for Server script. 
    -- No need to set for Local script.
    -- CustomContexts = {
    --     ["UserId"] = tostring(player.UserId),
    -- }
}

-- Call GenerateItemListAsync to get the recommendation pages
local success, recommendationPages = pcall(function()
    return RecommendationService:GenerateItemListAsync(request)
end)
```

### Method: RecommendationService:GetRecommendationItemAsync

**Signature:** `RecommendationService:GetRecommendationItemAsync(itemId: string): Dictionary`

This function returns a single recommendation item by its `ItemId`. This
is useful for getting the details of a specific item without having to
fetch a whole list.

This function can be called only from the **server**.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `itemId` | `string` |  | The ID of the item to retrieve. |

**Returns:** `Dictionary` — A dictionary representing the recommendation item with the following
fields:

- `ItemId` &mdash; The unique ID for the item.
- `ReferenceId` &mdash; The developer-provided ID for the item.
- `TracingId` &mdash; An ID for tracking recommendation sessions. This
  will be empty when fetching a single item directly.
- `Creator` &mdash; A table containing the `CreatorId` and
  `CreatorType`.
- `Attributes` &mdash; A list of content attributes associated with
  the item.
- `CustomTags` &mdash; A list of custom string tags.
- `Visibility` &mdash; An enum of type
  [RecommendationItemVisibility](/docs/reference/engine/enums/RecommendationItemVisibility.md).

**Get a single recommendation item**

This code snippet demonstrates how to retrieve a single recommendation item by
its ID.

```lua
local RecommendationService = game:GetService("RecommendationService")

local function getItem(itemId)
    local success, item = pcall(function()
        return RecommendationService:GetRecommendationItemAsync(itemId)
    end)
    if success and item then
        print("Successfully retrieved item: " .. item.ItemId)
        print("  ReferenceId: " .. item.ReferenceId)
        -- The TracingId will be empty when fetching a single item directly
        if item.Creator then
            print("  CreatorId: " .. tostring(item.Creator.CreatorId))
        end
        if item.CustomTags then
            print("  CustomTags: ")
            for _, customTag in ipairs(item.CustomTags) do
                print("    " .. customTag)
            end
        end
    else
        warn("Failed to retrieve item: " .. itemId .. ". Error: " .. tostring(item))
    end
end

-- Example usage (requires a valid itemId)
-- getItem("some-item-id")
```

### Method: RecommendationService:LogActionEvent

**Signature:** `RecommendationService:LogActionEvent(actionType: RecommendationActionType, itemId: string, tracingId: string, actionEventDetails?: Dictionary): ()`

This function logs a user action on a recommended item, such as a "like,"
"share," or "purchase." It requires the `itemId` of the item and a
`tracingId` from the GenerateItemListAsync response to link the action to
a specific recommendation context. Additional details about the action can
be provided in the `actionEventDetails` dictionary.

Logging actions is essential for recommendation configurations that rank
items based on user engagement such as number of likes or purchases.

This function can only be called from the **client**.

**Note:** Only `LogActionEvent` calls in production actually log actions.
Calling this function in Studio doesn't have any effect; you can call it
as many times as you want when testing.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actionType` | `RecommendationActionType` |  | The enum for the type of action. |
| `itemId` | `string` |  | The item ID returned from registration and [GenerateItemListAsync](/docs/reference/engine/classes/RecommendationService.md). |
| `tracingId` | `string` |  | The tracing ID returned from the [GenerateItemListAsync](/docs/reference/engine/classes/RecommendationService.md) response. Each item has a `TracingId`. |
| `actionEventDetails` | `Dictionary` | `nil` | A dictionary containing the following fields:  - `Weight` &mdash; A number representing the weight of the action.   Default is 1. - `DestinationPlaceId` &mdash; The ID of the place the user was sent   to after the action. Used for   [Play](/docs/reference/engine/enums/RecommendationActionType.md). - `CommentText` &mdash; Any text associated with the action, such as a   comment. Used for [Comment](/docs/reference/engine/enums/RecommendationActionType.md). - `ReactionType` &mdash; A string describing the type of reaction, for   example, "like" or "dislike". Used for   [AddReaction](/docs/reference/engine/enums/RecommendationActionType.md) or   [RemoveReaction](/docs/reference/engine/enums/RecommendationActionType.md). |

**Returns:** `()` — No return value.

**Logging a user action**

This code snippet demonstrates how to log a user action on a recommended item.

```lua
local RecommendationService = game:GetService("RecommendationService")

local function logLike(itemId, tracingId)
    local detail: RecommendationActionEventDetails = {
        ReactionType = "Like",
        Weight = 1.0
    }
    RecommendationService:LogActionEvent(Enum.RecommendationActionType.AddReaction, itemId, tracingId, detail)
    print("Logged 'Like' action for item: " .. itemId)
end

-- Example usage (requires a valid itemId and tracingId from GenerateItemListAsync)
-- logLike("item-id", "tracing-id")
```

### Method: RecommendationService:LogImpressionEvent

**Signature:** `RecommendationService:LogImpressionEvent(impressionType: RecommendationImpressionType, itemId: string, tracingId: string, impressionEventDetails?: Dictionary): ()`

This function logs an impression event, such as a user viewing a
recommended item. It requires the `itemId` and a `tracingId` to associate
the impression with the recommendation context. Details like view duration
and position can be passed in the `impressionEventDetails` dictionary to
provide more context for the recommendation engine.

Logging impressions, especially `Duration`, is critical for recommendation
configurations that rank items based on view time.

This function can only be called from the **client**.

**Note:** Only `LogImpressionEvent` calls in production actually log
impressions. Calling this function in Studio doesn't have any effect; you
can call it as many times as you want when testing.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `impressionType` | `RecommendationImpressionType` |  | The enum for the type of the impression. |
| `itemId` | `string` |  | The item ID returned from registration and [GenerateItemListAsync](/docs/reference/engine/classes/RecommendationService.md). |
| `tracingId` | `string` |  | The tracing ID returned from the [GenerateItemListAsync](/docs/reference/engine/classes/RecommendationService.md) response. Each item has a `TracingId`. |
| `impressionEventDetails` | `Dictionary` | `nil` | A dictionary containing the following fields:  - `Duration` &mdash; The duration of the impression in seconds. - `Weight` &mdash; A number representing the weight of the impression.   Default is 1. - `ItemPosition` &mdash; The position of the item in the   recommendation list. - `DepartureIntent` &mdash; The [RecommendationDepartureIntent](/docs/reference/engine/enums/RecommendationDepartureIntent.md)   indicating the user's intent when leaving a view. For example,   `Positive` if the view is considered good. |

**Returns:** `()` — No return value.

**Log a user impression**

This code snippet demonstrates how to log a user impression, such as viewing
an item.

```lua
local RecommendationService = game:GetService("RecommendationService")

local function logView(itemId, tracingId)
    local detail: RecommendationImpressionEventDetails = {
        Duration = 5, -- User viewed for 5 seconds
        ItemPosition = 1,
        DepartureIntent = Enum.RecommendationDepartureIntent.Neutral
    }
    RecommendationService:LogImpressionEvent(Enum.RecommendationImpressionType.View, itemId, tracingId, detail)
    print("Logged 'View' impression for item: " .. itemId)
end

-- Example usage (requires a valid itemId and tracingId from GenerateItemListAsync)
-- logView("some-item-id", "some-tracing-id")
```

### Method: RecommendationService:LogPreferenceEvent

**Signature:** `RecommendationService:LogPreferenceEvent(preferenceType: RecommendationPreferenceType, targetType: RecommendationPreferenceTargetType, targetId: string, tracingId: string, itemId: string): ()`

This function logs a user preference signal, such as follow, unfollow,
mute, or unmute, directed at another user, a universe, or a custom content
tag. It requires a `preferenceType`, a `targetType`, and a `targetId`
whose format depends on the target type: the user key for
[User](/docs/reference/engine/enums/RecommendationPreferenceTargetType.md), the universe ID as a
string for [Universe](/docs/reference/engine/enums/RecommendationPreferenceTargetType.md), or
the tag string for
[CustomTag](/docs/reference/engine/enums/RecommendationPreferenceTargetType.md). When the
preference originates from a recommendation card served by
[GenerateItemListAsync](/docs/reference/engine/classes/RecommendationService.md),
pass the card's `tracingId` and `itemId` to correlate the event with the
recommendation context; otherwise pass empty strings for both.

Logging preferences helps the recommendation engine personalize future
results across every recommendation surface, not just item feeds.

This function can only be called from the **client**.

**Note:** Only `LogPreferenceEvent` calls in production actually log
preferences. Calling this function in Studio doesn't have any effect; you
can call it as many times as you want when testing.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `preferenceType` | `RecommendationPreferenceType` |  | The enum for the type of preference. |
| `targetType` | `RecommendationPreferenceTargetType` |  | The enum for the type of target. |
| `targetId` | `string` |  | The identifier of the preference target. The format depends on `targetType`. |
| `tracingId` | `string` |  | The tracing ID returned from the [GenerateItemListAsync](/docs/reference/engine/classes/RecommendationService.md) response. Pass an empty string if the preference originates outside a recommendation feed. |
| `itemId` | `string` |  | The item ID returned from the [GenerateItemListAsync](/docs/reference/engine/classes/RecommendationService.md) response. Pass an empty string if the preference originates outside a recommendation feed. |

**Returns:** `()` — No return value.

### Method: RecommendationService:RegisterItemAsync

**Signature:** `RecommendationService:RegisterItemAsync(player: Player, registerRecommendationItemsRequest: Dictionary): Dictionary`

This function registers a new item to be included in recommendations. It
requires a `player` object and a `registerRecommendationItemsRequest`
dictionary containing details about the item, such as its content type,
reference ID, and custom tags. It returns a dictionary with the `ItemId`
and the `ReferenceId` of the newly registered item.

When selecting a `ContentType`, choose the type that best represents your
item. Note that different content types are not ranked against each other
directly. Instead, they are mixed into the final recommendation list based
on a configured ratio. For example, a configuration might display one
`Static` item for every ten items. If your experience only features a
single type of content, ensure that all registered items share the same
`ContentType`.

The `ItemId` is a unique ID returned by the `RecommendationService`. All
functions in the `RecommendationService` use the `ItemId` as input and
output.

The `ReferenceId` is a developer-provided identifier for an item. To make
sure that this reference ID is unique, we recommend that you use a UUID.
You can use this reference ID as a key to store rendering-specific
metadata in a data store.

When you register an item, you should only provide information that is
relevant for ranking and recommendations. All other data needed for
rendering should be stored separately in, for example, a data store. This
approach decouples the recommendation logic from the rendering process,
and results in a system that is more modular and easier to maintain.

`Attributes` is a list of content attributes associated with the item.
Each attribute in the list can contain the following fields:

- `AssetId` &mdash; The ID of an asset, such as an image or video.
- `Text` &mdash; A short text string, like a title.
- `Description` &mdash; A longer text description for the attribute.
- `SeekStartTime` / `SeekEndTime` &mdash; The start and end times for
  seeking within video content.
- `TrimStartTime` / `TrimEndTime` &mdash; The start and end times for
  trimming video content.

Common Error Codes:

- **HTTP 403 (Forbidden)** &mdash; This error can occur when you call
  `RegisterItemAsync` from Studio. Even if you run it as a server script
  in Studio, the request is not issued from a Roblox server. To resolve
  this, publish your experience and run it in the Roblox client.
- **HTTP 400 (Bad Request)** &mdash; This error indicates that a parameter
  is malformed. Common causes include a custom tag containing a comma or
  the `Attributes` table exceeding its size limit. If you encounter a 400
  error and have a large `Attributes` table, try reducing its size.
  Remember to only include attributes that are relevant for ranking.

This function can only be called from the **server**.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The player who created the item. |
| `registerRecommendationItemsRequest` | `Dictionary` |  | A dictionary containing the following fields:  - `ContentType` &mdash; The [RecommendationItemContentType](/docs/reference/engine/enums/RecommendationItemContentType.md)   specifying the type of content. Type is defined in a generic way.   For example, you can use `Static` for images, `Dynamic` for videos,   and `Interactive` for 3D models that support interaction. - `ReferenceId` &mdash; The developer-defined string that uniquely   identifies the item. - `Duration` &mdash; The duration of the content in seconds. - `Attributes` &mdash; The table of attributes for the item, such as   `AssetId` or `Description`. - `CustomTags` &mdash; The list of string tags for filtering and   boosting. Individual custom tags can't contain commas. - `Visibility` &mdash; The   [RecommendationItemVisibility](/docs/reference/engine/enums/RecommendationItemVisibility.md)   enum that controls the item's visibility, such as `Public` or   `Private`. |

**Returns:** `Dictionary` — A table with only two fields: `ItemId` and `ReferenceId`.

**Register a new item**

This code snippet demonstrates how to register a new item for recommendations.

```lua
local RecommendationService = game:GetService("RecommendationService")
local storage = game:GetService("ReplicatedStorage")

-- Assume a RemoteFunction named 'RegisterItemRemote' exists in ReplicatedStorage
local registerItemRemote = storage.RegisterItemRemote

registerItemRemote.OnServerInvoke = function(player, refId)
    local request: RegisterRecommendationItemRequest = {
        ContentType = Enum.RecommendationItemContentType.Dynamic,
        ReferenceId = refId,
        Duration = 60,
        Visibility = Enum.RecommendationItemVisibility.Public,
        CustomTags = {"locale:en-us", "seasonal:summer"},
        Attributes = {
			{
				AssetId = 123,
				Description = "test video",
				TrimStartTime = 0,
				TrimEndTime = 10.5
			}
		}
    }

    local success, response = pcall(function()
        return RecommendationService:RegisterItemAsync(player, request)
    end)
    if success and response then
        print("Successfully registered item. ItemId: " .. response.ItemId)
        return response.ItemId
    else
        warn("Failed to register item. Error: " .. tostring(response))
        return nil
    end
end
```

### Method: RecommendationService:RemoveItemAsync

**Signature:** `RecommendationService:RemoveItemAsync(itemId: string): ()`

This function removes an item from the recommendation system. It takes the
`itemId` of the item to be deleted as a parameter.

This function can be called from both the **server** and the **client**,
with the following limitations:

- When called from the server, it can only remove items registered under
  the same `universeId`.
- When called from the client, it can only remove items registered by the
  current `player`.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `itemId` | `string` |  | The itemId to remove. |

**Returns:** `()` — No return value.

**Remove an item**

This code snippet demonstrates how to remove an item from the recommendation
system.

```lua
local RecommendationService = game:GetService("RecommendationService")

local function removeItem(itemId)
    local success, err = pcall(function()
        return RecommendationService:RemoveItemAsync(itemId)
    end)
    if success then
        print("Successfully removed item: " .. itemId)
    else
        warn("Failed to remove item: " .. itemId .. ". Error: " .. tostring(err))
    end
end
```

### Method: RecommendationService:UpdateItemAsync

**Signature:** `RecommendationService:UpdateItemAsync(updateRecommendationItemRequest: Dictionary): ()`

This function updates the attributes of an existing recommendation item.
It takes an `updateRecommendationItemRequest` dictionary containing the
`itemId` and the fields to be updated. Any fields not included in the
request will remain unchanged.

Items with their
[RecommendationItemVisibility](/docs/reference/engine/enums/RecommendationItemVisibility.md) set to
`Private` are not recommended to other users, but they can still be
returned when a user requests their own creations by using the
`ConfigName` of `PlayerOwnedItems`.

In Roblox Moments, moderated items are set to `Private`. While this
prevents other users from seeing them, the item creator can still see
these moderated items and check their moderation status in their **My
Moments** tab.

This function can only be called from the **server**.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `updateRecommendationItemRequest` | `Dictionary` |  | A dictionary containing the following fields:  - `ItemId` &mdash; The ID of the item to update. - `ReferenceId` &mdash; The new developer-defined string to identify   the item. - `Creator` &mdash; The new creator for the item. Creator is a table   containing two fields: `CreatorId: number` and   `CreatorType: Enum.CreatorType`. - `Duration` &mdash; The new duration for the content in seconds. - `Visibility` &mdash; The new visibility setting for the item. - `Attributes` &mdash; The new table of attributes for the item. - `CustomTags` &mdash; The new list of string tags. Individual custom   tags can't contain commas. |

**Returns:** `()` — No return value.

**Update an item**

This code snippet demonstrates how to update an existing recommendation item.

```lua
local RecommendationService = game:GetService("RecommendationService")

local function updateItem(itemId)
    -- Only include the fields you want to update
    local request: UpdateRecommendationItemRequest = {
        ItemId = itemId,
        Visibility = Enum.RecommendationItemVisibility.Private,
        -- NOTE: the whole CustomTags list will be replaced with this new list
        CustomTags = {"updated-tag"}
    }

    local success, err = pcall(function()
        return RecommendationService:UpdateItemAsync(request)
    end)
    if success then
        print("Successfully updated item: " .. itemId)
    else
        warn("Failed to update item: " .. itemId .. ". Error: " .. tostring(err))
    end
end

-- Example usage
-- updateItem("some-item-id-to-update")
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