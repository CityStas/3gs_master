---
name: ChangeHistoryService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "**Must** be used by plugins to communicate to Studio how to undo and redo the changes which they make to the experience."
---

# Class: ChangeHistoryService

> **Must** be used by plugins to communicate to Studio how to undo and redo the
> changes which they make to the experience.

## Description

Plugin developers **must** use [ChangeHistoryService](/docs/reference/engine/classes/ChangeHistoryService.md) to tell Studio how
to undo and redo changes that their plugins make to experiences by recording.
Before making changes, a plugin calls
[ChangeHistoryService:TryBeginRecording()](/docs/reference/engine/classes/ChangeHistoryService.md), remembering the identifier
it assigns, then after making changes, the Plugin calls
[ChangeHistoryService:FinishRecording()](/docs/reference/engine/classes/ChangeHistoryService.md) to complete the recording.

Plugins may also programmatically invoke an undo or redo through
[ChangeHistoryService:Undo()](/docs/reference/engine/classes/ChangeHistoryService.md) or [ChangeHistoryService:Redo()](/docs/reference/engine/classes/ChangeHistoryService.md).

[ChangeHistoryService](/docs/reference/engine/classes/ChangeHistoryService.md) is not enabled at runtime, so calling its methods
in a running experience has no effect.

## Methods

### Method: ChangeHistoryService:FinishRecording

**Signature:** `ChangeHistoryService:FinishRecording(identifier: string, operation: FinishRecordingOperation, finalOptions: Dictionary?): ()`

Completes a recording that was started with
[TryBeginRecording()](/docs/reference/engine/classes/ChangeHistoryService.md). Pass
the `identifier` returned by that call along with an
[FinishRecordingOperation](/docs/reference/engine/enums/FinishRecordingOperation.md) describing what to do with the recorded
changes:

- [FinishRecordingOperation.Commit](/docs/reference/engine/enums/FinishRecordingOperation.md) adds the changes to the undo/redo
  history as a new waypoint.
- [FinishRecordingOperation.Cancel](/docs/reference/engine/enums/FinishRecordingOperation.md) discards the recording and
  reverts the changes it captured. The `identifier` is ignored for this
  operation, so a plugin can cancel its own in-progress recording without
  knowing the identifier.
- [FinishRecordingOperation.Append](/docs/reference/engine/enums/FinishRecordingOperation.md) merges the recording into the
  waypoint that immediately precedes it rather than creating a new one.

When the recording finishes, this method fires
[OnRecordingFinished](/docs/reference/engine/classes/ChangeHistoryService.md),
forwarding the `finalOptions` table. It raises an error if the calling
plugin has no recording in progress, or if `operation` is not
[FinishRecordingOperation.Cancel](/docs/reference/engine/enums/FinishRecordingOperation.md) and `identifier` does not match the
active recording. It has no effect when the service is disabled or while
an undo or redo is in progress.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `identifier` | `string` |  | Identifies the recording from the previous call to [TryBeginRecording()](/docs/reference/engine/classes/ChangeHistoryService.md). If the operation is [FinishRecordingOperation.Cancel](/docs/reference/engine/enums/FinishRecordingOperation.md), this value is ignored, and the recording is determined by context. |
| `operation` | `FinishRecordingOperation` |  | Specifies the operation to take. |
| `finalOptions` | `Dictionary?` |  | Optional table of values to pass to [OnRecordingFinished](/docs/reference/engine/classes/ChangeHistoryService.md). |

**Returns:** `()`

**ChangeHistoryService:TryBeginRecording**

To commit an undo/redo record, you need to first call
[TryBeginRecording()](/docs/reference/engine/classes/ChangeHistoryService.md) followed
by calling [FinishRecording()](/docs/reference/engine/classes/ChangeHistoryService.md).

```lua
local ChangeHistoryService = game:GetService("ChangeHistoryService")
local Selection = game:GetService("Selection")

local toolbar = plugin:CreateToolbar("Example Plugin")
local button = toolbar:CreateButton("Neon it up", "", "")

button.Click:Connect(function()
	local parts = {}
	for _, part in pairs(Selection:Get()) do
		if part:IsA("BasePart") then
			parts[#parts + 1] = part
		end
	end

	if #parts < 1 then
		-- Nothing to do.
		return
	end

	local recording = ChangeHistoryService:TryBeginRecording("Set selection to neon")
	if not recording then
		-- Handle error here. This indicates that your plugin began a previous
		-- recording and never completed it. You may only have one recording
		-- per plugin active at a time.
		return
	end

	for _, part in pairs(parts) do
		part.Material = Enum.Material.Neon
	end

	ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
end)
```

### Method: ChangeHistoryService:GetCanRedo

**Signature:** `ChangeHistoryService:GetCanRedo(): Tuple`

Reports whether [Redo()](/docs/reference/engine/classes/ChangeHistoryService.md) currently has
an action available to replay. It returns a boolean that is `true` when a
redoable waypoint exists ahead of the current position in the undo/redo
history; when that boolean is `true`, it also returns the name of the
waypoint that the next redo would replay.

The boolean is `false`, with no name returned, when the redo stack is
empty because the newest waypoint is already the current one, or when the
service is disabled (which is always the case at runtime).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `Tuple` — `true` followed by the name of the action that would be redone when a
redo is available; otherwise `false`.

### Method: ChangeHistoryService:GetCanUndo

**Signature:** `ChangeHistoryService:GetCanUndo(): Tuple`

Reports whether [Undo()](/docs/reference/engine/classes/ChangeHistoryService.md) currently has
an action available to revert. It returns a boolean that is `true` when an
undoable waypoint exists at the current position in the undo/redo history;
when that boolean is `true`, it also returns the name of the waypoint that
the next undo would revert.

The boolean is `false`, with no name returned, when the undo stack is
empty because the position is already at the base waypoint, or when the
service is disabled (which is always the case at runtime).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `Tuple` — `true` followed by the name of the action that would be undone when an
undo is available; otherwise `false`.

### Method: ChangeHistoryService:IsRecordingInProgress

**Signature:** `ChangeHistoryService:IsRecordingInProgress(identifier: string?): boolean`

Reports whether the calling plugin has a recording in progress that was
started with
[TryBeginRecording()](/docs/reference/engine/classes/ChangeHistoryService.md).

When called without an `identifier`, it returns `true` if any recording is
active for the plugin. When an `identifier` is supplied, it returns `true`
only if the active recording's identifier matches that value. It returns
`false` when the service is disabled or when the plugin has no active
recording.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `identifier` | `string?` |  | Optional identifier of a specific recording to check for. When omitted, the method reports whether _any_ recording is in progress for the plugin. |

**Returns:** `boolean` — `true` if a matching recording is in progress; otherwise `false`.

### Method: ChangeHistoryService:Redo

**Signature:** `ChangeHistoryService:Redo(): ()`

Replays the waypoint immediately ahead of the current position in the
undo/redo history, redoing the action that a matching
[Undo()](/docs/reference/engine/classes/ChangeHistoryService.md) had reverted, and advances the
redo pointer forward by one waypoint. After the waypoint is replayed, it
fires [OnRedo](/docs/reference/engine/classes/ChangeHistoryService.md) with the name of the
redone waypoint.

This method raises an error if a play is already in progress, if the
service is disabled (which is always the case at runtime), or if there is
nothing left to redo. Call
[GetCanRedo()](/docs/reference/engine/classes/ChangeHistoryService.md) first to confirm a
redo is available.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `()`

### Method: ChangeHistoryService:ResetWaypoints

**Signature:** `ChangeHistoryService:ResetWaypoints(): ()`

Records the current state as a waypoint named `base` and then merges every
existing waypoint into that single waypoint, leaving no actions to undo or
redo. Use this to establish a clean starting point so that later
[Undo()](/docs/reference/engine/classes/ChangeHistoryService.md) calls cannot revert past the
current state.

This method has no effect when the service is disabled (which is always
the case at runtime).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `()`

### Method: ChangeHistoryService:SetEnabled

**Signature:** `ChangeHistoryService:SetEnabled(state: boolean): ()`

Sets whether or not the ChangeHistoryService is enabled. When set to
false, the undo/redo list is cleared, and does not repopulate. When set to
true again, the original list is not restored, but further operations
append to the list once more

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `state` | `boolean` |  | Whether to enable (`true`) or disable (`false`) the service. |

**Returns:** `()`

### Method: ChangeHistoryService:SetWaypoint

**Signature:** `ChangeHistoryService:SetWaypoint(name: string): ()`

This method will be **deprecated soon** in favor of
[TryBeginRecording()](/docs/reference/engine/classes/ChangeHistoryService.md).

[ChangeHistoryService](/docs/reference/engine/classes/ChangeHistoryService.md) tracks plugin history as a stream of property
changes. [SetWaypoint()](/docs/reference/engine/classes/ChangeHistoryService.md) creates
a cut in that stream of property changes so that the undo and redo actions
know where to stop.

By convention, user-invoked actions in Studio **must** call
[SetWaypoint()](/docs/reference/engine/classes/ChangeHistoryService.md) _after_
completing their set of changes to the experience. Calling it **before** a
set of changes may clean up another misbehaving plugin which failed to set
a waypoint, but it's a poor reason to justify such usage in your own
plugin.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name to assign to the new waypoint, which appears in the undo/redo history. |

**Returns:** `()`

**ChangeHistoryService:SetWaypoint**

In order for the waypoints to work correctly, you need to set one both before
AND after you perform the action that should be able to be undone.

```lua
local ChangeHistoryService = game:GetService("ChangeHistoryService")
local Selection = game:GetService("Selection")

local toolbar = plugin:CreateToolbar("Example Plugin")
local button = toolbar:CreateButton("Neon it up", "", "")

button.Click:Connect(function()
	local parts = {}
	for _, part in pairs(Selection:Get()) do
		if part:IsA("BasePart") then
			parts[#parts + 1] = part
		end
	end

	if #parts > 0 then
		-- Calling SetWaypoint before the work will not cause any issues, however
		-- it is redundant, only the call AFTER the work is needed.
		--ChangeHistoryService:SetWaypoint("Setting selection to neon")

		for _, part in pairs(parts) do
			part.Material = Enum.Material.Neon
		end

		-- Call SetWaypoint AFTER completing the work
		ChangeHistoryService:SetWaypoint("Set selection to neon")
	else
		-- Nothing to do. You do not need to call SetWaypoint in the case where
		-- the action did not end up making any changes to the experience.
	end
end)
```

### Method: ChangeHistoryService:TryBeginRecording

**Signature:** `ChangeHistoryService:TryBeginRecording(name: string, displayName: string?): string?`

This method begins a recording to track changes to the data model. You
**must** call it prior to making changes to avoid future warnings or
errors.

When the recording is completed, you call
[FinishRecording()](/docs/reference/engine/classes/ChangeHistoryService.md) with the
returned recording identifier to complete the recording and update the
undo/redo stack.

This method will return `nil` if it fails to begin a recording. Recordings
fail if the plugin already has a recording in progress, or if the user is
in a solo playtest.

You may use
[IsRecordingInProgress()](/docs/reference/engine/classes/ChangeHistoryService.md)
to check the recording status of the plugin.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | Name of the action being performed suitable for logging and coding purposes. |
| `displayName` | `string?` |  | Name of the action being performed to display to the user. |

**Returns:** `string?` — A unique string identifier for the recording on success, or `nil` if
the recording could not be started.

**ChangeHistoryService:TryBeginRecording**

To commit an undo/redo record, you need to first call
[TryBeginRecording()](/docs/reference/engine/classes/ChangeHistoryService.md) followed
by calling [FinishRecording()](/docs/reference/engine/classes/ChangeHistoryService.md).

```lua
local ChangeHistoryService = game:GetService("ChangeHistoryService")
local Selection = game:GetService("Selection")

local toolbar = plugin:CreateToolbar("Example Plugin")
local button = toolbar:CreateButton("Neon it up", "", "")

button.Click:Connect(function()
	local parts = {}
	for _, part in pairs(Selection:Get()) do
		if part:IsA("BasePart") then
			parts[#parts + 1] = part
		end
	end

	if #parts < 1 then
		-- Nothing to do.
		return
	end

	local recording = ChangeHistoryService:TryBeginRecording("Set selection to neon")
	if not recording then
		-- Handle error here. This indicates that your plugin began a previous
		-- recording and never completed it. You may only have one recording
		-- per plugin active at a time.
		return
	end

	for _, part in pairs(parts) do
		part.Material = Enum.Material.Neon
	end

	ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
end)
```

### Method: ChangeHistoryService:Undo

**Signature:** `ChangeHistoryService:Undo(): ()`

Unplays the waypoint at the current position in the undo/redo history,
reverting the most recent recorded action, and steps the undo pointer back
by one waypoint. After the waypoint is reverted, it fires
[OnUndo](/docs/reference/engine/classes/ChangeHistoryService.md) with the name of the undone
waypoint.

This method raises an error if a play is already in progress, if the
service is disabled (which is always the case at runtime), or if there is
nothing left to undo. Call
[GetCanUndo()](/docs/reference/engine/classes/ChangeHistoryService.md) first to confirm an
undo is available.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `()`

## Events

### Event: ChangeHistoryService.OnRecordingFinished

**Signature:** `ChangeHistoryService.OnRecordingFinished(name: string, displayName: string?, identifier: string?, operation: FinishRecordingOperation, finalOptions: Dictionary?)`

Fires when a recording started with
[TryBeginRecording()](/docs/reference/engine/classes/ChangeHistoryService.md) is
completed through
[FinishRecording()](/docs/reference/engine/classes/ChangeHistoryService.md). The
`operation` argument reports how the recording was finished (`Commit`,
`Cancel`, or `Append`), and `finalOptions` is the optional table that was
passed to `FinishRecording()`.

*Security: PluginSecurity*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `name` | `string` | Name of the action being performed suitable for logging and coding purposes. |
| `displayName` | `string?` | Name of the action being performed to display to the user. |
| `identifier` | `string?` | The identifier for the recording. |
| `operation` | `FinishRecordingOperation` | The [FinishRecordingOperation](/docs/reference/engine/enums/FinishRecordingOperation.md) that completed the recording, either `Commit`, `Cancel`, or `Append`. |
| `finalOptions` | `Dictionary?` | Optional table from [FinishRecording()](/docs/reference/engine/classes/ChangeHistoryService.md). |

### Event: ChangeHistoryService.OnRecordingStarted

**Signature:** `ChangeHistoryService.OnRecordingStarted(name: string, displayName: string?)`

Fires when a plugin begins a recording with
[TryBeginRecording()](/docs/reference/engine/classes/ChangeHistoryService.md),
carrying the same `name` and `displayName` values that were passed to that
call.

*Security: PluginSecurity*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `name` | `string` | Name of the action being performed suitable for logging and coding purposes. |
| `displayName` | `string?` | Name of the action being performed to display to the user. |

### Event: ChangeHistoryService.OnRedo

**Signature:** `ChangeHistoryService.OnRedo(waypoint: string)`

Fires immediately after [Redo()](/docs/reference/engine/classes/ChangeHistoryService.md) replays
a waypoint, whether the redo was triggered by the user through Studio or
invoked programmatically. The `waypoint` argument is the name of the
action that was redone, matching the name that was recorded for that
waypoint.

*Security: PluginSecurity*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `waypoint` | `string` | The name of the waypoint (action) that was redone. |

### Event: ChangeHistoryService.OnUndo

**Signature:** `ChangeHistoryService.OnUndo(waypoint: string)`

Fires immediately after [Undo()](/docs/reference/engine/classes/ChangeHistoryService.md) reverts
a waypoint, whether the undo was triggered by the user through Studio or
invoked programmatically. The `waypoint` argument is the name of the
action that was undone, matching the name that was recorded for that
waypoint.

*Security: PluginSecurity*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `waypoint` | `string` | The name of the waypoint (action) that was undone. |

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