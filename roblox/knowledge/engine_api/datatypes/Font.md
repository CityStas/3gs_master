---
name: Font
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Describes the font used to render text."
---

# Font

Describes the font used to render text.

**Type:** datatype

## Description

Describes the font used to render text. Every font consists of a **font
family**, a **weight** like [FontWeight.Bold](/docs/reference/engine/enums/FontWeight.md), and a **style** like
[FontStyle.Italic](/docs/reference/engine/enums/FontStyle.md).

Font families are a type of asset, like images or meshes. Each font family
contains a number of font faces, and each face has a different weight and
style.

[Font](/docs/reference/engine/datatypes/Font.md) is used by the [TextLabel.FontFace](/docs/reference/engine/classes/TextLabel.md),
[TextButton.FontFace](/docs/reference/engine/classes/TextButton.md), [TextBox.FontFace](/docs/reference/engine/classes/TextBox.md), and similar properties.
See also [Font](/docs/reference/engine/enums/Font.md) as an older alternative to this datatype that is required
by some methods and properties.

| Name | Asset ID / Weights / Appearance |
| --- | --- |
| Accanthis ADF Std | `rbxasset://fonts/families/AccanthisADFStd.json`

 |
| Amatic SC | `rbxasset://fonts/families/AmaticSC.json`

 |
| Arimo | `rbxasset://fonts/families/Arimo.json`

 |
| Balthazar | `rbxasset://fonts/families/Balthazar.json`

 |
| Bangers | `rbxasset://fonts/families/Bangers.json`

 |
| Builder Extended | `rbxasset://fonts/families/BuilderExtended.json`

 |
| Builder Mono | `rbxasset://fonts/families/BuilderMono.json`

 |
| Builder Sans | `rbxasset://fonts/families/BuilderSans.json`

 |
| Comic Neue Angular | `rbxasset://fonts/families/ComicNeueAngular.json`

 |
| Creepster | `rbxasset://fonts/families/Creepster.json`

 |
| Denk One | `rbxasset://fonts/families/DenkOne.json`

 |
| Fondamento | `rbxasset://fonts/families/Fondamento.json`

 |
| Fredoka One | `rbxasset://fonts/families/FredokaOne.json`

 |
| Grenze Gotisch | `rbxasset://fonts/families/GrenzeGotisch.json`

 |
| Guru | `rbxasset://fonts/families/Guru.json`

 |
| Highway Gothic | `rbxasset://fonts/families/HighwayGothic.json`

 |
| Inconsolata | `rbxasset://fonts/families/Inconsolata.json`

 |
| Indie Flower | `rbxasset://fonts/families/IndieFlower.json`

 |
| Josefin Sans | `rbxasset://fonts/families/JosefinSans.json`

 |
| Jura | `rbxasset://fonts/families/Jura.json`

 |
| Kalam | `rbxasset://fonts/families/Kalam.json`

 |
| Luckiest Guy | `rbxasset://fonts/families/LuckiestGuy.json`

 |
| Merriweather | `rbxasset://fonts/families/Merriweather.json`

 |
| Michroma | `rbxasset://fonts/families/Michroma.json`

 |
| Montserrat | `rbxasset://fonts/families/Montserrat.json`

 |
| Nunito | `rbxasset://fonts/families/Nunito.json`

 |
| Oswald | `rbxasset://fonts/families/Oswald.json`

 |
| Patrick Hand | `rbxasset://fonts/families/PatrickHand.json`

 |
| Permanent Marker | `rbxasset://fonts/families/PermanentMarker.json`

 |
| Press Start 2P | `rbxasset://fonts/families/PressStart2P.json`

 |
| Roboto | `rbxasset://fonts/families/Roboto.json`

 |
| Roboto Condensed | `rbxasset://fonts/families/RobotoCondensed.json`

 |
| Roboto Mono | `rbxasset://fonts/families/RobotoMono.json`

 |
| Roman Antique | `rbxasset://fonts/families/RomanAntique.json`

 |
| Sarpanch | `rbxasset://fonts/families/Sarpanch.json`

 |
| Source Sans Pro | `rbxasset://fonts/families/SourceSansPro.json`

 |
| Special Elite | `rbxasset://fonts/families/SpecialElite.json`

 |
| Titillium Web | `rbxasset://fonts/families/TitilliumWeb.json`

 |
| Ubuntu | `rbxasset://fonts/families/Ubuntu.json`

 |
| Zekton | `rbxasset://fonts/families/Zekton.json`

 |

## Constructors

### Font.new

**Signature:** `Font.new(family: Content, weight?: FontWeight, style?: FontStyle)`

Creates a new [Font](/docs/reference/engine/datatypes/Font.md).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `family` | `Content` |  | The asset ID for the font family, starting with `rbxasset://` or `rbxassetid://`. |
| `weight` | `FontWeight` | `Enum.FontWeight.Regular` | How thick the text is. |
| `style` | `FontStyle` | `Enum.FontStyle.Normal` | Whether the text is normal or italic. |

**Font.new()**

Shows how to use [Font.new()](/docs/reference/engine/datatypes/Font.md).

```lua
local label = Instance.new("TextLabel")
label.FontFace = Font.new("rbxasset://fonts/families/Roboto.json", Enum.FontWeight.Light)
```

### Font.fromEnum

**Signature:** `Font.fromEnum(font: Font)`

Creates a [Font](/docs/reference/engine/datatypes/Font.md) from an [Font](/docs/reference/engine/enums/Font.md) value. Throws an error when
called with [Font.Unknown](/docs/reference/engine/enums/Font.md).

The following table indicates how each [Font](/docs/reference/engine/enums/Font.md) value maps to a font
[Family](/docs/reference/engine/datatypes/Font.md).

| Font Enums | Equivalent Family |
| --- | --- |
| [AmaticSC](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/AmaticSC.json` |
| [Antique](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/RomanAntique.json` |
| [Arcade](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/PressStart2P.json` |
| [Arimo](/docs/reference/engine/enums/Font.md), [ArimoBold](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Arimo.json` |
| [Bangers](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Bangers.json` |
| [Bodoni](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/AccanthisADFStd.json` |
| [BuilderSans](/docs/reference/engine/enums/Font.md), [BuilderSansMedium](/docs/reference/engine/enums/Font.md), [BuilderSansBold](/docs/reference/engine/enums/Font.md), [BuilderSansExtraBold](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/BuilderSans.json` |
| [Cartoon](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/ComicNeueAngular.json` |
| [Code](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Inconsolata.json` |
| [Creepster](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Creepster.json` |
| [DenkOne](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/DenkOne.json` |
| [Fantasy](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Balthazar.json` |
| [Fondamento](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Fondamento.json` |
| [FredokaOne](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/FredokaOne.json` |
| [Garamond](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Guru.json` |
| [GrenzeGotisch](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/GrenzeGotisch.json` |
| [Highway](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/HighwayGothic.json` |
| [IndieFlower](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/IndieFlower.json` |
| [JosefinSans](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/JosefinSans.json` |
| [Jura](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Jura.json` |
| [Kalam](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Kalam.json` |
| [Legacy](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/LegacyArial.json` |
| [LuckiestGuy](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/LuckiestGuy.json` |
| [Merriweather](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Merriweather.json` |
| [Michroma](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Michroma.json` |
| [Nunito](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Nunito.json` |
| [Oswald](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Oswald.json` |
| [PatrickHand](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/PatrickHand.json` |
| [PermanentMarker](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/PermanentMarker.json` |
| [Roboto](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Roboto.json` |
| [RobotoCondensed](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/RobotoCondensed.json` |
| [RobotoMono](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/RobotoMono.json` |
| [Sarpanch](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Sarpanch.json` |
| [SciFi](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Zekton.json` |
| [SourceSans](/docs/reference/engine/enums/Font.md), [SourceSansBold](/docs/reference/engine/enums/Font.md), [SourceSansItalic](/docs/reference/engine/enums/Font.md), [SourceSansLight](/docs/reference/engine/enums/Font.md), [SourceSansSemibold](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/SourceSansPro.json` |
| [SpecialElite](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/SpecialElite.json` |
| [TitilliumWeb](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/TitilliumWeb.json` |
| [Ubuntu](/docs/reference/engine/enums/Font.md) | `rbxasset://fonts/families/Ubuntu.json` |

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `font` | `Font` |  | The enum value of the font to use. |

**Font.fromEnum()**

Shows how to use [Font.fromEnum()](/docs/reference/engine/datatypes/Font.md).

```lua
local label = Instance.new("TextLabel")
label.FontFace = Font.fromEnum(Enum.Font.SciFi)

print(label.FontFace) --> Font { Family = rbxasset://fonts/families/Zekton.json, Weight = Regular, Style = Normal }
```

### Font.fromName

**Signature:** `Font.fromName(name: string, weight?: FontWeight, style?: FontStyle)`

This is a convenience method for creating fonts from the content folder.
The name you pass in will be converted into an asset ID like
`rbxasset://fonts/families/BuilderSans.json`.

The name can only contain alphabetical characters, digits, `_`
(underscore), and `-` (hyphen). It can't contain any spaces.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The name of the font. |
| `weight` | `FontWeight` | `Enum.FontWeight.Regular` | How thick the text is. |
| `style` | `FontStyle` | `Enum.FontStyle.Normal` | Whether the text is normal or italic. |

**Font.fromName()**

Shows how to use [Font.fromName()](/docs/reference/engine/datatypes/Font.md).

```lua
local label = Instance.new("TextLabel")
label.FontFace = Font.fromName("FredokaOne")

print(label.FontFace) --> Font { Family = rbxasset://fonts/families/FredokaOne.json, Weight = Regular, Style = Normal }
```

### Font.fromId

**Signature:** `Font.fromId(id: number, weight?: FontWeight, style?: FontStyle)`

This is a convenience method for creating fonts from an asset ID number.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `id` | `number` |  | The asset ID of the font as a number. |
| `weight` | `FontWeight` | `Enum.FontWeight.Regular` | How thick the text is. |
| `style` | `FontStyle` | `Enum.FontStyle.Normal` | Whether the text is normal or italic. |

**Font.fromId()**

Shows how to use [Font.fromId()](/docs/reference/engine/datatypes/Font.md).

```lua
local label = Instance.new("TextLabel")
label.FontFace = Font.fromId(8836875837)

print(label.FontFace) --> Font { Family = rbxassetid://8836875837, Weight = Regular, Style = Normal }
```

## Properties

### Font.Family

**Type:** `Content`

The asset ID for the font family. These start with either `rbxasset://` or
`rbxassetid://`.

### Font.Weight

**Type:** `FontWeight`

How thick the text is. The default value is [FontWeight.Regular](/docs/reference/engine/enums/FontWeight.md).

When set, [Font.Bold](/docs/reference/engine/datatypes/Font.md) is updated and becomes `true` if the weight
is [FontWeight.SemiBold](/docs/reference/engine/enums/FontWeight.md) or thicker.

### Font.Style

**Type:** `FontStyle`

Whether the font is italic. The default value is [FontStyle.Normal](/docs/reference/engine/enums/FontStyle.md).

### Font.Bold

**Type:** `bool`

Whether the font is bold. Sets [Font.Weight](/docs/reference/engine/datatypes/Font.md) to
[FontWeight.Bold](/docs/reference/engine/enums/FontWeight.md) when `true`, or to [FontWeight.Regular](/docs/reference/engine/enums/FontWeight.md)
otherwise.