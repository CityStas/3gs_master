---
name: StyleSheet
last_updated: 2026-10-30T19:55:53Z
inherits:
  - StyleBase
  - Instance
  - Object
type: class
memory_category: Gui
summary: "Aggregates StyleRules and can be linked to DataModel trees to apply style properties to instances."
---

# Class: StyleSheet

> Aggregates [StyleRules](/docs/reference/engine/classes/StyleRule.md) and can be linked to [DataModel](/docs/reference/engine/classes/DataModel.md)
> trees to apply style properties to instances.

## Description

Aggregates [StyleRules](/docs/reference/engine/classes/StyleRule.md) and can be linked to [DataModel](/docs/reference/engine/classes/DataModel.md)
trees to apply style properties to instances. Note that a `StyleSheet` may
exist outside the [DataModel](/docs/reference/engine/classes/DataModel.md), but it cannot be derived or linked to a
[DataModel](/docs/reference/engine/classes/DataModel.md) tree in such a case.

## Methods

### Method: StyleSheet:GetDerives

**Signature:** `StyleSheet:GetDerives(): List<StyleSheet>`

Returns an array of other `StyleSheets` from which the `StyleSheet` is
deriving [StyleRules](/docs/reference/engine/classes/StyleRule.md) and token definitions.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `List<StyleSheet>` — Array of other `StyleSheets`.

### Method: StyleSheet:SetDerives

**Signature:** `StyleSheet:SetDerives(derives: Instances): ()`

Sets the `StyleSheet` to derive [StyleRules](/docs/reference/engine/classes/StyleRule.md) and token
definitions from one or more other `StyleSheets` in the order they are
listed. This method spawns the appropriate [StyleDerive](/docs/reference/engine/classes/StyleDerive.md) instances
and sets their priorities to establish the specified derivations.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local coreSheet = ReplicatedStorage:FindFirstChild("CoreSheet")

-- Create a tokens style sheet
local tokensSheet = Instance.new("StyleSheet")
tokensSheet.Name = "Tokens"
tokensSheet.Parent = ReplicatedStorage
-- Set tokens (attributes) on tokens sheet
tokensSheet:SetAttribute("LightGray", Color3.new(0.9, 0.9, 0.9))
tokensSheet:SetAttribute("DarkGray", Color3.new(0.2, 0.2, 0.2))

-- Create theme style sheets
local lightThemeSheet = Instance.new("StyleSheet")
lightThemeSheet.Name = "LightTheme"
lightThemeSheet:SetAttribute("Background", "$LightGray")
lightThemeSheet.Parent = ReplicatedStorage
local darkThemeSheet = Instance.new("StyleSheet")
darkThemeSheet.Name = "DarkTheme"
darkThemeSheet:SetAttribute("Background", "$DarkGray")
darkThemeSheet.Parent = ReplicatedStorage

-- Set theme sheets to derive from tokens sheet
lightThemeSheet:SetDerives({ tokensSheet })
darkThemeSheet:SetDerives({ tokensSheet })

local themeDerive = Instance.new("StyleDerive")
themeDerive.Parent = coreSheet
themeDerive.StyleSheet = lightThemeSheet

-- Function to dynamically change the derived theme for the core sheet
local function changeTheme()
	if themeDerive.StyleSheet == lightThemeSheet then
		themeDerive.StyleSheet = darkThemeSheet
	elseif themeDerive.StyleSheet == darkThemeSheet then
		themeDerive.StyleSheet = lightThemeSheet
	end
end
```

Note that if you've created a design using the
[Style Editor](/docs/en-us/ui/styling/editor.md), the **StyleSheet** sheet in
the **Design** folder of [ReplicatedStorage](/docs/reference/engine/classes/ReplicatedStorage.md) will contain a
[StyleDerive](/docs/reference/engine/classes/StyleDerive.md) to the **BaseStyleSheet** also in the **Design**
folder. When setting derives with `SetDerives()`, be sure to include the
base style sheet in the spot of least priority in relation to other
`StyleSheets` in the `derives` array.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `derives` | `Instances` |  | Array of other `StyleSheets` to derive [StyleRules](/docs/reference/engine/classes/StyleRule.md) and token definitions from. |

**Returns:** `()`

## Inherited Members

### From [StyleBase](/docs/reference/engine/classes/StyleBase.md)

- **Method `GetStyleRules(): List<StyleRule>`**: Returns an array of associated StyleRules.
- **Method `InsertStyleRule(rule: StyleRule, priority: int?): ()`**: Inserts a new StyleRule into the array of rules.
- **Method `SetStyleRules(rules: Instances): ()`**: Similar to InsertStyleRule() but lets
- **Event `StyleRulesChanged`**: Fires when one or more StyleRules is explicitly changed

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