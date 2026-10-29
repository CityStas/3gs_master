"""Движок политики лицензий (спека §5, §21; знания 03_license_policy.md).

Барьер 4 из четырёх. Ключевая идея: лицензионное решение принимает КОД, а не
модель. Модель передаёт строку лицензии, код отвечает «можно / нужно спросить /
нельзя». Если бы решение принимала модель, любая настойчивая формулировка в
чужом описании ассета («license: free to use!») могла бы закрыть вопрос.

Разделены два разных вопроса, которые легко перепутать:

  * `install_allowed`   — можно ли положить ассет в проект;
  * `attribution_required` — нужно ли записать автора.

CC-BY: установка разрешена, но атрибуция обязательна. Ассет с CC-BY, попавший
в проект без записанного автора, нарушает лицензию — поэтому атрибуция
проверяется как условие установки, а не как пожелание.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

# --------------------------------------------------------------------------
# Канонические лицензии. Ключ — то, что вернёт адаптер источника.
# --------------------------------------------------------------------------
CC0 = "CC0"
CC_BY = "CC-BY"
CC_BY_SA = "CC-BY-SA"
GPL = "GPL"
UNKNOWN = "UNKNOWN"

#: Лицензии, которые ставятся автоматически.
AUTO_APPROVE: frozenset[str] = frozenset({CC0, CC_BY})

#: Лицензии, требующие явного решения пользователя.
NEEDS_APPROVAL: frozenset[str] = frozenset({CC_BY_SA, GPL})

#: Лицензии, которые не устанавливаются вообще.
REJECT: frozenset[str] = frozenset({UNKNOWN})

#: Коммерческое использование.
COMMERCIAL_OK: frozenset[str] = frozenset({CC0, CC_BY})
# CC-BY-SA: коммерческое разрешено, но производное наследует лицензию (share-alike)
# -> это не «нельзя», это «спросить». Поэтому в COMMERCIAL_OK его нет,
# но и в отказе он не значится: вопрос решает пользователь.

# --------------------------------------------------------------------------
# Нормализация. Источники пишут лицензии по-разному.
# --------------------------------------------------------------------------
_NORMALIZE: list[tuple[re.Pattern, str]] = [
    (re.compile(r"^\s*cc0|public\s*domain|creative\s*commons\s*zero", re.I), CC0),
    (re.compile(r"^\s*cc[-\s]?by[-\s]?sa", re.I), CC_BY_SA),
    (re.compile(r"^\s*cc[-\s]?by\b", re.I), CC_BY),
    (re.compile(r"^\s*gpl|gnu\s+general\s+public", re.I), GPL),
]

#: Строки, которые считаются «лицензия не указана».
_EMPTY = re.compile(r"^\s*$|^(unknown|n/?a|none|unspecified|-{1,2})\s*$", re.I)


def normalize_license(raw: str | None) -> str:
    """Привести строку лицензии к канонической или вернуть UNKNOWN.

    Никогда не угадывает: неопознанная строка — это UNKNOWN, а UNKNOWN
    означает отказ. Молчаливое «наверное CC0» — прямой путь к нарушению.
    """
    if raw is None:
        return UNKNOWN
    text = raw.strip()
    if _EMPTY.match(text):
        return UNKNOWN
    for pattern, canonical in _NORMALIZE:
        if pattern.search(text):
            return canonical
    return UNKNOWN


@dataclass
class LicenseVerdict:
    """Результат проверки лицензии. Формат соответствует §10 спеки."""
    license: str
    commercial_use: bool
    attribution_required: bool
    redistribution_allowed: bool
    automatic_install_allowed: bool
    reason: str = ""
    requirements: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "license": self.license,
            "commercial_use": self.commercial_use,
            "attribution_required": self.attribution_required,
            "redistribution_allowed": self.redistribution_allowed,
            "automatic_install_allowed": self.automatic_install_allowed,
            "reason": self.reason,
            "requirements": self.requirements,
        }


def evaluate(raw_license: str | None) -> LicenseVerdict:
    """Решение по лицензии. Точка входа для всего остального кода."""
    lic = normalize_license(raw_license)

    if lic == CC0:
        return LicenseVerdict(
            license=CC0, commercial_use=True, attribution_required=False,
            redistribution_allowed=True, automatic_install_allowed=True,
            reason="CC0: ограничений нет",
        )

    if lic == CC_BY:
        return LicenseVerdict(
            license=CC_BY, commercial_use=True, attribution_required=True,
            redistribution_allowed=True, automatic_install_allowed=True,
            reason="CC-BY: установка разрешена, но авторство обязательно к записи",
            requirements=[
                "записать в asset.json: author, source_url, license, download_url",
                "атрибуция должна быть видна в игре (титры/экран благодарностей)",
            ],
        )

    if lic == CC_BY_SA:
        return LicenseVerdict(
            license=CC_BY_SA, commercial_use=False, attribution_required=True,
            redistribution_allowed=True, automatic_install_allowed=False,
            reason="CC-BY-SA: share-alike, требуется решение пользователя",
            requirements=[
                "производное произведение наследует лицензию CC-BY-SA",
                "установка только с явного согласия пользователя",
            ],
        )

    if lic == GPL:
        return LicenseVerdict(
            license=GPL, commercial_use=False, attribution_required=True,
            redistribution_allowed=True, automatic_install_allowed=False,
            reason="GPL: лицензия кода, требуется решение пользователя",
            requirements=[
                "GPL в ассетах игры требует юридического разбора",
                "установка только с явного согласия пользователя",
            ],
        )

    return LicenseVerdict(
        license=UNKNOWN, commercial_use=False, attribution_required=True,
        redistribution_allowed=False, automatic_install_allowed=False,
        reason="лицензия не определена — установка запрещена",
        requirements=[
            "найти лицензию на странице ассета и указать её явно",
            "без определённой лицензии ассет в проект не ставится",
        ],
    )


def check_installable(verdict: LicenseVerdict, approved_by_user: bool = False) -> tuple[bool, str]:
    """Можно ли ставить ассет. Возвращает (можно, причина отказа)."""
    if verdict.license in REJECT:
        return False, verdict.reason
    if verdict.automatic_install_allowed:
        return True, ""
    if approved_by_user:
        return True, ""
    return False, (
        f"{verdict.license} требует подтверждения пользователя. "
        f"Повтори вызов с явным согласием после его получения."
    )


def needs_attribution(verdict: LicenseVerdict) -> bool:
    return verdict.attribution_required


def check_attribution_complete(manifest: dict) -> tuple[bool, str]:
    """Проверить, что для требующей атрибуции лицензии всё записано.

    Вызывается перед установкой: CC-BY без автора — незакрытое требование
    лицензии, и установка такого ассета создаёт риск, а не решает задачу.
    """
    verdict = evaluate(manifest.get("license"))
    if not verdict.attribution_required:
        return True, ""
    missing = [f for f in ("author", "source_url", "license", "download_url")
               if not str(manifest.get(f) or "").strip()]
    if missing:
        return False, (
            f"лицензия {verdict.license} требует атрибуции, не заполнено: "
            f"{', '.join(missing)}"
        )
    return True, ""
