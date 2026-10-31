---
name: ScreenshotHud
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "A 2D user interface that allows users to capture and save screenshots to their local device."
---

# Class: ScreenshotHud

> A 2D user interface that allows users to capture and save screenshots to their
> local device.

## Description

The [ScreenshotHud](/docs/reference/engine/classes/ScreenshotHud.md) is a 2D user interface that allows users to capture
and save screenshots to their local device. It consists of the following UI
elements:

- An overlay containing the experience name and Roblox branding. These remain
  on screen when a screenshot is taken, although the experience name can be
  disabled through the [ScreenshotHud.ExperienceNameOverlayEnabled](/docs/reference/engine/classes/ScreenshotHud.md)
  property.
- A camera button that hides all UI except for the overlay and takes a
  screenshot.
- A close button that closes the [ScreenshotHud](/docs/reference/engine/classes/ScreenshotHud.md).

## Code Samples

**LocalScript**

```lua
local GuiService = game:GetService("GuiService")

local screenshotHud = GuiService:WaitForChild("ScreenshotHud")
screenshotHud.ExperienceNameOverlayEnabled = true
screenshotHud.OverlayFont = Enum.Font.GothamMedium
screenshotHud.Visible = true
```

## Properties

### Property: ScreenshotHud.CameraButtonIcon

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
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

Asset ID of the icon used for the camera button.

### Property: ScreenshotHud.CameraButtonIconContent

```json
{
  "type": "Content",
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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

The image [Content](/docs/reference/engine/datatypes/Content.md) used as the icon for the camera button on the
[ScreenshotHud](/docs/reference/engine/classes/ScreenshotHud.md). This is the [Content](/docs/reference/engine/datatypes/Content.md)-type equivalent of
the legacy [ScreenshotHud.CameraButtonIcon](/docs/reference/engine/classes/ScreenshotHud.md) property and supports
asset URIs. When set, the camera button displays the specified image
instead of the default icon.

### Property: ScreenshotHud.CameraButtonPosition

```json
{
  "type": "UDim2",
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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

Screen location of the camera button.

### Property: ScreenshotHud.CloseButtonPosition

```json
{
  "type": "UDim2",
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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

Screen location of the close button.

### Property: ScreenshotHud.CloseWhenScreenshotTaken

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
    "UI"
  ]
}
```

Determines whether the [ScreenshotHud](/docs/reference/engine/classes/ScreenshotHud.md) closes automatically when a
screenshot is taken.

### Property: ScreenshotHud.HideCoreGuiForCaptures

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
    "UI"
  ]
}
```

Determines whether Roblox's core GUI is hidden while a screenshot is
captured through the [ScreenshotHud](/docs/reference/engine/classes/ScreenshotHud.md). Defaults to `true`, so any
enabled [CoreGuiType](/docs/reference/engine/enums/CoreGuiType.md) elements are hidden for the duration of the
capture and restored afterward. A saved capture is only flagged as
GUI-free when both this property and
[ScreenshotHud.HidePlayerGuiForCaptures](/docs/reference/engine/classes/ScreenshotHud.md) are enabled.

### Property: ScreenshotHud.HidePlayerGuiForCaptures

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
    "UI"
  ]
}
```

Determines whether the local player's GUI is hidden while a screenshot is
captured through the [ScreenshotHud](/docs/reference/engine/classes/ScreenshotHud.md). Defaults to `true`, so any
enabled [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) instances under the
[Players.LocalPlayer](/docs/reference/engine/classes/Players.md)'s [PlayerGui](/docs/reference/engine/classes/PlayerGui.md) are hidden for the
duration of the capture and restored afterward. A saved capture is only
flagged as GUI-free when both this property and
[ScreenshotHud.HideCoreGuiForCaptures](/docs/reference/engine/classes/ScreenshotHud.md) are enabled.

### Property: ScreenshotHud.Visible

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
  "category": "State",
  "capabilities": [
    "UI"
  ]
}
```

Determines whether the [ScreenshotHud](/docs/reference/engine/classes/ScreenshotHud.md) is visible.

### Property: ScreenshotHud.ExperienceNameOverlayEnabled *(hidden)*

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

> **Deprecated:** This property is deprecated. Do not use it for new work.

Determines whether the experience name in the overlay is enabled.

### Property: ScreenshotHud.OverlayFont *(hidden)*

```json
{
  "type": "Enum.Font",
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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

> **Deprecated:** This property is deprecated. Do not use it for new work.

The [Font](/docs/reference/engine/datatypes/Font.md) used for the experience name in the overlay.

### Property: ScreenshotHud.UsernameOverlayEnabled *(hidden)*

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

> **Deprecated:** This property is deprecated. Do not use it for new work.

Currently has no effect.

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