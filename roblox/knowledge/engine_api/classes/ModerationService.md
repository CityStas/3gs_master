---
name: ModerationService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "Server-side service for submitting player captures to content moderation review and receiving the results asynchronously."
---

# Class: ModerationService

> Server-side service for submitting player captures to content moderation
> review and receiving the results asynchronously.

## Description

`ModerationService` lets server-side experience code submit user-generated
captures (screenshots taken with [CaptureService:CaptureScreenshot()](/docs/reference/engine/classes/CaptureService.md)
and videos recorded with [CaptureService:StartVideoCaptureAsync()](/docs/reference/engine/classes/CaptureService.md)) to
Roblox's content moderation pipeline and receive the review results
asynchronously.

## Methods

### Method: ModerationService:BindReviewableContentEventProcessor

**Signature:** `ModerationService:BindReviewableContentEventProcessor(priority: int, callback: Function): RBXScriptConnection`

Binds a callback that the server invokes for each moderation review event
produced for content registered through
[CreateReviewableContentAsync()](/docs/reference/engine/classes/ModerationService.md).

Once at least one processor is bound, review events are delivered to the
bound processors in `priority` order. The `callback` function receives a
single table with the following fields:

- `Id` — The reviewable-content ID the event refers to.
- `State` — The review state (`ReviewableContentState`).
- `Ref` — The optional caller-supplied reference string passed to
  [CreateReviewableContentAsync()](/docs/reference/engine/classes/ModerationService.md),
  present only when one was supplied.
- `ModerationResult` — Present when a moderation result is available, a
  table with a `Category` (`ModerationResultCategory`) and, when a
  violation is detected, a `Labels` array of `ModerationResultLabel`
  values.

Processors run as a chain: if a processor returns `true`, the event is
acknowledged, deleted from the backend, and removed from the pending set,
and no further processors run for that event. If it returns `false` (or
does not return a boolean), the next processor runs; if no processor
returns `true`, the event is left unacknowledged and redelivered on a
later poll.

*Security: None · Thread Safety: Unsafe · Capabilities: Consequences*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `priority` | `int` |  | Determines the order in which this processor is invoked relative to other bound processors. |
| `callback` | `Function` |  | The function invoked for each reviewable-content event. It receives a table describing the event and should return `true` to acknowledge the event or `false` to leave it for redelivery. |

**Returns:** `RBXScriptConnection` — A connection that can be disconnected to unregister the processor.

### Method: ModerationService:CreateReviewableContentAsync

**Signature:** `ModerationService:CreateReviewableContentAsync(config: Dictionary): string`

Registers one or more captures as a single unit of reviewable content and
starts its moderation review. This is a yielding function that must be
called on the server and is restricted to allow-listed universes; calling
it from a universe that is not permitted to use this API raises an error.

The `config` table accepts:

- `Id` — An optional caller-chosen ID for the reviewable content.
  Supplying an ID that already exists raises an error.
- `Ref` — An optional reference string echoed back on the events delivered
  to processors bound with
  [BindReviewableContentEventProcessor()](/docs/reference/engine/classes/ModerationService.md).
- `Content` — A list of items (currently limited to one), each containing
  either an `Image` or a `Video` table with a `UserId` (the owning player)
  and a `ContentKey` obtained from
  [CreateReviewableContentKey()](/docs/reference/engine/classes/ModerationService.md).

The method registers the content with the backend and returns the
reviewable content ID. Review results are later delivered to bound
processors as the moderation review completes.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Consequences*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `config` | `Dictionary` |  | A table of parameters describing the content to review, including an optional `Id`, an optional `Ref`, and a `Content` list of image or video items. |

**Returns:** `string` — The ID of the created reviewable content.

### Method: ModerationService:CreateReviewableContentKey

**Signature:** `ModerationService:CreateReviewableContentKey(content: Content): string`

Produces an opaque key that describes a single capture so it can be
submitted to
[CreateReviewableContentAsync()](/docs/reference/engine/classes/ModerationService.md).

The `content` must reference a supported capture (a temporary content URI
produced by [CaptureService:CaptureScreenshot()](/docs/reference/engine/classes/CaptureService.md), a
[ScreenshotCapture](/docs/reference/engine/classes/ScreenshotCapture.md) object, or a [VideoCapture](/docs/reference/engine/classes/VideoCapture.md) object). Any
other content raises an error.

*Security: None · Thread Safety: Unsafe · Capabilities: Consequences*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `content` | `Content` |  | A [Content](/docs/reference/engine/datatypes/Content.md) referring to a screenshot or video capture (a temporary URI from [CaptureService:CaptureScreenshot()](/docs/reference/engine/classes/CaptureService.md), a [ScreenshotCapture](/docs/reference/engine/classes/ScreenshotCapture.md), or a [VideoCapture](/docs/reference/engine/classes/VideoCapture.md)). |

**Returns:** `string` — An opaque content key identifying the capture.

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