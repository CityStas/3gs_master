# 2D game project rules

Rules that hold for any 2D game inside this repository. They exist because each one was
violated and produced a defect that looked like an engine bug.

## One source of truth per level

A level has exactly one authored representation and any number of generated ones.

- If the level exists in Godot, `Main.tscn` is the source and the JSON is generated from it.
- If the level is generated from art, the **art plus the build script** is the source, and the
  JSON is generated. The JSON is never edited by hand.

Never hand-edit both sides. The whole point of the intermediate JSON is that it is diffable
and reproducible.

## Collision is derived, and then verified visually

Any collision derived from art must be rendered **on top of** that art before it is trusted.
A build report with node counts and coordinate ranges is not evidence of alignment. The check
is an image.

## The game's look is a specification

When a working implementation already exists (another engine, another level), its constants
are the specification: icon sizes, margins, easing rates, pulse frequencies, string case.
Port the numbers, not the impression. "Close enough" values are how a port stops looking like
the original.

## Generated art is raw material

Cropping to the level's aspect ratio and a uniform scale are always applied; never stretch
axes independently. Masks are part of the asset, not an afterthought: a layer whose job is to
show the sky through it must have one, and its coverage must be asserted at build time.

## Every visual claim needs a test that can fail

- "The character walks on the ground" → histogram of `feet - terrain` over a simulated walk.
- "The collider matches the art" → an overlay render.
- "The level is traversable" → a scripted walk from spawn to the exit, reporting where it
  stopped.
- "The layer is visible" → its alpha coverage percentage.
- "The pixel HUD matches" → a screenshot at a fixed viewport size.

If a claim cannot fail, it is not a test.

## Localisation lives in data, not in the renderer

The pixel font has a fixed charset (`A-Z 0-9 ! : . - /`). UI strings must be authored in that
alphabet and stored in the level manifest / config, so a level's copy can be changed without
touching rendering code. Do not add glyphs to work around a string.

## Determinism before convenience

A test that runs through the real frame loop is not reproducible on a machine that also has a
human at the keyboard or a second browser open. Disable the loop, step the physics with a
fixed `dt`, and force the state you need. Prefer reading the simulation state directly over
inferring it from pixels.
