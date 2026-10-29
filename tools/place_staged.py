"""Copy a pack's staged artefacts to the paths the pack declares.

The scheduler places artefacts only when a pack runs to completion, and it
*removes* them from staging as it goes (`os.replace`). That is the right default
- a half-finished pack must not leave half a scene on disk - but it means a pack
that is stopped, or a partial re-run, leaves good work stranded in
`data/gen-staging/<run>/`.

This does the same mapping the scheduler does, without the move:

    <run>/images/<job-name>.png          ->  <project>/<job.out>
    <run>/masks/<job-name>-nobg.png      ->  <project>/<job.out>
    <run>/3d/<job-name>.glb              ->  <project>/<job.out>

Usage:
  python tools/place_staged.py --project projects/games/my_game \\
      --jobs projects/games/my_game/tools/pack.json \\
      --run data/gen-staging/20261008-034634 [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

SUBDIR = {"image": "images", "mask": "masks", "3d": "3d", "upscale": "images"}


def load_pack(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["jobs"] if isinstance(data, dict) else data


def find_staged(run: Path, job: dict) -> Path | None:
    """Locate a job's file in the staging tree.

    Matched by *prefix* rather than by an exact name: the pipeline writes
    `<slug><suffix><ext>` where the slug comes from `naming.derive_name`, which
    normalises and may transliterate, so the on-disk name is not guaranteed to
    be the job name byte for byte.
    """
    sub = SUBDIR.get(str(job.get("kind")), "3d")
    directory = run / sub
    if not directory.is_dir():
        return None
    stem = job["name"]
    for suffix in ("", "-nobg"):
        for ext in (".glb", ".spz", ".png", ".jpg", ".mp4"):
            hit = directory / f"{stem}{suffix}{ext}"
            if hit.exists():
                return hit
    # Fall back to a prefix scan.
    for candidate in sorted(directory.iterdir()):
        if candidate.stem.startswith(stem):
            return candidate
    return None


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--jobs", required=True)
    ap.add_argument("--run", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv[1:])

    project = Path(args.project).resolve()
    run = Path(args.run).resolve()
    jobs = load_pack(Path(args.jobs))

    placed = skipped = missing = 0
    for job in jobs:
        out = str(job.get("out") or "").strip()
        if not out:
            continue
        src = find_staged(run, job)
        if src is None:
            missing += 1
            print(f"  MISS  {job['name']:<22} (nothing in staging)")
            continue
        dst = project / out
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists() and dst.stat().st_size == src.stat().st_size:
            skipped += 1
            print(f"  same  {job['name']:<22} -> {out}  ({src.stat().st_size:,} B)")
            continue
        if args.dry_run:
            print(f"  WOULD {job['name']:<22} -> {out}  ({src.stat().st_size:,} B)")
        else:
            shutil.copy2(src, dst)
            print(f"  COPY  {job['name']:<22} -> {out}  ({src.stat().st_size:,} B)")
        placed += 1

    print(f"\nplaced={placed} already={skipped} missing={missing}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
