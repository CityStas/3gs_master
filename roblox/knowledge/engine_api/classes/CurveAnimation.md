---
name: CurveAnimation
last_updated: 2026-10-30T19:55:52Z
inherits:
  - AnimationClip
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Stores animation data in the form of curves for each individual channel to animate."
---

# Class: CurveAnimation

> Stores animation data in the form of curves for each individual channel to
> animate.

## Description

`CurveAnimation` is a subtype of [AnimationClip](/docs/reference/engine/classes/AnimationClip.md) consumed by Roblox's
animation system. It stores animation data for each animated channel in a rig
as a separate, individual curve. For example, `CurveAnimation` stores the
position channel for an articulated joint as a [Vector3Curve](/docs/reference/engine/classes/Vector3Curve.md), and it
might store the rotation channel as a [EulerRotationCurve](/docs/reference/engine/classes/EulerRotationCurve.md) or
[RotationCurve](/docs/reference/engine/classes/RotationCurve.md).

#### Structure

`CurveAnimation` stores curves in a hierarchical manner, matching the
hierarchy of the structure of [Motor6Ds](/docs/reference/engine/classes/Motor6D.md) or [Bones](/docs/reference/engine/classes/Bone.md)
in the animated model. Under each `CurveAnimation` instance lies a hierarchy
of [Folder](/docs/reference/engine/classes/Folder.md) instances representing animated joints in the model. Under
each such folder instance, several possible instances may exist. An instance
named `Position` of type [Vector3Curve](/docs/reference/engine/classes/Vector3Curve.md) can drive the local translation
of the [Motor6D](/docs/reference/engine/classes/Motor6D.md) or [Bone](/docs/reference/engine/classes/Bone.md) on the animated model, while an
instance named `Rotation` of type [EulerRotationCurve](/docs/reference/engine/classes/EulerRotationCurve.md) or
[RotationCurve](/docs/reference/engine/classes/RotationCurve.md) can drive the local rotation of the [Motor6D](/docs/reference/engine/classes/Motor6D.md) or
[Bone](/docs/reference/engine/classes/Bone.md) on the animated model.

#### Partial matching of hierarchy

You can match partial hierarchies to a model when playing a `CurveAnimation`
in Roblox's animation system. This means that not all joints need to be
present in the hierarchy for the existing joints to apply properly.
Furthermore, you can match hierarchies in a "relative" manner. For example,
the first child [Folder](/docs/reference/engine/classes/Folder.md) instance root can be `UpperTorso` and the
animation system matches that to any existing sub-hierarchies in the model.

#### Animating miscellaneous channels

`CurveAnimation` can also animate other numerical values in a model. For
example, you can animate FACS controls for facial animations by creating a
[Folder](/docs/reference/engine/classes/Folder.md) under the `CurveAnimation` instance named after an existing
[FaceControls](/docs/reference/engine/classes/FaceControls.md) instance in the model. Then, to animate individual facial
controllers, you can store individual [FloatCurve](/docs/reference/engine/classes/FloatCurve.md) instances named after
the animated [FaceControls](/docs/reference/engine/classes/FaceControls.md) property.

#### Usage when making animations

As with other [AnimationClip](/docs/reference/engine/classes/AnimationClip.md) types such as [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md),
you must first upload `CurveAnimation` instances to Roblox before playing
them. If you want to preview an animation before uploading it to Roblox, you
can generate a temporary ID using
[AnimationClipProvider:RegisterAnimationClip()](/docs/reference/engine/classes/AnimationClipProvider.md); this generates a hash
ID that you can use for localized animation testing.

If you want to download the `CurveAnimation` corresponding to an existing
uploaded animation using Luau scripts, use
[AnimationClipProvider:GetAnimationClipAsync()](/docs/reference/engine/classes/AnimationClipProvider.md).

## Inherited Members

### From [AnimationClip](/docs/reference/engine/classes/AnimationClip.md)

- **Property `Length`** (`float`): The length in seconds of this clip. Returns `0` until the animation has
- **Property `Loop`** (`boolean`): Determines whether the animation stored in this AnimationClip is
- **Property `Priority`** (`AnimationPriority`): Determines which clip takes priority when multiple animations are playing

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