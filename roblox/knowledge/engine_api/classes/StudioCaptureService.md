---
name: StudioCaptureService
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "A Studio-only service that lets plugins capture screenshots of the active place's 3D viewport."
---

# Class: StudioCaptureService

> A Studio-only service that lets plugins capture screenshots of the active
> place's 3D viewport.

## Description

`StudioCaptureService` is a Studio-only service that lets plugins capture
screenshots of the active place's 3D viewport. Use
[RequestScreenshotPermissionAsync()](/docs/reference/engine/classes/StudioCaptureService.md)
to obtain the user's permission,
[CanCaptureScreenshot()](/docs/reference/engine/classes/StudioCaptureService.md) to
check whether a capture is currently possible, and
[CaptureScreenshot()](/docs/reference/engine/classes/StudioCaptureService.md) to
request an image of the current view. All members require plugin security and
are only available within Studio.

## Methods

### Method: StudioCaptureService:CanCaptureScreenshot

**Signature:** `StudioCaptureService:CanCaptureScreenshot(): boolean`

Returns `false` when there is a known reason a screenshot cannot be
captured — for example, when this is not the active [DataModel](/docs/reference/engine/classes/DataModel.md) or
the plugin does not have permission — and `true` otherwise. A return value
of `true` does not guarantee that
[CaptureScreenshot()](/docs/reference/engine/classes/StudioCaptureService.md) will
succeed, because conditions can change between the two calls.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `boolean` — A boolean that is `false` when a screenshot is known to be
uncapturable, or `true` otherwise.

### Method: StudioCaptureService:CaptureScreenshot

**Signature:** `StudioCaptureService:CaptureScreenshot(screenshotOptions: Dictionary): StudioScreenshotCapture`

Captures a screenshot of the active [DataModel](/docs/reference/engine/classes/DataModel.md) according to
`screenshotOptions` and returns a [StudioScreenshotCapture](/docs/reference/engine/classes/StudioScreenshotCapture.md) in the
requested format. If an image of the requested size cannot be captured at
the requested position, the capture fails rather than clipping the image.

The `screenshotOptions` dictionary accepts the following keys:

- `Position` — a [Vector2](/docs/reference/engine/datatypes/Vector2.md) top-left offset of the captured
  region. Must be non-negative and defaults to `(0, 0)`.
- `CaptureSize` — a [Vector2](/docs/reference/engine/datatypes/Vector2.md) size of the region to capture. Both
  components must be positive.
- `OutputSize` — a [Vector2](/docs/reference/engine/datatypes/Vector2.md) size of the returned image. Both
  components must be positive; when it differs from `CaptureSize`,
  `ResampleMode` must also be provided.
- `ResampleMode` — the resampling filter used when `OutputSize` differs
  from `CaptureSize`.
- `Format` — an [StudioCaptureScreenshotFormat](/docs/reference/engine/enums/StudioCaptureScreenshotFormat.md) for the returned
  buffer. Defaults to [StudioCaptureScreenshotFormat.RGBA8](/docs/reference/engine/enums/StudioCaptureScreenshotFormat.md).
- `UICaptureMode` — an [UICaptureMode](/docs/reference/engine/enums/UICaptureMode.md) controlling whether UI is
  included in the capture. Defaults to [UICaptureMode.All](/docs/reference/engine/enums/UICaptureMode.md).

The returned [StudioScreenshotCapture](/docs/reference/engine/classes/StudioScreenshotCapture.md) is populated asynchronously:
its image buffer becomes available only after the capture and encoding
complete, and any errors are reported on the capture object.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `screenshotOptions` | `Dictionary` |  | A dictionary of options controlling the capture, such as `Position`, `CaptureSize`, `OutputSize`, `ResampleMode`, `Format`, and `UICaptureMode`. |

**Returns:** `StudioScreenshotCapture` — A [StudioScreenshotCapture](/docs/reference/engine/classes/StudioScreenshotCapture.md) that holds the requested image in
the requested format.

### Method: StudioCaptureService:RequestScreenshotPermissionAsync

**Signature:** `StudioCaptureService:RequestScreenshotPermissionAsync(): boolean`

This yielding function asks the user to grant the plugin permission to
capture screenshots from their Studio 3D view, returning `true` if
permission is granted and `false` otherwise. It can return immediately
without prompting when the plugin's permission is already known from an
earlier session, and it returns `false` without prompting when the global
screenshot setting is disabled.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `boolean` — A boolean that is `true` if the user granted permission and `false`
otherwise.

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