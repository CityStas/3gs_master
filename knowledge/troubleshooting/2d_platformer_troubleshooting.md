# 2D platformer troubleshooting (three.js + generated art)

Concrete symptoms, their real causes, and the check that distinguishes them.

## The canvas is tiny in the corner (300x150)

three.js's default `setSize` is 300x150. A level loader that only updates the **camera**
projection leaves the renderer at that default.

```js
// WRONG — GodotScene.resize only recomputes the camera
this.gs.resize(w, h);
// RIGHT — this.resize() also calls renderer.setSize
this.resize();
```

Check: `canvas.width/height` in the console. If it is 300x150 while `innerWidth` is 1280,
this is it.

## Everything is drawn but the game "does not start"

The start menu sets the scene tree to paused; nothing processes. When driving the game
programmatically, clearing the menu is not enough:

- Setting the mode flag does **not** repaint a `CanvasItem`. If `_process` stops calling
  `queue_redraw()` for that mode, the last menu frame stays on screen and screenshots show
  the menu over the game. Call `queue_redraw()` explicitly.
- The game-flow controller will also see the character "fall" and drive the scene to GAME
  OVER, which pauses everything again. Disable its `_process`.
- Instant-death trigger zones will kill the character in a corridor test. Disable their
  `_physics_process`.

## The character walks on air

Two different causes, two different checks.

1. **The profile follows decoration.** Look at the collision polygon drawn over the art. If
   the line climbs over mushroom caps, it is the profile. Fix with a morphological opening —
   see `art_to_collision_platformer.md`.
2. **The character legitimately rests on the higher of two columns.** The body is ~44 px wide;
   on a ledge edge the landing test picks the highest surface under the body, so the centre
   column reads as "floating" by up to half the body width. This is correct, not a bug.

To tell them apart, histogram `feet - terrain` over grounded frames. Cause 1 gives a mode that
is not 0. Cause 2 gives a mode of 0 with a thin tail.

## The character stops for no visible reason

The collider and the art disagree. Render the collider boxes over the art in world space. The
usual culprits are a prop collider placed by texture bbox (see
`platform_prop_collider_alignment.md`) and a collider whose centre rather than top was put on
the surface line.

Also check for a **thin** collider that was meant to be a landing pad but is being hit as a
wall: the X pass tests `surface < prev_feet - STEP_UP` across the whole body width, so a
platform whose top is more than `STEP_UP` above the feet blocks horizontal motion. That is
correct behaviour for an obstacle — verify the level *intends* an obstacle there.

## The character is blocked in mid-air by nothing

A collider exists where the art has a gap. Common with a platform that "floats": with a
215 px character and a 130 px prop, the prop cannot be walked under at any height within jump
range, so a floating collider is an invisible wall. Either seat it on the terrain or move it
out of the corridor.

## Enemies stack on one coordinate, or walk off the ledge

Each enemy needs its own patrol window clamped to the platform it stands on. Two enemies with
the same range converge. Also clamp to the run's ends, not to the level's, or an enemy walks
into a chasm.

## A layer renders nothing

Check its alpha coverage, not the job's success status:

```python
print(100 * (np.array(Image.open(f).convert("RGBA"))[:, :, 3] > 8).mean())
```

`0 %` means the mask step produced an empty image. `kind: mask` (BiRefNet) returns nothing for
a full-screen scene, because it segments a salient object and a background has none. Use a
luminance key for haze layers — see `parallax_layers_2d.md`.

## A layer covers the sky

The mask threshold is too high, so the layer is mostly opaque. Composite it over the layer it
will sit on at two or three thresholds and compare; the right value is the one where the sky
still reads through.

## A build looks stale

- **File size does not change** when you edit a float. Compare mtimes, and search the packed
  bytes for the value if you need certainty.
- **The browser serves a cached manifest.** Add `cache: 'no-cache'` to fetches of hand-edited
  content.
- **The web export may not include a new script.** If the export filter is
  `resources` (roots from `export_files` plus whatever is reachable), the traverser follows
  scene → resource links and does **not** follow `preload` from scripts. A new script must be
  added to `export_files` by hand, and the check is the export log
  (`grep "Storing File: res://scripts/"`), not the package size.

## `invalid UID ... using text path instead` in a web export

This is not cosmetic. It means the UID in the `.tres` and the UID the runtime knows (from
`.png.import`) disagree: an `[ext_resource]` without `uid=` makes the exporter take the UID
from the editor's cache (`.godot/uid_cache.bin`), which goes stale when assets are
reorganised. Fix by writing the `uid=` values from the corresponding `.import` files into the
`.tres`. Do not try to read `uid_cache.bin` by hand — the records are binary
(`int64 + len + path`) and the UID is not searchable as a string.

## Headless screenshots are blank

`--headless` uses a dummy driver with an empty buffer. Take screenshots with a real window and
a fixed frame rate, and wait for the frame properly:

```gdscript
await get_tree().process_frame
await RenderingServer.frame_post_draw
```

Also: `get_texture().get_image()` on the viewport returns **RGB8** (3 bytes per pixel), not
RGBA. Compute the stride as `size / (w * h)` rather than assuming 4.

## An `await`-based input test gives a false negative

`await get_tree().process_frame` resumes **before** nodes' `_process`. Immediately after
`Input.action_release(...)`, the state the game sees is still the old one. Wait one extra
frame before asserting that a release took effect.

## Simulated input does not reach the game

Emulate keys through the same path the game reads them from
(`Input.action_press/action_release` in Godot, `game.keys.add(code)` in the JS port), not by
synthesising DOM events. A menu that listens only for `InputEventMouseButton` will not respond
to keys at all — click it by computing the button's position from the frame layout.

## The test results are not reproducible

Something outside the harness is sending input. Disable the render loop and step the physics
directly with a fixed `dt`, and take the elapsed time from the node that accumulates it rather
than from a frame count, so the result does not depend on the real frame rate.
