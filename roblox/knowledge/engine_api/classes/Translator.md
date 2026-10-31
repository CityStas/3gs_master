---
name: Translator
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "The role of a Translator is to manufacture/return strings localized for the viewing player."
---

# Class: Translator

> The role of a Translator is to manufacture/return strings localized for the
> viewing player.

## Description

The role of a Translator is to manufacture/return strings localized for the
viewing player. It can be used to retrieve display-ready localized text from a
[LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md). The source of the [Translator.LocaleId](/docs/reference/engine/classes/Translator.md)
property, the set of tables it will search, and the order it will search them
in depends on which method was used to create the Translator instance.

The input for a Translator is the original development language string and a
context, where all or part of the context can be used to find a more
precise/situational translation for the source string.

The Translator can also be used to manufacture translated strings with inserts
(data replacements) which may change order based on the target language.

## Properties

### Property: Translator.LocaleId

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Basic"
  ]
}
```

The Roblox locale of the output translated strings from this table, for
example "en-us" or "es-es." Defaults to "en-us".

## Methods

### Method: Translator:FormatByKey

**Signature:** `Translator:FormatByKey(key: string, args: Variant): string`

Returns the localized text string in a [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) based on
its [Translator](/docs/reference/engine/classes/Translator.md) locale, by key. The optional **args** table is used
for filling format parameters in the matching text entry.

Note that this method will throw an error in the following cases:

- If none of the [LocalizationTables](/docs/reference/engine/classes/LocalizationTable.md) available to
  this [Translator](/docs/reference/engine/classes/Translator.md) include a value for the given key.
- If the
  [format string](/docs/en-us/production/localization/translate-dynamic-content.md)
  for the key uses numbered parameters and **args** is not an array.
- If the
  [format string](/docs/en-us/production/localization/translate-dynamic-content.md)
  uses named parameters and **args** is not a table of key-value pairs.
- If **args** is missing values for parameters that are used in the
  matching
  [format string](/docs/en-us/production/localization/translate-dynamic-content.md).

See
[Localize with scripting](/docs/en-us/production/localization/localize-with-scripting.md)
for more details and usage examples of this function.

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The **Key** value to look up and translate. |
| `args` | `Variant` |  | To be provided if the **Source** text and translations contain format strings. Will be a Luau table of values **or** key-value pairs, depending on whether the format strings are numbered or named. |

**Returns:** `string` — The localized text string associated with the given **key**, with any
format parameters filled in from **args**.

### Method: Translator:Translate

**Signature:** `Translator:Translate(context: Instance, text: string): string`

Returns the localized text string in a [LocalizationTable](/docs/reference/engine/classes/LocalizationTable.md) based on
its [Translator](/docs/reference/engine/classes/Translator.md) locale. This string will be in the context of the
provided object, given the provided **Source** text.

See
[Localize with scripting](/docs/en-us/production/localization/localize-with-scripting.md)
for more details and usage examples of this function.

#### Context Overrides

In some cases, duplicate **Source** strings may have completely different
translations in other languages. For example, the English noun "Screen"
can indicate both a computer screen and a window screen, but the Spanish
translations are completely different:

| A | B | C | D | E |
| --- | --- | --- | --- | --- |
| Key | Context | **Source** | Example | **es** |
|  |  | Screen |  | Pantalla |
|  |  | Screen |  | Mosquitero |
|  |  |  |  | |

In these cases, the first argument to this function &mdash; a valid
in-game [Instance](/docs/reference/engine/classes/Instance.md) &mdash; can be used as a "tie breaker" when
multiple GUI objects use the same source string. To implement this,
specify the "path" to the [Instance](/docs/reference/engine/classes/Instance.md) you'd like to override as the
**Context** value of the translation data:

| A | B | C | D | E |
| --- | --- | --- | --- | --- |
| Key | **Context** | Source | Example | es |
|  | workspace.ComputerScreen.SurfaceGui.TextLabel | Screen |  | Pantalla |
|  |  | Screen |  | Mosquitero |
|  |  |  |  | |

Then, when calling this function in a script, pass the same
[Instance](/docs/reference/engine/classes/Instance.md) as the first argument, followed by the **Source** lookup
text as the second argument:

*Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `context` | `Instance` |  | A valid in-game [Instance](/docs/reference/engine/classes/Instance.md) to use for context override as outlined above. Note that this argument can be arbitrary, for example `game`, if you don't require a context override. |
| `text` | `string` |  | The **Source** text to look up and translate. |

**Returns:** `string` — The translated text.

**Translate**

Demonstrates [Translator:Translate()](/docs/reference/engine/classes/Translator.md).

```lua
local Players = game:GetService("Players")
local LocalizationService = game:GetService("LocalizationService")

local success, translator = pcall(function()
	return LocalizationService:GetTranslatorForPlayerAsync(Players.LocalPlayer)
end)

if success then
	local trans = translator:Translate(workspace.ComputerScreen.SurfaceGui.TextLabel, "Screen")
	print(trans)
else
	warn("Cannot load translator for player!")
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