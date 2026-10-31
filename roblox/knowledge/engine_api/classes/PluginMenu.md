---
name: PluginMenu
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "A context menu that can be shown in Studio. Displays a list of PluginActions and supports submenus."
---

# Class: PluginMenu

> A context menu that can be shown in Studio. Displays a list of
> [PluginActions](/docs/reference/engine/classes/PluginAction.md) and supports submenus.

## Description

`PluginMenu` represents a context menu which can be shown in Studio to display
a list of [PluginActions](/docs/reference/engine/classes/PluginAction.md) and which also supports submenus.
A `PluginMenu` must be created using the [Plugin:CreatePluginMenu()](/docs/reference/engine/classes/Plugin.md)
method in order to work as expected.

## Code Samples

**Creating a PluginMenu and PluginMenuAction**

This code sample visualizes how [PluginMenus](/docs/reference/engine/classes/PluginMenu.md) and
[PluginActions](/docs/reference/engine/classes/PluginAction.md) behave when created for a [Plugin](/docs/reference/engine/classes/Plugin.md).
Outside of this example, you should not parent the plugin or its functional
components to the experience's workspace.

After executing the code, changing the created [BoolValue](/docs/reference/engine/classes/BoolValue.md) in the
experience's workspace opens the plugin's menus. Selecting an action from the
menus the function connected to the trigger signal.

```lua
-- This code can be pasted into the Command Bar, but only once
local pluginMenu = plugin:CreatePluginMenu(math.random(), "Test Menu")
pluginMenu.Name = "Test Menu"

pluginMenu:AddNewAction("ActionA", "A", "rbxasset://textures/loading/robloxTiltRed.png")
pluginMenu:AddNewAction("ActionB", "B", "rbxasset://textures/loading/robloxTilt.png")

local subMenu = plugin:CreatePluginMenu(math.random(), "C", "rbxasset://textures/explosion.png")
subMenu.Name = "Sub Menu"

subMenu:AddNewAction("ActionD", "D", "rbxasset://textures/whiteCircle.png")
subMenu:AddNewAction("ActionE", "E", "rbxasset://textures/icon_ROBUX.png")

pluginMenu:AddMenu(subMenu)
pluginMenu:AddSeparator()

pluginMenu:AddNewAction("ActionF", "F", "rbxasset://textures/sparkle.png")

local toggle = Instance.new("BoolValue")
toggle.Name = "TogglePluginMenu"
toggle.Parent = workspace

local function onToggled()
	if toggle.Value then
		toggle.Value = false

		local selectedAction = pluginMenu:ShowAsync()
		if selectedAction then
			print("Selected Action:", selectedAction.Text, "with ActionId:", selectedAction.ActionId)
		else
			print("User did not select an action!")
		end
	end
end

toggle.Changed:Connect(onToggled)
```

## Properties

### Property: PluginMenu.Icon

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance"
}
```

This property determines the icon to be displayed when used as a submenu.
It defaults to an empty string `""`.

### Property: PluginMenu.Title

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance"
}
```

This property determines the text to be displayed when a
[PluginMenu](/docs/reference/engine/classes/PluginMenu.md) is used as a submenu. It defaults to an empty string
`""`.

### Property: PluginMenu.Visible

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

This property determines whether a [PluginMenu](/docs/reference/engine/classes/PluginMenu.md) is shown when it is
displayed as a submenu of another menu, that is, when it has been added to
a parent menu through [PluginMenu:AddMenu()](/docs/reference/engine/classes/PluginMenu.md). It defaults to `true`;
setting it to `false` hides the submenu's entry in its parent menu.

## Methods

### Method: PluginMenu:AddAction

**Signature:** `PluginMenu:AddAction(action: Instance): ()`

Adds the given action to the menu.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `action` | `Instance` |  | The action to add. |

**Returns:** `()`

### Method: PluginMenu:AddMenu

**Signature:** `PluginMenu:AddMenu(menu: Instance): ()`

Adds the given menu as a separator.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `menu` | `Instance` |  | The menu to add as a submenu. Uses its [Title](/docs/reference/engine/classes/PluginMenu.md) and [Icon](/docs/reference/engine/classes/PluginMenu.md) to display. |

**Returns:** `()`

### Method: PluginMenu:AddNewAction

**Signature:** `PluginMenu:AddNewAction(actionId: string, text: string, icon: string): Instance`

Creates a temporary action that is hidden from Studio's **File**&nbsp;⟩
**Customize Shortcuts** window.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actionId` | `string` |  | Must be a unique string that identifies this [PluginAction](/docs/reference/engine/classes/PluginAction.md) from others. |
| `text` | `string` |  | The text to be displayed. |
| `icon` | `string` |  | The icon to be displayed. |

**Returns:** `Instance` — The created [PluginAction](/docs/reference/engine/classes/PluginAction.md).

### Method: PluginMenu:AddSeparator

**Signature:** `PluginMenu:AddSeparator(): ()`

Adds a separator between items in the menu.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `()`

### Method: PluginMenu:Clear

**Signature:** `PluginMenu:Clear(): ()`

Clears the menu.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `()`

### Method: PluginMenu:ShowAsync

**Signature:** `PluginMenu:ShowAsync(): Instance`

Shows the menu at the mouse cursor. It yields until either an item is
selected or the menu is closed. The selected action fires its
[PluginAction.Triggered](/docs/reference/engine/classes/PluginAction.md) event.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `Instance` — The [PluginAction](/docs/reference/engine/classes/PluginAction.md) item that was selected or `nil`.

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