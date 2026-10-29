#!/usr/bin/env python3
"""Плоский ключ фона для character-sheet: цвет угла -> альфа.

Зачем отдельно от `remove_bg`. Штатный вырез в пайплайне - BiRefNet, а это
salient-object сегментатор, обученный на **одном** субъекте. На листе из четырёх
фигур он может склеить панели в одну маску или потерять дальние ракурсы. Когда
лист сгенерирован на заведомо плоском фоне, ключ по цвету и дешевле, и
предсказуемее - и это ровно то, что нужно multiview-ноде, потому что она
композитит `rgb * alpha`.

    python tools/sheet_key.py sheet.png                    # -> sheet-keyed.png рядом
    python tools/sheet_key.py sheet.png -o out.png --tol 20
    python tools/sheet_key.py sheet.png --dry-run           # только боксы панелей

Фон берётся как **медиана цветов четырёх углов**: одиночный угол может попасть
на тень или на деталь, медиана - нет.

Альфа не бинарная, а рампой `tol .. tol+feather`: жёсткий порог оставляет по
контуру кайму из пикселей фона, и на меше это читается как «шов» вдоль силуэта.

Считается на numpy: лист 2048x2048 - это 4.2 млн пикселей, и питоновский цикл
по ним занимает десятки секунд против десятых долей у массива.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import numpy as np
    from PIL import Image
except ImportError:  # pragma: no cover
    raise SystemExit(
        "нужны Pillow и numpy: ./.venv/Scripts/python.exe -m pip install Pillow numpy")

#: Нижняя граница порога «похоже на фон» в RGB-евклиде, 0..441.
#: На идеально плоском фоне остаётся зерно сенсора в единицы единиц, и порог ниже
#: этого начинает собирать зерно как содержимое - поэтому снизу автоподбор упирается
#: именно сюда, а не в ноль.
MIN_TOL = 18.0
#: Сетка кандидатов для автоподбора: 18 -> ~215 геометрически.
_TOL_GRID = tuple(round(MIN_TOL * (1.18 ** i), 1) for i in range(16))
#: Ширина рамки перехода, чтобы контур не звенел.
DEFAULT_FEATHER = 8.0


def _corner_colour(rgb: np.ndarray, sample: int = 12) -> np.ndarray:
    """Медиана цветов четырёх угловых площадок."""
    h, w, _ = rgb.shape
    s = max(1, min(sample, w // 4, h // 4))
    corners = np.concatenate([
        rgb[0:s, 0:s].reshape(-1, 3),
        rgb[0:s, w - s:w].reshape(-1, 3),
        rgb[h - s:h, 0:s].reshape(-1, 3),
        rgb[h - s:h, w - s:w].reshape(-1, 3),
    ])
    return np.median(corners, axis=0)


def _border_spread(rgb: np.ndarray, band: int = 8) -> tuple[float, float]:
    """Разброс цвета по рамке изображения: (медиана, максимум) расстояния до медианы.

    Плоский фон даёт почти нулевой разброс. Виньетка или градиент дают разброс
    **больше `tol`** - и тогда ключ по одному цвету неминуемо примет фон за
    содержимое. Снаружи это выглядит как «заполнение 1.00» в отчёте по панелям,
    то есть bbox упирается в края и общий кроп раздувается на весь лист.
    Дешевле увидеть это здесь, чем потом гадать, почему меш вышел сплющенным.
    """
    h, w, _ = rgb.shape
    b = max(1, min(band, h // 8, w // 8))
    ring = np.concatenate([
        rgb[0:b, :].reshape(-1, 3),
        rgb[h - b:h, :].reshape(-1, 3),
        rgb[:, 0:b].reshape(-1, 3),
        rgb[:, w - b:w].reshape(-1, 3),
    ])
    med = np.median(ring, axis=0)
    d = np.sqrt(((ring - med) ** 2).sum(axis=1))
    return float(np.median(d)), float(d.max())


def _otsu(dist: np.ndarray, bins: int = 256, hi: float = 441.0) -> float:
    """Порог Оцу по карте расстояний до цвета фона.

    Карта расстояний почти всегда бимодальна: пик около нуля (фон) и широкий
    горб (фигура). Порог Оцу максимизирует межклассовую дисперсию, то есть
    проходит по минимуму между модами - ровно туда, куда мы бы поставили `tol`
    руками, перебирая значения и глядя на «заполнение» панелей.

    Это и есть замена ручному подбору: на листе с виньеткой разброс фона по
    рамке был 64.7 при `tol` по умолчанию 18, и ключ принимал градиент за
    содержимое. Оцу находит границу сам.

    На практике Оцу здесь - только **запасной** вариант. Он предполагает, что
    классы сопоставимы по размеру, а на листе фон занимает 85-90 % кадра: при
    светлой фигуре максимум межклассовой дисперсии уезжает вверх (109 против
    рабочих 70) и съедает светлые части силуэта. Основной путь - `_auto_tol`.
    """
    hist, edges = np.histogram(dist, bins=bins, range=(0.0, hi))
    hist = hist.astype(np.float64)
    total = hist.sum()
    if total <= 0:
        return 0.0
    p = hist / total
    centres = (edges[:-1] + edges[1:]) / 2.0
    omega = np.cumsum(p)
    mu = np.cumsum(p * centres)
    mu_total = mu[-1]
    denom = omega * (1.0 - omega)
    denom = np.where(denom <= 1e-12, 1e-12, denom)
    sigma_b = (mu_total * omega - mu) ** 2 / denom
    return float(centres[int(np.argmax(sigma_b))])


def _auto_tol(dist: np.ndarray, cols: int, rows: int,
              margin_frac: float = 0.01) -> tuple[float, str]:
    """Наименьший порог, при котором ни одна панель не «упирается» в свои края.

    Операционное определение «фон принят за содержимое» - это ровно то, что видно
    глазами в отчёте по панелям: bbox доходит до границы панели, заполнение
    становится 1.00, а общий кроп раздувается на весь лист. Значит, порог можно
    подобрать не по гистограмме, а по этому же признаку: взять **минимальный**
    `tol`, при котором у каждой панели есть отступ от края и при этом хоть что-то
    осталось.

    Почему не Оцу и не процентиль по рамке. Оцу предполагает сопоставимые по
    размеру классы, а фон занимает 85-90 % кадра - на виньетированном листе он дал
    109 против рабочих 70. Процентиль по рамке ломается в другую сторону: если
    фигура задевает край кадра (а на сетке 3x2 дальние ракурсы именно задевают),
    рамка перестаёт быть «заведомо фоном» и её p99.5 уезжает в 216-248, то есть
    порог стирает всё. Признак «bbox упёрся в край» не зависит ни от того, как
    распределены яркости, ни от того, чист ли край кадра.

    Отступ задан долей от меньшей стороны панели: у панели 512 и у панели 1024
    один и тот же процент означает разное число пикселей, а нам нужен именно
    относительный зазор.
    """
    h, w = dist.shape
    if w % cols or h % rows:
        return _otsu(dist), "Оцу (размер не делится на сетку нацело)"
    pw, ph = w // cols, h // rows
    m = max(2, int(round(min(pw, ph) * margin_frac)))

    # Шаг 2 по обеим осям: bbox от этого не сдвигается больше чем на пиксель, а
    # перебор полутора десятков порогов по 4 млн пикселей дешевеет вчетверо.
    ds = dist[::2, ::2]
    pws, phs = max(1, pw // 2), max(1, ph // 2)
    ms = max(1, m // 2)

    for tol in _TOL_GRID:
        for i in range(cols * rows):
            cx, cy = i % cols, i // cols
            sub = ds[cy * phs:(cy + 1) * phs, cx * pws:(cx + 1) * pws]
            mask = sub > tol
            if not mask.any():
                break
            rows_hit = np.flatnonzero(mask.any(axis=1))
            cols_hit = np.flatnonzero(mask.any(axis=0))
            if (rows_hit[0] <= ms or cols_hit[0] <= ms
                    or rows_hit[-1] >= phs - 1 - ms or cols_hit[-1] >= pws - 1 - ms):
                break
        else:
            return tol, (f"подбор по отступу от края панели "
                         f"(сетка {MIN_TOL:.0f}..{_TOL_GRID[-1]:.0f})")

    return _otsu(dist), "Оцу (ни один порог не дал отступа от края)"


def _bg_surface(rgb: np.ndarray, band_frac: float = 0.03) -> np.ndarray:
    """Оценка фона как квадратичной поверхности, подогнанной по рамке кадра.

    Зачем не один цвет. У сгенерированных листов фон почти всегда с виньеткой или
    градиентом: на нашем листе разброс по рамке доходил до 64.7, при том что сама
    фигура светлая (кожа, светло-песочная куртка). Глобальный порог в такой
    ситуации обречён: он либо оставляет виньетку - и тогда bbox упирается в края
    панели, а общий кроп раздувается на весь лист, - либо съедает светлые части
    фигуры. Ровно это и наблюдалось: `tol=18` давал заполнение 1.00, а автопорог
    Оцу (112.8) ужимал профиль с 0.57 до 0.26.

    Квадратичная поверхность снимает обе крайности, потому что и градиент, и
    виньетка низкочастотны. Подгонка идёт **только по рамке**, где фигуры заведомо
    нет, поэтому сама фигура на оценку не влияет.
    """
    h, w, _ = rgb.shape
    b = max(1, int(round(min(h, w) * band_frac)))
    ys, xs = np.mgrid[0:h, 0:w].astype(np.float32)
    ring = (xs < b) | (xs >= w - b) | (ys < b) | (ys >= h - b)
    idx = np.flatnonzero(ring.ravel())
    # Подвыборка: least squares по миллионам точек считается заметно дольше, а
    # шести коэффициентов точности не добавляет.
    step = max(1, idx.size // 20000)
    idx = idx[::step]

    xn = (xs.ravel()[idx] / max(1, w - 1)) * 2.0 - 1.0
    yn = (ys.ravel()[idx] / max(1, h - 1)) * 2.0 - 1.0
    design = np.stack([np.ones_like(xn), xn, yn, xn * xn, xn * yn, yn * yn], axis=1)
    samples = rgb.reshape(-1, 3)[idx]
    coef, *_ = np.linalg.lstsq(design, samples, rcond=None)

    Xn = (xs / max(1, w - 1)) * 2.0 - 1.0
    Yn = (ys / max(1, h - 1)) * 2.0 - 1.0
    grid = np.stack([np.ones_like(Xn), Xn, Yn, Xn * Xn, Xn * Yn, Yn * Yn], axis=-1)
    return np.clip(grid @ coef, 0.0, 255.0).astype(np.float32)


def _content_bbox(panel: Image.Image) -> tuple[int, int, int, int] | None:
    if panel.mode in ("RGBA", "LA"):
        alpha = panel.getchannel("A")
        if alpha.getextrema()[0] < 255:
            return alpha.getbbox()
    rgb = panel.convert("RGB")
    mask = rgb.convert("L").point(lambda v: 255 if v > 8 else 0)
    return mask.getbbox()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sheet", type=Path)
    ap.add_argument("-o", "--out", type=Path, default=None)
    ap.add_argument("--tol", default="auto",
                    help="порог расстояния до фона, или 'auto' (автоподбор по отступу "
                         "панелей от края, по умолчанию)")
    ap.add_argument("--feather", type=float, default=DEFAULT_FEATHER)
    ap.add_argument("--bg", choices=("surface", "corner"), default="surface",
                    help="модель фона: квадратичная поверхность по рамке (по умолчанию) "
                         "или один цвет угла")
    ap.add_argument("--cols", type=int, default=2, help="панелей по горизонтали")
    ap.add_argument("--rows", type=int, default=2, help="панелей по вертикали")
    ap.add_argument("--dry-run", action="store_true",
                    help="не писать файл, только показать боксы панелей")
    args = ap.parse_args()

    if not args.sheet.is_file():
        print(f"нет файла: {args.sheet}", file=sys.stderr)
        return 1

    img = Image.open(args.sheet).convert("RGB")
    rgb = np.asarray(img, dtype=np.float32)
    corner = _corner_colour(rgb)
    ring_med, ring_max = _border_spread(rgb)
    print(f"фон: угол rgb({corner[0]:.0f}, {corner[1]:.0f}, {corner[2]:.0f}), "
          f"разброс по рамке медиана {ring_med:.1f} / максимум {ring_max:.1f}")

    if args.bg == "surface":
        ref = _bg_surface(rgb)
        print("модель фона: квадратичная поверхность по рамке")
    else:
        ref = corner
        print("модель фона: один цвет угла")

    # Евклидово расстояние до фона, затем рампа tol..tol+feather.
    dist = np.sqrt(((rgb - ref) ** 2).sum(axis=2))

    if str(args.tol).lower() == "auto":
        tol, how = _auto_tol(dist, args.cols, args.rows)
        print(f"порог: auto -> {tol:.1f} ({how})")
    else:
        tol = float(args.tol)
        print(f"порог: задан вручную -> {tol:.1f}")

    if ring_max > tol:
        print(f"! фон НЕ плоский: разброс {ring_max:.1f} > tol {tol:.0f}. Градиент или "
              f"виньетка частично попадут в содержимое и раздуют общий кроп. "
              f"Автоподбор это компенсирует, подняв порог до отступа от края, но силуэт "
              f"может слегка раздаться; надёжнее перегенерировать лист с явным "
              f"требованием ровного фона.",
              file=sys.stderr)

    lo, hi = tol, tol + args.feather
    alpha = np.clip((dist - lo) / max(1e-6, hi - lo), 0.0, 1.0) * 255.0
    alpha = alpha.astype(np.uint8)

    kept = int((alpha > 0).sum())
    total = int(alpha.size)
    print(f"непрозрачных пикселей: {kept} из {total} ({100.0 * kept / max(1, total):.1f}%)")
    if kept < total * 0.01:
        print("! почти всё ушло в прозрачность - фон подобран неверно, поднять --tol",
              file=sys.stderr)

    out = Image.fromarray(np.dstack([rgb.astype(np.uint8), alpha]), "RGBA")

    w, h = out.size
    if w % args.cols or h % args.rows:
        print(f"! {w}x{h} не делится на {args.cols}x{args.rows} нацело", file=sys.stderr)
    pw, ph = w // args.cols, h // args.rows
    for i in range(args.cols * args.rows):
        cx, cy = i % args.cols, i // args.cols
        panel = out.crop((cx * pw, cy * ph, (cx + 1) * pw, (cy + 1) * ph))
        box = _content_bbox(panel)
        if box is None:
            print(f"панель {i} ({cx},{cy}): ПУСТО")
        else:
            bw, bh = box[2] - box[0], box[3] - box[1]
            print(f"панель {i} ({cx},{cy}): bbox {box} -> {bw}x{bh} "
                  f"(заполнение {bw / pw:.2f} x {bh / ph:.2f})")

    if args.dry_run:
        print("--dry-run: файл не записан")
        return 0

    dst = args.out or args.sheet.with_name(args.sheet.stem + "-keyed.png")
    out.save(dst)
    print(f"записано: {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
