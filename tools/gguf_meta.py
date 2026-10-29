"""Minimal GGUF metadata reader - only what the VRAM math needs.

No third-party deps: the format is a header, then length-prefixed key/value pairs, and
every value type is a fixed-size scalar, a string, or an array of them. We stop as soon
as the tensors begin (the info block ends before the tensor info table).
"""
from __future__ import annotations

import struct
from pathlib import Path

_GGUF_MAGIC = b"GGUF"

# gguf metadata value types
_T_UINT8, _T_INT8, _T_UINT16, _T_INT16, _T_UINT32, _T_INT32, _T_FLOAT32, _T_BOOL = range(8)
_T_STRING, _T_ARRAY, _T_UINT64, _T_INT64, _T_FLOAT64 = 8, 9, 10, 11, 12

_SCALAR = {
    _T_UINT8: ("<B", 1), _T_INT8: ("<b", 1),
    _T_UINT16: ("<H", 2), _T_INT16: ("<h", 2),
    _T_UINT32: ("<I", 4), _T_INT32: ("<i", 4),
    _T_FLOAT32: ("<f", 4), _T_BOOL: ("<?", 1),
    _T_UINT64: ("<Q", 8), _T_INT64: ("<q", 8), _T_FLOAT64: ("<d", 8),
}


class _Reader:
    def __init__(self, fh):
        self.fh = fh

    def raw(self, n: int) -> bytes:
        b = self.fh.read(n)
        if len(b) != n:
            raise EOFError("truncated GGUF header")
        return b

    def unpack(self, fmt: str, size: int):
        return struct.unpack(fmt, self.raw(size))[0]

    def u32(self) -> int:
        return self.unpack("<I", 4)

    def u64(self) -> int:
        return self.unpack("<Q", 8)

    def string(self) -> str:
        n = self.u64()
        if n > 1 << 24:  # a 16 MB "string" is a corrupt header, not a chat template
            raise ValueError("absurd string length in GGUF header")
        return self.raw(n).decode("utf-8", "replace")

    def value(self, vtype: int):
        if vtype in _SCALAR:
            fmt, size = _SCALAR[vtype]
            return self.unpack(fmt, size)
        if vtype == _T_STRING:
            return self.string()
        if vtype == _T_ARRAY:
            etype = self.u32()
            count = self.u64()
            # Arrays we care about are short (head counts, per-layer flags). Anything
            # huge (vocab) is skipped by type, not materialised.
            if etype == _T_STRING:
                for _ in range(count):
                    self.string()
                return "<strings>"
            if etype in _SCALAR:
                fmt, size = _SCALAR[etype]
                self.raw(size * count)
                return f"<{count} scalars>"
            raise ValueError(f"unsupported array element type {etype}")
        raise ValueError(f"unsupported GGUF value type {vtype}")


def read_metadata(path: str | Path) -> dict:
    """Return the GGUF key/value block as a dict. Raises on anything unexpected."""
    with open(path, "rb") as fh:
        r = _Reader(fh)
        if r.raw(4) != _GGUF_MAGIC:
            raise ValueError("not a GGUF file")
        version = r.u32()
        if version not in (2, 3):
            raise ValueError(f"unsupported GGUF version {version}")
        r.u64()  # tensor_count
        n_kv = r.u64()
        if n_kv > 1 << 20:
            raise ValueError("absurd metadata count")
        out: dict = {}
        for _ in range(n_kv):
            key = r.string()
            vtype = r.u32()
            try:
                out[key] = r.value(vtype)
            except ValueError:
                # An array type we do not decode still has to be stepped over, and we
                # cannot do that without knowing its element type - bail out entirely.
                raise
        return out


def describe(path: str | Path) -> dict:
    """Normalised, architecture-independent facts used by the VRAM/context math."""
    md = read_metadata(path)
    arch = str(md.get("general.architecture", "") or "")
    g = lambda k, d=None: md.get(f"{arch}.{k}", d)  # noqa: E731

    blocks = int(g("block_count", 0) or 0)
    kv_heads = g("attention.head_count_kv")
    if isinstance(kv_heads, str) or kv_heads is None:
        # Some models store an array (per layer). Fall back to head_count.
        kv_heads = g("attention.head_count", 1)
    kv_heads = int(kv_heads or 1)
    head_count = int(g("attention.head_count", kv_heads) or kv_heads)
    key_len = g("attention.key_length")
    if not key_len:
        emb = int(g("embedding_length", 0) or 0)
        key_len = emb // head_count if head_count and emb else 0
    key_len = int(key_len or 0)

    # Hybrid stacks (Qwen3.5-next & friends) only keep a full KV cache on every Nth
    # block; the rest are SSM layers with constant state. `serve-llm.cmd` measured this
    # on Qwen3.5-9B: 8 of 33 blocks are attention, 17 KiB/token at q8_0.
    interval = int(g("full_attention_interval", 0) or 0)
    if interval > 1:
        full_layers = max(1, blocks // interval)
    elif interval == 1:
        full_layers = blocks
    else:
        full_layers = blocks  # unknown -> assume the expensive case

    return {
        "arch": arch,
        "name": str(md.get("general.name", "") or ""),
        "blocks": blocks,
        "full_layers": full_layers,
        "kv_heads": kv_heads,
        "key_len": key_len,
        "ctx_train": int(g("context_length", 0) or 0),
        "has_chat_template": bool(md.get("tokenizer.chat_template")),
        "size": Path(path).stat().st_size,
        "raw": md,
    }
