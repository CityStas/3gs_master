---
name: ModuleScript
last_updated: 2026-10-30T19:55:52Z
inherits:
  - LuaSourceContainer
  - Instance
  - Object
type: class
memory_category: Script
summary: "A script type that runs once when LuaGlobals.require() is called with it. Returns exactly one value, usually a table of functions, to used by other scripts. Useful for compartmentalizing code."
---

# Class: ModuleScript

> A script type that runs once when [LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) is called with
> it. Returns exactly one value, usually a table of functions, to used by other
> scripts. Useful for compartmentalizing code.

## Description

A [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) is a script type that returns exactly one value by a
call to [LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md). [ModuleScripts](/docs/reference/engine/classes/ModuleScript.md) run
once and only once per Luau environment and return the exact same value for
subsequent calls to [LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md).

[ModuleScripts](/docs/reference/engine/classes/ModuleScript.md) are essential objects for adhering to the
"Don't Repeat Yourself" (DRY) principle, allowing you to write a function only
once and use it everywhere. Having multiple copies of a function is
problematic when you need to change their behavior, so you should define
functions or groups of functions in [ModuleScripts](/docs/reference/engine/classes/ModuleScript.md) and
have your [Scripts](/docs/reference/engine/classes/Script.md) and [LocalScripts](/docs/reference/engine/classes/LocalScript.md) call
[LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) on those modules.

It's important to know that return values from
[ModuleScripts](/docs/reference/engine/classes/ModuleScript.md) are independent with regards to
[Scripts](/docs/reference/engine/classes/Script.md) and [LocalScripts](/docs/reference/engine/classes/LocalScript.md), and other
environments like the
[Command&nbsp;Bar](/docs/en-us/studio/ui-overview.md#command-bar). Using
[LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) on a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) in a
[LocalScript](/docs/reference/engine/classes/LocalScript.md) will run the code on the client, even if a [Script](/docs/reference/engine/classes/Script.md)
did so already on the server. Therefore, be careful if you're using a
[ModuleScript](/docs/reference/engine/classes/ModuleScript.md) on the client and server at the same time, or debugging
it within Studio.

Note that the first call to [LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) will not yield
(halt) unless the [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) yields (calls [task.wait()](/docs/reference/engine/globals/task.md) for
example), in which case the current thread that called
[LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) will yield until the [ModuleScript](/docs/reference/engine/classes/ModuleScript.md)
returns a value. If a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) is attempting to
[LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) another [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) that in turn tries
to [LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) it, the thread will **hang and never halt**
(cyclic [LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) calls do not generate errors). Be
mindful of your module dependencies in large projects!

If a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) is uploaded to Roblox and the root module has the
name set to `MainModule`, it can be uploaded as a model and required using
[LuaGlobals.require()](/docs/reference/engine/globals/LuaGlobals.md) with the model's asset ID. Then it can be loaded
into your experience, although this logic only works on the server and will
error on the client. If other users want to use the module, it must be public.

## Code Samples

**Simple ModuleScript Example**

The code sample starts by creating a local variable holding an empty table. It
then fills the table with two placeholder functions, and then finally returns
the table. Using this code in a ModuleScript would make the `my_functions`
table (and thus any functions, tables or other values within it) available to
any Script, LocalScript or other ModuleScript.

```lua
-- Tables store multiple values in one variable
local MyFunctions = {}

-- Add a few functions to the table
function MyFunctions.foo()
	print("Foo!")
end

function MyFunctions.bar()
	print("Bar!")
end

-- ModuleScripts must return exactly one value
return MyFunctions
```

**Simple ModuleScript Usage**

This code sample shows how to use the require function on a ModuleScript, then
use the value that it returned. See the "Simple ModuleScript Example" for the
code to go with this sample.

```lua
-- The require function is provided a ModuleScript, then runs
-- the code, waiting until it returns a singular value.
local MyFunctions = require(script.Parent.MyFunctions)

-- These are some dummy functions defined in another code sample
MyFunctions.foo()
MyFunctions.bar()
```

## Properties

### Property: ModuleScript.Source

```json
{
  "type": "ProtectedString",
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
    "PluginOrOpenCloud"
  ]
}
```

The code to be executed.

If you want to read or modify a script that the user has open, consider
using the [ScriptEditorService](/docs/reference/engine/classes/ScriptEditorService.md) to interact with the Script Editor
instead.

### Property: ModuleScript.LinkedSource

```json
{
  "type": "ContentId",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "LoadUnownedAsset"
  ]
}
```

> **Deprecated:** This property is now replaced by [packages](/docs/en-us/projects/assets/packages.md) which has greater functionality.

Used to store a URL that points to an online script source. Binds the
online code to the script's [Script.Source](/docs/reference/engine/classes/Script.md).

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