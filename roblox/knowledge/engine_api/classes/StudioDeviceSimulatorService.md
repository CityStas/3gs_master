---
name: StudioDeviceSimulatorService
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
summary: "Service allowing you to control Studio's Device Simulator."
---

# Class: StudioDeviceSimulatorService

> Service allowing you to control Studio's Device Simulator.

## Description

Provides programmatic control over Studio's Device Simulator. Use this service
to switch between device presets, override resolution and pixel density,
control orientation and scaling, and manage custom device profiles from a
plugin or from an external tool connected through the MCP server.

All methods are asynchronous and yield the calling coroutine. The service is
available in **Edit mode** and **Play Client**. Methods that modify the active
simulation state are blocked in **PlayServer** mode.

##### Limitations

- All methods are asynchronous and yield the calling coroutine.
- Methods that modify the active simulation state (`SetDeviceAsync`,
  `StopSimulationAsync`, `SetOrientationAsync`, `SetResolutionAsync`,
  `SetPixelDensityAsync`, `SetScalingModeAsync`) error in PlayServer mode.
  They work in Edit mode and Play Client.
- `UpdateDeviceAsync` and `RemoveDeviceAsync` error when called on built-in
  presets.
- Resolution, DPI, and scaling mode methods require an active device and error
  when `GetDeviceAsync()` returns "default".
- Resolution and DPI overrides are session-level. They are not persisted and
  are cleared on `SetDeviceAsync`.
- Built-in presets are immutable.

## Methods

### Method: StudioDeviceSimulatorService:CreateDeviceAsync

**Signature:** `StudioDeviceSimulatorService:CreateDeviceAsync(config: Dictionary): string`

Creates a custom device and returns its newly assigned ID. Custom devices
are persisted to disk and appear in the Device Simulator UI.

Errors if any required field is missing or out of range.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `config` | `Dictionary` |  | A dictionary describing the new device. Required fields: `Name` (string, 1-200 characters, cannot be `"default"`), `Width` (int, 1-7680 pixels), `Height` (int, 1-4320 pixels), `PixelDensity` (int, 72-10000 DPI). Optional fields: `DeviceForm` ([DeviceForm](/docs/reference/engine/enums/DeviceForm.md), default Phone), `ResolutionScale` (float, default 1.0, max 10.0), `PortraitKeyboardHeight` (int, default 0), `LandscapeKeyboardHeight` (int, default 0). |

**Returns:** `string` — string

**Create Device example**

Example of CreateDeviceAsync method

```lua
local id = Simulator:CreateDeviceAsync({
    Name = "My Custom Tablet",
    Width = 2560,
    Height = 1600,
    PixelDensity = 300,
    DeviceForm = Enum.DeviceForm.Tablet,
})
```

### Method: StudioDeviceSimulatorService:GetDeviceAsync

**Signature:** `StudioDeviceSimulatorService:GetDeviceAsync(): string`

Returns the ID of the currently active device, or `"default"` if no device
is active.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `string` — string

### Method: StudioDeviceSimulatorService:GetDeviceInfoAsync

**Signature:** `StudioDeviceSimulatorService:GetDeviceInfoAsync(deviceId: string): Dictionary`

Returns a `DeviceConfiguration` for the specified device without
activating it. Useful for inspecting presets before choosing one to switch
to.

The returned dictionary contains the following fields:

| Field | Type | Create/Update | Description |
| --- | --- | --- | --- |
| `DeviceId` | string | Read-only | Unique identifier assigned by the service. |
| `Name` | string | Required | Display name. 1 to 200 characters. Cannot be `"default"`. |
| `Width` | number | Required | Screen width in pixels. Range: 1 to 7680. |
| `Height` | number | Required | Screen height in pixels. Range: 1 to 4320. |
| `PixelDensity` | number | Required | Pixel density in DPI. Range: 72 to 10000. |
| `DeviceForm` | [DeviceForm](/docs/reference/engine/enums/DeviceForm.md) | Optional (default: Phone) | One of Phone, Tablet, Desktop, Console, VR. |
| `IsCustom` | boolean | Read-only | `true` if the device was user-created. |
| `ResolutionScale` | number | Optional (default: 1.0) | Resolution scaling factor. Must be greater than 0, max 10.0. |
| `PortraitKeyboardHeight` | number | Optional (default: 0) | Virtual keyboard height in portrait mode. |
| `LandscapeKeyboardHeight` | number | Optional (default: 0) | Virtual keyboard height in landscape mode. |

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `deviceId` | `string` |  | The unique identifier of the device to query. Must be a valid ID from `GetDeviceListAsync()`; cannot be `"default"`. |

**Returns:** `Dictionary` — A dictionary containing the device configuration and passed to
`CreateDeviceAsync` and `UpdateDeviceAsync`.

### Method: StudioDeviceSimulatorService:GetDeviceListAsync

**Signature:** `StudioDeviceSimulatorService:GetDeviceListAsync(): Array`

Returns an array of device IDs for all available presets, including
built-in and custom devices.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `Array` — An array of device IDs.

**Get device list example**

Example of GetDeviceListAsync method

```lua
local Simulator = game:GetService("StudioDeviceSimulatorService")
local devices = Simulator:GetDeviceListAsync()

for _, deviceId in devices do
    print(deviceId)
end
```

### Method: StudioDeviceSimulatorService:GetOrientationAsync

**Signature:** `StudioDeviceSimulatorService:GetOrientationAsync(): ScreenOrientation`

Returns the current simulated orientation.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `ScreenOrientation` — ScreenOrientation

### Method: StudioDeviceSimulatorService:GetPixelDensityAsync

**Signature:** `StudioDeviceSimulatorService:GetPixelDensityAsync(): float`

Returns the current simulated pixel density.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `float` — number

### Method: StudioDeviceSimulatorService:GetResolutionAsync

**Signature:** `StudioDeviceSimulatorService:GetResolutionAsync(): Vector2`

Returns the current simulated resolution.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `Vector2` — Vector2

### Method: StudioDeviceSimulatorService:GetScalingModeAsync

**Signature:** `StudioDeviceSimulatorService:GetScalingModeAsync(): DeviceSimulatorScalingMode`

Returns the current [DeviceSimulatorScalingMode](/docs/reference/engine/enums/DeviceSimulatorScalingMode.md) for how the
simulated resolution maps to the Studio viewport. See
[SetScalingModeAsync()](/docs/reference/engine/classes/StudioDeviceSimulatorService.md)
for the available modes.

Requires an active device; errors when `GetDeviceAsync()` returns
`"default"`.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `DeviceSimulatorScalingMode` — The current [DeviceSimulatorScalingMode](/docs/reference/engine/enums/DeviceSimulatorScalingMode.md).

### Method: StudioDeviceSimulatorService:RemoveDeviceAsync

**Signature:** `StudioDeviceSimulatorService:RemoveDeviceAsync(deviceId: string): ()`

Removes a custom device.

Errors if the target is a built-in preset.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `deviceId` | `string` |  | The unique identifier of the custom device to remove. |

**Returns:** `()`

### Method: StudioDeviceSimulatorService:SetDeviceAsync

**Signature:** `StudioDeviceSimulatorService:SetDeviceAsync(deviceId: string): ()`

Activates the specified device. Passing `"default"` stops simulation and
is equivalent to calling `StopSimulationAsync`.

Errors in PlayServer mode. Errors if the device ID does not exist.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `deviceId` | `string` |  | The unique identifier of the device to activate, or `"default"` to stop simulation. |

**Returns:** `()`

### Method: StudioDeviceSimulatorService:SetOrientationAsync

**Signature:** `StudioDeviceSimulatorService:SetOrientationAsync(orientation: ScreenOrientation): ()`

Sets or gets the simulated screen orientation. Accepts Portrait,
LandscapeLeft, or LandscapeRight. Other values will error.

Errors in PlayServer mode.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `orientation` | `ScreenOrientation` |  | The target screen orientation. Accepted values are [ScreenOrientation.Portrait](/docs/reference/engine/enums/ScreenOrientation.md), [ScreenOrientation.LandscapeLeft](/docs/reference/engine/enums/ScreenOrientation.md), or [ScreenOrientation.LandscapeRight](/docs/reference/engine/enums/ScreenOrientation.md). |

**Returns:** `()`

### Method: StudioDeviceSimulatorService:SetPixelDensityAsync

**Signature:** `StudioDeviceSimulatorService:SetPixelDensityAsync(density: float): ()`

Overrides or returns the simulated pixel density in DPI. Session-level;
cleared on device switch.

This method requires an active device. `SetPixelDensityAsync` also errors
in PlayServer mode.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `density` | `float` |  | The pixel density override in DPI. Must be between 72 and 10000. |

**Returns:** `()`

### Method: StudioDeviceSimulatorService:SetResolutionAsync

**Signature:** `StudioDeviceSimulatorService:SetResolutionAsync(width: int, height: int): ()`

Overrides the simulated viewport resolution or returns the current
resolution as a Vector2. Overrides are session-level and cleared when you
switch devices.

Coordinates are in landscape space: the first parameter maps to the
horizontal axis in landscape, the second to the vertical axis. In
portrait, axes are swapped automatically.

Both methods require an active device. They error if `GetDeviceAsync()`
returns `"default"`. `SetResolutionAsync` also errors in PlayServer mode.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `width` | `int` |  | The viewport width in pixels (horizontal axis in landscape orientation). Range: 1 to 7680. |
| `height` | `int` |  | The viewport height in pixels (vertical axis in landscape orientation). Range: 1 to 4320. |

**Returns:** `()`

### Method: StudioDeviceSimulatorService:SetScalingModeAsync

**Signature:** `StudioDeviceSimulatorService:SetScalingModeAsync(mode: DeviceSimulatorScalingMode): ()`

Controls how the simulated resolution maps to the Studio viewport.

- `ScaleToPhysicalSize` scales the viewport to approximate physical device
  size.
- `ActualResolution` renders at exact pixel resolution.
- `FitToWindow` scales to fill the viewport.

Both methods require an active device. `SetScalingModeAsync` also errors
in PlayServer mode.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `mode` | `DeviceSimulatorScalingMode` |  | The scaling mode to apply. One of [DeviceSimulatorScalingMode.ScaleToPhysicalSize](/docs/reference/engine/enums/DeviceSimulatorScalingMode.md), [DeviceSimulatorScalingMode.ActualResolution](/docs/reference/engine/enums/DeviceSimulatorScalingMode.md), or [DeviceSimulatorScalingMode.FitToWindow](/docs/reference/engine/enums/DeviceSimulatorScalingMode.md). |

**Returns:** `()`

### Method: StudioDeviceSimulatorService:StopSimulationAsync

**Signature:** `StudioDeviceSimulatorService:StopSimulationAsync(): ()`

Stops the active simulation. Prefer this over `SetDeviceAsync("default")`
for clarity.

Errors in PlayServer mode.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `()`

### Method: StudioDeviceSimulatorService:UpdateDeviceAsync

**Signature:** `StudioDeviceSimulatorService:UpdateDeviceAsync(deviceId: string, config: Dictionary): ()`

Updates a custom device's configuration.

Errors if the target is a built-in preset.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `deviceId` | `string` |  | The unique identifier of the custom device to update. |
| `config` | `Dictionary` |  | A dictionary of device fields to apply. Uses patch semantics: omitted optional fields retain their current values. Same schema as `CreateDeviceAsync()`. |

**Returns:** `()`

**Update Device example**

Example of UpdateDeviceAsync method

```lua
Simulator:UpdateDeviceAsync(id, {
    Name = "My Custom Tablet",
    Width = 2732,
    Height = 2048,
    PixelDensity = 264,
    DeviceForm = Enum.DeviceForm.Tablet,
})
```

## Events

### Event: StudioDeviceSimulatorService.ConfigurationChanged

**Signature:** `StudioDeviceSimulatorService.ConfigurationChanged()`

Fires when the active simulation state changes: device switch,
orientation, resolution, pixel density, scaling mode, or user interaction
with the Device Simulator UI. Does not fire for catalog-only operations
such as `CreateDeviceAsync`, `UpdateDeviceAsync` on a non-active device,
`RemoveDeviceAsync` on a non-active device, or `GetDeviceInfoAsync`.

Getter calls inside the handler are async and will yield.

*Security: PluginSecurity*

**Configuration changed example**

Example of ConfigurationChanged event

```lua
Simulator.ConfigurationChanged:Connect(function()
    local deviceId = Simulator:GetDeviceAsync()
    if deviceId ~= "default" then
        local res = Simulator:GetResolutionAsync()
        print(string.format("Active: %s @ %dx%d", deviceId, res.X, res.Y))
    end
end)
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