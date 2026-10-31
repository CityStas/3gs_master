---
name: KeyCode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Byte keycodes that represent the key or button involved in user input."
---

# KeyCode

Byte keycodes that represent the key or button involved in user input.

**Type:** enum

## Description

The `KeyCode` enum contains a list of byte keycodes that represent the key or
button involved in user input. This enum also includes buttons and axes
present on gamepads, and 96 `World[]` values for non-standard buttons.

Note that keyboard values refer to the physical position of buttons on a
standard QWERTY keyboard. Provided the user's system is configured correctly,
the location of keys (such as
<kbd>W</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd>) will remain the same on
other keyboard types such as Dvorak keyboards where it would map to
<kbd>,</kbd><kbd>A</kbd><kbd>O</kbd><kbd>E</kbd>.

See also [InputObject](/docs/reference/engine/classes/InputObject.md), used for keyboard and gamepad input.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 |  |
| `Backspace` | 8 | The `Backspace` key. |
| `Tab` | 9 | The `Tab` key. |
| `Clear` | 12 | Only present on certain keyboards. |
| `Return` | 13 | Frequently known as **Enter**. |
| `Pause` | 19 | Only present on certain keyboards. |
| `Escape` | 27 | The `Escape` key. |
| `Space` | 32 | The `Space` key. |
| `QuotedDouble` | 34 | The `"` key. |
| `Hash` | 35 | The `#` key. |
| `Dollar` | 36 | The `$` key. |
| `Percent` | 37 | The `%` key. |
| `Ampersand` | 38 | The `&` key. |
| `Quote` | 39 | The `'` key. |
| `LeftParenthesis` | 40 | The `(` key. |
| `RightParenthesis` | 41 | The `)` key. |
| `Asterisk` | 42 | The `*` key. |
| `Plus` | 43 | The `+` key. |
| `Comma` | 44 | The `,` key. |
| `Minus` | 45 | The `-` key. |
| `Period` | 46 | The `.` key. |
| `Slash` | 47 | The `/` key. |
| `Zero` | 48 | The `0` key. |
| `One` | 49 | The `1` key. |
| `Two` | 50 | The `2` key. |
| `Three` | 51 | The `3` key. |
| `Four` | 52 | The `4` key. |
| `Five` | 53 | The `5` key. |
| `Six` | 54 | The `6` key. |
| `Seven` | 55 | The `7` key. |
| `Eight` | 56 | The `8` key. |
| `Nine` | 57 | The `9` key. |
| `Colon` | 58 | The `:` key. |
| `Semicolon` | 59 | The `;` key. |
| `LessThan` | 60 | The `<` key. |
| `Equals` | 61 | The `=` key. |
| `GreaterThan` | 62 | The `>` key. |
| `Question` | 63 | The `?` key. |
| `At` | 64 | The `@` key. |
| `LeftBracket` | 91 | The `[` key. |
| `BackSlash` | 92 | The `\` key. |
| `RightBracket` | 93 | The `]` key. |
| `Caret` | 94 | The `^` key. |
| `Underscore` | 95 | The `_` key. |
| `Backquote` | 96 | The `` ` `` key. |
| `A` | 97 | The `A` key. |
| `B` | 98 | The `B` key. |
| `C` | 99 | The `C` key. |
| `D` | 100 | The `D` key. |
| `E` | 101 | The `E` key. |
| `F` | 102 | The `F` key. |
| `G` | 103 | The `G` key. |
| `H` | 104 | The `H` key. |
| `I` | 105 | The `I` key. |
| `J` | 106 | The `J` key. |
| `K` | 107 | The `K` key. |
| `L` | 108 | The `L` key. |
| `M` | 109 | The `M` key. |
| `N` | 110 | The `N` key. |
| `O` | 111 | The `O` key. |
| `P` | 112 | The `P` key. |
| `Q` | 113 | The `Q` key. |
| `R` | 114 | The `R` key. |
| `S` | 115 | The `S` key. |
| `T` | 116 | The `T` key. |
| `U` | 117 | The `U` key. |
| `V` | 118 | The `V` key. |
| `W` | 119 | The `W` key. |
| `X` | 120 | The `X` key. |
| `Y` | 121 | The `Y` key. |
| `Z` | 122 | The `Z` key. |
| `LeftCurly` | 123 | The `{` key. |
| `Pipe` | 124 | The `\|` key. |
| `RightCurly` | 125 | The `}` key. |
| `Tilde` | 126 | The `~` key. |
| `Delete` | 127 | The `Del` key. |
| `World0` | 160 | Deprecated |
| `World1` | 161 | Deprecated |
| `World2` | 162 | Deprecated |
| `World3` | 163 | Deprecated |
| `World4` | 164 | Deprecated |
| `World5` | 165 | Deprecated |
| `World6` | 166 | Deprecated |
| `World7` | 167 | Deprecated |
| `World8` | 168 | Deprecated |
| `World9` | 169 | Deprecated |
| `World10` | 170 | Deprecated |
| `World11` | 171 | Deprecated |
| `World12` | 172 | Deprecated |
| `World13` | 173 | Deprecated |
| `World14` | 174 | Deprecated |
| `World15` | 175 | Deprecated |
| `World16` | 176 | Deprecated |
| `World17` | 177 | Deprecated |
| `World18` | 178 | Deprecated |
| `World19` | 179 | Deprecated |
| `World20` | 180 | Deprecated |
| `World21` | 181 | Deprecated |
| `World22` | 182 | Deprecated |
| `World23` | 183 | Deprecated |
| `World24` | 184 | Deprecated |
| `World25` | 185 | Deprecated |
| `World26` | 186 | Deprecated |
| `World27` | 187 | Deprecated |
| `World28` | 188 | Deprecated |
| `World29` | 189 | Deprecated |
| `World30` | 190 | Deprecated |
| `World31` | 191 | Deprecated |
| `World32` | 192 | Deprecated |
| `World33` | 193 | Deprecated |
| `World34` | 194 | Deprecated |
| `World35` | 195 | Deprecated |
| `World36` | 196 | Deprecated |
| `World37` | 197 | Deprecated |
| `World38` | 198 | Deprecated |
| `World39` | 199 | Deprecated |
| `World40` | 200 | Deprecated |
| `World41` | 201 | Deprecated |
| `World42` | 202 | Deprecated |
| `World43` | 203 | Deprecated |
| `World44` | 204 | Deprecated |
| `World45` | 205 | Deprecated |
| `World46` | 206 | Deprecated |
| `World47` | 207 | Deprecated |
| `World48` | 208 | Deprecated |
| `World49` | 209 | Deprecated |
| `World50` | 210 | Deprecated |
| `World51` | 211 | Deprecated |
| `World52` | 212 | Deprecated |
| `World53` | 213 | Deprecated |
| `World54` | 214 | Deprecated |
| `World55` | 215 | Deprecated |
| `World56` | 216 | Deprecated |
| `World57` | 217 | Deprecated |
| `World58` | 218 | Deprecated |
| `World59` | 219 | Deprecated |
| `World60` | 220 | Deprecated |
| `World61` | 221 | Deprecated |
| `World62` | 222 | Deprecated |
| `World63` | 223 | Deprecated |
| `World64` | 224 | Deprecated |
| `World65` | 225 | Deprecated |
| `World66` | 226 | Deprecated |
| `World67` | 227 | Deprecated |
| `World68` | 228 | Deprecated |
| `World69` | 229 | Deprecated |
| `World70` | 230 | Deprecated |
| `World71` | 231 | Deprecated |
| `World72` | 232 | Deprecated |
| `World73` | 233 | Deprecated |
| `World74` | 234 | Deprecated |
| `World75` | 235 | Deprecated |
| `World76` | 236 | Deprecated |
| `World77` | 237 | Deprecated |
| `World78` | 238 | Deprecated |
| `World79` | 239 | Deprecated |
| `World80` | 240 | Deprecated |
| `World81` | 241 | Deprecated |
| `World82` | 242 | Deprecated |
| `World83` | 243 | Deprecated |
| `World84` | 244 | Deprecated |
| `World85` | 245 | Deprecated |
| `World86` | 246 | Deprecated |
| `World87` | 247 | Deprecated |
| `World88` | 248 | Deprecated |
| `World89` | 249 | Deprecated |
| `World90` | 250 | Deprecated |
| `World91` | 251 | Deprecated |
| `World92` | 252 | Deprecated |
| `World93` | 253 | Deprecated |
| `World94` | 254 | Deprecated |
| `World95` | 255 | Deprecated |
| `KeypadZero` | 256 | The `0` key on the keypad cluster. |
| `KeypadOne` | 257 | The `1` key on the keypad cluster. |
| `KeypadTwo` | 258 | The `2` key on the keypad cluster. |
| `KeypadThree` | 259 | The `3` key on the keypad cluster. |
| `KeypadFour` | 260 | The `4` key on the keypad cluster. |
| `KeypadFive` | 261 | The `5` key on the keypad cluster. |
| `KeypadSix` | 262 | The `6` key on the keypad cluster. |
| `KeypadSeven` | 263 | The `7` key on the keypad cluster. |
| `KeypadEight` | 264 | The `8` key on the keypad cluster. |
| `KeypadNine` | 265 | The `9` key on the keypad cluster. |
| `KeypadPeriod` | 266 | The `.` key on the keypad cluster. |
| `KeypadDivide` | 267 | The `/` key on the keypad cluster. |
| `KeypadMultiply` | 268 | The `*` key on the keypad cluster. |
| `KeypadMinus` | 269 | The `-` key on the keypad cluster. |
| `KeypadPlus` | 270 | The `+` key on the keypad cluster. |
| `KeypadEnter` | 271 | The `Enter` key on the keypad cluster. |
| `KeypadEquals` | 272 | The `=` key on the keypad cluster. |
| `Up` | 273 | The `↑` arrow key. |
| `Down` | 274 | The `↓` arrow key. |
| `Right` | 275 | The `→` arrow key. |
| `Left` | 276 | The `←` arrow key. |
| `Insert` | 277 | The `Insert` key. |
| `Home` | 278 | The `Home` key. |
| `End` | 279 | The `End` key. |
| `PageUp` | 280 | The `PgUp` key. |
| `PageDown` | 281 | The `PgDown` key. |
| `F1` | 282 | The `F1` key. |
| `F2` | 283 | The `F2` key. |
| `F3` | 284 | The `F3` key. |
| `F4` | 285 | The `F4` key. |
| `F5` | 286 | The `F5` key. |
| `F6` | 287 | The `F6` key. |
| `F7` | 288 | The `F7` key. |
| `F8` | 289 | The `F8` key. |
| `F9` | 290 | The `F9` key. |
| `F10` | 291 | The `F10` key. |
| `F11` | 292 | The `F11` key. |
| `F12` | 293 | The `F12` key. |
| `F13` | 294 | The `F13` key. Only present on certain keyboards. |
| `F14` | 295 | The `F14` key. Only present on certain keyboards. |
| `F15` | 296 | The `F15` key. Only present on certain keyboards. |
| `NumLock` | 300 | The `Num Lock` key on the keypad cluster. |
| `CapsLock` | 301 | The `Caps Lock` key. |
| `ScrollLock` | 302 | The `Scr Lock` key. |
| `RightShift` | 303 | The right side `Shift` key. |
| `LeftShift` | 304 | The left side `Shift` key. |
| `RightControl` | 305 | The right side `Ctrl` key. |
| `LeftControl` | 306 | The left side `Ctrl` key. |
| `RightAlt` | 307 | The right side `Alt` key. |
| `LeftAlt` | 308 | The left side `Alt` key. |
| `RightMeta` | 309 | The right side `Meta` key. |
| `LeftMeta` | 310 | The left side `Meta` key. |
| `LeftSuper` | 311 | The left side `Super` key. Better known as the Windows key or <kbd>Cmd</kbd> key. |
| `RightSuper` | 312 | The right side `Super` key. Better known as the Windows key or <kbd>Cmd</kbd> key. |
| `Mode` | 313 | Only present on certain keyboards. |
| `Compose` | 314 | Only present on certain keyboards. |
| `Help` | 315 | Only present on certain keyboards. |
| `Print` | 316 | Only present on certain keyboards. |
| `SysReq` | 317 | Only present on certain keyboards. |
| `Break` | 318 | Only present on certain keyboards. |
| `Menu` | 319 | The `Menu` key. |
| `Power` | 320 | Only present on certain keyboards. |
| `Euro` | 321 | The `€` key. Only present on certain keyboards. |
| `Undo` | 322 | Only present on certain keyboards. |
| `ButtonX` | 1000 | Gamepad `X` button. |
| `ButtonY` | 1001 | Gamepad `Y` button. |
| `ButtonA` | 1002 | Gamepad `A` button. |
| `ButtonB` | 1003 | Gamepad `B` button. |
| `ButtonR1` | 1004 | Gamepad `R1` button. |
| `ButtonL1` | 1005 | Gamepad `L1` button. |
| `ButtonR2` | 1006 | Gamepad `R2` button. |
| `ButtonL2` | 1007 | Gamepad `L2` button. |
| `ButtonR3` | 1008 | Gamepad `R3` button. |
| `ButtonL3` | 1009 | Gamepad `L3` button. |
| `ButtonStart` | 1010 | Gamepad `Start` button. |
| `ButtonSelect` | 1011 | Gamepad `Select` button. |
| `DPadLeft` | 1012 | Left arrow on a gamepad D-pad. |
| `DPadRight` | 1013 | Right arrow on a gamepad D-pad. |
| `DPadUp` | 1014 | Up arrow on a gamepad D-pad. |
| `DPadDown` | 1015 | Down arrow on a gamepad D-pad. |
| `Thumbstick1` | 1016 | Gamepad primary thumbstick. |
| `Thumbstick2` | 1017 | Gamepad secondary thumbstick. |
| `Thumbstick1Up` | 1018 | Up vector on the gamepad primary thumbstick. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md). |
| `Thumbstick1Down` | 1019 | Down vector on the gamepad primary thumbstick. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md). |
| `Thumbstick1Left` | 1020 | Left vector on the gamepad primary thumbstick. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md). |
| `Thumbstick1Right` | 1021 | Right vector on the gamepad primary thumbstick. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md). |
| `Thumbstick2Up` | 1022 | Up vector on the gamepad secondary thumbstick. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md). |
| `Thumbstick2Down` | 1023 | Down vector on the gamepad secondary thumbstick. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md). |
| `Thumbstick2Left` | 1024 | Left vector on the gamepad secondary thumbstick. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md). |
| `Thumbstick2Right` | 1025 | Right vector on the gamepad secondary thumbstick. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md). |
| `MouseLeftButton` | 1026 | The left mouse button, also commonly referred to as "button 1" on a generic mouse. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md). |
| `MouseRightButton` | 1027 | The right mouse button, also commonly referred to as "button 2" on a generic mouse. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md). |
| `MouseMiddleButton` | 1028 | The middle mouse button, also commonly referred to as "button 3" on a generic mouse. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md). |
| `MouseBackButton` | 1029 |  |
| `MouseNoButton` | 1030 |  |
| `MouseX` | 1031 |  |
| `MouseY` | 1032 |  |
| `MousePosition` | 1033 | The position of a mouse in the viewport. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md). |
| `TouchPosition` | 1034 | The position of a touch in the viewport. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md). |
| `MouseWheel` | 1035 | The scroll delta (change) of a mouse wheel. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md), returning a velocity in scroll units per second (where one scroll unit is approximately equivalent to a standard mouse wheel notch) under a [Direction1D](/docs/reference/engine/enums/InputActionType.md) action type. |
| `TrackpadPan` | 1040 | The pan delta (change) from a trackpad two-finger pan gesture. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md), returning a velocity in pixels per second under a [Direction2D](/docs/reference/engine/enums/InputActionType.md) action type. |
| `TrackpadPinch` | 1045 | The scale delta (change) from a trackpad two-finger pinch gesture. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md), returning a velocity in scroll units per second (where one scroll unit is approximately equivalent to a standard mouse wheel notch) under a [Direction1D](/docs/reference/engine/enums/InputActionType.md) action type. |
| `MouseDelta` | 1048 | The movement delta (change) of the mouse cursor. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md), returning a velocity in pixels per second under a [Direction2D](/docs/reference/engine/enums/InputActionType.md) action type. |
| `TouchDelta` | 1049 | The movement delta (change) of a touch input. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md), returning a velocity in pixels per second under a [Direction2D](/docs/reference/engine/enums/InputActionType.md) action type. |
| `TouchPinch` | 1050 | The scale delta (change) from a touch two-finger pinch gesture. Primarily used in the [Input Action System](/docs/en-us/input/input-action-system.md), returning a velocity in pixels per second under a [Direction1D](/docs/reference/engine/enums/InputActionType.md) action type. |
| `ButtonCenter` | 1051 | TV remote `Center` button. |
| `ButtonBack` | 1052 | TV remote `Back` button. |
| `ButtonUp` | 1053 | [MicroGamepad](https://create.roblox.com/docs/reference/engine/enums/PreferredInput#MicroGamepad) (including TV remotes) `Up` directional button. |
| `ButtonDown` | 1054 | [MicroGamepad](https://create.roblox.com/docs/reference/engine/enums/PreferredInput#MicroGamepad) (including TV remotes) `Down` directional button. |
| `ButtonLeft` | 1055 | [MicroGamepad](https://create.roblox.com/docs/reference/engine/enums/PreferredInput#MicroGamepad) (including TV remotes) `Left` directional button. |
| `ButtonRight` | 1056 | [MicroGamepad](https://create.roblox.com/docs/reference/engine/enums/PreferredInput#MicroGamepad) (including TV remotes) `Right` directional button. |