---
name: BrickColor
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A data type that provides a predefined list of named colors."
---

# BrickColor

A data type that provides a predefined list of named colors.

**Type:** datatype

## Description

The [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) data type provides a predefined list of named
colors, not to be confused with [Color3](/docs/reference/engine/datatypes/Color3.md), a more general data type
that describes RGB colors. The following code shows how to use
[BrickColor.new()](/docs/reference/engine/datatypes/BrickColor.md) to declare the [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) property of a
[Part](/docs/reference/engine/classes/Part.md).

```lua
local part = Instance.new("Part")

-- By color name
part.BrickColor = BrickColor.new("Pastel Blue")
print(part.BrickColor) --> Pastel Blue

-- By numerical index
part.BrickColor = BrickColor.new(11)
print(part.BrickColor) --> Pastel Blue

-- By RGB decimal values in range of 0-1
part.BrickColor = BrickColor.new(0.502, 0.734, 0.859)
print(part.BrickColor) --> Pastel Blue

-- By palette index
part.BrickColor = BrickColor.palette(70)
print(part.BrickColor) --> Gold
```

The following table is the list of available brick colors.

| Color | Name | Number | Palette Index | RGB Value (0‑255) | RGB Value (0‑1) |
| --- | --- | --- | --- | --- | --- |
|  | White | `1` | `87` | `242, 243, 243` | `0.950, 0.953, 0.953` |
|  | Grey | `2` |  | `161, 165, 162` | `0.632, 0.648, 0.636` |
|  | Light yellow | `3` |  | `249, 233, 153` | `0.977, 0.914, 0.600` |
|  | Brick yellow | `5` | `109` | `215, 197, 154` | `0.844, 0.773, 0.604` |
|  | Light green (Mint) | `6` |  | `194, 218, 184` | `0.761, 0.855, 0.722` |
|  | Light reddish violet | `9` | `88` | `232, 186, 200` | `0.910, 0.730, 0.785` |
|  | Pastel Blue | `11` | `51` | `128, 187, 219` | `0.502, 0.734, 0.859` |
|  | Light orange brown | `12` |  | `203, 132, 66` | `0.797, 0.518, 0.259` |
|  | Nougat | `18` | `110` | `204, 142, 105` | `0.800, 0.557, 0.412` |
|  | Bright red | `21` | `68` | `196, 40, 28` | `0.769, 0.157, 0.110` |
|  | Med. reddish violet | `22` |  | `196, 112, 160` | `0.769, 0.440, 0.628` |
|  | Bright blue | `23` | `21` | `13, 105, 172` | `0.051, 0.412, 0.675` |
|  | Bright yellow | `24` | `71` | `245, 205, 48` | `0.961, 0.804, 0.189` |
|  | Earth orange | `25` |  | `98, 71, 50` | `0.385, 0.279, 0.197` |
|  | Black | `26` | `3` | `27, 42, 53` | `0.106, 0.165, 0.208` |
|  | Dark grey | `27` |  | `109, 110, 108` | `0.428, 0.432, 0.424` |
|  | Dark green | `28` | `8` | `40, 127, 71` | `0.157, 0.499, 0.279` |
|  | Medium green | `29` | `59` | `161, 196, 140` | `0.632, 0.769, 0.550` |
|  | Lig. Yellowich orange | `36` |  | `243, 207, 155` | `0.953, 0.812, 0.608` |
|  | Bright green | `37` | `25` | `75, 151, 75` | `0.295, 0.593, 0.295` |
|  | Dark orange | `38` | `119` | `160, 95, 53` | `0.628, 0.373, 0.208` |
|  | Light bluish violet | `39` |  | `193, 202, 222` | `0.757, 0.793, 0.871` |
|  | Transparent | `40` |  | `236, 236, 236` | `0.926, 0.926, 0.926` |
|  | Tr. Red | `41` |  | `205, 84, 75` | `0.804, 0.330, 0.295` |
|  | Tr. Lg blue | `42` |  | `193, 223, 240` | `0.757, 0.875, 0.942` |
|  | Tr. Blue | `43` |  | `123, 182, 232` | `0.483, 0.714, 0.910` |
|  | Tr. Yellow | `44` |  | `247, 241, 141` | `0.969, 0.946, 0.553` |
|  | Light blue | `45` | `63` | `180, 210, 228` | `0.706, 0.824, 0.895` |
|  | Tr. Flu. Reddish orange | `47` |  | `217, 133, 108` | `0.851, 0.522, 0.424` |
|  | Tr. Green | `48` |  | `132, 182, 141` | `0.518, 0.714, 0.553` |
|  | Tr. Flu. Green | `49` |  | `248, 241, 132` | `0.973, 0.946, 0.518` |
|  | Phosph. White | `50` |  | `236, 232, 222` | `0.926, 0.910, 0.871` |
|  | Light red | `100` |  | `238, 196, 182` | `0.934, 0.769, 0.714` |
|  | Medium red | `101` | `101` | `218, 134, 122` | `0.855, 0.526, 0.479` |
|  | Medium blue | `102` | `20` | `110, 153, 202` | `0.432, 0.600, 0.793` |
|  | Light grey | `103` |  | `199, 193, 183` | `0.781, 0.757, 0.718` |
|  | Bright violet | `104` | `44` | `107, 50, 124` | `0.420, 0.197, 0.487` |
|  | Br. yellowish orange | `105` | `94` | `226, 155, 64` | `0.887, 0.608, 0.251` |
|  | Bright orange | `106` | `83` | `218, 133, 65` | `0.855, 0.522, 0.255` |
|  | Bright bluish green | `107` | `2` | `0, 143, 156` | `0.000, 0.561, 0.612` |
|  | Earth yellow | `108` |  | `104, 92, 67` | `0.408, 0.361, 0.263` |
|  | Bright bluish violet | `110` |  | `67, 84, 147` | `0.263, 0.330, 0.577` |
|  | Tr. Brown | `111` |  | `191, 183, 177` | `0.750, 0.718, 0.695` |
|  | Medium bluish violet | `112` |  | `104, 116, 172` | `0.408, 0.455, 0.675` |
|  | Tr. Medi. reddish violet | `113` |  | `229, 173, 200` | `0.899, 0.679, 0.785` |
|  | Med. yellowish green | `115` |  | `199, 210, 60` | `0.781, 0.824, 0.236` |
|  | Med. bluish green | `116` |  | `85, 165, 175` | `0.334, 0.648, 0.687` |
|  | Light bluish green | `118` |  | `183, 215, 213` | `0.718, 0.844, 0.836` |
|  | Br. yellowish green | `119` | `46` | `164, 189, 71` | `0.644, 0.742, 0.279` |
|  | Lig. yellowish green | `120` |  | `217, 228, 167` | `0.851, 0.895, 0.655` |
|  | Med. yellowish orange | `121` |  | `231, 172, 88` | `0.906, 0.675, 0.346` |
|  | Br. reddish orange | `123` |  | `211, 111, 76` | `0.828, 0.436, 0.299` |
|  | Bright reddish violet | `124` |  | `146, 57, 120` | `0.573, 0.224, 0.471` |
|  | Light orange | `125` | `100` | `234, 184, 146` | `0.918, 0.722, 0.573` |
|  | Tr. Bright bluish violet | `126` |  | `165, 165, 203` | `0.648, 0.648, 0.797` |
|  | Gold | `127` |  | `220, 188, 129` | `0.863, 0.738, 0.506` |
|  | Dark nougat | `128` |  | `174, 122, 89` | `0.683, 0.479, 0.350` |
|  | Silver | `131` |  | `156, 163, 168` | `0.612, 0.640, 0.659` |
|  | Neon orange | `133` | `82` | `213, 115, 61` | `0.836, 0.451, 0.240` |
|  | Neon green | `134` |  | `216, 221, 86` | `0.848, 0.867, 0.338` |
|  | Sand blue | `135` | `19` | `116, 134, 157` | `0.455, 0.526, 0.616` |
|  | Sand violet | `136` |  | `135, 124, 144` | `0.530, 0.487, 0.565` |
|  | Medium orange | `137` |  | `224, 152, 100` | `0.879, 0.597, 0.393` |
|  | Sand yellow | `138` |  | `149, 138, 115` | `0.585, 0.542, 0.451` |
|  | Earth blue | `140` |  | `32, 58, 86` | `0.126, 0.228, 0.338` |
|  | Earth green | `141` | `0` | `39, 70, 45` | `0.153, 0.275, 0.177` |
|  | Tr. Flu. Blue | `143` |  | `207, 226, 247` | `0.812, 0.887, 0.969` |
|  | Sand blue metallic | `145` |  | `121, 136, 161` | `0.475, 0.534, 0.632` |
|  | Sand violet metallic | `146` |  | `149, 142, 163` | `0.585, 0.557, 0.640` |
|  | Sand yellow metallic | `147` |  | `147, 135, 103` | `0.577, 0.530, 0.404` |
|  | Dark grey metallic | `148` |  | `87, 88, 87` | `0.342, 0.346, 0.342` |
|  | Black metallic | `149` |  | `22, 29, 50` | `0.087, 0.114, 0.197` |
|  | Light grey metallic | `150` |  | `171, 173, 172` | `0.671, 0.679, 0.675` |
|  | Sand green | `151` | `34` | `120, 144, 130` | `0.471, 0.565, 0.510` |
|  | Sand red | `153` | `114` | `149, 121, 119` | `0.585, 0.475, 0.467` |
|  | Dark red | `154` |  | `123, 46, 47` | `0.483, 0.181, 0.185` |
|  | Tr. Flu. Yellow | `157` |  | `255, 246, 123` | `1.000, 0.965, 0.483` |
|  | Tr. Flu. Red | `158` |  | `225, 164, 194` | `0.883, 0.644, 0.761` |
|  | Gun metallic | `168` |  | `117, 108, 98` | `0.459, 0.424, 0.385` |
|  | Red flip/flop | `176` |  | `151, 105, 91` | `0.593, 0.412, 0.357` |
|  | Yellow flip/flop | `178` |  | `180, 132, 85` | `0.706, 0.518, 0.334` |
|  | Silver flip/flop | `179` |  | `137, 135, 136` | `0.538, 0.530, 0.534` |
|  | Curry | `180` |  | `215, 169, 75` | `0.844, 0.663, 0.295` |
|  | Fire Yellow | `190` |  | `249, 214, 46` | `0.977, 0.840, 0.181` |
|  | Flame yellowish orange | `191` |  | `232, 171, 45` | `0.910, 0.671, 0.177` |
|  | Reddish brown | `192` | `103` | `105, 64, 40` | `0.412, 0.251, 0.157` |
|  | Flame reddish orange | `193` |  | `207, 96, 36` | `0.812, 0.377, 0.142` |
|  | Medium stone grey | `194` | `123` | `163, 162, 165` | `0.640, 0.636, 0.648` |
|  | Royal blue | `195` |  | `70, 103, 164` | `0.275, 0.404, 0.644` |
|  | Dark Royal blue | `196` |  | `35, 71, 139` | `0.138, 0.279, 0.546` |
|  | Bright reddish lilac | `198` |  | `142, 66, 133` | `0.557, 0.259, 0.522` |
|  | Dark stone grey | `199` | `122` | `99, 95, 98` | `0.389, 0.373, 0.385` |
|  | Lemon metalic | `200` |  | `130, 138, 93` | `0.510, 0.542, 0.365` |
|  | Light stone grey | `208` | `62` | `229, 228, 223` | `0.899, 0.895, 0.875` |
|  | Dark Curry | `209` |  | `176, 142, 68` | `0.691, 0.557, 0.267` |
|  | Faded green | `210` |  | `112, 149, 120` | `0.440, 0.585, 0.471` |
|  | Turquoise | `211` |  | `121, 181, 181` | `0.475, 0.710, 0.710` |
|  | Light Royal blue | `212` |  | `159, 195, 233` | `0.624, 0.765, 0.914` |
|  | Medium Royal blue | `213` |  | `108, 129, 183` | `0.424, 0.506, 0.718` |
|  | Rust | `216` |  | `144, 76, 42` | `0.565, 0.299, 0.165` |
|  | Brown | `217` | `111` | `124, 92, 70` | `0.487, 0.361, 0.275` |
|  | Reddish lilac | `218` |  | `150, 112, 159` | `0.589, 0.440, 0.624` |
|  | Lilac | `219` |  | `107, 98, 155` | `0.420, 0.385, 0.608` |
|  | Light lilac | `220` |  | `167, 169, 206` | `0.655, 0.663, 0.808` |
|  | Bright purple | `221` |  | `205, 98, 152` | `0.804, 0.385, 0.597` |
|  | Light purple | `222` |  | `228, 173, 200` | `0.895, 0.679, 0.785` |
|  | Light pink | `223` |  | `220, 144, 149` | `0.863, 0.565, 0.585` |
|  | Light brick yellow | `224` |  | `240, 213, 160` | `0.942, 0.836, 0.628` |
|  | Warm yellowish orange | `225` |  | `235, 184, 127` | `0.922, 0.722, 0.499` |
|  | Cool yellow | `226` | `73` | `253, 234, 141` | `0.993, 0.918, 0.553` |
|  | Dove blue | `232` |  | `125, 187, 221` | `0.491, 0.734, 0.867` |
|  | Medium lilac | `268` |  | `52, 43, 117` | `0.204, 0.169, 0.459` |
|  | Slime green | `301` | `1` | `80, 109, 84` | `0.314, 0.428, 0.330` |
|  | Smoky grey | `302` | `10` | `91, 93, 105` | `0.357, 0.365, 0.412` |
|  | Dark blue | `303` | `5` | `0, 16, 176` | `0.000, 0.063, 0.691` |
|  | Parsley green | `304` | `7` | `44, 101, 29` | `0.173, 0.397, 0.114` |
|  | Steel blue | `305` | `11` | `82, 124, 174` | `0.322, 0.487, 0.683` |
|  | Storm blue | `306` | `12` | `51, 88, 130` | `0.200, 0.346, 0.510` |
|  | Lapis | `307` | `13` | `16, 42, 220` | `0.063, 0.165, 0.863` |
|  | Dark indigo | `308` | `14` | `61, 21, 133` | `0.240, 0.083, 0.522` |
|  | Sea green | `309` | `16` | `52, 142, 64` | `0.204, 0.557, 0.251` |
|  | Shamrock | `310` | `17` | `91, 154, 76` | `0.357, 0.604, 0.299` |
|  | Fossil | `311` | `29` | `159, 161, 172` | `0.624, 0.632, 0.675` |
|  | Mulberry | `312` | `23` | `89, 34, 89` | `0.350, 0.134, 0.350` |
|  | Forest green | `313` | `24` | `31, 128, 29` | `0.122, 0.502, 0.114` |
|  | Cadet blue | `314` | `39` | `159, 173, 192` | `0.624, 0.679, 0.753` |
|  | Electric blue | `315` | `30` | `9, 137, 207` | `0.036, 0.538, 0.812` |
|  | Eggplant | `316` | `33` | `123, 0, 123` | `0.483, 0.000, 0.483` |
|  | Moss | `317` | `35` | `124, 156, 107` | `0.487, 0.612, 0.420` |
|  | Artichoke | `318` | `36` | `138, 171, 133` | `0.542, 0.671, 0.522` |
|  | Sage green | `319` | `37` | `185, 196, 177` | `0.726, 0.769, 0.695` |
|  | Ghost grey | `320` | `50` | `202, 203, 209` | `0.793, 0.797, 0.820` |
|  | Lilac | `321` | `42` | `167, 94, 155` | `0.655, 0.369, 0.608` |
|  | Plum | `322` | `43` | `123, 47, 123` | `0.483, 0.185, 0.483` |
|  | Olivine | `323` | `47` | `148, 190, 129` | `0.581, 0.746, 0.506` |
|  | Laurel green | `324` | `48` | `168, 189, 153` | `0.659, 0.742, 0.600` |
|  | Quill grey | `325` | `49` | `223, 223, 222` | `0.875, 0.875, 0.871` |
|  | Crimson | `327` | `56` | `151, 0, 0` | `0.593, 0.000, 0.000` |
|  | Mint | `328` | `60` | `177, 229, 166` | `0.695, 0.899, 0.651` |
|  | Baby blue | `329` | `64` | `152, 194, 219` | `0.597, 0.761, 0.859` |
|  | Carnation pink | `330` | `65` | `255, 152, 220` | `1.000, 0.597, 0.863` |
|  | Persimmon | `331` | `66` | `255, 89, 89` | `1.000, 0.350, 0.350` |
|  | Maroon | `332` | `69` | `117, 0, 0` | `0.459, 0.000, 0.000` |
|  | Gold | `333` | `70` | `239, 184, 56` | `0.938, 0.722, 0.220` |
|  | Daisy orange | `334` | `72` | `248, 217, 109` | `0.973, 0.851, 0.428` |
|  | Pearl | `335` | `75` | `231, 231, 236` | `0.906, 0.906, 0.926` |
|  | Fog | `336` | `76` | `199, 212, 228` | `0.781, 0.832, 0.895` |
|  | Salmon | `337` | `90` | `255, 148, 148` | `1.000, 0.581, 0.581` |
|  | Terra Cotta | `338` | `79` | `190, 104, 98` | `0.746, 0.408, 0.385` |
|  | Cocoa | `339` | `81` | `86, 36, 36` | `0.338, 0.142, 0.142` |
|  | Wheat | `340` | `84` | `241, 231, 199` | `0.946, 0.906, 0.781` |
|  | Buttermilk | `341` | `85` | `254, 243, 187` | `0.997, 0.953, 0.734` |
|  | Mauve | `342` | `77` | `224, 178, 208` | `0.879, 0.699, 0.816` |
|  | Sunrise | `343` | `78` | `212, 144, 189` | `0.832, 0.565, 0.742` |
|  | Tawny | `344` | `91` | `150, 85, 85` | `0.589, 0.334, 0.334` |
|  | Rust | `345` | `92` | `143, 76, 42` | `0.561, 0.299, 0.165` |
|  | Cashmere | `346` | `95` | `211, 190, 150` | `0.828, 0.746, 0.589` |
|  | Khaki | `347` | `96` | `226, 220, 188` | `0.887, 0.863, 0.738` |
|  | Lily white | `348` | `97` | `237, 234, 234` | `0.930, 0.918, 0.918` |
|  | Seashell | `349` | `98` | `233, 218, 218` | `0.914, 0.855, 0.855` |
|  | Burgundy | `350` | `102` | `136, 62, 62` | `0.534, 0.244, 0.244` |
|  | Cork | `351` | `104` | `188, 155, 93` | `0.738, 0.608, 0.365` |
|  | Burlap | `352` | `105` | `199, 172, 120` | `0.781, 0.675, 0.471` |
|  | Beige | `353` | `106` | `202, 191, 163` | `0.793, 0.750, 0.640` |
|  | Oyster | `354` | `107` | `187, 179, 178` | `0.734, 0.702, 0.699` |
|  | Pine Cone | `355` | `112` | `108, 88, 75` | `0.424, 0.346, 0.295` |
|  | Fawn brown | `356` | `113` | `160, 132, 79` | `0.628, 0.518, 0.310` |
|  | Hurricane grey | `357` | `115` | `149, 137, 136` | `0.585, 0.538, 0.534` |
|  | Cloudy grey | `358` | `116` | `171, 168, 158` | `0.671, 0.659, 0.620` |
|  | Linen | `359` | `117` | `175, 148, 131` | `0.687, 0.581, 0.514` |
|  | Copper | `360` | `118` | `150, 103, 102` | `0.589, 0.404, 0.400` |
|  | Medium brown | `361` | `120` | `86, 66, 54` | `0.338, 0.259, 0.212` |
|  | Bronze | `362` | `121` | `126, 104, 63` | `0.495, 0.408, 0.248` |
|  | Flint | `363` | `124` | `105, 102, 92` | `0.412, 0.400, 0.361` |
|  | Dark taupe | `364` | `125` | `90, 76, 66` | `0.353, 0.299, 0.259` |
|  | Burnt Sienna | `365` | `126` | `106, 57, 9` | `0.416, 0.224, 0.036` |
|  | Institutional white | `1001` | `86` | `248, 248, 248` | `0.973, 0.973, 0.973` |
|  | Mid gray | `1002` | `108` | `205, 205, 205` | `0.804, 0.804, 0.804` |
|  | Really black | `1003` | `127` | `17, 17, 17` | `0.067, 0.067, 0.067` |
|  | Really red | `1004` | `67` | `255, 0, 0` | `1.000, 0.000, 0.000` |
|  | Deep orange | `1005` | `57` | `255, 176, 0` | `1.000, 0.691, 0.000` |
|  | Alder | `1006` | `41` | `180, 128, 255` | `0.706, 0.502, 1.000` |
|  | Dusty Rose | `1007` | `80` | `163, 75, 75` | `0.640, 0.295, 0.295` |
|  | Olive | `1008` | `45` | `193, 190, 66` | `0.757, 0.746, 0.259` |
|  | New Yeller | `1009` | `58` | `255, 255, 0` | `1.000, 1.000, 0.000` |
|  | Really blue | `1010` | `22` | `0, 0, 255` | `0.000, 0.000, 1.000` |
|  | Navy blue | `1011` | `6` | `0, 32, 96` | `0.000, 0.126, 0.377` |
|  | Deep blue | `1012` | `4` | `33, 84, 185` | `0.130, 0.330, 0.726` |
|  | Cyan | `1013` | `40` | `4, 175, 236` | `0.016, 0.687, 0.926` |
|  | CGA brown | `1014` | `93` | `170, 85, 0` | `0.667, 0.334, 0.000` |
|  | Magenta | `1015` | `55` | `170, 0, 170` | `0.667, 0.000, 0.667` |
|  | Pink | `1016` | `53` | `255, 102, 204` | `1.000, 0.400, 0.800` |
|  | Deep orange | `1017` |  | `255, 175, 0` | `1.000, 0.687, 0.000` |
|  | Teal | `1018` | `9` | `18, 238, 212` | `0.071, 0.934, 0.832` |
|  | Toothpaste | `1019` | `18` | `0, 255, 255` | `0.000, 1.000, 1.000` |
|  | Lime green | `1020` | `27` | `0, 255, 0` | `0.000, 1.000, 0.000` |
|  | Camo | `1021` | `15` | `58, 125, 21` | `0.228, 0.491, 0.083` |
|  | Grime | `1022` | `26` | `127, 142, 100` | `0.499, 0.557, 0.393` |
|  | Lavender | `1023` | `31` | `140, 91, 159` | `0.550, 0.357, 0.624` |
|  | Pastel light blue | `1024` | `38` | `175, 221, 255` | `0.687, 0.867, 1.000` |
|  | Pastel orange | `1025` | `89` | `255, 201, 201` | `1.000, 0.789, 0.789` |
|  | Pastel violet | `1026` | `52` | `177, 167, 255` | `0.695, 0.655, 1.000` |
|  | Pastel blue-green | `1027` | `28` | `159, 243, 233` | `0.624, 0.953, 0.914` |
|  | Pastel green | `1028` | `61` | `204, 255, 204` | `0.800, 1.000, 0.800` |
|  | Pastel yellow | `1029` | `74` | `255, 255, 204` | `1.000, 1.000, 0.800` |
|  | Pastel brown | `1030` | `99` | `255, 204, 153` | `1.000, 0.800, 0.600` |
|  | Royal purple | `1031` | `32` | `98, 37, 209` | `0.385, 0.146, 0.820` |
|  | Hot pink | `1032` | `54` | `255, 0, 191` | `1.000, 0.000, 0.750` |

## Constructors

### BrickColor.new

**Signature:** `BrickColor.new(val: number)`

Constructs a [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) from its numerical index (**Number** in
color reference table). If the provided number does not correspond to a
valid [BrickColor](/docs/reference/engine/datatypes/BrickColor.md), the constructor returns the default "Medium
stone grey".

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `val` | `number` |  | The unique numerical index that identifies a brick color. |

### BrickColor.new

**Signature:** `BrickColor.new(r: number, g: number, b: number)`

Constructs the closest [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) that can be matched to the
specified RGB components, each between `0` and `1`. The match is
determined by finding the [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) whose color has the
smallest total distance (sum of absolute differences per channel) from the
given values across all known brick colors.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `r` | `number` |  | The red component of the desired color, between `0` and `1`. |
| `g` | `number` |  | The green component of the desired color, between `0` and `1`. |
| `b` | `number` |  | The blue component of the desired color, between `0` and `1`. |

### BrickColor.new

**Signature:** `BrickColor.new(name: string)`

Constructs a [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) from its name, for example
`"Pastel Blue"`. The name must match one of the entries in the color table
exactly. If the name does not match a known [BrickColor](/docs/reference/engine/datatypes/BrickColor.md), the
constructor returns the default "Medium stone grey".

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The exact name of the brick color as listed in the color table. |

### BrickColor.new

**Signature:** `BrickColor.new(color: Color3)`

Constructs the closest [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) that can be matched to the
specified [Color3](/docs/reference/engine/datatypes/Color3.md). The match uses the same closest-color
algorithm as [BrickColor.new(r, g, b)](/docs/reference/engine/datatypes/BrickColor.md), comparing the
[Color3](/docs/reference/engine/datatypes/Color3.md) against every known brick color and returning the one
with the smallest total channel distance.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `color` | `Color3` |  | The [Color3](/docs/reference/engine/datatypes/Color3.md) to match against all known brick colors. |

### BrickColor.palette

**Signature:** `BrickColor.palette(paletteValue: number)`

Constructs a [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) from its zero-based 128-color palette
index (**Palette Index** in color reference table). This is the same
palette shown in the Studio color picker. An error is thrown if the index
is out of bounds.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `paletteValue` | `number` |  | A zero-based index into the 128-color palette (`0` through `127`). |

### BrickColor.random

**Signature:** `BrickColor.random()`

Returns a random [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) selected from the 128-color
palette. Each call may return a different color.

### BrickColor.White

**Signature:** `BrickColor.White()`

Returns the "White" [BrickColor](/docs/reference/engine/datatypes/BrickColor.md).

### BrickColor.Gray

**Signature:** `BrickColor.Gray()`

Returns the "Medium stone grey" [BrickColor](/docs/reference/engine/datatypes/BrickColor.md). This is the same
color used as the default when a [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) cannot be resolved.

### BrickColor.DarkGray

**Signature:** `BrickColor.DarkGray()`

Returns the "Dark stone grey" [BrickColor](/docs/reference/engine/datatypes/BrickColor.md).

### BrickColor.Black

**Signature:** `BrickColor.Black()`

Returns the "Black" [BrickColor](/docs/reference/engine/datatypes/BrickColor.md).

### BrickColor.Red

**Signature:** `BrickColor.Red()`

Returns the "Bright red" [BrickColor](/docs/reference/engine/datatypes/BrickColor.md).

### BrickColor.Yellow

**Signature:** `BrickColor.Yellow()`

Returns the "Bright yellow" [BrickColor](/docs/reference/engine/datatypes/BrickColor.md).

### BrickColor.Green

**Signature:** `BrickColor.Green()`

Returns the "Dark green" [BrickColor](/docs/reference/engine/datatypes/BrickColor.md).

### BrickColor.Blue

**Signature:** `BrickColor.Blue()`

Returns the "Bright blue" [BrickColor](/docs/reference/engine/datatypes/BrickColor.md).

## Properties

### BrickColor.Number

**Type:** `number`

The unique number that identifies the [BrickColor](/docs/reference/engine/datatypes/BrickColor.md). This is the
same integer used by [BrickColor.new()](/docs/reference/engine/datatypes/BrickColor.md) to construct the color
and corresponds to the **Number** column in the color table above.
Read-only.

### BrickColor.r

**Type:** `number`

The red component of the [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) (between `0` and `1`). This
is equivalent to `BrickColor.Color.R`. Read-only.

### BrickColor.g

**Type:** `number`

The green component of the [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) (between `0` and `1`).
This is equivalent to `BrickColor.Color.G`. Read-only.

### BrickColor.b

**Type:** `number`

The blue component of the [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) (between `0` and `1`).
This is equivalent to `BrickColor.Color.B`. Read-only.

### BrickColor.Name

**Type:** `string`

The name associated with the [BrickColor](/docs/reference/engine/datatypes/BrickColor.md), for example
`"Pastel Blue"`. This is the same string accepted by
[BrickColor.new()](/docs/reference/engine/datatypes/BrickColor.md). Read-only.

### BrickColor.Color

**Type:** `Color3`

The [Color3](/docs/reference/engine/datatypes/Color3.md) associated with the [BrickColor](/docs/reference/engine/datatypes/BrickColor.md). The
individual components of this value are the same as `BrickColor.r`,
`BrickColor.g`, and `BrickColor.b`. Read-only.