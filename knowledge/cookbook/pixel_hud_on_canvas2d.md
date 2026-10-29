# Pixel-art HUD on a 2D canvas (instead of DOM/CSS)

## When to use

The game is drawn as pixel art and the HUD must match. Rebuilding the HUD as DOM elements —
`border-radius`, `backdrop-filter`, system monospace, `box-shadow` — produces something that
reads as *ordinary web UI* glued over a game, and it is immediately visible next to pixel
art. It is not a matter of taste: the game's whole visual language is "every edge lands on a
whole pixel", and CSS does not respect that.

## The architecture

Two canvases:

```html
<div id="app"></div>              <!-- WebGL: the game -->
<canvas id="hud"></canvas>        <!-- 2D: the HUD, pointer-events: none -->
```

The HUD canvas is **not** a WebGL overlay and **not** DOM. It is a second, transparent 2D
canvas stretched over the first.

## Draw in logical scene space, scale in one transform

Take the viewport size from the renderer, not from the window, and set up one transform:

```js
ctx.setTransform(dpr * s, 0, 0, dpr * s, 0, 0);   // s = windowWidth / logicalViewWidth
```

Everything after that is drawn in **viewport units** — the same units the engine's
`viewport_size` gives in Godot. A HUD element placed at `(22, 20)` is at the same spot in
both engines regardless of window size, and the CSS-stretch behaviour matches the game's
`stretch = expand` mode for free.

`image-rendering: pixelated` on the game canvas; the HUD canvas is vector-ish but everything
is drawn on integer coordinates anyway.

## Font: carry the glyph table, do not import a font

A 5x7 bitmap font defined **in code** beats a webfont: no network request, no anti-aliasing,
no subpixel phase, and it is trivially portable from the original engine.

```js
export const GW = 5, GH = 7, GAP = 1;
export const GLYPHS = { A: ['01110','10001', ...], ... };
export function drawText(ctx, text, x, y, px, colors, opts) { ... }
```

Blit each `#` of a glyph as a `fillRect(x, y, px, px)`. Two hard rules:

1. **Integer positions only.** The "bold" style is implemented by growing every pixel
   rectangle by `bold` px on each side — adjacent rectangles then overlap, and at a
   fractional offset their rasterisation phase changes per glyph, so letters jitter and blur.
   Run anything that moves (pulse, bob, swing) through `Math.round` / `roundf`.
2. **A limited charset is a design constraint, not a bug.** The 5x7 table covers
   `A-Z 0-9 ! : . - /` and space. Cyrillic, `x` (multiplication) and `+` are not in it. That
   means UI strings must be authored in the font's alphabet — `X5 AMMO`, not `×5 патронов`.
   Translate the strings at the data layer (the level manifest), not by inventing glyphs
   mid-render.

## Alpha is not a transition

Fading a "dense" pixel label in or out with `globalAlpha` or `modulate` reads as *the letters
are translucent* — you can see the background through the glyphs — and users report it as a
defect. Show/hide in a single frame by flipping `visible` / skipping the draw call. The same
applies to scaling: do not interpolate the pixel size.

## Port the numbers, not the impression

The HUD constants are the specification. Port them literally from the original scripts and
keep their names:

| Thing | Value |
|---|---|
| heart / mushroom icon | 9x8, drawn at `px = 2.9` |
| bolt icon | 5x5 at `px = 3.4` |
| HP segments | `42x21`, gap 5, border 2 |
| margins | `[22, 20]`, icon gap 13, row gap 18 |
| HP smoothing | `move_toward(shown, hp, dt * 3.2)` |
| low-HP heart pulse | `0.72 + 0.28 * sin(t * 7)` |
| damage flash decay | `dt * 2.0` |
| overlay fade | `min(1, fade + dt * 2.2)`, alpha gate `clamp((fade - 0.45) / 0.55, 0, 1)` |
| overlay title | DEMO px 22 / GAME OVER px 15 / END OF SCENE px 7 |
| overlay bob | `sin(t * 1.7) * (11 | 7)` |

Inventing "close enough" values is how a port stops looking like the original.

## Overlay input must be captured before the game sees it

The HUD canvas has `pointer-events: none` so clicks reach the game. Menu buttons therefore
need their own path — and they must **stop** the event, or a click on START also fires a
shot:

```js
addEventListener('pointerdown', (e) => {
  if (!hud.overlayActive) return;
  hud.pointer('down', e.clientX, e.clientY);
  e.stopPropagation(); e.preventDefault();
}, true);                      // capture phase, on window
```

The overlay's own hit test converts client coordinates to the same logical viewport units the
HUD draws in, then compares against the button rectangles the HUD itself laid out — one
`buttonSpec()` used by both drawing and hit testing, so the two cannot drift.

## Testing the HUD

Screenshot-driven testing hits an awkward snag: `page.screenshot()` in some harnesses issues a
real click at the viewport centre, which lands on a centred menu button and starts the game
by itself. If a game "auto-starts past the menu" during tests, instrument `beginPlay()` with a
stack trace before suspecting the game.
