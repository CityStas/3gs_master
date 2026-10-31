---
name: ProximityPromptService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - Service
  - NotBrowsable
summary: "Allows developers to interact with ProximityPrompt objects in a global way."
---

# Class: ProximityPromptService

> Allows developers to interact with [ProximityPrompt](/docs/reference/engine/classes/ProximityPrompt.md) objects in a global
> way.

## Description

**ProximityPromptService** allows developers to interact with
[ProximityPrompt](/docs/reference/engine/classes/ProximityPrompt.md) objects in a global way. It may be more convenient to
listen to events through this service rather than on individual
[ProximityPrompt](/docs/reference/engine/classes/ProximityPrompt.md) objects.

## Properties

### Property: ProximityPromptService.Enabled

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property determines whether [ProximityPrompts](/docs/reference/engine/classes/ProximityPrompt.md)
are enabled, and therefore shown, in-experience. When false, no prompts
will be shown.

For example, in a round-based system, you can disable prompts at certain
points in the experience to disable proximity-based interactions:

**Enabled**

Demonstrates [ProximityPromptService.Enabled](/docs/reference/engine/classes/ProximityPromptService.md).

```lua
local ProximityPromptService = game:GetService("ProximityPromptService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local enablePrompts = Instance.new("BindableEvent")
enablePrompts.Name = "EnablePrompts"
enablePrompts.Parent = ReplicatedStorage

-- Connect to the BindableEvent and fire from another script controlling experience logic
enablePrompts.Event:Connect(function(enabled)
	ProximityPromptService.Enabled = enabled
end)
```

### Property: ProximityPromptService.MaxIndicatorsVisible

```json
{
  "type": "int",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property sets the maximum number of prompt indicators that can be
visible at the same time. Indicators are lightweight distance hints shown
for [ProximityPrompts](/docs/reference/engine/classes/ProximityPrompt.md) when the player is within the
prompt's [MaxIndicatorDistance](/docs/reference/engine/classes/ProximityPrompt.md)
but still outside its
[MaxActivationDistance](/docs/reference/engine/classes/ProximityPrompt.md).

This property defaults to `16` and is clamped to the range `[0, 64]`.
Because indicators are opt-in per prompt — a prompt's
[MaxIndicatorDistance](/docs/reference/engine/classes/ProximityPrompt.md) defaults
to `0`, which disables its indicator — this property has no visible effect
unless at least one prompt sets a non-zero
[MaxIndicatorDistance](/docs/reference/engine/classes/ProximityPrompt.md).

### Property: ProximityPromptService.MaxPromptsVisible

```json
{
  "type": "int",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

This property indicates the maximum number of
[ProximityPrompts](/docs/reference/engine/classes/ProximityPrompt.md) that will be shown to the player.

## Events

### Event: ProximityPromptService.IndicatorHidden

**Signature:** `ProximityPromptService.IndicatorHidden(prompt: ProximityPrompt)`

This event triggers client-side in connected local scripts when the
indicator for a [ProximityPrompt](/docs/reference/engine/classes/ProximityPrompt.md) is no longer visible, such as when
the player moves outside the prompt's
[MaxIndicatorDistance](/docs/reference/engine/classes/ProximityPrompt.md) or the
prompt is disabled. It is the counterpart to
[IndicatorShown](/docs/reference/engine/classes/ProximityPromptService.md) and is
convenient for tearing down custom indicator UI globally rather than
connecting to each individual [ProximityPrompt](/docs/reference/engine/classes/ProximityPrompt.md).

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `prompt` | `ProximityPrompt` | The prompt whose indicator becomes hidden. |

### Event: ProximityPromptService.IndicatorShown

**Signature:** `ProximityPromptService.IndicatorShown(prompt: ProximityPrompt)`

This event triggers client-side in connected local scripts when the
indicator for a [ProximityPrompt](/docs/reference/engine/classes/ProximityPrompt.md) becomes visible, which happens
when the player moves within the prompt's
[MaxIndicatorDistance](/docs/reference/engine/classes/ProximityPrompt.md) but
remains outside its
[MaxActivationDistance](/docs/reference/engine/classes/ProximityPrompt.md).
Indicators are opt-in: a prompt only shows one when its
[MaxIndicatorDistance](/docs/reference/engine/classes/ProximityPrompt.md) is set
greater than `0` (the default of `0` disables the indicator). Listening on
the service rather than on each [ProximityPrompt](/docs/reference/engine/classes/ProximityPrompt.md) is convenient when
implementing custom indicator UI globally.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `prompt` | `ProximityPrompt` | The prompt whose indicator becomes visible. |

### Event: ProximityPromptService.PromptButtonHoldBegan

**Signature:** `ProximityPromptService.PromptButtonHoldBegan(prompt: ProximityPrompt, playerWhoTriggered: Player)`

This event triggers when the player begins holding down the
[KeyboardKeyCode](/docs/reference/engine/classes/ProximityPrompt.md) key/button on a
prompt with a non-zero [HoldDuration](/docs/reference/engine/classes/ProximityPrompt.md).

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `prompt` | `ProximityPrompt` | The prompt that the player begins interacting with. |
| `playerWhoTriggered` | `Player` | The player who holds the key/button. |

### Event: ProximityPromptService.PromptButtonHoldEnded

**Signature:** `ProximityPromptService.PromptButtonHoldEnded(prompt: ProximityPrompt, playerWhoTriggered: Player)`

This event triggers when the player stops holding down the
[KeyboardKeyCode](/docs/reference/engine/classes/ProximityPrompt.md) key/button on a
prompt with a non-zero [HoldDuration](/docs/reference/engine/classes/ProximityPrompt.md).

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `prompt` | `ProximityPrompt` | The prompt that the player stops interacting with. |
| `playerWhoTriggered` | `Player` | The player who releases the held key/button. |

### Event: ProximityPromptService.PromptHidden

**Signature:** `ProximityPromptService.PromptHidden(prompt: ProximityPrompt)`

This event triggers client-side in connected local scripts when a prompt
becomes hidden.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `prompt` | `ProximityPrompt` | The prompt instance that becomes hidden. |

### Event: ProximityPromptService.PromptShown

**Signature:** `ProximityPromptService.PromptShown(prompt: ProximityPrompt, inputType: ProximityPromptInputType)`

This event triggers client-side in connected local scripts when a prompt
becomes visible.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `prompt` | `ProximityPrompt` | The prompt instance that becomes visible. |
| `inputType` | `ProximityPromptInputType` | The input that triggered the event. |

### Event: ProximityPromptService.PromptTriggered

**Signature:** `ProximityPromptService.PromptTriggered(prompt: ProximityPrompt, playerWhoTriggered: Player)`

This event triggers when the player completes interaction with a prompt,
either when the [KeyboardKeyCode](/docs/reference/engine/classes/ProximityPrompt.md)
key/button is pressed, or after a specified amount of time holding the
key/button if the prompt's
[HoldDuration](/docs/reference/engine/classes/ProximityPrompt.md) is non-zero.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `prompt` | `ProximityPrompt` | The prompt that the player interacts with. |
| `playerWhoTriggered` | `Player` | The interacting player. |

### Event: ProximityPromptService.PromptTriggerEnded

**Signature:** `ProximityPromptService.PromptTriggerEnded(prompt: ProximityPrompt, playerWhoTriggered: Player)`

This event triggers when the player stops holding down the
[KeyboardKeyCode](/docs/reference/engine/classes/ProximityPrompt.md) key/button while
triggering a prompt. This is intended to allow interactions which require
the player to hold a key/button while something happens in-experience.

*Security: None · Capabilities: Input*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `prompt` | `ProximityPrompt` | The prompt that the player stops interacting with. |
| `playerWhoTriggered` | `Player` | The player that releases the key/button. |

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