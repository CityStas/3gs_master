---
name: BillboardGui
last_updated: 2026-10-30T19:55:52Z
inherits:
  - LayerCollector
  - GuiBase2d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "A container for GuiObjects that renders in 3D space facing the camera."
---

# Class: BillboardGui

> A container for [GuiObjects](/docs/reference/engine/classes/GuiObject.md) that renders in 3D space facing
> the camera.

## Description

[BillboardGui](/docs/reference/engine/classes/BillboardGui.md) is a container for UI objects to appear in the 3D space
but always face the camera. The container's position is relative to the parent
[BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md) (or the
[Adornee](/docs/reference/engine/classes/BillboardGui.md)). For [BaseParts](/docs/reference/engine/classes/BasePart.md), the
[Position](/docs/reference/engine/classes/BasePart.md) property is used, while for
[Attachments](/docs/reference/engine/classes/Attachment.md), the
[WorldPosition](/docs/reference/engine/classes/Attachment.md) property is used.

![BillboardGui with a TextLabel describing the screen console it floats above.](/assets/ui/in-experience/BillboardGui-Diagram.jpg)

A billboard's [Size](/docs/reference/engine/classes/BillboardGui.md) property works slightly
differently than [GuiObject.Size](/docs/reference/engine/classes/GuiObject.md). While the **offset** components work
the same, the **scale** components are used as stud sizes in 3D space.

When creating a size-scaled [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) that contains a
[TextLabel](/docs/reference/engine/classes/TextLabel.md), it's useful to enable the label's
[TextScaled](/docs/reference/engine/classes/TextLabel.md) property so that its text scales along
with the billboard canvas as the camera distance changes.

Note that interactive UI elements like [ImageButtons](/docs/reference/engine/classes/ImageButton.md) and
[TextButtons](/docs/reference/engine/classes/TextButton.md) inside a [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) will only receive
user input if they are parented to the [PlayerGui](/docs/reference/engine/classes/PlayerGui.md), typically via
placing the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) inside [StarterGui](/docs/reference/engine/classes/StarterGui.md). The
[Adornee](/docs/reference/engine/classes/BillboardGui.md) property can be used to target a part or
attachment in the 3D world while the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) itself remains in
the [PlayerGui](/docs/reference/engine/classes/PlayerGui.md).

See [In-Experience UI](/docs/en-us/ui/in-experience-containers.md#billboard-ui)
for a guide on working with [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) containers.

##### Caching Behavior

To help improve performance, the appearance of a [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) is
cached until one of the following occurs, after which its appearance will be
recomputed on the next rendering frame.

- A descendant is added to or removed from the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md).
- A property of a descendant of the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) changes.
- A property of the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) itself changes.

## Properties

### Property: BillboardGui.Active

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

Controls whether the descendants will receive input events. If the
[BillboardGui](/docs/reference/engine/classes/BillboardGui.md) contains a [GuiButton](/docs/reference/engine/classes/GuiButton.md), that button will become
clickable only if [Active](/docs/reference/engine/classes/BillboardGui.md) is set to `true` on
both the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) **and** the button.

Note that interactive UI elements like [ImageButtons](/docs/reference/engine/classes/ImageButton.md)
and [TextButtons](/docs/reference/engine/classes/TextButton.md) inside a [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) will only
receive user input if they are parented to the [PlayerGui](/docs/reference/engine/classes/PlayerGui.md),
typically via placing the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) inside [StarterGui](/docs/reference/engine/classes/StarterGui.md).
The [Adornee](/docs/reference/engine/classes/BillboardGui.md) property can be used to target a
part or attachment in the 3D world while the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) itself
remains in the [PlayerGui](/docs/reference/engine/classes/PlayerGui.md).

### Property: BillboardGui.Adornee

```json
{
  "type": "Instance",
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

Sets the target [BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md) that the
[BillboardGui](/docs/reference/engine/classes/BillboardGui.md) is positioned relative to, overriding the parent part
or attachment.

### Property: BillboardGui.AlwaysOnTop

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

This property determines whether the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) will always
render on top of other 3D objects.

When set to `false` (default), the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) renders like other
3D content and is occluded by other 3D objects. When set to `true`, the
[BillboardGui](/docs/reference/engine/classes/BillboardGui.md) always renders on top of 3D content and the
appearance changes significantly:

- Colors match how they appear inside a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md).
- Text may appear sharper on high DPI devices.
- [LightInfluence](/docs/reference/engine/classes/BillboardGui.md) is treated as though
  it's `0`.
- [Brightness](/docs/reference/engine/classes/BillboardGui.md) has no effect.

### Property: BillboardGui.Brightness

```json
{
  "type": "float",
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

This property determines the factor by which the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md)
container's light is scaled when
[LightInfluence](/docs/reference/engine/classes/BillboardGui.md) is `0`. By default,
this property is `1` and can be set to any number between `0` and `1000`.
By modifying this property, the apparent brightness of a
[BillboardGui](/docs/reference/engine/classes/BillboardGui.md) can be better matched to its environment. For
instance, a video billboard can be brightened inside a dark room by
increasing [Brightness](/docs/reference/engine/classes/BillboardGui.md) to `10`.

Note that [Brightness](/docs/reference/engine/classes/BillboardGui.md) is inaccessible in
Studio and has no effect when either
[LightInfluence](/docs/reference/engine/classes/BillboardGui.md) is `1` or
[AlwaysOnTop](/docs/reference/engine/classes/BillboardGui.md) is `true`.

### Property: BillboardGui.ClipsDescendants

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
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

When set to `true` (default), portions of [GuiObjects](/docs/reference/engine/classes/GuiObject.md)
that fall outside of the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) canvas borders will not be
drawn.

Even when this property is `false`, [GuiObjects](/docs/reference/engine/classes/GuiObject.md) that are
**completely** outside of the canvas will not render.

### Property: BillboardGui.CurrentDistance

```json
{
  "type": "float",
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

The current distance in studs that the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) is from the
player's camera. A changed event does not fire for this property unless
[DistanceStep](/docs/reference/engine/classes/BillboardGui.md) is more than `0`.

### Property: BillboardGui.DistanceStep

```json
{
  "type": "float",
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

Determines the size [CurrentDistance](/docs/reference/engine/classes/BillboardGui.md)
increments and decrements in studs as the player's camera moves closer and
further from the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md). The property defaults to `0`.

### Property: BillboardGui.ExtentsOffset

```json
{
  "type": "Vector3",
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

This property determines how the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) is offset from its
[Adornee](/docs/reference/engine/classes/BillboardGui.md), relative to the [Camera](/docs/reference/engine/classes/Camera.md)
orientation, in units half the dimensions of the model's
[Camera](/docs/reference/engine/classes/Camera.md)-aligned bounding box.

See also [StudsOffset](/docs/reference/engine/classes/BillboardGui.md) which works
similarly but uses stud units, or
[ExtentsOffsetWorldSpace](/docs/reference/engine/classes/BillboardGui.md) which
works similarly except the offset orientation is relative to the global
axes.

### Property: BillboardGui.ExtentsOffsetWorldSpace

```json
{
  "type": "Vector3",
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

This property determines how the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) is offset from its
[Adornee](/docs/reference/engine/classes/BillboardGui.md), relative to the global axes, in
units half the dimensions of the model's axis-aligned bounding box.

See also [StudsOffset](/docs/reference/engine/classes/BillboardGui.md) which works
similarly but uses stud units, or
[ExtentsOffset](/docs/reference/engine/classes/BillboardGui.md) which works similarly
except the offset orientation is relative to the [Camera](/docs/reference/engine/classes/Camera.md).

### Property: BillboardGui.LightInfluence

```json
{
  "type": "float",
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

Controls how much the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) is influenced by environmental
lighting, in a range from `0` to `1`. Setting this to `1` means that
surrounding lighting has complete control over the appearance, while
setting it to `0` means that the lighting has no effect.

### Property: BillboardGui.MaxDistance

```json
{
  "type": "float",
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

This property controls how far from the camera the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md)
will be displayed before it stops rendering. A value of `0` or `inf`
(default) means there is no limit and it will render infinitely far away.

For [BillboardGuis](/docs/reference/engine/classes/BillboardGui.md) that appear outdoors, it's
recommended that [MaxDistance](/docs/reference/engine/classes/BillboardGui.md) is high
enough to ensure that the container's UI is sufficiently small on the
screen when it appears or disappears, minimizing the sudden pop‑in/out
effect.

### Property: BillboardGui.PlayerToHideFrom

```json
{
  "type": "Instance",
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

Used by scripts to hide the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) from a specific player.

To hide a [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) from more than one player, place it into
[StarterGui](/docs/reference/engine/classes/StarterGui.md) and use a script to set the
[Enabled](/docs/reference/engine/classes/BillboardGui.md) property according to whether the
[LocalPlayer](/docs/reference/engine/classes/Players.md) should be able to see it. The
[Adornee](/docs/reference/engine/classes/BillboardGui.md) property can be used to attach the
[BillboardGui](/docs/reference/engine/classes/BillboardGui.md) to a [BasePart](/docs/reference/engine/classes/BasePart.md) or [Attachment](/docs/reference/engine/classes/Attachment.md) in the
[Workspace](/docs/reference/engine/classes/Workspace.md), instead of parenting it.

### Property: BillboardGui.Size

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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

Controls the size that the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) will have on screen.
Unlike [GuiObject.Size](/docs/reference/engine/classes/GuiObject.md), the
[scale](/docs/en-us/ui/position-and-size.md#size) components of this property
set the billboard's stud size in 3D space.

### Property: BillboardGui.SizeOffset

```json
{
  "type": "Vector2",
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

A 2D offset in size-relative units that acts like an anchor point. This
can be used similarly to the [GuiObject.AnchorPoint](/docs/reference/engine/classes/GuiObject.md) property, but
the values are different.

Size Offset | Explanation
| `0, 0` | The default in which UI will be anchored at its center. |
| --- | --- |
| `0.5, 0.5` | UI will anchor at the bottom left. |
| `0.5, -0.5` | UI will anchor at the top left. |
| `-0.5, 0.5` | UI will anchor at the top right. |
| `-0.5, -0.5` | UI will anchor at the bottom right. |

See also [StudsOffset](/docs/reference/engine/classes/BillboardGui.md),
[StudsOffsetWorldSpace](/docs/reference/engine/classes/BillboardGui.md),
[ExtentsOffset](/docs/reference/engine/classes/BillboardGui.md), and
[ExtentsOffsetWorldSpace](/docs/reference/engine/classes/BillboardGui.md) which
are offset properties that work in 3D space instead.

### Property: BillboardGui.StudsOffset

```json
{
  "type": "Vector3",
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

This property determines how the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) is offset from its
[Adornee](/docs/reference/engine/classes/BillboardGui.md) in studs, relative to the
[Camera](/docs/reference/engine/classes/Camera.md) orientation.

See also [StudsOffsetWorldSpace](/docs/reference/engine/classes/BillboardGui.md)
which works similarly except the offset orientation is relative to the
global axes.

### Property: BillboardGui.StudsOffsetWorldSpace

```json
{
  "type": "Vector3",
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

This property determines how the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) is offset from its
[Adornee](/docs/reference/engine/classes/BillboardGui.md) in studs, relative to the global
axes.

See also [StudsOffset](/docs/reference/engine/classes/BillboardGui.md) which works
similarly except the offset orientation is relative to the [Camera](/docs/reference/engine/classes/Camera.md).

### Property: BillboardGui.DistanceLowerLimit

```json
{
  "type": "float",
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
    "UI"
  ]
}
```

Determines the distance in studs at which the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) will
stop scaling larger in size relative to the player's current camera, with
a default of `0`. If the
[CurrentDistance](/docs/reference/engine/classes/BillboardGui.md) of the
[BillboardGui](/docs/reference/engine/classes/BillboardGui.md) is below this value, it will not scale any larger
than it would at this distance.

### Property: BillboardGui.DistanceUpperLimit

```json
{
  "type": "float",
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
    "UI"
  ]
}
```

Determines the distance in studs at which the [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) will
stop scaling smaller in size relative to the player's current camera. If
the [CurrentDistance](/docs/reference/engine/classes/BillboardGui.md) of the
[BillboardGui](/docs/reference/engine/classes/BillboardGui.md) is above this value, it will not scale any smaller
than it would at this distance.

This property is ignored if the value is less than `0`. The default value
is `-1`, meaning the property is ignored by default.

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