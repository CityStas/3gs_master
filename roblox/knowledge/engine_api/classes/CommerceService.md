---
name: CommerceService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "Supports real-world purchases that you can bundle with digital benefits."
---

# Class: CommerceService

> Supports real-world purchases that you can bundle with digital benefits.

## Description

[CommerceService](/docs/reference/engine/classes/CommerceService.md) is a service that supports real-world purchases that
you can bundle with virtual items. For information on eligibility and
implementation, see
[Commerce products](/docs/en-us/production/monetization/commerce-products.md).

## Methods

### Method: CommerceService:GetCommerceProductInfoAsync

**Signature:** `CommerceService:GetCommerceProductInfoAsync(commerceProductId: string): Dictionary`

Retrieves information about the products that you are selling and surface
them within your experience. How you surface products to your users is
entirely up to you.

| Name | string | Localized name of of the physical item |
| --- | --- | --- |
| Description | string | Localized description of the physical item |
| IconImageAssetId | number | The image asset ID of main default image of the physical item |
| DisplayPrice | string | Localized price string with currency symbol of the physical item. e.g. “$4.99“ |
| IsPurchasable | bool | If the item can be added to a merchant checkout session, i.e. item is in stock, or can be backordered |

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `commerceProductId` | `string` |  | The identifier of the commerce product to look up, either the numeric ID or the full `COM-`-prefixed form. |

**Returns:** `Dictionary` — A dictionary of information about the commerce product, including
whether it `IsForSale`, an `Item` sub-table of display details
(`Name`, `Description`, `IconImageAssetId`, `DisplayPrice`, and
`IsPurchasable`), and the `Benefits` granted by purchasing it.

### Method: CommerceService:PromptCommerceProductPurchase

**Signature:** `CommerceService:PromptCommerceProductPurchase(user: Player, commerceProductId: string): ()`

Prompts a user to purchase a commerce product using the provided
`commerceProductId`. Opens a webview that guides the user through the
purchasing flow.

*Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `user` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) to prompt with the purchase flow. When called from a client script, this must be the local player. |
| `commerceProductId` | `string` |  | The identifier of the commerce product to purchase, either the numeric ID or the full `COM-`-prefixed form. |

**Returns:** `()`

### Method: CommerceService:PromptRealWorldCommerceBrowser

**Signature:** `CommerceService:PromptRealWorldCommerceBrowser(player: Player, url: string): ()`

This is a legacy endpoint that is not meant for use. To open the webview
to the purchasing flow for real world commerce, see
[CommerceService:PromptCommerceProductPurchase](/docs/reference/engine/classes/CommerceService.md). For more
information, see
[Commerce products](/docs/en-us/production/monetization/commerce-products.md)

*Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) for whom the browser opens. When called from a client script, this must be the local player. |
| `url` | `string` |  | The real-world commerce URL to open. The URL must be on the commerce allowlist, or the request is ignored. |

**Returns:** `()`

### Method: CommerceService:UserEligibleForRealWorldCommerceAsync

**Signature:** `CommerceService:UserEligibleForRealWorldCommerceAsync(): boolean`

This is a legacy endpoint that is not meant for use. To check if a user is
eligible for real world commerce, see
[PolicyService.IsEligibleToPurchaseCommerceProduct](/docs/reference/engine/classes/PolicyService.md). For more
information, see
[Commerce products](/docs/en-us/production/monetization/commerce-products.md)

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Returns:** `boolean` — `true` if the current user is eligible for real-world commerce.

## Events

### Event: CommerceService.PromptCommerceProductPurchaseFinished

**Signature:** `CommerceService.PromptCommerceProductPurchaseFinished(user: Player, productId: string)`

Use this signal to detect when a user has completed the purchasing flow
and the webview has closed to resume gameplay within the experience.
**This signal does not indicate a successful purchase**, so do not grant
virtual items solely from this signal.

While optional, it is recommended to use this signal to reorient your
users on Android, as the commerce purchasing flow will have forced them
into portrait mode.

*Security: None · Capabilities: Monetization*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `user` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) who was prompted with the purchase flow. |
| `productId` | `string` | The identifier of the commerce product whose purchase flow finished. |

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