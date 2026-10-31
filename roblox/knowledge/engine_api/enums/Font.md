---
name: Font
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the font used to render text in GUI objects such as Class.TextLabel, Class.TextButton, and Class.TextBox. This is a legacy property. For new work, use Font, FontFace, and FontFace instead."
---

# Font

Determines the font used to render text in GUI objects such as
Class.TextLabel, Class.TextButton, and Class.TextBox. This is a legacy
property. For new work, use [Font](/docs/reference/engine/datatypes/Font.md),
[FontFace](/docs/reference/engine/classes/TextLabel.md), and [FontFace](/docs/reference/engine/classes/TextButton.md)
instead.

**Type:** enum

## Description

The `Font` enum is used in [TextBox](/docs/reference/engine/classes/TextBox.md), [TextLabel](/docs/reference/engine/classes/TextLabel.md),
[TextButton](/docs/reference/engine/classes/TextButton.md), and similar GUI objects to determine how the element will
render its text.

See also [Font](/docs/reference/engine/datatypes/Font.md) as a newer alternative to this enum which
encapsulates fonts as a datatype and provides access to more fonts than this
enum allows.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Legacy` | 0 |  |
| `Arial` | 1 | `Arial` has been removed. Using it will map to the `Arimo` font family of the [Font](/docs/reference/engine/datatypes/Font.md) data type. |
| `ArialBold` | 2 | `ArialBold` has been removed. Using it will map to the `Arimo` font family of the [Font](/docs/reference/engine/datatypes/Font.md) data type. |
| `SourceSans` | 3 |  |
| `SourceSansBold` | 4 |  |
| `SourceSansLight` | 5 |  |
| `SourceSansItalic` | 6 |  |
| `Bodoni` | 7 |  |
| `Garamond` | 8 |  |
| `Cartoon` | 9 |  |
| `Code` | 10 |  |
| `Highway` | 11 |  |
| `SciFi` | 12 |  |
| `Arcade` | 13 |  |
| `Fantasy` | 14 |  |
| `Antique` | 15 |  |
| `SourceSansSemibold` | 16 |  |
| `Gotham` | 17 | `Gotham` has been removed. Using it will map to the `Montserrat` font family of the [Font](/docs/reference/engine/datatypes/Font.md) data type. |
| `GothamMedium` | 18 | `GothamMedium` has been removed. Using it will map to the `Montserrat` font family of the [Font](/docs/reference/engine/datatypes/Font.md) data type. |
| `GothamBold` | 19 | `GothamBold` has been removed. Using it will map to the `Montserrat` font family of the [Font](/docs/reference/engine/datatypes/Font.md) data type. |
| `GothamBlack` | 20 | `GothamBlack` has been removed. Using it will map to the `Montserrat` font family of the [Font](/docs/reference/engine/datatypes/Font.md) data type. |
| `AmaticSC` | 21 |  |
| `Bangers` | 22 |  |
| `Creepster` | 23 |  |
| `DenkOne` | 24 |  |
| `Fondamento` | 25 |  |
| `FredokaOne` | 26 |  |
| `GrenzeGotisch` | 27 |  |
| `IndieFlower` | 28 |  |
| `JosefinSans` | 29 |  |
| `Jura` | 30 |  |
| `Kalam` | 31 |  |
| `LuckiestGuy` | 32 |  |
| `Merriweather` | 33 |  |
| `Michroma` | 34 |  |
| `Nunito` | 35 |  |
| `Oswald` | 36 |  |
| `PatrickHand` | 37 |  |
| `PermanentMarker` | 38 |  |
| `Roboto` | 39 |  |
| `RobotoCondensed` | 40 |  |
| `RobotoMono` | 41 |  |
| `Sarpanch` | 42 |  |
| `SpecialElite` | 43 |  |
| `TitilliumWeb` | 44 |  |
| `Ubuntu` | 45 |  |
| `BuilderSans` | 46 | See [Builder Font License](/docs/en-us/resources/builder-font-license.md). |
| `BuilderSansMedium` | 47 | See [Builder Font License](/docs/en-us/resources/builder-font-license.md). |
| `BuilderSansBold` | 48 | See [Builder Font License](/docs/en-us/resources/builder-font-license.md). |
| `BuilderSansExtraBold` | 49 | See [Builder Font License](/docs/en-us/resources/builder-font-license.md). |
| `Arimo` | 50 |  |
| `ArimoBold` | 51 |  |
| `Unknown` | 100 | Set when the GUI object's font face is set to a [Font](/docs/reference/engine/datatypes/Font.md) that has no corresponding enum value. |