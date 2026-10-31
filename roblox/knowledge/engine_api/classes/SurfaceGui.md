---
name: SurfaceGui
last_updated: 2026-10-30T19:55:53Z
inherits:
  - SurfaceGuiBase
  - LayerCollector
  - GuiBase2d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Container for GuiObjects that are rendered on the surface of a part."
---

# Class: SurfaceGui

> Container for GuiObjects that are rendered on the surface of a part.

## Description

[SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) allows for the rendering of UI objects onto a part's
surface in the 3D world while also allowing for basic user interaction to
occur. Similar to [Decals](/docs/reference/engine/classes/Decal.md) and [Textures](/docs/reference/engine/classes/Texture.md), UI
objects such as [TextLabels](/docs/reference/engine/classes/TextLabel.md) and
[ImageLabels](/docs/reference/engine/classes/ImageLabel.md) parented to a [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) face the same
direction as the surface they're on, editable through the
[Face](/docs/reference/engine/classes/SurfaceGui.md) property.

![SurfaceGui on a 3D part in the place with an ImageLabel child to depict a screen console.](/assets/ui/in-experience/SurfaceGui-Diagram.jpg)

Note that interactive UI elements like [ImageButtons](/docs/reference/engine/classes/ImageButton.md) and
[TextButtons](/docs/reference/engine/classes/TextButton.md) inside a [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) will only receive
user input if they are parented to the [PlayerGui](/docs/reference/engine/classes/PlayerGui.md), typically via
placing the [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) inside [StarterGui](/docs/reference/engine/classes/StarterGui.md) (the
[Adornee](/docs/reference/engine/classes/SurfaceGui.md) property can be used to target a part in
the 3D world while the [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) itself remains in the
[PlayerGui](/docs/reference/engine/classes/PlayerGui.md)). Additionally, the part's
[CanQuery](/docs/reference/engine/classes/BasePart.md) property must be `true` for the interactive
UI element to receive input.

See [In-Experience UI](/docs/en-us/ui/in-experience-containers.md#surface-ui) for
a guide on working with [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) containers.

##### Caching Behavior

To help improve performance, the appearance of a [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) is cached
until one of the following occurs, after which its appearance will be
recomputed on the next rendering frame.

- A descendant is added to or removed from the [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md).
- A property of a descendant of the [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) changes.
- A property of the [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) itself changes.

## Properties

### Property: SurfaceGui.AlwaysOnTop

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

This property determines whether the [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) will always render
on top of other 3D objects.

When set to `false` (default), the [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) renders like other
3D content and is occluded by other 3D objects. When set to `true`, the
[SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) always renders on top of 3D content and the appearance
changes significantly:

- Colors match how they appear inside a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md).
- Text may appear sharper on high DPI devices.
- [LightInfluence](/docs/reference/engine/classes/SurfaceGui.md) is treated as though
  it's `0`.
- [Brightness](/docs/reference/engine/classes/SurfaceGui.md) has no effect.

### Property: SurfaceGui.Brightness

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

This property determines the factor by which the [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md)
container's light is scaled when
[LightInfluence](/docs/reference/engine/classes/SurfaceGui.md) is `0`. By default, this
property is `1` and can be set to any number between `0` and `1000`. By
modifying this property, the apparent brightness of a [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md)
can be better matched to its environment. For instance, a video billboard
can be brightened inside a dark room by increasing
[Brightness](/docs/reference/engine/classes/SurfaceGui.md) to `10`.

Note that [Brightness](/docs/reference/engine/classes/SurfaceGui.md) is inaccessible in
Studio and has no effect when either
[LightInfluence](/docs/reference/engine/classes/SurfaceGui.md) is `1` or
[AlwaysOnTop](/docs/reference/engine/classes/SurfaceGui.md) is `true`.

### Property: SurfaceGui.CanvasSize

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
  "category": "Sizing",
  "capabilities": [
    "UI"
  ]
}
```

The size of a "virtual screen" in "virtual pixels" which makes
[SurfaceGuis](/docs/reference/engine/classes/SurfaceGui.md) pixel-to-pixel compatible with
[ScreenGuis](/docs/reference/engine/classes/ScreenGui.md).

### Property: SurfaceGui.ClipsDescendants

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
that fall outside of the [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) canvas borders will not be
drawn.

Even when this property is `false`, [GuiObjects](/docs/reference/engine/classes/GuiObject.md) that are
**completely** outside of the canvas will not render.

### Property: SurfaceGui.LightInfluence

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

Controls how much the [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) is influenced by environmental
lighting, in a range from `0` to `1`. Setting this to `1` means that
surrounding lighting has complete control over the appearance, while
setting it to `0` means that the lighting has no effect.

### Property: SurfaceGui.MaxDistance

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

This property controls how far from the camera the [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) will
be displayed before it stops rendering. A value of `0` means there is no
limit and it will render infinitely far away. The default value of `1000`
works fine for most cases.

For [SurfaceGuis](/docs/reference/engine/classes/SurfaceGui.md) that appear outdoors, it's recommended
that [MaxDistance](/docs/reference/engine/classes/SurfaceGui.md) is high enough to ensure
that the container's UI is sufficiently small on the screen when it
appears or disappears, minimizing the sudden pop‑in/out effect.

### Property: SurfaceGui.PixelsPerStud

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
  "category": "Sizing",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the density of pixels used for each world-space
stud to render the contents of the [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md). Higher values will
cause the various [GuiObjects](/docs/reference/engine/classes/GuiObject.md) within to appear smaller if
they are kept the same size. Conversely, lower values will cause objects
to appear larger. However, if the [GuiObjects](/docs/reference/engine/classes/GuiObject.md) are scaled
proportionally through use of [UIScale](/docs/reference/engine/classes/UIScale.md), [GuiObject.Size](/docs/reference/engine/classes/GuiObject.md),
[TextLabel.TextSize](/docs/reference/engine/classes/TextLabel.md), or similar, this property allows for higher
definition to be used.

It's important to select a value based on how far away you expect a player
to view the [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md). Also be mindful that a large pixel density
could negatively affect performance if the face of the adorned part is
large enough.

### Property: SurfaceGui.SizingMode

```json
{
  "type": "SurfaceGuiSizingMode",
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
  "category": "Sizing",
  "capabilities": [
    "UI"
  ]
}
```

When set to [SurfaceGuiSizingMode.PixelsPerStud](/docs/reference/engine/enums/SurfaceGuiSizingMode.md) (default), the
[SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) renders with a variable size based on
[PixelsPerStud](/docs/reference/engine/classes/SurfaceGui.md) and the surface's size in
studs.

When set to [SurfaceGuiSizingMode.FixedSize](/docs/reference/engine/enums/SurfaceGuiSizingMode.md), the [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md)
renders with a fixed size set through
[CanvasSize](/docs/reference/engine/classes/SurfaceGui.md).

### Property: SurfaceGui.ToolPunchThroughDistance

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

Sets the distance in which left clicking starts acting on the
[SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) instead of for the held [Tool](/docs/reference/engine/classes/Tool.md). If a character is
within this distance of the [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md), the [Tool](/docs/reference/engine/classes/Tool.md) will not
activate on click.

### Property: SurfaceGui.ZOffset

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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

Layers this [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) in relation to others on the same face
(changing this does not visually "lift" or "sink" a [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md)
from the surface).

## Inherited Members

### From [SurfaceGuiBase](/docs/reference/engine/classes/SurfaceGuiBase.md)

- **Property `Active`** (`boolean`): Determines whether the SurfaceGui sinks user input; `true` by
- **Property `Adornee`** (`Instance`): BasePart on which to apply the SurfaceGui, overriding the
- **Property `Face`** (`NormalId`): NormalId face upon which to apply the SurfaceGui.

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