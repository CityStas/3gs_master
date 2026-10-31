---
name: ScriptContext
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
summary: "A service that manages the execution of all BaseScript objects."
---

# Class: ScriptContext

> A service that manages the execution of all [BaseScript](/docs/reference/engine/classes/BaseScript.md) objects.

## Description

This service controls all [BaseScript](/docs/reference/engine/classes/BaseScript.md) objects. Most of the properties
and methods of this service are locked for internal use.

## Methods

### Method: ScriptContext:EnableCoverage

**Signature:** `ScriptContext:EnableCoverage(instance: Instance): ()`

Requires `PluginOrOpenCloud` security; not callable from game scripts.
Registers `instance` as a coverage root so the engine records per-line and
per-function execution coverage for `instance` and every script descended
from it. Retrieve the recorded data with
[ScriptContext:GetCoverageStats()](/docs/reference/engine/classes/ScriptContext.md).

*Security: None · Thread Safety: Unsafe · Capabilities: PluginOrOpenCloud*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `instance` | `Instance` |  | The instance to track; coverage is recorded for this instance and every script descended from it. |

**Returns:** `()`

### Method: ScriptContext:GetCoverageStats

**Signature:** `ScriptContext:GetCoverageStats(): Array`

Requires `PluginOrOpenCloud` security; not callable from experience
scripts. Returns an array of coverage results, one entry per tracked
script. Each entry is a table with a `Script` field (the script
[Instance](/docs/reference/engine/classes/Instance.md)) and a `GetHits()` function. Calling `GetHits()` returns
two arrays: per-line hit counts, where `-1` marks a line that was never
executed or was excluded, and per-function records containing each
function's `Name`, `Line`, and `Hits`.

Like [ScriptContext:EnableCoverage()](/docs/reference/engine/classes/ScriptContext.md), this method raises an error
if coverage collection is not enabled.

*Security: None · Thread Safety: Unsafe · Capabilities: PluginOrOpenCloud*

**Returns:** `Array` — An array of per-script coverage tables, each with a `Script` field and
a `GetHits` function for retrieving line and function hit counts.

### Method: ScriptContext:SetTimeout

**Signature:** `ScriptContext:SetTimeout(seconds: double): ()`

Sets the watchdog time limit that the engine applies to running scripts.
The value becomes the per-resumption execution budget: if a thread runs
for longer than `seconds` since it was last resumed without yielding, the
watchdog aborts it with the runtime error
`Script timeout: exhausted allowed execution time`.

The timeout defaults to `0`, which disables the watchdog so that scripts
may run without any time limit. Call this method with a positive value to
enable enforcement, or pass `0` to turn it back off.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `seconds` | `double` |  | The maximum time, in seconds, that a script may run between yields before the watchdog interrupts it. A value of `0` disables the timeout. |

**Returns:** `()`

## Events

### Event: ScriptContext.Error

**Signature:** `ScriptContext.Error(message: string, stackTrace: string, script: Instance)`

Fires when an unhandled error occurs while running a script, reporting the
error to any listening code. The engine raises this event from its
error-reporting path when a thread terminates with an error, passing the
error `message`, a formatted `stackTrace` string, and the `script` that
was running.

This event does not fire for errors raised by the watchdog when a script
exceeds its execution-time limit (see [ScriptContext:SetTimeout()](/docs/reference/engine/classes/ScriptContext.md)).

*Security: None · Capabilities: Logging*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `message` | `string` | The error message describing what went wrong. |
| `stackTrace` | `string` | The call stack at the point the error occurred, formatted as a string. |
| `script` | `Instance` | The script in which the error occurred. |

**ScriptContext.Error**

When an error occurs, this example prints the name of the script that errored,
the reason it errored, and a trace of the error.

```lua
local ScriptContext = game:GetService("ScriptContext")

local function onError(message, trace, script)
	print(script:GetFullName(), "errored!")
	print("Reason:", message)
	print("Trace:", trace)
end

ScriptContext.Error:Connect(onError)

-- Somewhere, in another script

error("Error occurred!")
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