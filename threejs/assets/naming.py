"""Deterministic asset naming.

ComfyUI writes `ComfyUI_00007_.glb` / `Qwen21/t2i_00003.png` and increments a counter on
every run. Those names are useless downstream: a three.js scene cannot reference
`ComfyUI_00007_.glb` and mean anything, and two runs are indistinguishable.

So every artefact produced by this pipeline is written to `assets/<kind>/` under a slug
derived from the request that produced it, with a numeric suffix only on collision.

Cyrillic prompts are transliterated rather than dropped - the user writes Russian and a
slug like `personazh-rycar` beats `asset-3f9a`.
"""
from __future__ import annotations

import re
from pathlib import Path

_CYR = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", "ж": "zh",
    "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o",
    "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "ts",
    "ч": "ch", "ш": "sh", "щ": "sch", "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu",
    "я": "ya",
}
# Tokenizer must be unicode-aware: `[^a-z0-9]+` eats Cyrillic *before* transliteration
# can see it, and every token collapses to nothing. Split first, transliterate after.
_WORD_SPLIT = re.compile(r"[^\w]+", re.UNICODE)
_NON_SLUG = re.compile(r"[^a-z0-9]+")

# Words that carry no identifying information and only bloat the filename.
_STOP = {
    "a", "an", "the", "of", "and", "or", "in", "on", "at", "to", "for", "with",
    "create", "make", "generate", "render", "please", "image", "picture", "photo",
    "model", "asset", "3d", "character", "создай", "сделай", "сгенерируй", "картинка",
    "модель", "персонаж", "изображение",
}


def translit(text: str) -> str:
    out = []
    for ch in text.lower():
        out.append(_CYR.get(ch, ch))
    return "".join(out)


def slugify(text: str, max_len: int = 48, keep_stopwords: bool = False) -> str:
    """`"Создай синего мохнатого монстра"` -> `sinego-mohnatogo-monstra`.

    Stop-words are filtered on the *original* tokens: transliterating first turns
    `создай` into `sozday`, which no stop-word list would ever match.
    """
    raw_tokens = [t for t in _WORD_SPLIT.split(str(text or "").lower()) if t]
    if not keep_stopwords:
        kept = [t for t in raw_tokens if t not in _STOP]
        if kept:
            raw_tokens = kept
    s = _NON_SLUG.sub("-", translit("-".join(raw_tokens))).strip("-")
    if not s:
        return "asset"
    s = "-".join(p for p in s.split("-") if p)[:max_len].strip("-")
    return s or "asset"


def unique_path(directory: Path, slug: str, suffix: str, ext: str) -> Path:
    """`assets/3d/monster.glb`, then `monster-2.glb`, `monster-3.glb` ..."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    name = f"{slug}{suffix}{ext}"
    candidate = directory / name
    n = 2
    while candidate.exists():
        candidate = directory / f"{slug}{suffix}-{n}{ext}"
        n += 1
    return candidate


def derive_name(prompt: str = "", explicit: str = "") -> str:
    """An explicit `name` always wins; otherwise the prompt decides."""
    if explicit and str(explicit).strip():
        return slugify(explicit)
    return slugify(prompt)
