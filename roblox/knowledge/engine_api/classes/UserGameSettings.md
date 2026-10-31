---
name: UserGameSettings
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
summary: "`UserGameSettings` is a singleton class found inside of the UserSettings singleton. It holds various persistent settings relating to how the user wants to control their camera, and their character."
---

# Class: UserGameSettings

> `UserGameSettings` is a singleton class found inside of the
> [UserSettings](/docs/reference/engine/classes/UserSettings.md) singleton. It holds various persistent settings relating
> to how the user wants to control their camera, and their character.

## Description

`UserGameSettings` is a singleton class found inside of the
[UserSettings](/docs/reference/engine/classes/UserSettings.md) singleton. It holds various persistent settings relating
to how the user wants to control their camera, and their character.

The properties on this class reflect both the user-facing options exposed in
the in-game settings menu (such as graphics quality, master volume, camera and
control modes) as well as other contextual user-configurable state that is not
surfaced in the menu itself (such as internal onboarding progress, VR comfort
options, window layout, and debug or profiling configuration). As a result,
some properties listed here may not correspond to anything visible in the
settings UI, and many are restricted to internal Roblox scripts.

You can access this object from a [LocalScript](/docs/reference/engine/classes/LocalScript.md) via:

```lua
UserSettings():GetService("UserGameSettings")
```

This object is intended to be used on the client only, as it serves no purpose
on the server. It will also reflect your own settings when testing in Roblox
Studio.

## Code Samples

**UserGameSettings Listener**

A basic example that shows how you can listen to changes in the user's
settings. With this code pasted into a LocalScript running in the
StarterPlayerScripts, you can change settings in Roblox's game menu, and see
their values appear in the output as detected changes.

```lua
local gameSettings = UserSettings().GameSettings

local function onGameSettingChanged(nameOfSetting)
	-- Fetch the value of this setting through a pcall to make sure we can retrieve it.
	-- Sometimes the event fires with properties that LocalScripts can't access.
	local canGetSetting, setting = pcall(function()
		return gameSettings[nameOfSetting]
	end)

	if canGetSetting then
		print("Your " .. nameOfSetting .. " has changed to: " .. tostring(setting))
	end
end

gameSettings.Changed:Connect(onGameSettingChanged)
```

## Properties

### Property: UserGameSettings.AllTutorialsDisabled

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Indicates whether all in-game tutorials have been disabled by the user.

### Property: UserGameSettings.BadgeVisible

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Indicates whether badge notifications are visible to the client.

### Property: UserGameSettings.CameraMode

```json
{
  "type": "CustomCameraMode",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Control"
}
```

The custom camera mode currently in-use by the client.

### Property: UserGameSettings.ChatVisible

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Indicates whether the in-game chat is visible to the client.

### Property: UserGameSettings.ComputerCameraMovementMode

```json
{
  "type": "ComputerCameraMovementMode",
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
  "category": "Control",
  "capabilities": [
    "Input"
  ]
}
```

The camera movement mode currently in-use by the client on desktop.

### Property: UserGameSettings.ComputerMovementMode

```json
{
  "type": "ComputerMovementMode",
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
  "category": "Control",
  "capabilities": [
    "Input"
  ]
}
```

The type of controls being used by the client on desktop.

### Property: UserGameSettings.ControlMode

```json
{
  "type": "ControlMode",
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
  "category": "Control",
  "capabilities": [
    "Input"
  ]
}
```

Toggles whether or not the client can use the Mouse Lock Switch mode.

### Property: UserGameSettings.Fullscreen

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Indicates whether the client's window is currently in full screen mode.

### Property: UserGameSettings.GamepadCameraSensitivity

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
    "Input"
  ]
}
```

Describes how sensitive the camera is when using a gamepad.

### Property: UserGameSettings.GraphicsOptimizationMode

```json
{
  "type": "GraphicsOptimizationMode",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance"
}
```

The graphics optimization mode used by the client to balance visual
quality and performance.

### Property: UserGameSettings.GraphicsQualityLevel

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance"
}
```

The current graphics quality level being used by the client.

### Property: UserGameSettings.HasEverUsedVR

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Indicates whether the user has ever launched the client in VR mode.

### Property: UserGameSettings.MasterVolume

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

A <a href="/docs/en-us/luau/numbers.md">float</a> between 0 and 1
representing the volume of the game's client.

### Property: UserGameSettings.MasterVolumeStudio

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

A float between 0 and 1 representing the master volume used in Roblox
Studio.

### Property: UserGameSettings.MaxQualityEnabled

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance"
}
```

Indicates whether the client's graphics quality is set to the maximum
available level.

### Property: UserGameSettings.MouseSensitivity

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
    "Input"
  ]
}
```

A float between 0 and 4 representing the sensitivity of the client's
camera sensitivity.

### Property: UserGameSettings.OnboardingsCompleted

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

A comma-separated list of onboarding IDs that the user has completed.

### Property: UserGameSettings.PartyVoiceVolume

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

A float between 0 and 1 representing the volume of party voice chat.

### Property: UserGameSettings.PeoplePageLayout

```json
{
  "type": "PeoplePageLayout",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

The layout style used to display the people page in the in-game menu.

### Property: UserGameSettings.PlayerListVisible

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Indicates whether the in-game player list is visible to the client.

### Property: UserGameSettings.PlayerNamesEnabled

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Indicates whether player names are displayed above characters in the game.

### Property: UserGameSettings.RCCProfilerRecordFrameRate

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
  "category": "Data"
}
```

Internal MicroProfiler setting specifying the frame rate used when
capturing server-side RCC profiler data.

### Property: UserGameSettings.RCCProfilerRecordTimeFrame

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
  "category": "Data"
}
```

Internal MicroProfiler setting specifying the duration over which
server-side RCC profiler data is captured.

### Property: UserGameSettings.RotationType

```json
{
  "type": "RotationType",
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
  "category": "Control",
  "capabilities": [
    "Input"
  ]
}
```

Controls how the client's character is rotated.

### Property: UserGameSettings.SavedQualityLevel

```json
{
  "type": "SavedQualitySetting",
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
    "Players"
  ]
}
```

The graphics quality level set by the client.

### Property: UserGameSettings.StartMaximized

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Indicates whether Roblox Studio should launch in a maximized window.

### Property: UserGameSettings.StartScreenPosition

```json
{
  "type": "Vector2",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

The screen position of the client's window when the application launches.

### Property: UserGameSettings.StartScreenSize

```json
{
  "type": "Vector2",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

The size of the client's window when the application launches.

### Property: UserGameSettings.TouchCameraMovementMode

```json
{
  "type": "TouchCameraMovementMode",
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
  "category": "Control",
  "capabilities": [
    "Input"
  ]
}
```

The camera type in-use by the client while on a mobile device.

### Property: UserGameSettings.TouchMovementMode

```json
{
  "type": "TouchMovementMode",
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
  "category": "Control",
  "capabilities": [
    "Input"
  ]
}
```

The type of controls being used by the client on a mobile device.

### Property: UserGameSettings.UsedCoreGuiIsVisibleToggle

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Indicates whether the user has toggled the visibility of core GUI
elements.

### Property: UserGameSettings.UsedCustomGuiIsVisibleToggle

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Indicates whether the user has toggled the visibility of custom GUI
elements.

### Property: UserGameSettings.UsedHideHudShortcut

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Indicates whether the user has used the keyboard shortcut for hiding the
HUD.

### Property: UserGameSettings.VignetteEnabled

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Indicates whether the VR vignette comfort effect is enabled.

### Property: UserGameSettings.VoiceChatVolume

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

A float between `0` and `2` representing the volume of in-game voice chat.

### Property: UserGameSettings.VREnabled

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Indicates whether the client is currently running in VR mode.

### Property: UserGameSettings.VRRotationIntensity

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

The intensity of camera rotation when turning in VR.

### Property: UserGameSettings.VRSmoothRotationEnabled

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Indicates whether smooth rotation is used instead of snap rotation in VR.

## Methods

### Method: UserGameSettings:GetCameraYInvertValue

**Signature:** `UserGameSettings:GetCameraYInvertValue(): int`

Returns the camera's Y-invert value.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `int` — The camera's current Y-axis inversion multiplier.

### Method: UserGameSettings:GetOnboardingCompleted

**Signature:** `UserGameSettings:GetOnboardingCompleted(onboardingId: string): boolean`

Checks whether or not the given onboarding has been completed yet, which
is useful for avoiding showing the onboarding animation again.

If onboardingId is not one of the accepted IDs, an error is thrown.

The onboarding process is one-way. This means that, as a developer, you
can force the onboarding process to completion but cannot reset it.

See also:

- [UserGameSettings:SetOnboardingCompleted()](/docs/reference/engine/classes/UserGameSettings.md), sets onboarding as
  completed

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `onboardingId` | `string` |  | The onboarding ID to inquire about. |

**Returns:** `boolean` — Whether or not the onboarding in particular has been completed yet.

### Method: UserGameSettings:InFullScreen

**Signature:** `UserGameSettings:InFullScreen(): boolean`

Returns true if the user's Roblox window is in full screen mode.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Returns:** `boolean` — Whether the user's Roblox window is in full screen mode.

### Method: UserGameSettings:InStudioMode

**Signature:** `UserGameSettings:InStudioMode(): boolean`

Returns true if the client's game session is in Roblox Studio.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Returns:** `boolean` — Whether the current client session is running in Roblox Studio.

### Method: UserGameSettings:SetCameraYInvertVisible

**Signature:** `UserGameSettings:SetCameraYInvertVisible(): ()`

If called, Roblox toggles the menu option to invert the user's camera y
axis.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `()`

### Method: UserGameSettings:SetGamepadCameraSensitivityVisible

**Signature:** `UserGameSettings:SetGamepadCameraSensitivityVisible(): ()`

If called, Roblox toggles the menu option to control the camera
sensitivity with gamepads.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `()`

### Method: UserGameSettings:SetOnboardingCompleted

**Signature:** `UserGameSettings:SetOnboardingCompleted(onboardingId: string): ()`

Sets the given onboarding as completed, so it won't be shown again to the
user the next time they play.

Currently, this function only accepts
[DynamicThumbstick](/docs/en-us/luau/strings.md), and it is used to
persistently track whether or not the player has finished the tutorial for
the Dynamic Thumbstick control scheme. If onboardingId is not one of the
accepted IDs, an error is thrown.

The onboarding process is one-way. This means that, as a developer, you
can force the onboarding process to completion but cannot reset it.

See also:

- [UserGameSettings:GetOnboardingCompleted()](/docs/reference/engine/classes/UserGameSettings.md), checks if onboarding
  has been completed

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `onboardingId` | `string` |  | The onboarding ID to set as completed. |

**Returns:** `()`

## Events

### Event: UserGameSettings.FullscreenChanged

**Signature:** `UserGameSettings.FullscreenChanged(isFullscreen: boolean)`

Fires if the user's full screen mode is changed. The event will only fire
on desktop devices that can toggle full screen mode. The game will always
be in full screen on mobile devices and consoles.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `isFullscreen` | `boolean` | Whether the user's Roblox window is now in full screen mode. |

**Full Screen Mode Detection**

A LocalScript that demonstrates how you can detect whether a game is in full
screen or not.

```lua
local gameSettings = UserSettings().GameSettings

local function checkFullScreenMode()
	local inFullscreen = gameSettings:InFullScreen()
	if inFullscreen then
		print("Full Screen mode enabled!")
	else
		print("Full Screen mode disabled!")
	end
end

checkFullScreenMode()
gameSettings.FullscreenChanged:Connect(checkFullScreenMode)
```

### Event: UserGameSettings.StudioModeChanged

**Signature:** `UserGameSettings.StudioModeChanged(isStudioMode: boolean)`

Fired when the user's client switches between Studio mode and in-game
mode. This gets fired periodically in Roblox Studio when a session starts.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `isStudioMode` | `boolean` | Whether the client session is now running in Roblox Studio. |

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