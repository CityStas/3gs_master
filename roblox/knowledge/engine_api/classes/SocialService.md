---
name: SocialService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "Facilitates social functions that impact relationships made on the Roblox platform."
---

# Class: SocialService

> Facilitates social functions that impact relationships made on the Roblox
> platform.

## Description

**SocialService** facilitates social functions that impact relationships made
on the Roblox platform. Its primary usage is to show
[invite prompts](/docs/en-us/production/promotion/invite-prompts.md) and the
phone book to players, allowing them to send invitation requests to their
friends through [PromptGameInvite()](/docs/reference/engine/classes/SocialService.md)
and [PromptPhoneBook()](/docs/reference/engine/classes/SocialService.md) respectively.
You may leverage signals when such requests are made.

## Methods

### Method: SocialService:CanSendCallInviteAsync

**Signature:** `SocialService:CanSendCallInviteAsync(player: Instance): boolean`

Returns `true` if the given [Player](/docs/reference/engine/classes/Player.md) can send a call invite to a
friend. You should always use the result of this method before calling
[PromptPhoneBook()](/docs/reference/engine/classes/SocialService.md) since the
ability to open the phone book may vary depending on the player.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The [Player](/docs/reference/engine/classes/Player.md) instance of the player potentially sending a call invite. |

**Returns:** `boolean` — Whether the specified player can send a call invite.

**SocialService:PromptPhoneBook()**

The following code sample, placed within a child [LocalScript](/docs/reference/engine/classes/LocalScript.md) of a
[GuiButton](/docs/reference/engine/classes/GuiButton.md), uses
[CanSendCallInviteAsync()](/docs/reference/engine/classes/SocialService.md) to
confirm that the player can make a call. If so, it connects
[PromptPhoneBook()](/docs/reference/engine/classes/SocialService.md) to the button's
[Activated](/docs/reference/engine/classes/GuiButton.md) event.

```lua
local Players = game:GetService("Players")
local SocialService = game:GetService("SocialService")

local player = Players.LocalPlayer
local button = script.Parent
button.Visible = false

-- Function to check whether the player can send a call invite
local function canSendCallingInvite(sendingPlayer)
	local success, canSend = pcall(function()
		return SocialService:CanSendCallInviteAsync(sendingPlayer)
	end)
	return success and canSend
end

local canCall = canSendCallingInvite(player)
if canCall then
	button.Visible = true
	button.Activated:Connect(function()
		SocialService:PromptPhoneBook(player, "")
	end)
end
```

### Method: SocialService:CanSendGameInviteAsync

**Signature:** `SocialService:CanSendGameInviteAsync(player: Instance, recipientId?: User): boolean`

[CanSendGameInviteAsync()](/docs/reference/engine/classes/SocialService.md)
returns `true` if the given [Player](/docs/reference/engine/classes/Player.md) can invite other players to the
current experience. You should always use the result of this method before
calling [PromptGameInvite()](/docs/reference/engine/classes/SocialService.md) since
the ability to invite players may vary depending on the platform or
player.

See
[Player Invite Prompts](/docs/en-us/production/promotion/invite-prompts.md)
for more details on implementing player invite prompts, customizing
prompts and notifications, and using launch data.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The [Player](/docs/reference/engine/classes/Player.md) instance of the player potentially sending an invite. |
| `recipientId` | `User` | `U1.AQAAAAAAAAAAAAAAAAAAAAA` | Optional [Player.UserId](/docs/reference/engine/classes/Player.md) of the potential **recipient**, used to check whether the sender can invite that specific recipient. |

**Returns:** `boolean` — Whether the specified player can send an invite.

**Sending an Invite**

The following code sample uses
[CanSendGameInviteAsync()](/docs/reference/engine/classes/SocialService.md) to
confirm whether the local [Player](/docs/reference/engine/classes/Player.md) can send an invite. If `true`, it
then prompts the invite using
[PromptGameInvite()](/docs/reference/engine/classes/SocialService.md).

```lua
local SocialService = game:GetService("SocialService")
local Players = game:GetService("Players")

local player = Players.LocalPlayer

-- Function to check whether the player can send an invite
local function canSendGameInvite(sendingPlayer)
	local success, canSend = pcall(function()
		return SocialService:CanSendGameInviteAsync(sendingPlayer)
	end)
	return success and canSend
end

local canInvite = canSendGameInvite(player)
if canInvite then
	SocialService:PromptGameInvite(player)
end
```

### Method: SocialService:GetEventRsvpStatusAsync

**Signature:** `SocialService:GetEventRsvpStatusAsync(eventId: string): RsvpStatus`

Returns the local player's RSVP status for the given event. Events must be
in the current experience and must not have already started. If the event
has already started, this method will return an error.

Use
[GetUpcomingExperienceEventsAsync()](/docs/reference/engine/classes/SocialService.md)
to obtain a valid event ID at runtime rather than hardcoding one. Note
that you can use
[PromptRsvpToEventAsync()](/docs/reference/engine/classes/SocialService.md) to
prompt the player to change their RSVP status for the event.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `eventId` | `string` |  | The event ID of the event to prompt the player to change their RSVP status for. This must be a valid event ID that exists in the current experience, represented as a string (not a number). |

**Returns:** `RsvpStatus` — Returns an [RsvpStatus](/docs/reference/engine/enums/RsvpStatus.md) indicating the player's current RSVP
status for the event. If the player has not RSVP'd to the event, this
will return [RsvpStatus.None](/docs/reference/engine/enums/RsvpStatus.md).

**SocialService:PromptRsvpToEventAsync()**

The following example checks if a player is RSVP'd to an event; if not, it
gives them the option to RSVP. If the player is already RSVP'd, it gives them
the option to cancel their RSVP.

The following [Script](/docs/reference/engine/classes/Script.md) assumes that
[RunContext](/docs/reference/engine/classes/BaseScript.md) is set to [RunContext.Client](/docs/reference/engine/enums/RunContext.md)
and that two sibling [ProximityPrompts](/docs/reference/engine/classes/ProximityPrompt.md) are in place:
one for following the event and one for unfollowing the event. The prompts are
enabled or disabled based on the player's RSVP status.

```lua
local SocialService = game:GetService("SocialService")

local EVENT_ID = "YOUR_EVENT_ID"

local followPrompt: ProximityPrompt = script.Parent.FollowProximityPrompt
local unFollowPrompt: ProximityPrompt = script.Parent.UnfollowProximityPrompt

local function updatePrompt(rsvpStatus: Enum.RsvpStatus)
	if rsvpStatus == Enum.RsvpStatus.Going then
		unFollowPrompt.Enabled = true
		followPrompt.Enabled = false
	else
		unFollowPrompt.Enabled = false
		followPrompt.Enabled = true
	end
end

local success, currentRsvpStatus = pcall(function()
	return SocialService:GetEventRsvpStatusAsync(EVENT_ID)
end)

if not success then
	-- Could not retrieve RSVP status; don't enable either proximity prompt
	warn("Failed to get RSVP status:", currentRsvpStatus)
	return
end

print("CurrentRsvpStatus:", currentRsvpStatus)

updatePrompt(currentRsvpStatus)

unFollowPrompt.Triggered:Connect(function(player)
	local rsvpStatus = SocialService:PromptRsvpToEventAsync(EVENT_ID)
	updatePrompt(rsvpStatus)
end)

followPrompt.Triggered:Connect(function(player)
	local rsvpStatus = SocialService:PromptRsvpToEventAsync(EVENT_ID)
	updatePrompt(rsvpStatus)
end)
```

### Method: SocialService:GetExperienceEventAsync

**Signature:** `SocialService:GetExperienceEventAsync(eventId: string): ExperienceEvent?`

`GetExperienceEventAsync()` yields until the request completes and then
returns a dictionary describing the requested event. The dictionary
contains the following fields:

- `Id` (string)
- `Title` (string)
- `Subtitle` (string)
- `Description` (string)
- `DisplayTitle` (string)
- `DisplaySubtitle` (string)
- `DisplayDescription` (string)
- `ThumbnailIds` (array of numbers): Asset IDs for the event thumbnails.
  The first ID is the primary thumbnail.
- `StartTime` (dictionary)
  - `Day` (number)
  - `Year` (number)
  - `Month` (number)
  - `Minute` (number)
  - `Millisecond` (number)
  - `Hour` (number)
  - `Second` (number)
- `EndTime` (dictionary)
  - `Day` (number)
  - `Year` (number)
  - `Month` (number)
  - `Minute` (number)
  - `Millisecond` (number)
  - `Hour` (number)
  - `Second` (number)
- `HasStarted` (boolean)
- `HasEnded` (boolean)
- `Status` ([ExperienceEventStatus](/docs/reference/engine/enums/ExperienceEventStatus.md))
- `UserRsvpStatus` ([RsvpStatus](/docs/reference/engine/enums/RsvpStatus.md) or `nil`)

If the event cannot be found, belongs to a different experience, or the
response is malformed, this method returns `nil`. Requests may also fail
with a `HttpError <status>` message if the service returns an unexpected
error code.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `eventId` | `string` |  | The string identifier of the event to retrieve. Must correspond to an event in the current experience. |

**Returns:** `ExperienceEvent?` — A dictionary describing the event, or `nil` if the event does not
exist, belongs to another experience, or is otherwise unavailable.

**SocialService:GetUpcomingExperienceEventsAsync()**

Finds the next event that has not started and prompts the player to RSVP. This
avoids hardcoded IDs by discovering events at runtime.

```lua
local SocialService = game:GetService("SocialService")

-- Discover the next upcoming/active event and prompt the player to RSVP
local function promptNextUpcomingEvent()
	local success, eventsOrError = pcall(function()
		return SocialService:GetUpcomingExperienceEventsAsync()
	end)
	if not success then
		warn("Failed to load upcoming events:", eventsOrError)
		return
	end

	local upcomingEvents = eventsOrError

	local selectedEvent
	for _, event in ipairs(upcomingEvents) do
		if not event.HasStarted and not event.HasEnded then
			selectedEvent = event
			break
		end
	end

	if selectedEvent then
		local success, result = pcall(function()
			return SocialService:PromptRsvpToEventAsync(selectedEvent.Id)
		end)
		if not success then
			warn("RSVP prompt failed:", result)
		end
	else
		warn("No future events available to prompt.")
		return
	end
end

promptNextUpcomingEvent()
```

### Method: SocialService:GetPartyAsync

**Signature:** `SocialService:GetPartyAsync(partyId: string): Array`

Returns an array of dictionaries containing data for all members
associated with the given `partyId`. The returned array reflects the
current state of the party across all active server instances within the
experience and it is ordered by the time each party member accepted the
party invite. This means the first element in the array is the earliest to
accept and the last is the most recent.

This method is useful for retrieving up-to-date information about all
party members currently in the experience and across different servers,
enabling coordinated group behavior such as teleportation, matchmaking, or
party-based gameplay logic.

Each dictionary in the returned array contains the following fields:

| Key | Value Type | Description |
| --- | --- | --- |
| `UserId` | number | The player's [Player.UserId](/docs/reference/engine/classes/Player.md) property. |
| `PlaceId` | number | The [DataModel.PlaceId](/docs/reference/engine/classes/DataModel.md) of the place the party member is currently in. |
| `JobId` | string | The [DataModel.JobId](/docs/reference/engine/classes/DataModel.md) of the server instance the user currently resides in. |
| `PrivateServerId` | string | If applicable, the [DataModel.PrivateServerId](/docs/reference/engine/classes/DataModel.md) when the party member is in a private or reserved server. |
| `ReservedServerAccessCode` | string | If applicable, the legacy access code for the reserved server that the user currently resides in. For new work, use [TeleportOptions.ReservedServerId](/docs/reference/engine/classes/TeleportOptions.md) with [TeleportService:TeleportAsync()](/docs/reference/engine/classes/TeleportService.md) instead. |

To test this service in your experience, use the
[Party Simulator](/docs/en-us/studio/testing-modes.md#party-simulation) in
Roblox Studio or publish the experience and play it in the Roblox
application.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `partyId` | `string` |  | The unique identifier of the party to retrieve member data for, corresponding to a [Player.PartyId](/docs/reference/engine/classes/Player.md) value. |

**Returns:** `Array` — An array of dictionaries representing the members of the specified
party who are currently in the experience.

**SocialService:GetPartyAsync()**

The following example checks if a player is in a party when they join. If so,
it retrieves the latest party data using [SocialService:GetPartyAsync()](/docs/reference/engine/classes/SocialService.md)
and outputs the details of each party member.

```lua
local SocialService = game:GetService("SocialService")
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	local partyId = player.PartyId

	if partyId == "" then
		warn("Player is not in a party")
		return
	end

	local success, partyData = pcall(function()
		return SocialService:GetPartyAsync(partyId)
	end)

	if success and partyData then
		for _, partyMemberData in partyData do
			print(
				partyMemberData.UserId,
				partyMemberData.PlaceId,
				partyMemberData.JobId,
				partyMemberData.PrivateServerId,
				partyMemberData.ReservedServerAccessCode
			)
		end
	else
		warn("Failed to retrieve party data")
	end
end)
```

### Method: SocialService:GetPlayersByPartyId

**Signature:** `SocialService:GetPlayersByPartyId(partyId: string): List<Player>`

Returns a table of all presently connected [Player](/docs/reference/engine/classes/Player.md) objects whose
[Player.PartyId](/docs/reference/engine/classes/Player.md) property matches the provided `partyId`. This
method behaves similarly to [Players:GetPlayers()](/docs/reference/engine/classes/Players.md) but filters the
results to include only those players belonging to the specified party.

To test this service in your experience, use the
[Party Simulator](/docs/en-us/studio/testing-modes.md#party-simulation) in
Roblox Studio or publish the experience and play it in the Roblox
application.

*Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `partyId` | `string` |  | The unique identifier of the party to filter players by, corresponding to a [Player.PartyId](/docs/reference/engine/classes/Player.md) value. |

**Returns:** `List<Player>` — A table of [Player](/docs/reference/engine/classes/Player.md) objects whose [Player.PartyId](/docs/reference/engine/classes/Player.md)
property matches the passed `partyId`.

**SocialService:GetPlayersByPartyId()**

The following example listens for when a player joins the experience. If the
player is part of a party, it uses [SocialService:GetPlayersByPartyId()](/docs/reference/engine/classes/SocialService.md)
to retrieve all players in the same party who are currently connected to the
server. It then outputs the name of each party member.

```lua
local SocialService = game:GetService("SocialService")
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	local partyId = player.PartyId

	if partyId ~= "" then
		local partyPlayers: { Player } = SocialService:GetPlayersByPartyId(partyId)

		for _, partyMember in partyPlayers do
			print("Party Member: " .. partyMember.Name)
		end
	else
		warn("Player is not in a party")
	end
end)
```

**Team Rebalance with Party Integration**

This code sample demonstrates how to assign players to [Teams](/docs/reference/engine/classes/Team.md)
based on their [Player.PartyId](/docs/reference/engine/classes/Player.md) using the
[SocialService:GetPlayersByPartyId()](/docs/reference/engine/classes/SocialService.md) method. When a player joins the
experience, the script checks whether they're part of a party. If so, it
attempts to assign them to the same team as other party members. If no match
is found or the player isn't in a party, they're placed on the team with fewer
members to maintain balance.

```lua
local Teams = game:GetService("Teams")
local Players = game:GetService("Players")
local SocialService = game:GetService("SocialService")

local redTeam = Instance.new("Team")
redTeam.Name = "Red Team"
redTeam.TeamColor = BrickColor.Red()
redTeam.AutoAssignable = false
redTeam.Parent = Teams

local blueTeam = Instance.new("Team")
blueTeam.Name = "Blue Team"
blueTeam.TeamColor = BrickColor.Blue()
blueTeam.AutoAssignable = false
blueTeam.Parent = Teams

local function assignPlayerToTeam(player)
	local partyId = player.PartyId

	if partyId == "" then
		assignBalancedTeam(player)
		return
	end

	local teams = { redTeam, blueTeam }
	local matchingTeam = nil
	local partyPlayers = SocialService:GetPlayersByPartyId(partyId)

	for _, partyPlayer in partyPlayers do
		if partyPlayer ~= player and table.find(teams, partyPlayer.Team) then
			matchingTeam = partyPlayer.Team
			break
		end
	end

	if matchingTeam then
		player.Team = matchingTeam
		player.TeamColor = matchingTeam.TeamColor
	else
		assignBalancedTeam(player)
	end
end

function assignBalancedTeam(player)
	local redCount = #redTeam:GetPlayers()
	local blueCount = #blueTeam:GetPlayers()
	local chosenTeam = redCount <= blueCount and redTeam or blueTeam

	player.Team = chosenTeam
	player.TeamColor = chosenTeam.TeamColor
end

local function groupPlayersByParty()
	local seenPartyIds = {}
	local groupedPlayers = {}

	for _, player in Players:GetPlayers() do
		if player.PartyId == "" then
			table.insert(groupedPlayers, { player })
		elseif not table.find(seenPartyIds, player.PartyId) then
			table.insert(seenPartyIds, player.PartyId)

			local partyPlayers = SocialService:GetPlayersByPartyId(player.PartyId)
			table.insert(groupedPlayers, partyPlayers)
		end
	end

	return groupedPlayers
end

-- Call this function to rebalance teams
local function rebalanceTeams()
	local groups = groupPlayersByParty()

	table.sort(groups, function(a, b)
		return #a > #b
	end)

	for _, player in Players:GetPlayers() do
		player.Team = nil
	end

	for _, group in groups do
		local redCount = #redTeam:GetPlayers()
		local blueCount = #blueTeam:GetPlayers()

		local bestTeam
		if redCount <= blueCount then
			bestTeam = redTeam
		else
			bestTeam = blueTeam
		end

		for _, player in group do
			player.Team = bestTeam
			player.TeamColor = bestTeam.TeamColor
		end
	end

	for _, player in Players:GetPlayers() do
		player:LoadCharacterAsync()
	end
end

Players.PlayerAdded:Connect(function(player)
	assignPlayerToTeam(player)

	player:LoadCharacterAsync()

	player:GetPropertyChangedSignal("PartyId"):Connect(function()
		if player.PartyId ~= "" then
			assignPlayerToTeam(player)
		end
	end)
end)
```

### Method: SocialService:GetUpcomingExperienceEventsAsync

**Signature:** `SocialService:GetUpcomingExperienceEventsAsync(): List<ExperienceEvent>`

`GetUpcomingExperienceEventsAsync()` yields while the client requests data
for the current experience and then returns an array of dictionaries, each
with the same structure described in
[GetExperienceEventAsync()](/docs/reference/engine/classes/SocialService.md).
The array includes only events that are currently active or have not yet
ended, excluding cancelled, moderated, or unpublished events. Results are
sorted so the soonest start time appears first.

Use this method to discover valid event IDs at runtime rather than
hardcoding them; hardcoded IDs become stale when events end and cause RSVP
prompts to fail until the experience is republished.

If the service indicates there are no matching events, this method returns
an empty array. Requests may raise a `HttpError <status>` message if the
service returns an unexpected error code.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Returns:** `List<ExperienceEvent>` — An array of dictionaries describing each active or upcoming event in
the current experience, ordered by soonest start time first.

**SocialService:GetUpcomingExperienceEventsAsync()**

Finds the next event that has not started and prompts the player to RSVP. This
avoids hardcoded IDs by discovering events at runtime.

```lua
local SocialService = game:GetService("SocialService")

-- Discover the next upcoming/active event and prompt the player to RSVP
local function promptNextUpcomingEvent()
	local success, eventsOrError = pcall(function()
		return SocialService:GetUpcomingExperienceEventsAsync()
	end)
	if not success then
		warn("Failed to load upcoming events:", eventsOrError)
		return
	end

	local upcomingEvents = eventsOrError

	local selectedEvent
	for _, event in ipairs(upcomingEvents) do
		if not event.HasStarted and not event.HasEnded then
			selectedEvent = event
			break
		end
	end

	if selectedEvent then
		local success, result = pcall(function()
			return SocialService:PromptRsvpToEventAsync(selectedEvent.Id)
		end)
		if not success then
			warn("RSVP prompt failed:", result)
		end
	else
		warn("No future events available to prompt.")
		return
	end
end

promptNextUpcomingEvent()
```

### Method: SocialService:HideSelfView

**Signature:** `SocialService:HideSelfView(): ()`

Hides the calling player's self view. If this method is called while the
self view is already hidden, it does nothing.

*Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Returns:** `()`

### Method: SocialService:PromptFeedbackSubmissionAsync

**Signature:** `SocialService:PromptFeedbackSubmissionAsync(options: Dictionary?): ()`

Displays a dialog to the player, allowing them to provide feedback about
their experience or submit a player support ticket.

- The submitted feedback becomes available to developers in the Creator
  Dashboard under the **Audience** > **Feedback** section.
- The submitted player support requests become available to developers in
  the Creator Dashboard under the **Audience** > **Player Support**
  section. The Player Support flow is currently in **alpha** and is only
  available to select experiences.

This method yields until the player either submits feedback, dismisses the
dialog, or a timeout is reached. As an asynchronous operation, it should
be called using `task.spawn()` or within a coroutine.

#### Feedback Types

The `FeedbackType` key in the options dictionary determines which flow is
displayed:

- [FeedbackType.Feedback](/docs/reference/engine/enums/FeedbackType.md) (default) — Displays a general feedback
  prompt where the player can rate and comment on the experience.
- [FeedbackType.PlayerSupport](/docs/reference/engine/enums/FeedbackType.md) — (**Alpha; select experiences only**)
  Displays a player support flow where the player can submit a categorized
  support ticket directly to the experience developer. This enables
  in-experience customer support without requiring players to leave the
  game.

#### Feedback Flow

When `FeedbackType` is [FeedbackType.Feedback](/docs/reference/engine/enums/FeedbackType.md) (or omitted), the
player is shown a general feedback prompt where they can rate and
optionally comment on the experience. Submitted feedback appears in the
Creator Dashboard under **Audience** > **Feedback**. Players can submit
feedback once per day per experience.

#### Player Support Flow (Alpha)

When `FeedbackType` is set to [FeedbackType.PlayerSupport](/docs/reference/engine/enums/FeedbackType.md), the
player is guided through a support ticket submission flow. This flow is
currently in **alpha** and is only available to select experiences. The
prompt presents a form where the player selects a category, writes a
description of their issue, and chooses whether to share their user ID
with the developer. The available categories are:

| Category | Description |
| --- | --- |
| Bug Report | The player is reporting a bug or technical issue. |
| Data Restore Request | The player is requesting that lost or corrupted data be restored. |
| Purchasing Issue | The player has an issue with an in-experience purchase. |
| Other | A general issue that does not fit the other categories. |

The player also chooses whether to share their [Player.UserId](/docs/reference/engine/classes/Player.md) with
the developer as part of the ticket.

#### Eligibility

Before showing the prompt, this method performs an eligibility check. The
eligibility rules differ depending on the feedback type.

A player is ineligible for the **Feedback** flow if:

- The player is the experience owner (developers cannot submit feedback
  for their own experiences).
- The player has been rate limited (submitted too many reviews recently).
- The player does not meet age requirements.

A player is ineligible for the **Player Support** flow if:

- The player does not meet age requirements.
- The player already has 5 in-progress tickets.
- The player is banned from the experience.

If the player is ineligible, the prompt displays a message indicating that
feedback or support is unavailable and the method returns without error.

#### Notes

- This service does not work during playtesting in Roblox Studio. To test
  the feedback prompt, you must publish the experience and play it in the
  Roblox application.
- The method will time out and resume if the player does not interact with
  the prompt within a reasonable period.
- If the submission fails due to a text filter violation or network error,
  the player is notified within the dialog.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `options` | `Dictionary?` |  | Optional `Dictionary` configuring the prompt. Supported keys: - `FeedbackType` ([FeedbackType](/docs/reference/engine/enums/FeedbackType.md)). Selects which feedback flow to display. Defaults to [FeedbackType.Feedback](/docs/reference/engine/enums/FeedbackType.md). |

**Returns:** `()`

**SocialService:PromptFeedbackSubmissionAsync()**

The following example shows how to prompt players for feedback at appropriate
moments in your experience, such as after reaching a milestone or completing a
level.

```lua
local SocialService = game:GetService("SocialService")

-- Function to prompt for feedback
local function promptForFeedback()
    local success, errorMessage = pcall(function()
        SocialService:PromptFeedbackSubmissionAsync()
    end)

    if success then
        print("Feedback prompt completed")
    else
        warn("Failed to prompt for feedback:", errorMessage)
    end
end

-- Prompt for feedback when player reaches a milestone
local function onMilestoneReached()
    promptForFeedback()
end

-- Example usage: Connect to a game event
game.ReplicatedStorage.MilestoneReached.OnClientEvent:Connect(onMilestoneReached)
```

**SocialService:PromptFeedbackSubmissionAsync() — Player Support**

The following example shows how to prompt players to submit a support ticket
from within an experience, such as from a help menu button.

```lua
local SocialService = game:GetService("SocialService")

local function promptPlayerSupport()
    local success, errorMessage = pcall(function()
        SocialService:PromptFeedbackSubmissionAsync({
            FeedbackType = Enum.FeedbackType.PlayerSupport,
        })
    end)

    if success then
        print("Player support prompt completed")
    else
        warn("Failed to prompt for player support:", errorMessage)
    end
end

-- Example usage: Connect to a help button in a ScreenGui
local helpButton = script.Parent:WaitForChild("HelpButton")
helpButton.Activated:Connect(function()
    task.spawn(promptPlayerSupport)
end)
```

### Method: SocialService:PromptGameInvite

**Signature:** `SocialService:PromptGameInvite(player: Instance, experienceInviteOptions?: Instance): ()`

[PromptGameInvite()](/docs/reference/engine/classes/SocialService.md) displays an
invite prompt to the local player through which they may invite their
friends to the current experience. Before calling this method, you should
use
[CanSendGameInviteAsync()](/docs/reference/engine/classes/SocialService.md) to
determine whether the player can send an invite, as this ability may vary
depending on the platform or player.

See
[Player Invite Prompts](/docs/en-us/production/promotion/invite-prompts.md)
for more details on implementing invite prompts, customizing prompts and
notifications, and using launch data.

*Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The [Player](/docs/reference/engine/classes/Player.md) to prompt with the invite popup. |
| `experienceInviteOptions` | `Instance` | `nil` | Optional [ExperienceInviteOptions](/docs/reference/engine/classes/ExperienceInviteOptions.md) object for customizing the prompt. |

**Returns:** `()`

**Sending an Invite**

The following code sample uses
[CanSendGameInviteAsync()](/docs/reference/engine/classes/SocialService.md) to
confirm whether the local [Player](/docs/reference/engine/classes/Player.md) can send an invite. If `true`, it
then prompts the invite using
[PromptGameInvite()](/docs/reference/engine/classes/SocialService.md).

```lua
local SocialService = game:GetService("SocialService")
local Players = game:GetService("Players")

local player = Players.LocalPlayer

-- Function to check whether the player can send an invite
local function canSendGameInvite(sendingPlayer)
	local success, canSend = pcall(function()
		return SocialService:CanSendGameInviteAsync(sendingPlayer)
	end)
	return success and canSend
end

local canInvite = canSendGameInvite(player)
if canInvite then
	SocialService:PromptGameInvite(player)
end
```

### Method: SocialService:PromptLinkSharingAsync

**Signature:** `SocialService:PromptLinkSharingAsync(player: Player, options?: Dictionary): Tuple`

This call is restricted to server scripts. After a link is successfully
generated, the target player will either be prompted to open a share sheet
with the generated link, or the link will be copied directly to the
clipboard if share sheet functionality is not available to the player.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | Prompts the given [Player](/docs/reference/engine/classes/Player.md) with a Roblox platform-level share sheet with a generated share link. |
| `options` | `Dictionary` | `nil` | `Dictionary` that specifies the configuration for the generated link. It includes the following optional key-value pairs:  - `FallbackLinkId` (string). Determines how this share link will   direct player to once expired. Default to experience join link. - `ExpirationSeconds` (number). Determines time to expiration once the   share link is created. Truncates to nearest integer. Defaults to   86,400. - `PreviewTitle` (string) Preview title of the share link. - `PreviewDescription` (string) Preview description of the share link. - `PreviewAssetId` (number) Image asset ID used for share link   preview. - `LaunchData` (string). Used to set a parameter in   [Player:GetJoinData()](/docs/reference/engine/classes/Player.md) when a player joined using the   generated share link. |

**Returns:** `Tuple` — A tuple containing an [PromptLinkSharingResult](/docs/reference/engine/enums/PromptLinkSharingResult.md) indicating the
result of the link sharing prompt.

**Prompt Link Sharing Async**

Demonstrates [SocialService:PromptLinkSharingAsync()](/docs/reference/engine/classes/SocialService.md).

```lua
local HttpService = game:GetService("HttpService")
local SocialService = game:GetService("SocialService")

local success, result  = pcall(function()
	local data = {
    	promoCode = "j7du67"
	}

	local launchData = HttpService:JSONEncode(data)

	local LinkSharingOptions = {
		ExpirationSeconds = 20000,
		PreviewTitle = "Awesome Game",
		PreviewDescription = "Lets play together",
		LaunchData = launchData,
	}

	return SocialService:PromptLinkSharingAsync(player, LinkSharingOptions)
end)

if not success or result ~= Enum.PromptLinkSharingResult.Success then
	warn("PromptLinkSharingAsync failed:", tostring(result))
end
```

### Method: SocialService:PromptPhoneBook

**Signature:** `SocialService:PromptPhoneBook(player: Instance, tag: string): ()`

Prompts the given [Player](/docs/reference/engine/classes/Player.md) with the phone book. If the player
chooses to call someone, the
[CallInviteStateChanged](/docs/reference/engine/classes/SocialService.md) event
fires. You should use
[CanSendCallInviteAsync()](/docs/reference/engine/classes/SocialService.md)
prior to calling [PromptPhoneBook()](/docs/reference/engine/classes/SocialService.md)
since the ability to see the phone book may vary depending on the player.

If a player is not eligible to open the phone book, an error dialog is
shown.

*Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The player to prompt with the phone book. |
| `tag` | `string` |  | String to help differentiate between various phone book "entry points" or similar. For example, you can pass a string defining what region of an experience the calling player's character is currently in. |

**Returns:** `()`

**SocialService:PromptPhoneBook()**

The following code sample, placed within a child [LocalScript](/docs/reference/engine/classes/LocalScript.md) of a
[GuiButton](/docs/reference/engine/classes/GuiButton.md), uses
[CanSendCallInviteAsync()](/docs/reference/engine/classes/SocialService.md) to
confirm that the player can make a call. If so, it connects
[PromptPhoneBook()](/docs/reference/engine/classes/SocialService.md) to the button's
[Activated](/docs/reference/engine/classes/GuiButton.md) event.

```lua
local Players = game:GetService("Players")
local SocialService = game:GetService("SocialService")

local player = Players.LocalPlayer
local button = script.Parent
button.Visible = false

-- Function to check whether the player can send a call invite
local function canSendCallingInvite(sendingPlayer)
	local success, canSend = pcall(function()
		return SocialService:CanSendCallInviteAsync(sendingPlayer)
	end)
	return success and canSend
end

local canCall = canSendCallingInvite(player)
if canCall then
	button.Visible = true
	button.Activated:Connect(function()
		SocialService:PromptPhoneBook(player, "")
	end)
end
```

### Method: SocialService:PromptRsvpToEventAsync

**Signature:** `SocialService:PromptRsvpToEventAsync(eventId: string): RsvpStatus`

`PromptRsvpToEventAsync()` displays a prompt to the local player through
which they may change their RSVP status to the given event.

Events must be in the current experience and must not have already
started. If the event has already started, this method will return an
error.

Note that you can use
[GetEventRsvpStatusAsync()](/docs/reference/engine/classes/SocialService.md)
to check the player's current RSVP status before calling this method.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `eventId` | `string` |  | The event ID of the event to prompt the player to change their RSVP status for. This must be a valid event ID that exists in the current experience, represented as a string (not a number). |

**Returns:** `RsvpStatus` — Returns a [RsvpStatus](/docs/reference/engine/enums/RsvpStatus.md) indicating the player's new RSVP status
after the prompt is closed. If the player closes the prompt without
changing their RSVP status, this will return [RsvpStatus.None](/docs/reference/engine/enums/RsvpStatus.md) or
their old [RsvpStatus](/docs/reference/engine/enums/RsvpStatus.md) if they had already selected a status.

**SocialService:PromptRsvpToEventAsync()**

The following example checks if a player is RSVP'd to an event; if not, it
gives them the option to RSVP. If the player is already RSVP'd, it gives them
the option to cancel their RSVP.

The following [Script](/docs/reference/engine/classes/Script.md) assumes that
[RunContext](/docs/reference/engine/classes/BaseScript.md) is set to [RunContext.Client](/docs/reference/engine/enums/RunContext.md)
and that two sibling [ProximityPrompts](/docs/reference/engine/classes/ProximityPrompt.md) are in place:
one for following the event and one for unfollowing the event. The prompts are
enabled or disabled based on the player's RSVP status.

```lua
local SocialService = game:GetService("SocialService")

local EVENT_ID = "YOUR_EVENT_ID"

local followPrompt: ProximityPrompt = script.Parent.FollowProximityPrompt
local unFollowPrompt: ProximityPrompt = script.Parent.UnfollowProximityPrompt

local function updatePrompt(rsvpStatus: Enum.RsvpStatus)
	if rsvpStatus == Enum.RsvpStatus.Going then
		unFollowPrompt.Enabled = true
		followPrompt.Enabled = false
	else
		unFollowPrompt.Enabled = false
		followPrompt.Enabled = true
	end
end

local success, currentRsvpStatus = pcall(function()
	return SocialService:GetEventRsvpStatusAsync(EVENT_ID)
end)

if not success then
	-- Could not retrieve RSVP status; don't enable either proximity prompt
	warn("Failed to get RSVP status:", currentRsvpStatus)
	return
end

print("CurrentRsvpStatus:", currentRsvpStatus)

updatePrompt(currentRsvpStatus)

unFollowPrompt.Triggered:Connect(function(player)
	local rsvpStatus = SocialService:PromptRsvpToEventAsync(EVENT_ID)
	updatePrompt(rsvpStatus)
end)

followPrompt.Triggered:Connect(function(player)
	local rsvpStatus = SocialService:PromptRsvpToEventAsync(EVENT_ID)
	updatePrompt(rsvpStatus)
end)
```

### Method: SocialService:ShowSelfView

**Signature:** `SocialService:ShowSelfView(selfViewPosition?: SelfViewPosition): ()`

Shows the calling player's self view. If this method is called while the
self view is already visible, it does nothing.

*Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `selfViewPosition` | `SelfViewPosition` | `LastPosition` | The position to place the self view . |

**Returns:** `()`

### Method: SocialService:PromptLinkSharing

**Signature:** `SocialService:PromptLinkSharing(player: Player, options?: Dictionary): Tuple`

> **Deprecated:** Use [PromptLinkSharingAsync()](/docs/reference/engine/classes/SocialService.md) instead.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | Prompts the given [Player](/docs/reference/engine/classes/Player.md) with a Roblox platform-level share sheet with a generated share link. |
| `options` | `Dictionary` | `nil` | `Dictionary` that specifies the configuration for the generated link. It includes the following optional key-value pairs:  - `FallbackLinkId` (string). Determines how this share link will   direct player to once expired. Default to experience join link. - `ExpirationSeconds` (number). Determines time to expiration once the   share link is created. Truncates to nearest integer. Defaults to   86,400. - `PreviewTitle` (string) Preview title of the share link. - `PreviewDescription` (string) Preview description of the share link. - `PreviewAssetId` (number) Image asset ID used for share link   preview. - `LaunchData` (string). Used to set a parameter in   [Player:GetJoinData()](/docs/reference/engine/classes/Player.md) when a player joined using the   generated share link. |

**Returns:** `Tuple` — A tuple containing an [PromptLinkSharingResult](/docs/reference/engine/enums/PromptLinkSharingResult.md) indicating the
result of the link sharing prompt.

## Events

### Event: SocialService.CallInviteStateChanged

**Signature:** `SocialService.CallInviteStateChanged(player: Instance, inviteState: InviteState)`

This event fires when a player's call invite state changes.

*Security: None · Capabilities: Social*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Instance` | The [Player](/docs/reference/engine/classes/Player.md) instance of the player who had a call invite state change. |
| `inviteState` | `InviteState` | The new call invite state. |

**SocialService.CallInviteStateChanged**

```lua
local SocialService = game:GetService("SocialService")

local button = script.Parent
local isPhonebookOpen = false

SocialService.CallInviteStateChanged:Connect(function(_, inviteState)
	local isCalling = inviteState == Enum.InviteState.Placed

	if isCalling or isPhonebookOpen then
		button.Visible = false
	else
		button.Visible = true
	end
end)
```

### Event: SocialService.GameInvitePromptClosed

**Signature:** `SocialService.GameInvitePromptClosed(player: Instance, recipientIds: Array)`

This event fires when a player closes an invite prompt.

*Security: None · Capabilities: Social*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Instance` | The [Player](/docs/reference/engine/classes/Player.md) instance of the player who closed the prompt. |
| `recipientIds` | `Array` | No longer populated; an empty array. |

### Event: SocialService.PhoneBookPromptClosed

**Signature:** `SocialService.PhoneBookPromptClosed(player: Instance)`

Fires when a player closes the phone book prompt.

*Security: None · Capabilities: Social*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Instance` | The [Player](/docs/reference/engine/classes/Player.md) instance of the player who closed the phone book. |

### Event: SocialService.ShareSheetClosed

**Signature:** `SocialService.ShareSheetClosed(player: Player)`

Fires on the server when the player closes or dismisses the platform share
sheet that was opened as a result of a successful call to
[PromptLinkSharingAsync()](/docs/reference/engine/classes/SocialService.md).
The `player` argument is the [Player](/docs/reference/engine/classes/Player.md) who closed the share sheet.

*Security: None · Capabilities: Social*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) who closed the share sheet. |

## Callbacks

### Callback: SocialService.OnCallInviteInvoked

**Signature:** `SocialService.OnCallInviteInvoked(tag: string, callParticipantIds: Array): Instance`

A callback to process when a call is placed from the phone book. The `tag`
parameter can be used to differentiate between different "entry points" or
similar, as described in
[PromptPhoneBook()](/docs/reference/engine/classes/SocialService.md). Only one
callback can be set.

*Security: None · Thread Safety: Unsafe · Capabilities: Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tag` | `string` |  | String to help differentiate between various phone book entry points. |
| `callParticipantIds` | `Array` |  | Array containing all of the players involved in the call. The caller will always be the first player in the array. |

**Returns:** `Instance` — Table including the `PlaceId` and `ReservedServerAccessCode` keys
whose values are the [DataModel.PlaceId](/docs/reference/engine/classes/DataModel.md) and the server access
code returned by [TeleportService:ReserveServerAsync()](/docs/reference/engine/classes/TeleportService.md),
respectively.

**SocialService.OnCallInviteInvoked**

```lua
local SocialService = game:GetService("SocialService")
local TeleportService = game:GetService("TeleportService")

SocialService.OnCallInviteInvoked = function()
	local placeId = 0123456789 -- This is the place ID of the desired place to drop call participants into
	local accessCode = TeleportService:ReserveServerAsync(placeId)

	return { ReservedServerAccessCode = accessCode, PlaceId = placeId }
end
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