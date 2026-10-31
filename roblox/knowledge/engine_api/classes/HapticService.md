---
name: HapticService
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
summary: "Provides haptic feedback to controllers and devices."
---

# Class: HapticService

> Provides haptic feedback to controllers and devices.

## Description

`HapticService` allows scripts to query vibration support and set motor
intensities on gamepad controllers, VR controllers, and mobile devices. Use
[IsVibrationSupported()](/docs/reference/engine/classes/HapticService.md) and
[IsMotorSupported()](/docs/reference/engine/classes/HapticService.md) to check device
capabilities, then [SetMotor()](/docs/reference/engine/classes/HapticService.md) to drive a
specific [VibrationMotor](/docs/reference/engine/enums/VibrationMotor.md) on a given [UserInputType](/docs/reference/engine/enums/UserInputType.md). Motor output
is scaled by the user's haptic intensity preference in their Roblox settings.

As this service is client-side only, it can only be used in a
[LocalScript](/docs/reference/engine/classes/LocalScript.md), a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) required by a [LocalScript](/docs/reference/engine/classes/LocalScript.md),
or a [Script](/docs/reference/engine/classes/Script.md) with [RunContext](/docs/reference/engine/classes/BaseScript.md) set to
[RunContext.Client](/docs/reference/engine/enums/RunContext.md).

This service has been superseded by [HapticEffect](/docs/reference/engine/classes/HapticEffect.md), which supports
waveform-based effects, looping, spatial attenuation, and preset effect types.
For new work, use [HapticEffect](/docs/reference/engine/classes/HapticEffect.md) instead.

## Methods

### Method: HapticService:GetMotor

**Signature:** `HapticService:GetMotor(inputType: UserInputType, vibrationMotor: VibrationMotor): Tuple`

Returns the current vibration value set to the specified
[UserInputType](/docs/reference/engine/classes/InputObject.md) and [VibrationMotor](/docs/reference/engine/enums/VibrationMotor.md).
This will not return anything if
[SetMotor()](/docs/reference/engine/classes/HapticService.md) has not been called prior.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `inputType` | `UserInputType` |  | The specified [UserInputType](/docs/reference/engine/enums/UserInputType.md). |
| `vibrationMotor` | `VibrationMotor` |  | The specified [VibrationMotor](/docs/reference/engine/enums/VibrationMotor.md). |

**Returns:** `Tuple` — The current vibration value set to the specified [UserInputType](/docs/reference/engine/enums/UserInputType.md)
and [VibrationMotor](/docs/reference/engine/enums/VibrationMotor.md) or `nil` if
[SetMotor()](/docs/reference/engine/classes/HapticService.md) has not been called prior.

### Method: HapticService:IsMotorSupported

**Signature:** `HapticService:IsMotorSupported(inputType: UserInputType, vibrationMotor: VibrationMotor): boolean`

Returns `true` if the specified motor is available to be used with the
specified [UserInputType](/docs/reference/engine/enums/UserInputType.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `inputType` | `UserInputType` |  | The specific [UserInputType](/docs/reference/engine/enums/UserInputType.md) being checked for [VibrationMotor](/docs/reference/engine/enums/VibrationMotor.md) support. |
| `vibrationMotor` | `VibrationMotor` |  | The specified [VibrationMotor](/docs/reference/engine/enums/VibrationMotor.md) checked to see if it supports the specified [UserInputType](/docs/reference/engine/enums/UserInputType.md). |

**Returns:** `boolean` — Boolean of `true` if the specified motor is available to be used with
the specified [UserInputType](/docs/reference/engine/enums/UserInputType.md), `false` if not.

### Method: HapticService:IsVibrationSupported

**Signature:** `HapticService:IsVibrationSupported(inputType: UserInputType): boolean`

Returns `true` if the specified [UserInputType](/docs/reference/engine/enums/UserInputType.md) supports haptic
feedback.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `inputType` | `UserInputType` |  | The specified [UserInputType](/docs/reference/engine/enums/UserInputType.md) checked to see if it supports haptic feedback. |

**Returns:** `boolean` — Boolean of `true` if the specified [UserInputType](/docs/reference/engine/enums/UserInputType.md) supports
haptic feedback.

### Method: HapticService:SetMotor

**Signature:** `HapticService:SetMotor(inputType: UserInputType, vibrationMotor: VibrationMotor, vibrationValues: Tuple): ()`

Sets the vibration intensity of the specified `inputType` and
`vibrationMotor`. Note that almost all usage cases specify
[UserInputType.Gamepad1](/docs/reference/engine/enums/UserInputType.md) for `inputType` which is internally mapped
to the device's respective hardware.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `inputType` | `UserInputType` |  | The specified [UserInputType](/docs/reference/engine/enums/UserInputType.md). |
| `vibrationMotor` | `VibrationMotor` |  | The specified [VibrationMotor](/docs/reference/engine/enums/VibrationMotor.md). |
| `vibrationValues` | `Tuple` |  | How intensely the motor should vibrate. Only uses the first value in the tuple, which should be a number. |

**Returns:** `()`

**HapticService:SetMotor()**

This example makes the small motor vibrate depending on how much pressure is
applied to the left trigger, and the large motor vibrate depending on how much
pressure is applied to the right trigger.

```lua
local UserInputService = game:GetService("UserInputService")
local HapticService = game:GetService("HapticService")

local cachedInputs = {}

local keyToVibration = {
	[Enum.KeyCode.ButtonL2] = Enum.VibrationMotor.Small,
	[Enum.KeyCode.ButtonR2] = Enum.VibrationMotor.Large,
}

local function onInputChanged(property)
	if property == "Position" then
		HapticService:SetMotor(inputType, vibrationMotor, input.Position.Z)
	end
end

local function onInputBegan(input)
	if not cachedInputs[input] then
		local inputType = input.UserInputType
		if inputType.Name:find("Gamepad") then
			local vibrationMotor = keyToVibration[input.KeyCode]
			if vibrationMotor then
				-- Watch this input manually to accurately update the vibration motor
				cachedInputs[input] = input.Changed:Connect(onInputChanged)
			end
		end
	end
end

UserInputService.InputBegan:Connect(onInputBegan)
```

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