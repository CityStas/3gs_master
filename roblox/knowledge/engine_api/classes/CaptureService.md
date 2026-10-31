---
name: CaptureService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "A service which provides control over screenshot and video capture features."
---

# Class: CaptureService

> A service which provides control over screenshot and video capture features.

## Description

`CaptureService` is a client-side service that allows developers to control
how the screenshot and video capture feature integrates with their
experiences. It can be used to include preset moments where a capture is
automatically taken for a user, and that user can then save, share, or delete
the capture.

## Methods

### Method: CaptureService:CaptureScreenshot

**Signature:** `CaptureService:CaptureScreenshot(onCaptureReady: Function): ()`

This method captures a screenshot for the user but does not immediately
save it to their **Captures** gallery within the experience's main menu.
Instead, a temporary `contentId` is created to identify the new capture.

Note that any screenshots taken by this method will not be accessible via
[ReadCapturesFromGalleryAsync()](/docs/reference/engine/classes/CaptureService.md)
or be uploadable via
[UploadCaptureAsync()](/docs/reference/engine/classes/CaptureService.md).

The `onCaptureReady` callback can be used to prompt the user to save or
share the screenshot:

*Security: None · Thread Safety: Unsafe · Capabilities: Capture*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `onCaptureReady` | `Function` |  | A callback function that is called with the `contentId` of the new capture once it is ready. |

**Returns:** `()`

**Capture Screenshot**

Demonstrates [CaptureService:CaptureScreenshot()](/docs/reference/engine/classes/CaptureService.md).

```lua
local CaptureService = game:GetService("CaptureService")

-- Reference to an ImageLabel parent of the script containing this code
local imageLabel = script.Parent

local function onCaptureReady(contentId)
	imageLabel.Image = contentId
end

CaptureService:CaptureScreenshot(onCaptureReady)
```

### Method: CaptureService:CheckUploadCaptureStatusAsync

**Signature:** `CaptureService:CheckUploadCaptureStatusAsync(token: string): Tuple`

Client-side function that checks the status of a capture upload started
with
[StartUploadCaptureAsync()](/docs/reference/engine/classes/CaptureService.md),
using the returned `token`. Returns a tuple of the current
[UploadCaptureResult](/docs/reference/engine/enums/UploadCaptureResult.md) and, once the upload finishes successfully, the
asset ID of the uploaded capture.

Poll until a terminal state. While processing, the result is
[UploadCaptureResult.UploadPending](/docs/reference/engine/enums/UploadCaptureResult.md) and the asset ID is `0`.
[UploadCaptureResult.Success](/docs/reference/engine/enums/UploadCaptureResult.md) includes the final asset ID;
[UploadCaptureResult.CaptureModerated](/docs/reference/engine/enums/UploadCaptureResult.md) means moderation rejected the
capture; [UploadCaptureResult.UploadFailed](/docs/reference/engine/enums/UploadCaptureResult.md) means the upload did not
complete.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Capture*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `token` | `string` |  | The token returned by [StartUploadCaptureAsync()](/docs/reference/engine/classes/CaptureService.md) that identifies the in-progress upload. |

**Returns:** `Tuple` — Tuple of (result: [UploadCaptureResult](/docs/reference/engine/enums/UploadCaptureResult.md), assetId: `number`)

### Method: CaptureService:PromptCaptureGalleryPermissionAsync

**Signature:** `CaptureService:PromptCaptureGalleryPermissionAsync(captureGalleryPermission: CaptureGalleryPermission): boolean`

This client-side function prompts a user for permission to access their
local captures. Once they have accepted or rejected the prompt, it returns
a boolean representing their choice. This function is a necessary
prerequisite to `ReadCapturesFromGalleryAsync` and `UploadCaptureAsync`,
as both of these require gallery permissions to work.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Capture*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `captureGalleryPermission` | `CaptureGalleryPermission` |  | An [CaptureGalleryPermission](/docs/reference/engine/enums/CaptureGalleryPermission.md) representing the type of access for which the user will be prompted. |

**Returns:** `boolean` — A boolean representing whether or not the user has allowed access to
their captures.

**Prompt capture gallery permission**

This code snippet demonstrates how to prompt a user for access to their
captures gallery.

```lua
local CaptureService = game:GetService("CaptureService")

local function isGalleryAccessGranted()
	local accepted = CaptureService:PromptCaptureGalleryPermissionAsync(Enum.CaptureGalleryPermission.ReadAndUpload)
	return accepted
end
```

### Method: CaptureService:PromptSaveCapturesToGallery

**Signature:** `CaptureService:PromptSaveCapturesToGallery(captures: Array, resultCallback: Function): ()`

This method prompts the user to save the captures identified by the
provided `contentIds` or [Capture](/docs/reference/engine/classes/Capture.md) objects to their **Captures**
gallery within the experience's main menu.

*Security: None · Thread Safety: Unsafe · Capabilities: Capture*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `captures` | `Array` |  | An array of content IDs and/or [Capture](/docs/reference/engine/classes/Capture.md) objects. |
| `resultCallback` | `Function` |  | A callback function that will be invoked with a dictionary mapping each `contentId` and/or [Capture](/docs/reference/engine/classes/Capture.md) object to a boolean indicating if the user accepted saving that capture. |

**Returns:** `()`

### Method: CaptureService:PromptShareCapture

**Signature:** `CaptureService:PromptShareCapture(captureContent: Content, launchData: string, onAcceptedCallback: Function, onDeniedCallback: Function): ()`

This method prompts the user to share the capture identified by the
provided `contentId` or [Capture](/docs/reference/engine/classes/Capture.md) object using the native share
sheet on their device.

The capture is shared along with an invite link to the experience when
supported. Not all devices support including both a screenshot or video
and an invite link.

The `launchData` will be available in the `launchData` field for users who
join through the invite link.

For users or devices who are not eligible to use share sheets, this method
prompts them to download the capture instead.

*Security: None · Thread Safety: Unsafe · Capabilities: Capture*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `captureContent` | `Content` |  | A [Content](/docs/reference/engine/datatypes/Content.md) containing a `contentId` or [Capture](/docs/reference/engine/classes/Capture.md) object. |
| `launchData` | `string` |  | An optional string to include as launch data in the invite link. |
| `onAcceptedCallback` | `Function` |  | An optional callback function invoked if the user accepts sharing. |
| `onDeniedCallback` | `Function` |  | An optional callback function invoked if the user denies sharing. |

**Returns:** `()`

**Prompt Share Capture**

Demonstrates [CaptureService:PromptShareCapture()](/docs/reference/engine/classes/CaptureService.md).

```lua
local CaptureService = game:GetService("CaptureService")

local function onShareAccepted()
	print("Capture share was accepted!")
end

local function onShareDenied()
	print("Capture share was denied!")
end

local onCaptureReady = function(result, videoCapture)
	if videoCapture then
		local captureContent = Content.fromObject(videoCapture)
		CaptureService:PromptShareCapture(captureContent, "launchData" , onShareAccepted, onShareDenied)
	end
end

CaptureService:StartVideoCaptureAsync(onCaptureReady, {})
```

### Method: CaptureService:ReadCapturesFromGalleryAsync

**Signature:** `CaptureService:ReadCapturesFromGalleryAsync(captureTypeFilters?: Array, readFromAllEligibleExperiences?: boolean): Tuple`

This client-side function returns a paginated list of captures from the
user's gallery as a [CapturesPages](/docs/reference/engine/classes/CapturesPages.md) object sorted
reverse-chronologically, which can be used to iterate through the
captures. The results can be filtered by capture type with the
`captureTypeFilters` parameter. If this parameter isn't provided, the
function returns all captures.

If `readFromAllEligibleExperiences` is `true`, captures from all eligible
experiences will be read. If `false`, only those from the current
experience will be read. Additionally, captures taken with
[CaptureScreenshot()](/docs/reference/engine/classes/CaptureService.md) and
subsequently saved with
[PromptSaveCapturesToGallery()](/docs/reference/engine/classes/CaptureService.md)
will not be returned by this method.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Capture*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `captureTypeFilters` | `Array` | `{}` | An array of [CaptureType](/docs/reference/engine/enums/CaptureType.md). |
| `readFromAllEligibleExperiences` | `boolean` | `false` | A boolean; default is `false`. |

**Returns:** `Tuple` — Tuple of (result: [ReadCapturesFromGalleryResult](/docs/reference/engine/enums/ReadCapturesFromGalleryResult.md), capturesPages:
[CapturesPages](/docs/reference/engine/classes/CapturesPages.md))

**Read captures from gallery and iterate over pages**

This code snippet demonstrates how to fetch captures from a user gallery,
iterate over the result pages, and return all captures.

```lua
local CaptureService = game:GetService("CaptureService")

local function readCapturesFromGallery()
	local allCaptures = {}

	local capturesPages
	local success, result = pcall(function()
		local readResult, pages = CaptureService:ReadCapturesFromGalleryAsync({}, false)
		if readResult == Enum.ReadCapturesFromGalleryResult.Success then
			capturesPages = pages
		end
		return readResult
	end)

	if not success or result ~= Enum.ReadCapturesFromGalleryResult.Success then
		-- Likely a permissions error, see CaptureService:PromptCaptureGalleryPermissionAsync()
		warn("Failed to fetch initial captures: " .. result.Name)
		return
	end

	-- Iterate through current page
	local currentPage = capturesPages:GetCurrentPage()

	for _, capture in currentPage do
		table.insert(allCaptures, capture)
	end

	-- Advance to next page until finished
	while not capturesPages.IsFinished do
		local advanceToNextPageSuccess, _ = pcall(function()
			capturesPages:AdvanceToNextPageAsync()
		end)

		if not advanceToNextPageSuccess then
			return
		end

		currentPage = capturesPages:GetCurrentPage()
		for _, capture in currentPage do
			table.insert(allCaptures, capture)
		end
	end

	return allCaptures
end
```

### Method: CaptureService:StartUploadCaptureAsync

**Signature:** `CaptureService:StartUploadCaptureAsync(capture: Capture): Tuple`

Client-side function that begins uploading a [Capture](/docs/reference/engine/classes/Capture.md) (for example,
one from
[ReadCapturesFromGalleryAsync()](/docs/reference/engine/classes/CaptureService.md))
to the asset system. Unlike
[UploadCaptureAsync()](/docs/reference/engine/classes/CaptureService.md), which
blocks until the asset is created, this returns as soon as the upload
starts with a tuple of [UploadCaptureResult](/docs/reference/engine/enums/UploadCaptureResult.md) and a `token` string.
Use this when the user might leave before the upload finishes; a pending
`UploadCaptureAsync` is lost if the player leaves. Pass the token to
[CheckUploadCaptureStatusAsync()](/docs/reference/engine/classes/CaptureService.md)
to poll for completion and the resulting asset ID.

The user must grant gallery access through
[PromptCaptureGalleryPermissionAsync()](/docs/reference/engine/classes/CaptureService.md);
without it, the result is [UploadCaptureResult.NeedPermission](/docs/reference/engine/enums/UploadCaptureResult.md). The
capture must be eligible and present in the gallery. Uploads are
rate-limited per user and return
[UploadCaptureResult.UploadQuotaReached](/docs/reference/engine/enums/UploadCaptureResult.md) when exceeded.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Capture*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `capture` | `Capture` |  | The [Capture](/docs/reference/engine/classes/Capture.md) to upload. |

**Returns:** `Tuple` — Tuple of (result: [UploadCaptureResult](/docs/reference/engine/enums/UploadCaptureResult.md), token: `string`)

### Method: CaptureService:StartVideoCaptureAsync

**Signature:** `CaptureService:StartVideoCaptureAsync(onCaptureReady: Function, captureParams?: Dictionary): VideoCaptureStartedResult`

This method initiates a video capture recording. The recording will
continue until the
[StopVideoCapture()](/docs/reference/engine/classes/CaptureService.md) method is
called, or when 30 seconds have passed, whichever comes first. During the
video recording, all user voices are muted.

The `onCaptureReady` callback can be used to prompt the user to save or
share the video capture.

The `captureParams` parameter is currently non-operational.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Capture*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `onCaptureReady` | `Function` |  | A callback function that is called on video capture completion with a [VideoCaptureResult](/docs/reference/engine/enums/VideoCaptureResult.md) and, if successful, a [VideoCapture](/docs/reference/engine/classes/VideoCapture.md). |
| `captureParams` | `Dictionary` | `nil` | A dictionary of optional parameters that modify capture behavior. Currently non-operational. |

**Returns:** `VideoCaptureStartedResult` — A [VideoCaptureStartedResult](/docs/reference/engine/enums/VideoCaptureStartedResult.md) indicating whether the video
recording started successfully.

**Start Video Capture Async**

Demonstrates [CaptureService:StartVideoCaptureAsync()](/docs/reference/engine/classes/CaptureService.md).

```lua
local CaptureService = game:GetService("CaptureService")

local tool = Instance.new("Tool")
tool.Parent = workspace

local onCaptureReady = function(result, videoCapture)
	if result ~= Enum.VideoCaptureResult.Success and result ~= Enum.VideoCaptureResult.TimeLimitReached or not videoCapture then
		print("Video recording failed to complete for reason:", result)
	else
		-- Prompt the user to save the video capture to their gallery
		CaptureService:PromptSaveCapturesToGallery({ videoCapture }, function()
			print("Capture saved")
		end)
	end
end

tool.Activated:Connect(function()
	local videoRecordingAllowedResult: Enum.VideoCaptureStartedResult = CaptureService:StartVideoCaptureAsync(onCaptureReady, {})
	if videoRecordingAllowedResult ~= Enum.VideoCaptureStartedResult.Success then
		print("Video recording failed to start for reason:", videoRecordingAllowedResult)
	end
end)
```

### Method: CaptureService:StopVideoCapture

**Signature:** `CaptureService:StopVideoCapture(): ()`

This method ends a video capture that was started by the
[StartVideoCaptureAsync()](/docs/reference/engine/classes/CaptureService.md)
method.

*Security: None · Thread Safety: Unsafe · Capabilities: Capture*

**Returns:** `()`

### Method: CaptureService:TakeScreenshotCaptureAsync

**Signature:** `CaptureService:TakeScreenshotCaptureAsync(onCaptureReady: Function, captureParams?: Dictionary): ()`

This method initiates a screenshot capture. The `onCaptureReady` callback
can be used to prompt the user to save or share the screenshot capture.

Use the [UICaptureMode](/docs/reference/engine/enums/UICaptureMode.md) parameter in `captureParams` to specify
whether UI elements should be in the screenshot. By default, this is set
to [UICaptureMode.None](/docs/reference/engine/enums/UICaptureMode.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Capture*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `onCaptureReady` | `Function` |  | A callback function that is called on screenshot capture completion with a [ScreenshotCaptureResult](/docs/reference/engine/enums/ScreenshotCaptureResult.md) and, if successful, a [ScreenshotCapture](/docs/reference/engine/classes/ScreenshotCapture.md). |
| `captureParams` | `Dictionary` | `nil` | A dictionary that modifies capture behavior. |

**Returns:** `()`

**Take Screenshot Capture Async**

Demonstrates [CaptureService:TakeScreenshotCaptureAsync()](/docs/reference/engine/classes/CaptureService.md).

```lua
local CaptureService = game:GetService("CaptureService")

local parent = Instance.new("Tool")
parent.Parent = workspace

local onCaptureReady = function(result, screenshotCapture)
	if result ~= Enum.ScreenshotCaptureResult.Success or not screenshotCapture then
		print("Screenshot failed to complete for reason:", result)
	else
		-- Prompt the user to save the screenshot capture to their gallery
		CaptureService:PromptSaveCapturesToGallery({ screenshotCapture }, function(results)
			for capture, result in pairs(results) do
				if result then
					print("Capture saved")
				end
			end
		end)
	end
end

parent.Activated:Connect(function()
	CaptureService:TakeScreenshotCaptureAsync(onCaptureReady, { UICaptureMode = Enum.UICaptureMode.All })
end)
```

### Method: CaptureService:UploadCaptureAsync

**Signature:** `CaptureService:UploadCaptureAsync(capture: Capture): Tuple`

This client-side function uploads a capture, like one retrieved from
`ReadCapturesFromGalleryAsync`, to the asset system. It returns a tuple of
the result and the asset ID.

Notes:

- This function will only work properly if the Maturity and Compliance
  questionnaire has been filled out for the experience.
- For video capture types, there is an upload limit of 20 videos per day
  per user; when that limit is exceeded, the result is
  [UploadCaptureResult.UploadQuotaReached](/docs/reference/engine/enums/UploadCaptureResult.md), which lets you
  distinguish quota exhaustion from other failures.
- This function can take up to several minutes to finish executing, and
  the user will need to remain in the experience.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Capture*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `capture` | `Capture` |  | The [Capture](/docs/reference/engine/classes/Capture.md) to upload. |

**Returns:** `Tuple` — Tuple of (result: [UploadCaptureResult](/docs/reference/engine/enums/UploadCaptureResult.md), assetId: `number`)

**Upload capture to asset system**

This code snippet demonstrates how to upload a capture to the asset system.

```lua
local CaptureService = game:GetService("CaptureService")

local function uploadCapture(capture: Capture)
	local success, result = pcall(function()
		local uploadCaptureResult, assetId = CaptureService:UploadCaptureAsync(capture)

		if uploadCaptureResult ~= Enum.UploadCaptureResult.Success then
			-- Handle failure
			return nil
		end

		return assetId
	end)

	if not success then
		-- Handle error
		return nil
	end

	return result
end
```

## Events

### Event: CaptureService.CaptureBegan

**Signature:** `CaptureService.CaptureBegan(captureType: CaptureType)`

This event fires right before a new capture is taken. It can be used to
customize the capture experience, for example by hiding certain GUI
elements.

*Security: None · Capabilities: Capture*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `captureType` | `CaptureType` | An [CaptureType](/docs/reference/engine/enums/CaptureType.md) indicating whether the capture is a screenshot or video. |

### Event: CaptureService.CaptureEnded

**Signature:** `CaptureService.CaptureEnded(captureType: CaptureType)`

This event fires after a new capture completes. It can be used to restore
any changes made when the [CaptureBegan](/docs/reference/engine/classes/CaptureService.md)
event fired.

*Security: None · Capabilities: Capture*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `captureType` | `CaptureType` | An [CaptureType](/docs/reference/engine/enums/CaptureType.md) indicating whether the capture was a screenshot or video. |

### Event: CaptureService.UserCaptureSaved

**Signature:** `CaptureService.UserCaptureSaved(captureContentId: ContentId)`

This event fires when the user saves a screenshot using the Roblox
screenshot capture UI. It can be used for analytics or to prompt the user
to share their capture.

*Security: None · Capabilities: Capture*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `captureContentId` | `ContentId` | The `contentId` identifying the screenshot that the user saved. |

### Event: CaptureService.CaptureSaved

**Signature:** `CaptureService.CaptureSaved(captureInfo: Dictionary)`

> **Deprecated:** This event has been superseded by the [UserCaptureSaved](/docs/reference/engine/classes/CaptureService.md) event.

Fires when a screenshot capture is saved to the user's gallery. Provides a
`captureInfo` dictionary with `contentId`, `filePath`, and `type`. Fires
only for screenshot captures, not video captures.

Deprecated; use [UserCaptureSaved](/docs/reference/engine/classes/CaptureService.md)
instead, which fires with the saved capture's `contentId` directly.

*Security: None · Capabilities: Capture*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `captureInfo` | `Dictionary` | A dictionary containing `contentId`, `filePath`, and `type` fields describing the saved capture. |

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