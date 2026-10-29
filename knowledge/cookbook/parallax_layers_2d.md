# Parallax layers for a painted 2D level: ordering, masks and alpha

## When to use

A 2D level's background is built from several wide painted strips that scroll at different
speeds. You have generated art for the layers and need to place them so that each one is
actually visible, and so the whole thing reads as depth rather than as a flat backdrop with a
mushy middle.

## Layer order is decided by opacity, not by distance

The instinct is "far layers go behind". It is wrong when the far layer is **opaque**: anything
you place behind an opaque layer is never seen. A generated "far background" is usually a
complete scene including its own sky, so it is opaque by construction (it is generated
without a mask).

Consequence: a layer that is supposed to sit *between* far and mid must be placed **in front
of** the opaque far layer, and must therefore have a mask — you need to see the sky through
it. In the reference project the depth order is:

| Layer | Scroll x | Depth | Opaque? |
|---|---|---|---|
| Backdrop (flat colour) | — | -200 | yes |
| far_back | 0.25 | -100 | yes (generated without mask) |
| **far_mid** | 0.38 | -99 | no — masked silhouette strip |
| mid | 0.5 | -98 | no — masked framing strip |
| gameplay | 1.0 | -4 | no — the walkable strip |
| props | 1.0 | -3..3 | no |

The far_mid layer is *closer* than far_back in parallax terms but sits *in front* of it. That
is not a contradiction, it is the only way an opaque far layer can have anything in front of
it.

## Scroll scales must be spread, and 1.0 is the gameplay plane

0.25 / 0.38 / 0.5 / 1.0 gives four distinct rates. Two layers at the same rate read as one
layer. Anything that the character collides with must scroll at 1.0.

## Masking a layer: BiRefNet is the wrong tool for haze

`kind: mask` (BiRefNet) segments a **salient object**. A full-screen parallax strip has no
salient object, and the model returns an **empty mask** — silently. The result is a layer that
is 100 % transparent in the scene, and the "new depth layer" renders nothing while every
build report still says the file was produced.

Check it explicitly; a mask job reporting success is not evidence of content:

```python
alpha = np.array(Image.open(out).convert("RGBA"))[:, :, 3]
print(f"opaque {100 * (alpha > 8).mean():.0f}%")     # 0% == the job produced nothing
```

For a depth/haze layer the right alpha is a **soft luminance key**, because depth in a painted
layer is drawn as brightness: distant haze is light, near silhouettes are dark.

```python
lum = 0.299*r + 0.587*g + 0.114*b
alpha = clip((THR - lum) / SOFT, 0, 1)
```

This gives a soft edge, which is what a haze layer wants — a binary cut-out would look like
cardboard. Calibrate the threshold by compositing the keyed layer over the layer it will sit
on and looking at the result:

| THR | Opaque | Result |
|---|---|---|
| 70 | 82 % | whole screen goes dark, the far nebula disappears — too much |
| 45 | 46 % | still closes off the sky |
| 35 | 22 % | only vine/foliage silhouettes remain, sky shows through — correct |

The threshold is not portable between layers; it depends on how dark the generated art is.
22 % opaque was the right answer for a "cave interior framing" strip, and the only way to
find it was to render the composite at three settings and compare.

## Make the gameplay layer readable

The walkable strip should be generated with a prompt that asks for a **crisp silhouette
against the sky** and "the solid ground filling the entire lower third edge to edge". Layers
behind it are allowed to be low-contrast and foggy; the gameplay layer must not be, because
collision is derived from its alpha (see `art_to_collision_platformer.md`).

## Stretching: one uniform factor

Level strips are a fixed aspect (3:1 in the reference project: 2170x725) while generators emit
2.67:1 (2048x768). Crop to the target aspect by centre and scale by **one** factor for both
axes. Scaling x and y by different factors makes a parallax layer drift relative to its
neighbours, because its apparent scroll rate is a function of its width.

## Verify

Render the whole level with all layers composited in world space and look at it. Seams
between repeated strips, a layer that covers the sky, and a layer that contributes nothing
are all obvious in one image and invisible in a per-file report.
