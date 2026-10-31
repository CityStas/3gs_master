---
name: PluginConnectionService
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
summary: "This service is used by plugins to communicate with other instances of themselves running in other data models."
---

# Class: PluginConnectionService

> This service is used by plugins to communicate with other instances of
> themselves running in other data models.

## Description

This service is used by plugins to communicate with other instances of
themselves running in other data models (e.g. a plugin in the Studio edit data
model can communicate with the instance of that same plugin in the Studio
playtest Server data model). Plugins can retrieve [PluginConnection](/docs/reference/engine/classes/PluginConnection.md)
objects from this service, which provide an API for sending messages across
the data model boundary. All access to this class is restricted to Plugin
security. The command bar is not currently supported.

## Code Samples

**PluginConnection echo Plugin**

This plugin demonstrates using PluginConnectionService end-to-end

On the edit data model, it listens for incoming connections from test data
models. On the test data model, it looks for its connection back to the edit
data model. In either case: When a connection is found, the plugin binds to it
to receive messages from the other data model and makes arrangements to clean
up when the connection disconencts or plugin unloads. After connecting, the
test data models send a greeting, and both sides of each connection send
messages back and forth for the duration of the test session.

```lua
local Service = game:GetService("PluginConnectionService")
local TestType = Enum.PluginConnectionTargetType.Test
local EditType = Enum.PluginConnectionTargetType.Edit

local function MakeConnection(Connection: PluginConnection, Side: string)
	assert(Connection.Connected)
	local Count = 0
	local Binding = Connection:BindToMessage(function(Msg: string)
		print(Msg)
		task.wait(1)
		if Connection.Connected then
			Connection:SendMessage(`Hello from {Side} iteration {Count}`)
		end
		Count += 1
	end)
	plugin.Unloading:Connect(function()
		Binding:Disconnect()
	end)
	Connection:GetPropertyChangedSignal("Connected"):Once(function()
		assert(not Connection.Connected)
		print("Disconnected", Connection.TargetId)
	end)
end

if Service:CanHaveConnectionType(TestType) then
	for _, ExistingConnection in Service:GetPluginConnectionsOfType(TestType) do
		MakeConnection(ExistingConnection, "Edit")
	end
	Service.Connected:Connect(function(NewConnection)
		if NewConnection.Type == TestType then
			MakeConnection(NewConnection, "Edit")
		end
	end)
elseif Service:CanHaveConnectionType(EditType) then
	local Connections = Service:GetPluginConnectionsOfType(EditType)
	assert(#Connections <= 1)
	local Connection: PluginConnection? = nil
	if #Connections == 1 then
		Connection = Connections[1]
	else
		while true do
			local NewConnection = Service.Connected:Wait()
			if NewConnection.Type == EditType then
				Connection = NewConnection
				break
			end
		end
	end
	assert(Connection)
	assert(Connection.Connected)

	MakeConnection(Connection, if game:GetService("RunService"):IsServer() then "Server" else "Client")
	Connection:SendMessage("Hello Edit!")
end
```

## Methods

### Method: PluginConnectionService:CanHaveConnectionType

**Signature:** `PluginConnectionService:CanHaveConnectionType(type: PluginConnectionTargetType): boolean`

Checks if the current data model can potentially have connections of a
given [PluginConnectionTargetType](/docs/reference/engine/enums/PluginConnectionTargetType.md). Note that it is possible for this
function to return true even if no such connections currently exist.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `type` | `PluginConnectionTargetType` |  | The connection type to check. |

**Returns:** `boolean` — Whether the current data model can potentially have connections of the
given type.

### Method: PluginConnectionService:GetPluginConnectionsOfType

**Signature:** `PluginConnectionService:GetPluginConnectionsOfType(type: PluginConnectionTargetType): List<PluginConnection>`

Returns a list of currently connected [PluginConnection](/docs/reference/engine/classes/PluginConnection.md) objects
with the given connection type. Each `PluginConnection` from this list
will initially have their `Connected` property set to true and correspond
to a connected data model related to the current data model according to
their [PluginConnectionTargetType](/docs/reference/engine/enums/PluginConnectionTargetType.md). For example, an edit data model
may have [PluginConnectionTargetType.Test](/docs/reference/engine/enums/PluginConnectionTargetType.md) connections to communicate
with its ongoing playtest data models, and each test data model will have
an [PluginConnectionTargetType.Edit](/docs/reference/engine/enums/PluginConnectionTargetType.md) connection back to its edit data
model.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `type` | `PluginConnectionTargetType` |  | The connection type to check. |

**Returns:** `List<PluginConnection>` — An array of the currently connected [PluginConnection](/docs/reference/engine/classes/PluginConnection.md) objects
with that target type.

## Events

### Event: PluginConnectionService.Connected

**Signature:** `PluginConnectionService.Connected(conn: PluginConnection)`

Fires just after a new [PluginConnection](/docs/reference/engine/classes/PluginConnection.md) successfully connects.
Plugins may listen for this signal to learn when a new data model that
they can communicate with becomes available.

Note: On startup, it is possible some
[PluginConnections](/docs/reference/engine/classes/PluginConnection.md) already exist. Plugins should
query [PluginConnectionService:GetPluginConnectionsOfType()](/docs/reference/engine/classes/PluginConnectionService.md) for
each type they are interested in after connecting to this function.

*Security: PluginSecurity*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `conn` | `PluginConnection` | The newly connected [PluginConnection](/docs/reference/engine/classes/PluginConnection.md). |

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