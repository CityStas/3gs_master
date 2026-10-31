---
name: ReflectionService
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
summary: "A service that allows scripts to query the engine's API at runtime for information about classes, properties, methods, and events."
---

# Class: ReflectionService

> A service that allows scripts to query the engine's API at runtime for
> information about classes, properties, methods, and events.

## Description

`ReflectionService` allows scripts to query the engine for details about its
API, including required security permissions, functionality, and inheritance
structure. You can use this service to dynamically inspect classes and their
properties, methods, and events, which can be useful for debugging, tooling,
or creating dynamic behaviors based on the engine's capabilities.

The following is an example script that inspects classes and their properties:

## Code Samples

**ReflectionService Overview**

Demonstrates [ReflectionService](/docs/reference/engine/classes/ReflectionService.md).

```lua
local ReflectionService = game:GetService("ReflectionService")

-- Create a SecurityCapabilities object with all capabilities
local allCapabilities = SecurityCapabilities.new(table.unpack(Enum.SecurityCapability:GetEnumItems()))

-- Get all classes accessible with all capabilities
local allClasses = ReflectionService:GetClasses({ Security = allCapabilities })
print("Total classes:", #allClasses)

-- Get a specific class
local partClass = ReflectionService:GetClass("Part")
if partClass then
	print("\nPart class:")
	print("  Name:", partClass.Name)
	print("  Superclass:", partClass.Superclass and tostring(partClass.Superclass) or "none")
end

-- Get the first 5 properties of a class
local properties = ReflectionService:GetPropertiesOfClass("Part", { Security = allCapabilities })
print("\nPart properties:", #properties)
for i = 1, math.min(5, #properties) do
	print("  -", properties[i].Name)
end
```

## Methods

### Method: ReflectionService:GetClass

**Signature:** `ReflectionService:GetClass(className: string, filter?: Dictionary): ReflectedClass?`

Given a class name in the Roblox API, returns a `ReflectedClass`
dictionary with information about the associated class's reflection state.
If no such class name exists, returns `nil`.

If you pass in a `ReflectionClassFilter` dictionary, you can adjust the
set of eligible classes and adjust the output behavior:

```lua
{
	-- The security context to use; can be more expansive than the current script's security
	Security: SecurityCapabilities?, -- default: SecurityCapabilities.fromCurrent()
	-- Require classes to derive from the passed-in class name
	IsA: string?, -- default: nil
	-- Whether to exclude Studio display information about the class
	ExcludeDisplay: boolean?, -- default: false
}
```

If the class name is valid, you'll get the following `ReflectedClass`
dictionary as output:

```lua
{
	-- The name of the class
	Name: string,
	-- Whether the class is serialized (able to be saved to disk)
	Serialized: boolean,
	-- The class's parent in the instance hierarchy (unless it's the root)
	Superclass: string?,
	-- The names of the class's direct children in the instance hierarchy
	Subclasses: {string},
	-- Studio display information
	Display: {
		-- Always "General" for classes
		Category: string,
		-- A message indicating that the class is deprecated, if applicable
		DeprecationMessage: string?,
	}?,
	-- The security permissions required to access this class
	Permits: {
		-- If the class is a Service, the security capabilities required to obtain access. If not applicable, this field isn't present
		GetService: SecurityCapabilities?,
		-- The security capabilities required to create an instance of this class. If not possible, this field isn't present
		New: SecurityCapabilities?,
	}
}
```

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  | The name of the class for which you wish to retrieve information. |
| `filter` | `Dictionary` | `nil` | An optional filter to restrict or expand the set of classes that this method can return and change the method's behavior. |

**Returns:** `ReflectedClass?` — A `ReflectedClass` dictionary with reflection information if the class
exists; otherwise, `nil`.

### Method: ReflectionService:GetClasses

**Signature:** `ReflectionService:GetClasses(filter?: Dictionary): List<ReflectedClass>`

Returns a list of `ReflectedClass` dictionaries for all classes in the
Roblox API that match the provided filter criteria.

If you pass in a `ReflectionClassFilter` dictionary, you can adjust the
set of eligible classes and adjust the output behavior:

```lua
{
	-- The security context to use; can be more expansive than the current script's security
	Security: SecurityCapabilities?, -- default: SecurityCapabilities.fromCurrent()
	-- Require classes to derive from the passed-in class name
	IsA: string?, -- default: nil
	-- Whether to exclude Studio display information about the classes
	ExcludeDisplay: boolean?, -- default: false
}
```

You'll get a list of `ReflectedClass` dictionaries as output, each with
the same structure as described in the `GetClass` method. If there are no
classes that match the filter criteria, you'll receive an empty list.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `filter` | `Dictionary` | `nil` | An optional filter to restrict or expand the set of classes that this method can return and change the method's behavior. |

**Returns:** `List<ReflectedClass>` — A list of `ReflectedClass` dictionaries with reflection information
for each class that matches the filter criteria.

### Method: ReflectionService:GetEventsOfClass

**Signature:** `ReflectionService:GetEventsOfClass(className: string, filter?: Dictionary): List<ReflectedEvent>`

Given a class name in the Roblox API, returns a list of `ReflectedEvent`
dictionaries for all events of that class that match the provided filter
criteria. If no such class name exists, returns `nil`.

If you pass in a `ReflectionMemberFilter` dictionary, you can adjust the
set of eligible events and adjust the output behavior:

```lua
{
	-- The security context to use; can be more expansive than the current script's security
	Security: SecurityCapabilities?, -- default: SecurityCapabilities.fromCurrent()
	-- Whether to exclude inherited events from superclasses
	ExcludeInherited: boolean?, -- default: false
	-- Whether to exclude Studio display information about the events
	ExcludeDisplay: boolean?, -- default: false
}
```

If the class name is valid and that class has events, you'll get a list of
`ReflectedEvent` dictionaries as output, each with the following
structure:

```lua
{
	-- The name of the event
	Name: string,
	-- The superclass from which the property is inherited, or the class name if not inherited
	Owner: string,
	-- A list of all parameters the event passes to connected functions
	Parameters: {
		{
			-- The name of the parameter
			Name: string,
			-- The type of the parameter
			Type: ReflectionType,
		}
	},
	-- Studio display information
	Display: {
		-- A message indicating that the event is deprecated, if applicable
		DeprecationMessage: string?,
	}?,
	-- The security permissions required to access this event
	Permits: {
		-- The security permissions required to listen for the event in any context
		Listen: SecurityCapabilities?,
	},
}
```

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  | The name of the class for which you wish to retrieve events. |
| `filter` | `Dictionary` | `nil` | An optional filter to restrict or expand the set of events that this method can return and change the method's behavior. |

**Returns:** `List<ReflectedEvent>` — A list of `ReflectedEvent` dictionaries with reflection information
for each event of the class that matches the filter criteria.

### Method: ReflectionService:GetMethodsOfClass

**Signature:** `ReflectionService:GetMethodsOfClass(className: string, filter?: Dictionary): List<ReflectedMethod>`

Given a class name in the Roblox API, returns a list of `ReflectedMethod`
dictionaries for all methods of that class that match the provided filter
criteria. If no such class name exists, returns `nil`.

If you pass in a `ReflectionMemberFilter` dictionary, you can adjust the
set of eligible methods and adjust the output behavior:

```lua
{
	-- The security context to use; can be more expansive than the current script's security
	Security: SecurityCapabilities?, -- default: SecurityCapabilities.fromCurrent()
	-- Whether to exclude inherited methods from superclasses
	ExcludeInherited: boolean?, -- default: false
	-- Whether to exclude Studio display information about the methods
	ExcludeDisplay: boolean?, -- default: false
}
```

If the class name is valid and that class has methods, you'll get a list
of `ReflectedMethod` dictionaries as output, each with the following
structure:

```lua
{
	-- The name of the method
	Name: string,
	-- The superclass from which the property is inherited, or the class name if not inherited
	Owner: string,
	-- A list of all parameters the method takes
	Parameters: {
		{
			-- The name of the parameter
			Name: string,
			-- The type of the parameter
			Type: ReflectionType,
			-- The default value of the parameter, if it has one
			DefaultValue: any?,
		}
	},
	-- The return type of the method; "void" if none
	ReturnType: ReflectionType,
	-- Whether the method is yielding
	CanYield: boolean,
	-- Studio display information
	Display: {
		-- A message indicating that the method is deprecated, if applicable
		DeprecationMessage: string?,
	}?,
	-- The security permissions required to access this method
	Permits: {
		-- The security permissions required to call the method in a single-threaded context
		Call: SecurityCapabilities?,
		-- The security permissions required to call the method in a parallel context
		CallParallel: SecurityCapabilities?,
	},
}
```

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  | The name of the class for which you wish to retrieve methods. |
| `filter` | `Dictionary` | `nil` | An optional filter to restrict or expand the set of methods that this method can return and change the method's behavior. |

**Returns:** `List<ReflectedMethod>` — A list of `ReflectedMethod` dictionaries with reflection information
for each method of the class that matches the filter criteria.

### Method: ReflectionService:GetPropertiesOfClass

**Signature:** `ReflectionService:GetPropertiesOfClass(className: string, filter?: Dictionary): List<ReflectedProperty>`

Given a class name in the Roblox API, returns a list of
`ReflectedProperty` dictionaries for all properties of that class that
match the provided filter criteria. If no such class name exists, returns
`nil`.

If you pass in a `ReflectionMemberFilter` dictionary, you can adjust the
set of eligible properties and adjust the output behavior:

```lua
{
	-- The security context to use; can be more expansive than the current script's security
	Security: SecurityCapabilities?, -- default: SecurityCapabilities.fromCurrent()
	-- Whether to exclude inherited properties from superclasses
	ExcludeInherited: boolean?, -- default: false
	-- Whether to exclude Studio display information about the properties
	ExcludeDisplay: boolean?, -- default: false
}
```

If the class name is valid and that class has properties, you'll get a
list of `ReflectedProperty` dictionaries as output, each with the
following structure:

```lua
{
	-- The name of the property
	Name: string,
	-- The superclass from which the property is inherited, or the class name if not inherited
	Owner: string,
	-- Whether the property is serialized (able to be saved to disk or sent over the network)
	Serialized: boolean,
	-- The type of the property
	Type: ReflectionType,
	-- The content type of the property, if applicable
	ContentType: Enum.AssetType?,
	-- Studio display information
	Display: {
		-- The category under which the property is listed in Studio
		Category: string,
		-- A message indicating that the property is deprecated, if applicable
		DeprecationMessage: string?,
	}?,
	-- The security permissions required to access this property
	Permits: {
		-- The security context required to read this property
		Read: SecurityCapabilities?,
		-- The security context required to read this property while thread-safe
		ReadParallel: SecurityCapabilities?,
		-- The security context required to write to this property
		Write: SecurityCapabilities?,
		-- The security context required to write to this property while thread-safe
		WriteParallel: SecurityCapabilities?,
	},
}
```

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` |  | The name of the class for which you wish to retrieve properties. |
| `filter` | `Dictionary` | `nil` | An optional filter to restrict or expand the set of properties that this method can return and change the method's behavior. |

**Returns:** `List<ReflectedProperty>` — A list of `ReflectedProperty` dictionaries with reflection information
for each property of the class that matches the filter criteria.

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