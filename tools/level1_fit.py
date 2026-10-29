#!/usr/bin/env python
"""Fit generated level layers onto the exact texture size the web3d scene expects.

The generators produce whatever aspect their workflow is configured for (z-image
returns 1856x768 for a "21:9" request - 2.417:1, not the 2.333:1 the name suggests).
The parallax tiles in `web3d/level.json` are built from the level_0 reference layers,
which are 2170x725 (2.993:1) for far/mid and 2172x724 for gameplay.

**Matching the reference size is mandatory, not cosmetic.** `scene.js` builds a
Parallax2D layer as `content.clone(true)` at `k * repeat` - a hard-edged neighbour, not
a wrap - and `sector2.json` swaps this texture onto the ODD tiles only, leaving the even
tiles as the level_0 originals. So a new layer sits directly beside a reference layer,
painted on the same plane geometry. If the sizes disagree the two are scaled to the
plane differently and the seam jumps at every tile boundary as the camera scrolls.

So the source is scaled to the target WIDTH and the excess height is cropped away. The
sources are 1856x768 (2.417:1) and the target is 2.993:1 - wider - so the source has
spare height, not spare width. Scaling up x1.169 to the target width and dropping 173px
of height keeps the art edge to edge with no transparent gaps, and the 19% it discards
is vertical margin - which is exactly where the prompts put the least detail ("darker
toward the bottom edge for a parallax layer").

`anchor` decides which vertical margin survives, because the layers are not symmetric:
`far_back` must keep its horizon and ground, `mid_layer` must keep the canopy hanging
from the top. Anchoring is per-file and overridable from the command line.

Two things that are easy to get wrong and are handled here:

  * **Alpha must be premultiplied before the resize.** `mid_layer` and `gameplay_layer`
    are RGBA cut-outs; the RGB of a fully transparent pixel is meaningless (often black),
    and a plain LANCZOS resize blends it into the visible edge, leaving a dark fringe
    around every island. Premultiply -> resize -> unpremultiply removes it.
  * **The output mode must match the reference.** `far_back.png` is RGB (a full
    background, nothing to cut out); `mid_layer.png`/`gameplay_layer.png` are RGBA. The
    source mode is preserved rather than normalising everything to RGBA.

Usage
-----
    python tools/level1_fit.py                    # ded_test level_1 (raw -> final)
    python tools/level1_fit.py --check            # report sizes only, write nothing
    python tools/level1_fit.py --subdir Shrooms/level_0 --in-place   # regression check
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from threejs import config  # noqa: E402

try:
    from PIL import Image
except ImportError:  # pragma: no cover - the message is the point
    raise SystemExit(
        "Pillow is required:  .venv/Scripts/python.exe -m pip install Pillow"
    )

try:
    import numpy as np
except ImportError:  # pragma: no cover
    np = None


# Target geometry, taken from level.json's texture table - the level_0 reference layers
# are the source of truth, not the generator's nominal aspect.
#
#   size   - the exact pixel size the plane geometry was built against
#   anchor - which vertical band survives the height crop:
#              "bottom" keeps the horizon and ground (far background, islands)
#              "top"    keeps the canopy hanging from above (mid layer)
#   source - path relative to --subdir; None means "already at the target name".
#            `far-back-2` is generated into raw/ because a background needs no mask,
#            while mid/gameplay are written straight to their final name by BiRefNet.
LAYERS = {
    "far_back.png":       {"size": (2170, 725), "anchor": "bottom",
                           "source": "raw/far_back_2.png"},
    "mid_layer.png":      {"size": (2170, 725), "anchor": "top",
                           "source": None},
    "gameplay_layer.png": {"size": (2172, 724), "anchor": "bottom",
                           "source": None},
}


def _resize(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    """LANCZOS resize that does not bleed transparent pixels into the edges."""
    if img.mode != "RGBA" or np is None:
        return img.resize(size, Image.LANCZOS)

    a = np.asarray(img, dtype=np.float32) / 255.0
    rgb, alpha = a[..., :3], a[..., 3:4]
    pm = Image.fromarray(
        (np.concatenate([rgb * alpha, alpha], axis=-1) * 255.0 + 0.5).astype(np.uint8),
        "RGBA")
    out = np.asarray(pm.resize(size, Image.LANCZOS), dtype=np.float32) / 255.0
    rgb2, alpha2 = out[..., :3], out[..., 3:4]
    with np.errstate(divide="ignore", invalid="ignore"):
        unpm = np.where(alpha2 > 0, rgb2 / np.maximum(alpha2, 1e-6), 0.0)
    return Image.fromarray(
        (np.concatenate([np.clip(unpm, 0, 1), alpha2], axis=-1) * 255.0 + 0.5)
        .astype(np.uint8), "RGBA")


def _alpha_stats(img: Image.Image) -> str:
    """Fraction of the frame that is not fully transparent - catches a mask that
    cut everything away, which otherwise looks like a perfectly fine PNG."""
    if img.mode != "RGBA" or np is None:
        return "opaque"
    a = np.asarray(img)[..., 3]
    return f"{100.0 * (a > 8).mean():.1f}% opaque"


def fit(src_path: Path, dst_path: Path, target: tuple[int, int], *,
        anchor: str = "bottom", check: bool = False) -> dict:
    """Scale `src_path` to the target width, crop the excess height, write to `dst_path`."""
    tw, th = target
    src = Image.open(src_path)
    sw, sh = src.size
    mode = src.mode

    if (sw, sh) == (tw, th):
        detail = "already the target size"
        if not check and src_path != dst_path:
            src.save(dst_path, "PNG", optimize=True)
            detail += f", copied to {dst_path.name}"
        return {"src": src_path, "dst": dst_path, "from": (sw, sh), "to": (tw, th),
                "mode": mode, "detail": detail, "changed": src_path != dst_path}

    s = tw / sw
    nh = round(sh * s)
    resized = _resize(src, (tw, nh))

    extra = nh - th
    if extra < 0:
        # target is TALLER than the source aspect: padding is unavoidable, so centre
        # on a transparent canvas rather than distorting the art.
        out = Image.new("RGBA" if mode == "RGBA" else "RGB", (tw, th),
                        (0, 0, 0, 0) if mode == "RGBA" else (0, 0, 0))
        out.paste(resized, (0, (th - nh) // 2))
        detail = f"scale x{s:.4f} -> {tw}x{nh}, pad {th - nh}px height (centred)"
    else:
        top = 0 if anchor == "top" else (extra // 2 if anchor == "center" else extra)
        out = resized.crop((0, top, tw, top + th))
        detail = (f"scale x{s:.4f} -> {tw}x{nh}, crop {extra}px height "
                  f"(anchor={anchor})")

    stats = _alpha_stats(out)
    if check:
        return {"src": src_path, "dst": dst_path, "from": (sw, sh), "to": (tw, th),
                "mode": mode, "detail": "would " + detail, "stats": stats,
                "changed": True}

    out.save(dst_path, "PNG", optimize=True)
    return {"src": src_path, "dst": dst_path, "from": (sw, sh), "to": (tw, th),
            "mode": mode, "detail": detail, "stats": stats, "changed": True}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project", "-p", default="projects/games/my_game")
    ap.add_argument("--subdir", default="Shrooms/level_1")
    ap.add_argument("--check", action="store_true", help="report only, write nothing")
    ap.add_argument("--in-place", action="store_true",
                    help="ignore the source map; every layer is already at its final name")
    ap.add_argument("--anchor", choices=("top", "bottom", "center"),
                    help="override the vertical anchor for every layer")
    args = ap.parse_args()

    project = config.resolve_project(args.project)
    root = project / args.subdir
    if not root.is_dir():
        raise SystemExit(f"no such directory: {root}")

    print(f"project : {project}")
    print(f"layers  : {root}")
    print(f"mode    : {'CHECK ONLY' if args.check else 'writing PNGs'}\n")

    problems: list[str] = []
    for name, spec in LAYERS.items():
        target = spec["size"]
        anchor = args.anchor or spec["anchor"]
        dst = root / name
        src_rel = None if args.in_place else spec["source"]
        src = (root / src_rel) if src_rel else dst

        if not src.exists():
            if dst.exists():
                src = dst            # fall back to the final file if the raw is gone
            else:
                print(f"  MISSING  {name}  (no source at {src})")
                problems.append(f"{name}: no source")
                continue

        r = fit(src, dst, target, anchor=anchor, check=args.check)
        fw, fh = r["from"]
        flag = "ok  " if (fw, fh) == target else "FIT "
        origin = f"from {src_rel}" if src_rel else "in place"
        print(f"  {flag} {name:20s} {fw}x{fh} {r['mode']:4s} ({origin})")
        print(f"       -> {target[0]}x{target[1]} {r['mode']:4s}  {r['detail']}")
        if "stats" in r:
            print(f"       {r['stats']}")

    print()
    if problems:
        print(f"{len(problems)} layer(s) not ready - run the pack first:")
        print("  .venv/Scripts/python.exe tools/generate.py --project projects/games/my_game "
              "--jobs assets/packs/ded_test_level1.json")
        return 1
    print("check complete (nothing written)" if args.check
          else "all layers written at the reference size")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
