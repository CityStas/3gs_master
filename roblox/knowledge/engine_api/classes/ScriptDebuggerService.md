---
name: ScriptDebuggerService
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
summary: "Provides programmatic breakpoint management, execution control, and runtime inspection of Luau scripts during a playtest."
---

# Class: ScriptDebuggerService

> Provides programmatic breakpoint management, execution control, and runtime
> inspection of Luau scripts during a playtest.

## Description

`ScriptDebuggerService` exposes the Roblox Studio Luau debugger for
programmatic use. It provides functionality for breakpoint management,
execution control, and runtime state inspection.

**APIs in this class are currently in beta and are subject to breaking
changes.**

#### Breakpoint Propagation

Breakpoints set in the **edit** [DataModel](/docs/reference/engine/classes/DataModel.md) are set on the specific
script instance and do not propagate to clones, but they propagate to
corresponding scripts in play data models at the start of a playtest.
Breakpoints set in a **play** [DataModel](/docs/reference/engine/classes/DataModel.md) propagate to script clones in
the same data model and to corresponding scripts in other data models.

#### Parallel Threads

The behavior of this API with parallel Luau is undefined.

## Methods

### Method: ScriptDebuggerService:AddBreakpoint

**Signature:** `ScriptDebuggerService:AddBreakpoint(scriptInstance: LuaSourceContainer, breakpoint: Dictionary): ScriptBreakpointResult`

Adds a breakpoint to the specified script. If a breakpoint already exists
on the same script and line, its data is replaced with the new
configuration.

Errors if the script instance or breakpoint argument is invalid.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `scriptInstance` | `LuaSourceContainer` |  | The [LuaSourceContainer](/docs/reference/engine/classes/LuaSourceContainer.md) to place the breakpoint on. |
| `breakpoint` | `Dictionary` |  | Dictionary describing the breakpoint configuration through the following key-value pairs:  - `Line` — Required 1-based line number. - `Enabled` — Optional boolean whether the breakpoint is active.   Default is `true`. - `Condition` — Optional string indicating the Luau expression which   must be truthy to pause, for example `"health < 10"`. - `LogMessage` — Optional string message logged when the breakpoint is   hit. This string is parsed as a comma-separated list of Luau   expressions, evaluated in the breakpoint's scope, and concatenated   [LuaGlobals.print()](/docs/reference/engine/globals/LuaGlobals.md)‑style with spaces between segments.   String literals are quoted; bare identifiers reference live values.   For example, `"'count is', count"` produces output like   `count is 7`. - `ContinueExecution` — If `true`, the [DataModel](/docs/reference/engine/classes/DataModel.md) does not   pause when the breakpoint is hit. Default is `false`. |

**Returns:** `ScriptBreakpointResult` — Dictionary indicating whether the breakpoint was placed successfully
and on which line. Includes the following key-value pairs:

- `Verified` — Boolean value indicating whether the breakpoint was
  placed successfully.
- `Line` — The line number the breakpoint was placed on.
- `Message` — Optional explanation if `Verified` is `false`.

### Method: ScriptDebuggerService:ClearBreakpoints

**Signature:** `ScriptDebuggerService:ClearBreakpoints(): ()`

Removes all breakpoints across all scripts.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `()`

### Method: ScriptDebuggerService:Evaluate

**Signature:** `ScriptDebuggerService:Evaluate(expression: string, frameId?: int?): ScriptEvaluateResult`

Evaluates a Luau expression in the context of the specified stack frame,
or globally if no `frameId` is provided.

Errors if the expression has a syntax error or `frameId` is invalid.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `expression` | `string` |  | The Luau expression to evaluate. |
| `frameId` | `int?` | `nil` | Optional frame identifier. If omitted, evaluates globally. |

**Returns:** `ScriptEvaluateResult` — Dictionary with the following key-value pairs:

- `Result` — String representation of the evaluated result.
- `Type` — String indicating the Luau type of the result (`"number"`,
  `"string"`, `"table"`, `"Instance"`, etc.).
- `VariablesReference` — If greater than `0`, drill into with
  [GetVariables()](/docs/reference/engine/classes/ScriptDebuggerService.md).

### Method: ScriptDebuggerService:GetRootVariables

**Signature:** `ScriptDebuggerService:GetRootVariables(frameId: int): List<ScriptVariable>`

Returns the root variables (locals, upvalues, globals) for the specified
stack frame. Each variable includes a `VariablesReference` field; if
greater than `0`, pass it to
[GetVariables()](/docs/reference/engine/classes/ScriptDebuggerService.md) to drill into
children.

Errors if `frameId` is invalid. Returns empty if the [DataModel](/docs/reference/engine/classes/DataModel.md) is
not stopped at a breakpoint or exception, or when stopped via
[Pause()](/docs/reference/engine/classes/ScriptDebuggerService.md).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `frameId` | `int` |  | The frame identifier from a debug stack frame `Id` field (see [GetStackTrace()](/docs/reference/engine/classes/ScriptDebuggerService.md)). |

**Returns:** `List<ScriptVariable>` — An array of script variable dictionaries, each containing the
following key-value pairs:

- `Name` — String value indicating the variable name or table key.
- `Value` — String representation of the value.
- `Type` — String indicating the Luau type (`"number"`, `"string"`,
  `"table"`, `"Instance"`, etc.).
- `Scope` — [ScriptVariableScope](/docs/reference/engine/enums/ScriptVariableScope.md) value (children inherit
  parent's scope).
- `VariablesReference` — If greater than `0`, call
  [GetVariables()](/docs/reference/engine/classes/ScriptDebuggerService.md) with
  this to get children.

### Method: ScriptDebuggerService:GetStackTrace

**Signature:** `ScriptDebuggerService:GetStackTrace(threadId: int, startFrame?: int?): DebugStackTraceResult`

Returns the call stack for a paused thread, ordered innermost (current
execution point) to outermost. Use `startFrame` (1‑based) for paginated
retrieval of large stacks.

Errors if `threadId` or `startFrame` is invalid.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `threadId` | `int` |  | The thread identifier from a script debug thread `Id` field (see [GetThreads()](/docs/reference/engine/classes/ScriptDebuggerService.md)). |
| `startFrame` | `int?` | `nil` | Optional 1-based frame index for paginated retrieval. |

**Returns:** `DebugStackTraceResult` — Dictionary containing the frames ordered innermost (current) to
outermost. Contains the following key-value pairs:

- `Frames` — Array of debug stack frame dictionaries. Each dictionary
  item contains the following key-value pairs:
  - `Id` — Numerical frame identifier; use with
    [GetRootVariables()](/docs/reference/engine/classes/ScriptDebuggerService.md)
    and [Evaluate()](/docs/reference/engine/classes/ScriptDebuggerService.md).
  - `Name` — Human-readable name of the function at this frame.
  - `ScriptPath` — Full instance path of the script, for example
    `"ServerScriptService.MainScript"`.
  - `Line` — 1-based line number where execution is paused at this
    frame.
- `TotalFrames` — Total frame count, provided when paginating.

### Method: ScriptDebuggerService:GetThreads

**Signature:** `ScriptDebuggerService:GetThreads(): List<ScriptDebugThread>`

Returns all paused Luau threads. Should be called when the
[DataModel](/docs/reference/engine/classes/DataModel.md) is stopped (typically inside
[OnStopped](/docs/reference/engine/classes/ScriptDebuggerService.md)). Returns empty results
when the [DataModel](/docs/reference/engine/classes/DataModel.md) is not stopped at a breakpoint or exception, or
when stopped via [Pause()](/docs/reference/engine/classes/ScriptDebuggerService.md).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `List<ScriptDebugThread>` — An array of script debug thread dictionaries, each containing the
following key-value pairs:

- `Id` — Numerical thread identifier; use with
  [GetStackTrace()](/docs/reference/engine/classes/ScriptDebuggerService.md) and
  stepping.
- `Name` — Human-readable name of the script.

### Method: ScriptDebuggerService:GetVariables

**Signature:** `ScriptDebuggerService:GetVariables(variablesReference: int): List<ScriptVariable>`

Drills into structured variables such as tables and
[Instances](/docs/reference/engine/classes/Instance.md). Pass a `VariablesReference` obtained from a
script variable returned by
[GetRootVariables()](/docs/reference/engine/classes/ScriptDebuggerService.md) or a
previous call to this method.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `variablesReference` | `int` |  | A reference from a previous script variable's `VariablesReference` field (see [GetRootVariables()](/docs/reference/engine/classes/ScriptDebuggerService.md)). |

**Returns:** `List<ScriptVariable>` — An array of script variable dictionaries representing the children in
the same format as variable dictionaries from
[GetRootVariables()](/docs/reference/engine/classes/ScriptDebuggerService.md).
Returns empty if the [DataModel](/docs/reference/engine/classes/DataModel.md) is not stopped at a breakpoint
or exception, or when stopped via
[Pause()](/docs/reference/engine/classes/ScriptDebuggerService.md).

### Method: ScriptDebuggerService:Pause

**Signature:** `ScriptDebuggerService:Pause(): ()`

Requests the debugger to pause at the next safe point. This method is
asynchronous and returns immediately. When the thread pauses,
[OnStopped](/docs/reference/engine/classes/ScriptDebuggerService.md) fires with reason
[ScriptStoppedReason.Pause](/docs/reference/engine/enums/ScriptStoppedReason.md). Has no effect if already stopped.

Only meaningful when the [DataModel](/docs/reference/engine/classes/DataModel.md) is running during a playtest.
Calling `Pause()` while already stopped at a breakpoint has no effect.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `()`

### Method: ScriptDebuggerService:RemoveBreakpoint

**Signature:** `ScriptDebuggerService:RemoveBreakpoint(scriptInstance: LuaSourceContainer, line: int): boolean`

Removes the breakpoint at the specified line in the given script. Returns
`false` if no breakpoint exists on the line (no-op). Errors if the script
instance or line number is invalid.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `scriptInstance` | `LuaSourceContainer` |  | The [LuaSourceContainer](/docs/reference/engine/classes/LuaSourceContainer.md) containing the breakpoint. |
| `line` | `int` |  | The 1-based line number of the breakpoint to remove. |

**Returns:** `boolean` — `true` if a breakpoint was removed, `false` if no breakpoint existed
on the line.

### Method: ScriptDebuggerService:SetExceptionBreakMode

**Signature:** `ScriptDebuggerService:SetExceptionBreakMode(breakMode: DebugBreakModeType): ()`

Sets the exception break mode on **all** [DataModels](/docs/reference/engine/classes/DataModel.md). Use
[DebugBreakModeType](/docs/reference/engine/enums/DebugBreakModeType.md) to specify when the debugger should pause on
exceptions.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `breakMode` | `DebugBreakModeType` |  | The [DebugBreakModeType](/docs/reference/engine/enums/DebugBreakModeType.md) to set. |

**Returns:** `()`

## Events

### Event: ScriptDebuggerService.Resumed

**Signature:** `ScriptDebuggerService.Resumed(threadIds: Array)`

Fires when a previously paused thread resumes. After this event, all
`frameId` values, `VariablesReference` values, and script variable objects
from that thread are invalidated. Re-fetch them the next time the
[DataModel](/docs/reference/engine/classes/DataModel.md) stops if needed.

Avoid modifying the [DataModel](/docs/reference/engine/classes/DataModel.md), throwing unhandled errors, or
calling async yielding functions inside this event handler.

*Security: PluginSecurity*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `threadIds` | `Array` | An array of thread identifiers that resumed. |

## Callbacks

### Callback: ScriptDebuggerService.OnStopped

**Signature:** `ScriptDebuggerService.OnStopped(stopped: Dictionary): ScriptResumeAction`

The primary mechanism for reacting to debugger pauses. Set this to a
function that receives a `stopped` payload and returns a script resume
action dictionary indicating how execution should continue.

Only one `OnStopped` per [DataModel](/docs/reference/engine/classes/DataModel.md) is allowed; it is not inherited
from the edit [DataModel](/docs/reference/engine/classes/DataModel.md).

If the callback returns nothing or throws,
[DebuggerResumeType.Resume](/docs/reference/engine/enums/DebuggerResumeType.md) is assumed. Avoid modifying the
[DataModel](/docs/reference/engine/classes/DataModel.md), throwing unhandled errors, or calling async yielding
functions inside this callback.

#### Late-Set Behavior

If `OnStopped` is set while the [DataModel](/docs/reference/engine/classes/DataModel.md) is already stopped at a
breakpoint and the previous value was `nil`, the callback runs
immediately.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `stopped` | `Dictionary` |  | Dictionary describing why the debugger paused. The following key-value pairs are valid:  - `Reason` — [ScriptStoppedReason](/docs/reference/engine/enums/ScriptStoppedReason.md) why the debugger paused. - `ThreadIds` — Array of thread identifiers that stopped. - `ExceptionText` — Error message present when `Reason` is   [ScriptStoppedReason.Exception](/docs/reference/engine/enums/ScriptStoppedReason.md). |

**Returns:** `ScriptResumeAction` — Dictionary specifying how to resume execution. Contains the following
key-value pairs:

- `steppedType` — [DebuggerResumeType](/docs/reference/engine/enums/DebuggerResumeType.md) describing how to resume.
- `threadId` — Number indicating which thread to step. Required for
  step actions.

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