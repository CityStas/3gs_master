---
name: Color3
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A color value comprised of red, green, and blue components."
---

# Color3

A color value comprised of red, green, and blue components.

**Type:** datatype

## Description

The [Color3](/docs/reference/engine/datatypes/Color3.md) data type describes a color using red, green, and blue
components in the range of 0 to 1. Unlike the [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) data type
which describes named colors, [Color3](/docs/reference/engine/datatypes/Color3.md) is used for precise coloring
of objects on screen through properties like [BasePart.Color](/docs/reference/engine/classes/BasePart.md) and
[GuiObject.BackgroundColor3](/docs/reference/engine/classes/GuiObject.md).

## Constructors

### Color3.new

**Signature:** `Color3.new(red?: number, green?: number, blue?: number)`

Returns a [Color3](/docs/reference/engine/datatypes/Color3.md) with the given red, green, and blue values.
The parameters should be within the range of 0 to 1.

```lua
local red = Color3.new(1, 0, 0)
local green = Color3.new(0, 1, 0)
local blue = Color3.new(0, 0, 1)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `red` | `number` | `0` | The red component of the color, from 0 to 1. |
| `green` | `number` | `0` | The green component of the color, from 0 to 1. |
| `blue` | `number` | `0` | The blue component of the color, from 0 to 1. |

### Color3.fromRGB

**Signature:** `Color3.fromRGB(red?: number, green?: number, blue?: number)`

Creates a [Color3](/docs/reference/engine/datatypes/Color3.md) with the given red, green, and blue
components. Unlike most other [Color3](/docs/reference/engine/datatypes/Color3.md) functions, the parameters
for this function should be within the range of 0 to 255.

```lua
local red = Color3.fromRGB(255, 0, 0)
local green = Color3.fromRGB(0, 255, 0)
local blue = Color3.fromRGB(0, 0, 255)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `red` | `number` | `0` | The red component of the color, from 0 to 255. |
| `green` | `number` | `0` | The green component of the color, from 0 to 255. |
| `blue` | `number` | `0` | The blue component of the color, from 0 to 255. |

### Color3.fromHSV

**Signature:** `Color3.fromHSV(hue: number, saturation: number, value: number)`

Creates a [Color3](/docs/reference/engine/datatypes/Color3.md) with the given hue, saturation, and value. The
parameters should be within the range of 0 to 1.

```lua
local red = Color3.fromHSV(1, 1, 1)
local green = Color3.fromHSV(0.3333333, 1, 1)
local white = Color3.fromHSV(0, 0, 1)
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `hue` | `number` |  | The hue of the color, from 0 to 1. |
| `saturation` | `number` |  | The saturation of the color, from 0 to 1. |
| `value` | `number` |  | The value (brightness) of the color, from 0 to 1. |

### Color3.fromHex

**Signature:** `Color3.fromHex(hex: string)`

Returns a new [Color3](/docs/reference/engine/datatypes/Color3.md) from a six- or three-character hexadecimal
format, case insensitive. A preceding hashtag (`#`) is ignored, if
present. This function interprets the given string as a typical web hex
color in the format `RRGGBB` or `RGB` (shorthand for `RRGGBB`). For
example, `#FFAA00` produces an orange color and is the same as `#FA0`.

```lua
local red = Color3.fromHex("FF0000")
local magenta = Color3.fromHex("ec008c")
local black = Color3.fromHex("000")
local white = Color3.fromHex("#FFF")
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `hex` | `string` |  | A three- or six-character hexadecimal color string, optionally prefixed with `#`. |

## Properties

### Color3.R

**Type:** `number`

The red value of the color.

### Color3.G

**Type:** `number`

The green value of the color.

### Color3.B

**Type:** `number`

The blue value of the color.

## Methods

### Color3:Lerp

**Signature:** `Color3:Lerp(color: Color3, alpha: number): Color3`

Returns a [Color3](/docs/reference/engine/datatypes/Color3.md) interpolated between two colors. The `alpha`
value should be within the range of 0 to 1.

```lua
local white = Color3.new(1, 1, 1)
local black = Color3.new(0, 0, 0)

local gray10 = white:Lerp(black, 0.1)
print(gray10)  --> 0.9, 0.9, 0.9

local gray50 = white:Lerp(black, 0.5)
print(gray50)  --> 0.5, 0.5, 0.5

local gray85 = white:Lerp(black, 0.85)
print(gray85)  --> 0.15, 0.15, 0.15
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `color` | `Color3` |  | The color to interpolate toward. |
| `alpha` | `number` |  | An interpolation value between 0 and 1, where 0 returns this color and 1 returns the target color. |

**Returns:** `Color3`

### Color3:ToHSV

**Signature:** `Color3:ToHSV(): number, number, number`

Returns the hue, saturation, and value of a [Color3](/docs/reference/engine/datatypes/Color3.md). This
function is the inverse operation of the [Color3.fromHSV()](/docs/reference/engine/datatypes/Color3.md)
constructor.

```lua
local red = Color3.fromRGB(255, 0, 0)
local green = Color3.fromRGB(0, 255, 0)

local redH, redS, redV = red:ToHSV()
print(redH, redS, redV)  --> 1 1 1

local greenH, greenS, greenV = green:ToHSV()
print(greenH, greenS, greenV)  --> 0.3333333 1 1
```

**Returns:** `number`, `number`, `number`

### Color3:ToHex

**Signature:** `Color3:ToHex(): string`

Converts the color to a six-character hexadecimal string representing the
color in the format `RRGGBB`. It is not prefixed with an octothorpe (`#`).

The returned string can be provided to [Color3.fromHex()](/docs/reference/engine/datatypes/Color3.md) to
produce the original color.

```lua
local red = Color3.fromRGB(255, 0, 0)
local magenta = Color3.fromRGB(236, 0, 140)

local redHex = red:ToHex()
print(redHex)  --> ff0000

local magentaHex = magenta:ToHex()
print(magentaHex)  --> ec008c
```

**Returns:** `string`

## Functions

### Color3.toHSV

**Signature:** `Color3.toHSV(color: Color3): number, number, number`

Returns the hue, saturation, and value of a [Color3](/docs/reference/engine/datatypes/Color3.md). This
function is the inverse operation of the [Color3.fromHSV()](/docs/reference/engine/datatypes/Color3.md)
constructor.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `color` | `Color3` |  | The Color3 to convert to HSV. |

**Returns:** `number`, `number`, `number`