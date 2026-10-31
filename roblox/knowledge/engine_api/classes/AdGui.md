---
name: AdGui
last_updated: 2026-10-30T19:55:51Z
inherits:
  - SurfaceGuiBase
  - LayerCollector
  - GuiBase2d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Internal
summary: "A surface-based GUI that displays immersive ads on a face of a Part in the 3D world."
---

# Class: AdGui

> A surface-based GUI that displays immersive ads on a face of a [Part](/docs/reference/engine/classes/Part.md) in
> the 3D world.

## Description

[AdGui](/docs/reference/engine/classes/AdGui.md) is a [SurfaceGuiBase](/docs/reference/engine/classes/SurfaceGuiBase.md) that renders immersive display ads
onto a face of the [Part](/docs/reference/engine/classes/Part.md) it's adorned to. When no ad is available, it
shows the creator-supplied [AdGui.FallbackImage](/docs/reference/engine/classes/AdGui.md), or a default Roblox
fallback image when that property is empty.

To render ads, the [AdGui](/docs/reference/engine/classes/AdGui.md) must be adorned to a block [Part](/docs/reference/engine/classes/Part.md)
that's a descendant of [Workspace](/docs/reference/engine/classes/Workspace.md), must be the only surface GUI on that
face, and must be at least the minimum eligible size. When these conditions
aren't met, the object displays a placeholder image in Studio's edit view and
renders nothing in a running experience.

## Properties

### Property: AdGui.AdShape

```json
{
  "type": "AdShape",
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

Determines the shape of the ad rendered by the [AdGui](/docs/reference/engine/classes/AdGui.md), including
the creative's aspect ratio on the part surface. Defaults to
[HorizontalRectangle](/docs/reference/engine/enums/AdShape.md), which is the only served shape aside
from the sentinel [Undefined](/docs/reference/engine/enums/AdShape.md).

### Property: AdGui.EnableVideoAds

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
    "UI",
    "Monetization"
  ]
}
```

The property enables the AdGui to serve video ads.

### Property: AdGui.FallbackImage

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

A creator-supplied image that the [AdGui](/docs/reference/engine/classes/AdGui.md) displays when it has no
served ad to render. Defaults to an empty content string; while empty, the
[AdGui](/docs/reference/engine/classes/AdGui.md) renders a default Roblox fallback image instead.

### Property: AdGui.FallbackImageContent

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

A [Content](/docs/reference/engine/datatypes/Content.md)-typed property that holds the fallback image the
[AdGui](/docs/reference/engine/classes/AdGui.md) displays when no served ad is available. It is the
content-typed backing for [AdGui.FallbackImage](/docs/reference/engine/classes/AdGui.md) (a legacy
`TextureId` string); writing to either property updates the same
underlying storage. Unlike `FallbackImage`, this property accepts
[asset URIs](/docs/en-us/projects/assets.md#asset-uris) and references
to [EditableImage](/docs/reference/engine/classes/EditableImage.md) objects. When empty, the [AdGui](/docs/reference/engine/classes/AdGui.md) renders a
default Roblox fallback image instead.

### Property: AdGui.Status

```json
{
  "type": "AdUnitStatus",
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
  "category": "Behavior",
  "capabilities": [
    "UI",
    "Monetization"
  ]
}
```

A read-only property that reports whether the [AdGui](/docs/reference/engine/classes/AdGui.md) is actively
displaying a served ad. It's [Active](/docs/reference/engine/enums/AdUnitStatus.md) when the
[AdGui](/docs/reference/engine/classes/AdGui.md) is rendering ad content, and [Inactive](/docs/reference/engine/enums/AdUnitStatus.md)
otherwise.

## Callbacks

### Callback: AdGui.OnAdEvent

**Signature:** `AdGui.OnAdEvent(eventInfo: Dictionary): boolean`

> **Deprecated:** This callback has been deprecated and will never be called.

Used to react to the AdGui events.

*Security: None · Thread Safety: Unsafe · Capabilities: UI, Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `eventInfo` | `Dictionary` |  | Options table for the method:  - `PlayerId` – The user ID of the player related to the ad event. - `AdEventType` – A [AdEventType](/docs/reference/engine/enums/AdEventType.md) enum value describing the AdGui   events. |

**Returns:** `boolean` — Whether the callback has successfully reacted to the event.

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