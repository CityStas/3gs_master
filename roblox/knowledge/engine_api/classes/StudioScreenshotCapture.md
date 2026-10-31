---
name: StudioScreenshotCapture
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "Represents a single screenshot captured from Studio, exposing the resulting image buffer and the parameters the capture was taken with."
---

# Class: StudioScreenshotCapture

> Represents a single screenshot captured from Studio, exposing the resulting
> image buffer and the parameters the capture was taken with.

## Description

Studio-only capture result that requires plugin security — not available in
published experiences. Produced by
[CaptureScreenshot()](/docs/reference/engine/classes/StudioCaptureService.md) and
`CapturePluginGui()`. It holds the encoded image data together with the region
and format used for the capture, and reports progress through
[BufferStatus](/docs/reference/engine/classes/StudioScreenshotCapture.md).

The image is populated asynchronously.
[BufferStatus](/docs/reference/engine/classes/StudioScreenshotCapture.md) defaults to
[StudioCaptureBufferStatus.NotStarted](/docs/reference/engine/enums/StudioCaptureBufferStatus.md), becomes
[StudioCaptureBufferStatus.Pending](/docs/reference/engine/enums/StudioCaptureBufferStatus.md) while capturing and encoding,
[StudioCaptureBufferStatus.Ready](/docs/reference/engine/enums/StudioCaptureBufferStatus.md) once the image is available, or
[StudioCaptureBufferStatus.Error](/docs/reference/engine/enums/StudioCaptureBufferStatus.md) if capture failed. Retrieve the image
with [GetBuffer()](/docs/reference/engine/classes/StudioScreenshotCapture.md), read failure
details with [GetErrors()](/docs/reference/engine/classes/StudioScreenshotCapture.md), and
produce a resized copy with
[ScaleAsync()](/docs/reference/engine/classes/StudioScreenshotCapture.md).

## Properties

### Property: StudioScreenshotCapture.BufferFormat

```json
{
  "type": "StudioCaptureScreenshotFormat",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

The [StudioCaptureScreenshotFormat](/docs/reference/engine/enums/StudioCaptureScreenshotFormat.md) the capture's image data is
encoded in, and therefore the format of the buffer returned by
[GetBuffer()](/docs/reference/engine/classes/StudioScreenshotCapture.md). Defaults to
[StudioCaptureScreenshotFormat.RGBA8](/docs/reference/engine/enums/StudioCaptureScreenshotFormat.md), in which the buffer holds four
bytes (red, green, blue, alpha) per pixel; when
[StudioCaptureScreenshotFormat.PNG](/docs/reference/engine/enums/StudioCaptureScreenshotFormat.md), the buffer holds a PNG-encoded
image. This property is read-only and reflects the `Format` requested when
the capture was created.

### Property: StudioScreenshotCapture.BufferStatus

```json
{
  "type": "StudioCaptureBufferStatus",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

The [StudioCaptureBufferStatus](/docs/reference/engine/enums/StudioCaptureBufferStatus.md) describing where the capture is in
its lifecycle. Defaults to [StudioCaptureBufferStatus.NotStarted](/docs/reference/engine/enums/StudioCaptureBufferStatus.md), is
set to [StudioCaptureBufferStatus.Pending](/docs/reference/engine/enums/StudioCaptureBufferStatus.md) while the image is being
captured and encoded, becomes [StudioCaptureBufferStatus.Ready](/docs/reference/engine/enums/StudioCaptureBufferStatus.md) once
the image data is available, and becomes
[StudioCaptureBufferStatus.Error](/docs/reference/engine/enums/StudioCaptureBufferStatus.md) if the capture fails. Only when the
value is [StudioCaptureBufferStatus.Ready](/docs/reference/engine/enums/StudioCaptureBufferStatus.md) does
[GetBuffer()](/docs/reference/engine/classes/StudioScreenshotCapture.md) return image data;
otherwise that method raises an error. This property is read-only.

### Property: StudioScreenshotCapture.OriginalSize

```json
{
  "type": "Vector2",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

The pixel size of the capturable region measured from
[Position](/docs/reference/engine/classes/StudioScreenshotCapture.md) to the bottom-right
corner of the Studio view, computed as the screen resolution minus the
capture position and clamped to be non-negative. It describes the source
area before any cropping or scaling, as distinct from
[Resolution](/docs/reference/engine/classes/StudioScreenshotCapture.md), which is the pixel
size of the encoded image. This property is read-only.

### Property: StudioScreenshotCapture.Position

```json
{
  "type": "Vector2",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

The pixel offset of the top-left corner of the captured region from the
top-left of the Studio view. It reflects the `Position` supplied when the
capture was requested, defaulting to `(0, 0)` when none is given. This
property is read-only.

### Property: StudioScreenshotCapture.Resolution

```json
{
  "type": "Vector2",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

The width and height, in pixels, of the encoded image held by the capture.
It is set once the image has been captured and encoded (when
[BufferStatus](/docs/reference/engine/classes/StudioScreenshotCapture.md) becomes
[StudioCaptureBufferStatus.Ready](/docs/reference/engine/enums/StudioCaptureBufferStatus.md)), and for a capture produced by
[ScaleAsync()](/docs/reference/engine/classes/StudioScreenshotCapture.md) it equals the
requested output size. This property is read-only.

### Property: StudioScreenshotCapture.UICaptureMode

```json
{
  "type": "UICaptureMode",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

The [UICaptureMode](/docs/reference/engine/enums/UICaptureMode.md) that determines which user interface is
composited into the captured image. Defaults to [UICaptureMode.All](/docs/reference/engine/enums/UICaptureMode.md),
meaning all UI is included, and reflects the `UICaptureMode` requested
when the capture was created. This property is read-only.

## Methods

### Method: StudioScreenshotCapture:GetBuffer

**Signature:** `StudioScreenshotCapture:GetBuffer(): buffer`

Returns the captured screenshot as a `buffer` encoded in the capture's
[BufferFormat](/docs/reference/engine/classes/StudioScreenshotCapture.md). This method
only succeeds when
[BufferStatus](/docs/reference/engine/classes/StudioScreenshotCapture.md) is
[StudioCaptureBufferStatus.Ready](/docs/reference/engine/enums/StudioCaptureBufferStatus.md); if the image is not yet available
or the capture failed, it raises an error instead of returning a buffer.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `buffer` — A buffer containing the captured image data in the capture's
[BufferFormat](/docs/reference/engine/classes/StudioScreenshotCapture.md).

### Method: StudioScreenshotCapture:GetErrors

**Signature:** `StudioScreenshotCapture:GetErrors(): Array`

Returns an array of the error messages recorded for this capture. The
array is empty when no errors have occurred; when
[BufferStatus](/docs/reference/engine/classes/StudioScreenshotCapture.md) is
[StudioCaptureBufferStatus.Error](/docs/reference/engine/enums/StudioCaptureBufferStatus.md), it contains one or more messages
describing why the capture or scale failed.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `Array` — An array of strings describing any errors that occurred during the
capture.

### Method: StudioScreenshotCapture:ScaleAsync

**Signature:** `StudioScreenshotCapture:ScaleAsync(strategy: ResamplerMode, newSize: Vector2): StudioScreenshotCapture`

Returns a new [StudioScreenshotCapture](/docs/reference/engine/classes/StudioScreenshotCapture.md) whose image is computed from
this capture, resized to `newSize` using the given [ResamplerMode](/docs/reference/engine/enums/ResamplerMode.md).
The original capture is not modified. [ResamplerMode.Default](/docs/reference/engine/enums/ResamplerMode.md)
resamples with bilinear filtering, while [ResamplerMode.Pixelated](/docs/reference/engine/enums/ResamplerMode.md)
uses nearest-neighbor (point) sampling; the scaled capture inherits this
capture's [Position](/docs/reference/engine/classes/StudioScreenshotCapture.md),
[OriginalSize](/docs/reference/engine/classes/StudioScreenshotCapture.md),
[BufferFormat](/docs/reference/engine/classes/StudioScreenshotCapture.md), and
[UICaptureMode](/docs/reference/engine/classes/StudioScreenshotCapture.md).

This method yields until the scaled image has been encoded. It errors if
`newSize` is not positive, or if this capture's
[BufferStatus](/docs/reference/engine/classes/StudioScreenshotCapture.md) is not
[StudioCaptureBufferStatus.Ready](/docs/reference/engine/enums/StudioCaptureBufferStatus.md).

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `strategy` | `ResamplerMode` |  | The [ResamplerMode](/docs/reference/engine/enums/ResamplerMode.md) used to resample the image. [ResamplerMode.Default](/docs/reference/engine/enums/ResamplerMode.md) applies bilinear filtering; [ResamplerMode.Pixelated](/docs/reference/engine/enums/ResamplerMode.md) applies nearest-neighbor (point) sampling. |
| `newSize` | `Vector2` |  | The width and height, in pixels, of the scaled image. |

**Returns:** `StudioScreenshotCapture` — A new [StudioScreenshotCapture](/docs/reference/engine/classes/StudioScreenshotCapture.md) whose image is this capture
scaled to `newSize`.

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