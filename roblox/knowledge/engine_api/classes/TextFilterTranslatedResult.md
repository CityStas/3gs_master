---
name: TextFilterTranslatedResult
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "Holds the filtered source text and its filtered translations produced by TextService:FilterAndTranslateStringAsync()."
---

# Class: TextFilterTranslatedResult

> Holds the filtered source text and its filtered translations produced by
> [TextService:FilterAndTranslateStringAsync()](/docs/reference/engine/classes/TextService.md).

## Description

A [TextFilterTranslatedResult](/docs/reference/engine/classes/TextFilterTranslatedResult.md) is the object returned by
[TextService:FilterAndTranslateStringAsync()](/docs/reference/engine/classes/TextService.md). It bundles the filtered
source text together with filtered translations of that text into each
requested target locale.

Read [TextFilterTranslatedResult.SourceText](/docs/reference/engine/classes/TextFilterTranslatedResult.md) and
[TextFilterTranslatedResult.SourceLanguage](/docs/reference/engine/classes/TextFilterTranslatedResult.md) for the filtered original
text and its language, call
[TextFilterTranslatedResult:GetTranslationForLocale()](/docs/reference/engine/classes/TextFilterTranslatedResult.md) to retrieve the
filtered translation for a single locale, or call
[TextFilterTranslatedResult:GetTranslations()](/docs/reference/engine/classes/TextFilterTranslatedResult.md) to retrieve all of them
at once.

Instances of this class cannot be created, parented, or replicated; they are
only produced by the engine as the return value of the filtering call. That
call, [TextService:FilterAndTranslateStringAsync()](/docs/reference/engine/classes/TextService.md), is deprecated, so
new work should filter and translate chat through [TextChatService](/docs/reference/engine/classes/TextChatService.md)
instead.

## Properties

### Property: TextFilterTranslatedResult.SourceLanguage

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

The language string of the original text that was submitted to
[TextService:FilterAndTranslateStringAsync()](/docs/reference/engine/classes/TextService.md). This is the source
language that the translations returned by
[TextFilterTranslatedResult:GetTranslations()](/docs/reference/engine/classes/TextFilterTranslatedResult.md) were translated from.
This property is read-only.

### Property: TextFilterTranslatedResult.SourceText

```json
{
  "type": "TextFilterResult",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

A [TextFilterResult](/docs/reference/engine/classes/TextFilterResult.md) representing the filtered form of the original
text that was submitted to
[TextService:FilterAndTranslateStringAsync()](/docs/reference/engine/classes/TextService.md), in its
[TextFilterTranslatedResult.SourceLanguage](/docs/reference/engine/classes/TextFilterTranslatedResult.md). Use the returned
[TextFilterResult](/docs/reference/engine/classes/TextFilterResult.md) to obtain the correctly filtered string for each
recipient before displaying the untranslated text. This property is
read-only.

## Methods

### Method: TextFilterTranslatedResult:GetTranslationForLocale

**Signature:** `TextFilterTranslatedResult:GetTranslationForLocale(locale: string): TextFilterResult`

Returns the filtered [TextFilterResult](/docs/reference/engine/classes/TextFilterResult.md) for the translation of the
source text into `locale`, or `nil` if the result contains no translation
for that locale. The `locale` argument is normalized to its language
before lookup, so locale variants that share a language resolve to the
same translation.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `locale` | `string` |  | The locale identifier of the translation to retrieve. |

**Returns:** `TextFilterResult` — The filtered [TextFilterResult](/docs/reference/engine/classes/TextFilterResult.md) for the requested locale, or
`nil` if the result contains no translation for it.

### Method: TextFilterTranslatedResult:GetTranslations

**Signature:** `TextFilterTranslatedResult:GetTranslations(): Dictionary`

Returns a dictionary that maps each translation's language string to its
filtered [TextFilterResult](/docs/reference/engine/classes/TextFilterResult.md). The keys are the languages that the
source text was translated into for the requested target locales; use
[TextFilterTranslatedResult:GetTranslationForLocale()](/docs/reference/engine/classes/TextFilterTranslatedResult.md) to look up a
single locale directly.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `Dictionary` — A dictionary mapping each translation's language string to its
filtered [TextFilterResult](/docs/reference/engine/classes/TextFilterResult.md).

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