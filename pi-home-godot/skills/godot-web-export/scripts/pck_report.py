"""Godot 4 `.pck` inspector: what is inside, and what it costs over the wire.

    python pck_report.py web_ver/index.pck [--top 30] [--zlib]

Prints the file table, a per-extension breakdown, the biggest files, and - with
`--zlib` - how many bytes each of those would actually transfer once the server
compresses the response. That last column is the one that matters: a 2048² S3TC
texture is 5.3 MB in the pck and *also* ~4 MB on the wire (block-compressed data
does not compress), while a flat-colour atlas of the same size can shrink to
50 KB. Size on disk ranks the wrong assets.

Read-only; nothing is extracted to disk.

Godot 4 pck layout (GDPC v4, verified against 4.7.2):

    magic "GDPC" | version | ver_major | ver_minor | ver_patch | pack_flags
    file_base: u64        - data section starts here (0x70 = 112, just past
                            the header, followed by the RSRC marker block)
    dir_offset: u64       - absolute offset of the file table at the END of the
                            pack; reading `file_count` right after `file_base`
                            (the Godot 3 order) returns 0 and looks like an
                            empty pack
    then per file: path_len u32, path bytes, offset u64, size u64, md5[16],
    flags u32 - offsets are relative to `file_base` when PACK_REL_FILEBASE
    (1 << 1) is set in pack_flags.
"""

import struct
import sys
import zlib
from collections import defaultdict
from pathlib import Path

MAGIC = 0x43504447  # "GDPC"


def read_pck(path):
    """-> (pck_version, godot_version_tuple, [(name, absolute_offset, size)])"""
    with open(path, "rb") as fh:
        magic, version, vmaj, vmin, vpatch = struct.unpack("<IIIII", fh.read(20))
        if magic != MAGIC:
            raise SystemExit(f"not a pck: {hex(magic)}")
        flags = struct.unpack("<I", fh.read(4))[0]
        file_base = struct.unpack("<Q", fh.read(8))[0]
        dir_offset = struct.unpack("<Q", fh.read(8))[0]
        fh.seek(dir_offset)
        count = struct.unpack("<I", fh.read(4))[0]
        entries = []
        for _ in range(count):
            plen = struct.unpack("<I", fh.read(4))[0]
            raw = fh.read(plen)
            name = raw.split(b"\x00", 1)[0].decode("utf-8", "replace")
            offset, size = struct.unpack("<QQ", fh.read(16))
            fh.read(16)  # md5
            fh.read(4)   # flags
            entries.append((name, offset + file_base, size))
    return version, (vmaj, vmin, vpatch), entries


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        raise SystemExit(__doc__)
    path = Path(args[0])
    top = int(sys.argv[sys.argv.index("--top") + 1]) if "--top" in sys.argv else 25
    want_zlib = "--zlib" in sys.argv

    version, godot, entries = read_pck(path)
    total = sum(e[2] for e in entries)
    print(f"{path}: {len(entries)} files, {total / 1048576:.2f} MiB payload "
          f"(pck v{version}, godot {'.'.join(map(str, godot))})")

    by_ext = defaultdict(lambda: [0, 0])
    for name, _off, size in entries:
        ext = name.rsplit(".", 1)[-1].lower() if "." in name else "(none)"
        by_ext[ext][0] += 1
        by_ext[ext][1] += size
    print("\n-- by extension --")
    for ext, (n, size) in sorted(by_ext.items(), key=lambda kv: -kv[1][1])[:15]:
        print(f"{size / 1048576:9.2f} MiB  {n:5d}  .{ext}")

    print(f"\n-- top {top} by size on disk --")
    biggest = sorted(entries, key=lambda e: -e[2])[:top]
    if want_zlib:
        fh = open(path, "rb")
        rows = []
        for name, off, size in biggest:
            fh.seek(off)
            data = fh.read(size)
            rows.append((len(zlib.compress(data, 6)), size, name))
        print(f"{'raw':>9} {'zlib':>9}  {'ratio':>6}  name")
        for z, size, name in rows:
            print(f"{size / 1048576:8.2f}M {z / 1048576:8.2f}M  {z / size * 100:5.1f}%  {name}")
        print("\nSort by the zlib column before deciding what to cut: block-compressed")
        print("textures land near 100 %, PNG/OGG near 100 %, and procedural/flat")
        print("atlases can land under 20 % - those are nearly free to ship.")
    else:
        for name, _off, size in biggest:
            print(f"{size / 1048576:9.2f} MiB  {name}")


if __name__ == "__main__":
    main()
