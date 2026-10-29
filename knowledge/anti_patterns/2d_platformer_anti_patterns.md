# 2D platformer anti-patterns

Failure modes that look like a bug in the engine but are design mistakes in the level, the
collision derivation, or the test harness. Each one cost real debugging time on a real
project.

## Collision and terrain

- **Do not derive the walkable surface from the top opaque pixel of a column.** Decorative
  props grow on ledges and their caps become the surface. The character then walks on
  mushrooms. Use the run that reaches the ground band, plus a support test. See
  `art_to_collision_platformer.md`.
- **Do not treat an opaque-but-thin feature as ground.** Mist banks along the bottom edge are
  nearly opaque. Measure *thickness*, not opacity.
- **Do not let a smoothing filter invent terrain.** Any filter that ignores `None` (no
  terrain) in its window will grow cliffs into chasms. Re-apply the `None` mask after
  filtering.
- **Do not make a collider thinner than `max_fall_speed * dt`.** At 700 px/s and 1/60 s that
  is 11.7 px; a 5-7 px platform collider is passed straight through.
- **Do not put a collider's centre on the surface line.** Half the box ends up above the art.
- **Do not place a prop collider by its texture bbox.** Transparent padding and decorative
  sprigs put the box above the visible surface.
- **Do not build the terrain as a polygon to be navigated around.** A platformer's ground is
  an infinitely deep heightfield. A general polygon solver makes the character snag on
  interior edges.
- **Do not use the character's sprite width as its collision width.** A wide drawn sprite with
  a narrow hitbox is normal and desirable — it stops the character catching on scenery. Do not
  "fix" the resulting visual overlap.

## Motion

- **Do not resolve Y before X.** A character walking up a slope stands at the new height and
  then collides with it sideways, and sticks.
- **Do not omit the step-up allowance** on a profile derived from art. The profile is a curve;
  without `STEP_UP` the character catches on every pixel.
- **Do not derive camera position by arithmetic on the character position** when the camera
  has limits. Convert world rectangles to screen with the viewport's canvas transform, or the
  centre of the frame will not be where you computed it.

## Levels and content

- **Do not reuse the previous level's props "because they fit".** A continuation level that
  reuses the first level's platform sprite reads as a repaint. Generate new art for anything
  the player sees as a landmark.
- **Do not place enemies on one shared patrol range.** Two enemies with the same range
  converge on one coordinate and walk as a stack. Give each its own window, clamped to the
  platform it stands on.
- **Do not let a layer exist that contributes nothing.** A fully transparent layer still costs
  a draw and still appears in the build report as "produced". Assert opacity when you build
  it.
- **Do not put a blocking obstacle where the player cannot see why they stopped.** If the
  collider and the art disagree by even 20 px, it reads as an invisible wall.

## Text and UI

- **Do not fade a pixel-font label with alpha.** Translucent glyphs read as "the letters are
  showing through" and get reported as a bug. Toggle visibility.
- **Do not move pixel text by a fractional amount.** Bold pixel fonts overlap adjacent
  rectangles; at a fractional offset the rasterisation phase changes per glyph and the text
  jitters. Round every animated offset.
- **Do not build the HUD in DOM/CSS.** Rounded corners and system fonts next to pixel art read
  as web UI over a game.

## Testing

- **Do not verify a long level with one screenshot.** A screenshot of a character standing
  still says nothing about 3500 px of terrain.
- **Do not run a physics test through the real render loop** when real input can reach the
  page. Disable the loop and step the physics yourself, or external input will move the
  character mid-test and the results will be irreproducible.
- **Do not trust a test harness that shares a browser with the user.** An unexplained
  character drift was traced to input from outside the harness, not to the game.
- **Do not read a screenshot as evidence the file on disk changed.** Browsers serve stale
  content; add `cache: 'no-cache'` to hand-edited content fetches before believing a fix did
  nothing.
- **Do not conclude "the game auto-starts" from a screenshot test.** `page.screenshot()` in
  some harnesses clicks the viewport centre, which lands on a centred menu button.
- **Do not check a build's freshness by file size.** Editing a float coordinate or a frequency
  changes the bytes, not the size. Compare mtimes, and if necessary search the binary for the
  packed value (`struct.pack('<ff', x, y)` for a `Vector2`).

## Process

- **Do not hand-port a scene between engines.** Keep one source of truth and generate the
  other representation from it, or the two drift and the port stops being a port.
- **Do not merge the debug/parity viewer into the game page.** The viewer's value is that it
  is a clean "does the generated representation equal the source" check.
- **Do not assume a scene file survives an editor round-trip.** Nodes get dropped; diff the
  scene before and after editing it.
