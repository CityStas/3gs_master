---
name: EncodingService
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
summary: "Service providing common encoding, hashing, and compression methods."
---

# Class: EncodingService

> Service providing common encoding, hashing, and compression methods.

## Methods

### Method: EncodingService:Base64Decode

**Signature:** `EncodingService:Base64Decode(input: buffer): buffer`

Method takes a [buffer](/docs/reference/engine/globals/buffer.md) with data encoded in Base64 format and
decodes it into a new [buffer](/docs/reference/engine/globals/buffer.md).

If the input is not valid Base64 data, this method throws an error.

Base64 data is most often used for binary data encoding, so these
functions are designed to work on [buffer](/docs/reference/engine/globals/buffer.md) values.

If the data is stored in a string, [buffer.fromstring](/docs/reference/engine/globals/buffer.md) can be used
to quickly convert it into a buffer.

*Security: None · Thread Safety: Safe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `input` | `buffer` |  | [buffer](/docs/reference/engine/globals/buffer.md) containing Base64 data to decode |

**Returns:** `buffer` — [buffer](/docs/reference/engine/globals/buffer.md) with the decoded result

### Method: EncodingService:Base64Encode

**Signature:** `EncodingService:Base64Encode(input: buffer): buffer`

Method takes a [buffer](/docs/reference/engine/globals/buffer.md) with binary data and encodes it using
Base64.

Encoded result is returned as a new [buffer](/docs/reference/engine/globals/buffer.md).

*Security: None · Thread Safety: Safe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `input` | `buffer` |  | [buffer](/docs/reference/engine/globals/buffer.md) containing binary data to encode |

**Returns:** `buffer` — [buffer](/docs/reference/engine/globals/buffer.md) with the encoded result

### Method: EncodingService:CompressBuffer

**Signature:** `EncodingService:CompressBuffer(input: buffer, algorithm: CompressionAlgorithm, compressionLevel?: int): buffer`

Compresses the binary data stored in a [buffer](/docs/reference/engine/globals/buffer.md) using the
specified compression algorithm and compression level. The higher the
compression level, the longer it takes to compress, but the resulting
compression ratio might increase.

For [CompressionAlgorithm.Zstd](/docs/reference/engine/enums/CompressionAlgorithm.md), the allowed compression values are
from -7 to 22 inclusive.

*Security: None · Thread Safety: Safe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `input` | `buffer` |  | [buffer](/docs/reference/engine/globals/buffer.md) with binary data to compress |
| `algorithm` | `CompressionAlgorithm` |  | [CompressionAlgorithm](/docs/reference/engine/enums/CompressionAlgorithm.md) to use for compression |
| `compressionLevel` | `int` | `1` | optional integer compression level to use |

**Returns:** `buffer` — [buffer](/docs/reference/engine/globals/buffer.md) with compressed binary data

### Method: EncodingService:ComputeBufferHash

**Signature:** `EncodingService:ComputeBufferHash(input: buffer, algorithm: HashAlgorithm): buffer`

Uses a
[cryptographic hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
to compute a hash of the input [buffer](/docs/reference/engine/globals/buffer.md). Returns a new
[buffer](/docs/reference/engine/globals/buffer.md) with the binary data.

See descriptions of [HashAlgorithm](/docs/reference/engine/enums/HashAlgorithm.md) to learn of the supported digest
size for each hash.

#### Do not use this for passwords

None of these hashes are password hashing algorithms. They were designed
to be fast to execute, whereas password hashing should never be fast. You
shouldn't use this function for computing password hashes that will be
stored, or for deriving keys from passwords.

*Security: None · Thread Safety: Safe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `input` | `buffer` |  | [buffer](/docs/reference/engine/globals/buffer.md) with binary data to compute hash for |
| `algorithm` | `HashAlgorithm` |  | [HashAlgorithm](/docs/reference/engine/enums/HashAlgorithm.md) cryptographic hash function |

**Returns:** `buffer` — [buffer](/docs/reference/engine/globals/buffer.md) with the binary data of the hash

### Method: EncodingService:ComputeStringHash

**Signature:** `EncodingService:ComputeStringHash(input: string, algorithm: HashAlgorithm): string`

Uses a
[cryptographic hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
to compute a hash of the input string. Returns a new string with the
binary data.

See descriptions of [HashAlgorithm](/docs/reference/engine/enums/HashAlgorithm.md) to learn of the supported digest
size for each hash.

#### Do not use this for passwords

None of these hashes are password hashing algorithms. They were designed
to be fast to execute, whereas password hashing should never be fast. You
shouldn't use this function for computing password hashes that will be
stored, or for deriving keys from passwords.

*Security: None · Thread Safety: Safe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `input` | `string` |  | string to compute the hash for |
| `algorithm` | `HashAlgorithm` |  | [HashAlgorithm](/docs/reference/engine/enums/HashAlgorithm.md) cryptographic hash function |

**Returns:** `string` — String with the binary data of the hash

### Method: EncodingService:DecompressBuffer

**Signature:** `EncodingService:DecompressBuffer(input: buffer, algorithm: CompressionAlgorithm): buffer`

Decompresses the binary data stored in a [buffer](/docs/reference/engine/globals/buffer.md) using the
specified compression algorithm.

Decompression might throw an error if the compressed data doesn't contain
expected decompressed size, if it is larger than 1GB or if it is invalid.

It is recommended to use [EncodingService.GetDecompressedBufferSize](/docs/reference/engine/classes/EncodingService.md)
to find out the decompressed data size before attempting to decompress.
This is very important if the input buffer contents are outside of your
control (for example, from a client [RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md))

*Security: None · Thread Safety: Safe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `input` | `buffer` |  | [buffer](/docs/reference/engine/globals/buffer.md) with compressed binary data |
| `algorithm` | `CompressionAlgorithm` |  | [CompressionAlgorithm](/docs/reference/engine/enums/CompressionAlgorithm.md) to use for decompression |

**Returns:** `buffer` — [buffer](/docs/reference/engine/globals/buffer.md) with the decompressed binary data

### Method: EncodingService:GetDecompressedBufferSize

**Signature:** `EncodingService:GetDecompressedBufferSize(input: buffer, algorithm: CompressionAlgorithm): int?`

Reports the size of the decompressed data stored in a compressed
[buffer](/docs/reference/engine/globals/buffer.md). If the compressed data doesn't have a size or the size
is corrupted or invalid (larger than 1GB), function returns `nil`. When a
`nil` is returned, attempting to use
[EncodingService.DecompressBuffer](/docs/reference/engine/classes/EncodingService.md) on this [buffer](/docs/reference/engine/globals/buffer.md) will
throw an error.

*Security: None · Thread Safety: Safe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `input` | `buffer` |  | [buffer](/docs/reference/engine/globals/buffer.md) with compressed binary data |
| `algorithm` | `CompressionAlgorithm` |  | [CompressionAlgorithm](/docs/reference/engine/enums/CompressionAlgorithm.md) used to compress it |

**Returns:** `int?` — Integer size of the decompressed data or 'nil'

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