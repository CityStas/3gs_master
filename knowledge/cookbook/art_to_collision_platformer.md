# Deriving walkable collision from generated level art

## When to use

A 2D side-scroller level whose ground is a **generated painting**, not a tilemap: one wide
transparent PNG (a "gameplay layer") showing the terrain strip, with parallax layers behind
it. You need a collision profile that a character can walk on, and the art is regenerated
from a new seed every iteration, so hand-authoring the polygon is not an option.

The rule the whole method serves: **the feet must land where the drawn moss is.** A profile
that is 20 px off is not a rounding error, it reads as "the character walks on air".

## The trap: "top opaque pixel of the column"

The naive rule — for each column, take the topmost pixel with alpha > 0 — fails on every
real generated background, in three separate ways. All three were hit on the same level.

| Symptom | Cause | Fix (see below) |
|---|---|---|
| Character walks over mushroom caps | Decorative mushrooms/grass grow *on* the ledge; their cap is the top opaque pixel | Morphological opening on the profile |
| Character walks on fog | The generator paints a nearly-opaque mist bank along the bottom edge | Support test: require solid rock under the column |
| Polygon bridges every chasm | Mist columns are opaque, so the "run reaching the ground band" never breaks | Same support test, plus `None` propagation |

## Step 1 — find the ground band, do not scan from the top

```python
frac[y] = (opaque pixels in row y) / width
band_bottom = argmax(frac)          # the row where the art is widest
```

`band_bottom` is the row the terrain mass sits on. For each column, walk **up** from
`band_bottom` while pixels are opaque; that gives the top of the contiguous run *containing
the ground*, which is what a walkable surface is. Clip the search at
`band_bottom - SLACK` so a column that runs all the way to the top of the image does not
produce a surface 400 px up.

This alone already removes most floating props: a mushroom whose cap is disconnected from
the ground never reaches `band_bottom` in one run.

## Step 2 — support test (rock, not mist)

Mist is **opaque but thin**. Rock is thick. So measure thickness, not opacity:

```python
y = band_bottom
while y < h and alpha[y][x] > SOLID:
    y += 1
if y - band_bottom < MIN_DEPTH:
    continue                        # this column has no platform
```

Measured on a 2048x768 z-image gameplay layer: mist banks are 6..29 px thick, rock is
80..180 px. `MIN_DEPTH = 50`, `SOLID = 200` separates them with a wide margin.

Columns that fail become `None`. `None` is the *only* thing that creates a cliff, so the
splitter downstream must treat `None` as a hard boundary — see step 5.

## Step 3 — median filter, two passes

One pass of median window 21, run twice, flattens the pixel-level noise of the moss edge
without eating real steps. Two passes of a narrow window beat one wide window: a wide window
rounds off genuine ledges.

`None` values are skipped inside the window (not treated as 0 or as a large number), so the
filter does not drag a cliff edge inward.

## Step 4 — morphological opening (this is the one people miss)

A decorative mushroom cap is a **local peak** of the profile. On the measured level the cap
was ~45 source px wide and rose 20 world px — wider than the median window, so the median
left it alone. Raising the median window to cover it would flatten the real terrain steps.

Opening separates the two cases by **shape**, not amplitude: erode then dilate with a flat
element wider than the unwanted feature. In a y-down profile:

```python
eroded[i] = max(vals[i-half : i+half+1])   # y grows downward: max = lowest point
out[i]    = min(eroded[i-half : i+half+1]) # min = highest point of the eroded profile
```

Any peak narrower than the window disappears; monotone slopes and wide shelves are
untouched. `OPEN_WIN = 61` removed a 45 px cap; real ledges survived.

**Restore `None` from the input afterwards.** Opening happily *invents* a surface in a
column that had none (the window still contains valid neighbours), which silently grows
cliffs into chasms by up to `half` px. The alpha decides where the cliff is, not the filter:

```python
out.append(v if vals[i] is not None else None)
```

## Step 5 — sample, simplify, close

- Sample every 6 source px.
- Douglas-Peucker with `eps = 5` **world** px → 50-60 points per level (hand-measured
  reference level: 53).
- Split into runs where the horizontal gap exceeds `MIN_GAP` (70 world px): a 20 px hole is
  something the character falls through instantly, not a chasm.
- Close each run into a polygon by appending `(last_x, max_y + 160)` and
  `(first_x, max_y + 160)` so the shape is solid downward.

## Step 6 — verify visually, in world space

Numbers do not prove alignment. Render the polygon **on top of the art**, in the same world
transform the runtime uses (Sprite2D is centred: `world = position ± texture_size * scale / 2`).

Two bugs in the checker itself are worth knowing, because both make the overlay lie in the
reassuring direction:

- `Image.alpha_composite(art, (dx, dy))` with a negative `dx`/`dy` (a parallax layer whose
  left edge is off-screen) **silently draws nothing**. Crop both the sprite and the
  destination to the intersection instead.
- The sprite must be resized to `world_size * view_scale`, not to its texture size. Miss the
  factor and every sprite is `1/scale` too small and slides off the view — you then "confirm"
  that art is missing where it is present.

With those fixed, the overlay shows at a glance whether the yellow surface line runs along
the moss or floats over it. `games/ded_test/tools/level_overlay.py` is a working
implementation (~200 lines, PIL only).

## Step 7 — verify by walking, deterministically

A screenshot of a character standing still proves nothing about a 3.5 km level. Run the
physics yourself, with the render loop disabled, so no real input can interfere:

```js
const realUpdate = game.update.bind(game);
game.update = () => {};              // rAF loop off — the test must be deterministic
game.keys.clear();
game.keys.add('KeyD');
for (let i = 0; i < 60 * 120; i++) {
  if (player.grounded && blockedAhead()) game.keys.add('Space');
  game._stepPlayer(1 / 60);
  // record player.x, player.y, world.terrainAt(player.x), player.grounded
}
game.update = realUpdate;
```

Then look at the **histogram of `feet - terrain` over grounded frames**. On the fixed level:
572 frames at exactly `0`, 71 at `-1`, and a thin tail down to `-22` at ledge edges (the body
is 44 px wide, so it legitimately rests on the higher of two nearby columns). Before the
fix the mode was not 0. That histogram is the acceptance criterion.

Large negative outliers are fine **if** the character is standing on a separate collider —
check `terrainAt` is not just reporting the ground below a floating platform.

## Pitfalls

- **Do not** derive the profile from the composite of all layers. Use the gameplay layer
  alone; behind it is sky.
- **Do not** assume the gameplay layer's texture top is the walkable top. See
  `platform_prop_collider_alignment.md` — the same alpha-bbox trap applies to props.
- **Do not** trust the profile to be "flat enough". Measure the y-span and compare it with
  the hand-authored reference level; on the measured project the generated profile ended up
  *flatter* (26 px span) than the hand-measured one (53 px), which was the goal.
