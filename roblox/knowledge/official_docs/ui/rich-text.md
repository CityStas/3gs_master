---
title: "Rich text markup"
url: /docs/en-us/ui/rich-text
last_updated: 2026-10-30T19:56:02Z
description: "Rich Text Markup are simple markup tags to style sections of a string."
---

# Rich text markup

UI **rich text** utilizes simple markup tags to style sections of a string in bold, italics, underline, fill color, stroke variations, and more. You can apply styling tags to `Class.TextLabel`, `Class.TextButton`, and `Class.TextBox` objects.

## Enable rich text

You must enable rich text on a per-object basis through its **RichText** property in the [Properties](/docs/en-us/studio/properties.md) window, or by setting the property to `true` in a `Class.LocalScript`.

```lua
local title = Instance.new("TextLabel")
title.RichText = true

title.Text = "Use a <b>bold title</b>"
```

> **Info:** When editing an object's **Text** property in Studio, toggling the **RichText** checkbox in the [Properties](/docs/en-us/studio/properties.md) window displays the text string as a final render. This is useful for identifying and correcting mistakes in any [supported tags](#supported-tags).
> **Warning:**[Localizing](/docs/en-us/production/localization.md) a game to support other languages removes rich text formatting tags. To ensure formatting appears in other languages, re-apply the tags manually to your localized strings.
## Supported tags

Rich text tags are similar to XML/HTML tags and you must include both an opening and closing tag around the formatted text.

`<b>Formatted text</b>`

You can also nest tags inside each other as long as you close them in the reverse order of how you opened them.

`<b><i><u>Formatted text</u></i></b>`

### Font color

`<font color=""> </font>`

> `I want the <font color="#FF7800">orange</font> candy.` `I want the <font color="rgb(255,125,0)">orange</font> candy.`
### Font size

`<font size=""> </font>`

> `<font size="40">This is big.</font> <font size="20">This is small.</font>`
### Font face

`<font face=""> </font>`

> `<font face="Michroma">This is Michroma face.</font>`
> **Info:** Font face/family names are listed on the `Datatype.Font` enum reference page.
### Font family

`<font family=""> </font>`

> `<font family="rbxasset://fonts/families/Michroma.json">This is Michroma face.</font>`
> **Info:** Font face/family names are listed on the `Datatype.Font` enum reference page.
### Font weight

`<font weight=""> </font>`

> `This is normal. <font weight="heavy">This is heavy.</font>` `This is normal. <font weight="900">This is heavy.</font>`
> **Info:** Font weight can be a case-insensitive string name including `Thin`, `ExtraLight`, `Light`, `Regular`, `Medium`, `SemiBold`, `Bold`, `ExtraBold`, or `Heavy`; it can also be a number in factors of 100 between `100` and `900`.
### Font transparency

`<font transparency=""> </font>`

> `Text at <font transparency="0.5">50% transparency</font>.`
### Stroke

`<stroke> </stroke>`

| Parameter | Equivalent Property | Example Values |
| --- | --- | --- |
| `color` | `Class.UIStroke.Color` | `"rgb(255,125,0)"`, `"#FF7800"` |
| `thickness` or `th` | `Class.UIStroke.Thickness` | `"1"`, `"4"`, `"0.5"` |
| `transparency` or `tr` | `Class.UIStroke.Transparency` | `"0"`, `"0.5"`, `"1"` |
| `joins` | `Class.UIStroke.LineJoinMode` | `"round"`, `"bevel"`, `"miter"` |
| `sizing` | `Class.UIStroke.StrokeSizingMode` | `"fixed"`, `"scaled"` |

> `You won <stroke color="#00A2FF" thickness="2" transparency="0.25" joins="miter">25 gems</stroke>.`
> **Info:** See [UI appearance modifiers](/docs/en-us/ui/appearance-modifiers.md#stroke) for details on `<stroke>` tag parameters such as `thickness` and `joins`.
### Bold

`<b> </b>`

> `Text in <b>bold</b>.`
### Italic

`<i> </i>`

> `Text <i>italicized</i>.`
### Underline

`<u> </u>`

> `Text <u>underlined</u>.`
### Strikethrough

`<s> </s>`

> `Text with <s>strikethrough</s> applied.`
### Line break

`<br/>`

> `New line occurs after this sentence.<br/>Next sentence...`
### Uppercase

`<uppercase> </uppercase>``<uc> </uc>`

> `<uppercase>Uppercase</uppercase> makes words read loudly!` `<uc>Uppercase</uc> makes words read loudly!`
### Small caps

`<smallcaps> </smallcaps>``<sc> </sc>`

> `My name is <smallcaps>Diva Dragonslayer</smallcaps>.` `My name is <sc>Diva Dragonslayer</sc>.`
### Mark

`<mark> </mark>`

> `Text <mark color="#009966" transparency="0">highlighted</mark>.`
### Comment

`<!-- -->`

> `After this is a comment...<!--This does not appear in the final text--> and now more text...`
## Escape forms

If you want to render certain characters like `<` or `>` and exempt them from consideration as part of rich text tags, you can write them in their **escape form**.

| Character | Escape | Example | Result |
| --- | --- | --- | --- |
| `<` | `&lt;` | `10 &lt; 100` | 10 < 100 |
| `>` | `&gt;` | `100 &gt; 10` | 100 > 10 |
| `"` | `&quot;` | `Meet &quot;Diva Dragonslayer&quot;` | Meet "Diva Dragonslayer" |
| `'` | `&apos;` | `Diva&apos;s pet is a falcon!` | Diva's pet is a falcon! |
| `&` | `&amp;` | `Render another escape form <b>&amp;lt;</b> by escaping an ampersand` | Render another escape form **&lt;** by escaping an ampersand |
