---
name: ScreenGui
last_updated: 2026-10-30T19:55:53Z
inherits:
  - LayerCollector
  - GuiBase2d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Primary container of on-screen 2D user interface elements."
---

# Class: ScreenGui

> Primary container of on-screen 2D user interface elements.

## Description

[ScreenGui](/docs/reference/engine/classes/ScreenGui.md) is a storage container for 2D [GuiObjects](/docs/reference/engine/classes/GuiObject.md)
displayed on the user's screen. A [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) only shows if parented to
a player's [PlayerGui](/docs/reference/engine/classes/PlayerGui.md); parenting a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) to
[StarterGui](/docs/reference/engine/classes/StarterGui.md) ensures it clones into each player's [PlayerGui](/docs/reference/engine/classes/PlayerGui.md) when
they join the experience and their character first spawns. See
[On‑Screen UI Containers](/docs/en-us/ui/on-screen-containers.md) for further
details.

![Example ScreenGui with various GuiObject children, including a Frame, TextLabel, TextBox, and ImageButton.](../../../assets/ui/ui-objects/ScreenGui-Example.jpg)

For performance improvements, the appearance of a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) is cached
until one of the following events occurs:

- A descendant is added to or removed from it.
- A property of a descendant changes.
- A property of the [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) itself changes.

If any of these events occur, the [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) appearance is recomputed
on the next frame it gets rendered.

## Properties

### Property: ScreenGui.ClipToDeviceSafeArea

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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

If this property is `true`, all [GuiObject](/docs/reference/engine/classes/GuiObject.md) descendants of the
[ScreenGui](/docs/reference/engine/classes/ScreenGui.md) will be clipped to the device's safe area (see
[ScreenInsets](/docs/reference/engine/enums/ScreenInsets.md)). The default is `true` to maintain backwards
compatibility of UI that is intentionally hidden offscreen, such as
objects that slide into view from a screen edge when they're needed.

![Mobile device showing UI button clipped by device safe
area](../../../assets/engine-api/classes/ScreenGui/ClipToDeviceSafeArea-True.png)

If this property is `false`, [GuiObject](/docs/reference/engine/classes/GuiObject.md) descendants will **not** be
clipped to the device's safe area and may be obscured by the camera notch
or other screen cutouts.

![Mobile device showing UI button overflowing device safe
area, obscured by screen camera notch](../../../assets/engine-api/classes/ScreenGui/ClipToDeviceSafeArea-False.png)

Note that this property will be ignored if you set
[ScreenInsets](/docs/reference/engine/classes/ScreenGui.md) to [None](/docs/reference/engine/enums/ScreenInsets.md),
as doing so implies that you intentionally want to disregard the device's
safe insets.

### Property: ScreenGui.DisplayOrder

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
    "UI"
  ]
}
```

This property controls the Z-index order in which multiple
[ScreenGui](/docs/reference/engine/classes/ScreenGui.md) containers are drawn. Those with a higher
[DisplayOrder](/docs/reference/engine/classes/ScreenGui.md) will be drawn on top of those
with a lower value.

### Property: ScreenGui.IgnoreGuiInset

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

If this property is `false` (default),
[ScreenInsets](/docs/reference/engine/classes/ScreenGui.md) is set to
[CoreUISafeInsets](/docs/reference/engine/enums/ScreenInsets.md), effectively keeping its bounds below
the Roblox top bar core UI.

If this property is changed to `true` and
[ScreenInsets](/docs/reference/engine/classes/ScreenGui.md) is currently set to
[CoreUISafeInsets](/docs/reference/engine/enums/ScreenInsets.md),
[ScreenInsets](/docs/reference/engine/classes/ScreenGui.md) will be set to
[DeviceSafeInsets](/docs/reference/engine/enums/ScreenInsets.md).

See [ScreenInsets](/docs/reference/engine/classes/ScreenGui.md) for details on how screen
insets affect the contents of a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md).

### Property: ScreenGui.SafeAreaCompatibility

```json
{
  "type": "SafeAreaCompatibility",
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

This property specifies whether automatic UI compatibility transformations
are applied to descendant "fullscreen" [GuiObjects](/docs/reference/engine/classes/GuiObject.md) of the
[ScreenGui](/docs/reference/engine/classes/ScreenGui.md) on displays with screen cutouts. Eligibility occurs if
the total area of the descendant [GuiObject](/docs/reference/engine/classes/GuiObject.md) (including any applied
border or [UIStroke](/docs/reference/engine/classes/UIStroke.md)) covers the device's safe area both
horizontally and vertically. See the [SafeAreaCompatibility](/docs/reference/engine/enums/SafeAreaCompatibility.md) enum
reference for details.

The default value is [FullscreenExtension](/docs/reference/engine/enums/SafeAreaCompatibility.md) in
order to automatically improve the appearance of UI that was authored for
screens without any cutouts. However, it's recommended that you avoid
fullscreen extensions for new work; instead, use the
[ScreenInsets](/docs/reference/engine/classes/ScreenGui.md) property to specify which
insets should be respected for different [ScreenGui](/docs/reference/engine/classes/ScreenGui.md) containers.

Note that descendant UI objects will continue to be clipped by the
device's safe area if
[ClipToDeviceSafeArea](/docs/reference/engine/classes/ScreenGui.md) is set to
`true`.

### Property: ScreenGui.ScreenInsets

```json
{
  "type": "ScreenInsets",
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

This property controls the safe area insets that are applied to the
contents of the [ScreenGui](/docs/reference/engine/classes/ScreenGui.md).

The default of [CoreUISafeInsets](/docs/reference/engine/enums/ScreenInsets.md) keeps all descendant
[GuiObjects](/docs/reference/engine/classes/GuiObject.md) inside the core UI safe area, clear of the
Roblox top bar buttons and other screen cutouts like the device's camera
notch.

![Mobile device showing UI buttons inside core UI safe area](../../../assets/engine-api/enums/ScreenInsets/CoreUISafeInsets.png)

If you set this property to [None](/docs/reference/engine/enums/ScreenInsets.md), UI objects may be
obscured behind core UI objects or device cutouts like the camera notch.
As a result, you should only use [None](/docs/reference/engine/enums/ScreenInsets.md) for a
[ScreenGui](/docs/reference/engine/classes/ScreenGui.md) that contains noninteractive content like background
images.

See
[On-Screen UI Containers](/docs/en-us/ui/on-screen-containers.md#screen-insets)
for alternative examples.

## Inherited Members

### From [LayerCollector](/docs/reference/engine/classes/LayerCollector.md)

- **Property `Enabled`** (`boolean`): Toggles the visibility of this LayerCollector.
- **Property `ResetOnSpawn`** (`boolean`): Determines if the LayerCollector resets (deletes itself and
- **Property `ZIndexBehavior`** (`ZIndexBehavior`): Controls how GuiObject.ZIndex behaves on all descendants of this
- **Method `GetLayoutNodeTree(): Dictionary`**:  *(deprecated)*

### From [GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md)

- **Property `AbsolutePosition`** (`Vector2`): Describes the actual screen position of a GuiBase2d element, in
- **Property `AbsoluteRotation`** (`float`): Describes the actual screen rotation of a GuiBase2d element, in
- **Property `AbsoluteSize`** (`Vector2`): Describes the actual screen size of a GuiBase2d element, in
- **Property `AutoLocalize`** (`boolean`): When set to `true`, localization will be applied to this GuiBase2d
- **Property `Localize`** (`boolean`): Automatically set to true when a localization table's *(deprecated, hidden)*
- **Property `RootLocalizationTable`** (`LocalizationTable`): A reference to a LocalizationTable to be used to apply automated
- **Property `SelectionBehaviorDown`** (`SelectionBehavior`): Customizes gamepad selection behavior in the down direction.
- **Property `SelectionBehaviorLeft`** (`SelectionBehavior`): Customizes gamepad selection behavior in the left direction.
- **Property `SelectionBehaviorRight`** (`SelectionBehavior`): Customizes gamepad selection behavior in the right direction.
- **Property `SelectionBehaviorUp`** (`SelectionBehavior`): Customizes gamepad selection behavior in the up direction.
- **Property `SelectionGroup`** (`boolean`): Allows customization of gamepad selection movement.
- **Event `SelectionChanged`**: Fires when the gamepad selection moves to, leaves, or changes within the

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