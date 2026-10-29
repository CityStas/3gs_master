# Aligning a prop collider with its drawn sprite (the alpha-bbox trap)

## When to use

A prop that must be **stood on** (a floating platform, a crate, a rock ledge) is a generated
sprite placed in a scene, and the collider is derived from the sprite's box rather than
authored by hand. If the collider is placed by "sprite position ± half the texture size",
the character floats above the prop by a constant, visible amount.

## Why it happens

An `alpha`-cropped prop sprite is cropped to the *bounding box of any non-transparent
pixel*. Decorative details on top of the prop — grass tufts, small mushrooms, thin sprigs —
stick up above the walkable surface, so the bbox top is **above** the surface. Measured on a
generated floating rock island (718x527 after crop):

| Row | Opaque fraction | What it is |
|---|---|---|
| 7 | 0 % | first pixels appear |
| 12-42 | 5-11 % | grass blades, a small mushroom cap |
| 48 | 21 % | **the moss surface** |
| 54+ | 41 %+ | the rock body |

So a collider placed at the texture top sits **13 world px** above the moss at the scale the
prop is used. That is the entire "the character floats" bug.

## The fix: place the collider on the "solid line"

Define the prop's surface row as the first row where the opaque fraction crosses a
threshold, and drive both the sprite and the collider from it:

```python
def alpha_band(path, frac=0.20):
    """First and last row whose opaque fraction >= frac."""
```

`frac = 0.20` cleanly separates sprigs (5-11 % of the width) from the body (20-40 % right
after the line). Then:

```python
r_top, r_bot = alpha_band(prop)
pscale  = PLATFORM_H / (r_bot - r_top + 1)     # scale by the VISIBLE height
sprite_y    = gy - rise + (tex_h / 2 - r_top) * pscale   # row r_top lands on gy - rise
collider_y  = gy - rise + COLLIDER_THICK / 2             # top of box on the same line
```

Two things fall out of this and both matter:

1. **`PLATFORM_H` becomes the size of the object, not the size of the file.** Every time the
   art is re-cropped the file size changes; deriving the scale from the visible band keeps
   the in-world size stable without re-tuning a magic number.
2. **The collider's top, not its centre, goes on the surface line.** Centring the box on the
   line puts half its thickness above the moss — a smaller version of the same bug.

## Make the collider thick enough to not be tunnelled

A thin collider (5-7 px) is **passed through** by a falling character. At a terminal velocity
of 700 px/s and a 1/60 s step, the character moves 11.7 px per frame. Use ~26 px. This is a
discrete-collision artefact, not a tuning preference: the landing test is
`prev_feet <= surface <= feet`, so any thickness below `max_fall * dt` fails.

## Do not make a standing prop "float"

A prop the character must jump onto is a blocking obstacle. Check the geometry before
choosing its height:

- Character height `H`, prop height `P`, jump apex `A`.
- To **walk under** it, the prop's bottom must be above the character's head, i.e.
  `rise > H + P`. With `H = 215`, `P = 130`, that is `rise > 345` — beyond a 300 px jump
  apex, so the prop would be unreachable decoration.
- To **jump onto** it, `rise < A`. With `A = 180` (base jump) or ~300 (with jump sustain),
  `rise = P = 130` works and seats the prop's bottom on the terrain.

Pick one; a prop that is neither walk-under-able nor jump-onto-able is an invisible wall with
a picture attached. Seating the bottom on the terrain is the readable choice: it looks like a
boulder in the corridor, which is exactly what it is.

## Verify

Put the character on the collider programmatically and check the numbers, then take one
screenshot zoomed on the contact point:

```js
player.x = colliderX; player.y = colliderTop - FEET_OFF;
// expect: player.y + FEET_OFF === colliderTop, and the sprite's drawn top row === colliderTop
```

In the overlay renderer, draw the prop sprite and its collider box together — if the box top
does not sit on the drawn surface, it is still wrong.
