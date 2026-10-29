"""Сетевой guard: единственное место, где решается «можно ли сюда ходить».

Барьер 1 из четырёх. Логика fail-closed: всё, что не разрешено явно, запрещено.

Зачем: как только у агента появляется сетевое скачивание, открывается целый класс
атак, которого у Godot-only агента не было:

  * SSRF — модель (или строка в чужом описании ассета) подсовывает URL на локальный
    сервис, и агент превращается в средство доступа к внутренней сети;
  * редирект-обход — разрешённый хост отвечает 302 на 127.0.0.1 или на чужой домен;
  * отравленный ответ — API отдаёт ссылку на посторонний хост, и «скачивание из
    Poly Haven» уходит на произвольный сайт;
  * подмена схемы — file://, ftp://, data: вместо https.

Поэтому проверяется не только URL, который попросила модель, но и КАЖДЫЙ редирект,
и каждый URL, извлечённый из чужого ответа. Хост, а не подстрока: `kenney.nl.evil.com`
не должен проходить проверку на `kenney.nl`.
"""
from __future__ import annotations

import ipaddress
import socket
from dataclasses import dataclass
from urllib.parse import urlparse

# --------------------------------------------------------------------------
# Домены, с которых разрешено скачивание. Хост сверяется точно или как
# поддомен (`.polyhaven.com` разрешает `dl.polyhaven.com`).
#
# Домены добавлены осознанно, по одному на источник из 01_sources.md.
# itch.io здесь НЕТ: у него нет API, загрузки часто за формой, и автоматический
# вход под учётными данными пользователя — красная линия политики §17.
# --------------------------------------------------------------------------
ALLOWED_HOSTS: frozenset[str] = frozenset({
    # Poly Haven — официальный API + отдача файлов
    "polyhaven.com",
    "api.polyhaven.com",
    "dl.polyhaven.org",
    # Kenney — каталог и прямые ссылки на пакеты
    "kenney.nl",
    # Godot Asset Store / Asset Library
    "store.godotengine.org",
    "godotengine.org",
    "github.com",
    "raw.githubusercontent.com",
    # OpenGameArt (v2, но домен фиксируем сразу — политика одна)
    "opengameart.org",
})

ALLOWED_SCHEMES = frozenset({"https"})

# --------------------------------------------------------------------------
# Хосты, допустимые ТОЛЬКО как цель редиректа, но не как исходный URL.
#
# Зачем это разделение. Godot Asset Store отдаёт скачивание через 302 на
# ПРЕДПОДПИСАННЫЙ URL объектного хранилища (проверено: fra1.digitaloceanspaces.com
# с X-Amz-Signature, живёт 600 с). Заблокировать его — значит сделать магазин
# неработоспособным, потому что другого пути к файлу у него нет.
#
# Но разрешать такие хосты как обычную цель нельзя: иначе «скачай вот отсюда»
# с произвольного адреса в объектном хранилище проходит проверку, а это уже
# обход доменной политики. Поэтому:
#   * модель НЕ МОЖЕТ передать такой хост — check_url его не пропустит;
#   * переход на него разрешён только если его выдал как редирект уже
#     проверенный домен из ALLOWED_HOSTS (см. check_redirect).
#
# Предподписанный URL одноразовый и привязан к конкретному объекту, поэтому
# «подсунуть туда что-то другое» через редирект от доверенного домена нельзя.
# --------------------------------------------------------------------------
REDIRECT_ONLY_HOSTS: frozenset[str] = frozenset({
    "digitaloceanspaces.com",
    "fra1.digitaloceanspaces.com",
    "ams3.digitaloceanspaces.com",
    "sfo3.digitaloceanspaces.com",
    "nyc3.digitaloceanspaces.com",
    "sgp1.digitaloceanspaces.com",
    # GitHub Releases (аддоны часто публикуются там)
    "objects.githubusercontent.com",
    "github-releases.githubusercontent.com",
    "codeload.github.com",
})

# Потолки. Один ассет-пак обычно 1-300 МБ; HDRI 8k бывает ~100 МБ.
MAX_FILE_BYTES = 512 * 1024 * 1024          # 512 МБ на один файл
MAX_TOTAL_BYTES = 2 * 1024 * 1024 * 1024    # 2 ГБ на одну сессию скачивания
MAX_REDIRECTS = 5


class NetworkDenied(PermissionError):
    """URL вне разрешённой сетевой области."""


@dataclass
class FetchBudget:
    """Счётчик скачанного в рамках одной операции.

    Нужен, чтобы серия «легальных» запросов не превратилась в выкачивание
    сотен гигабайт: каждый отдельный файл может быть в пределах лимита,
    а сумма — давно нет.
    """
    total_bytes: int = 0
    files: int = 0

    def spend(self, n: int) -> None:
        if self.total_bytes + n > MAX_TOTAL_BYTES:
            raise NetworkDenied(
                f"превышен лимит скачивания за сессию: "
                f"{self.total_bytes + n} > {MAX_TOTAL_BYTES} байт"
            )
        self.total_bytes += n
        self.files += 1


def _host_allowed(host: str) -> bool:
    host = host.lower().rstrip(".")
    for allowed in ALLOWED_HOSTS:
        if host == allowed:
            return True
        # поддомен разрешённого домена: dl.polyhaven.org для polyhaven.org
        if host.endswith("." + allowed):
            return True
    return False


def _host_redirect_only(host: str) -> bool:
    host = host.lower().rstrip(".")
    for allowed in REDIRECT_ONLY_HOSTS:
        if host == allowed or host.endswith("." + allowed):
            return True
    return False


def _is_private_address(host: str) -> bool:
    """Локальный/приватный адрес — всегда отказ, даже если домен разрешён.

    Ловит SSRF: `127.0.0.1`, `localhost`, `10.x`, `192.168.x`, `169.254.x`
    (метаданные облака), `::1`. Проверяется и литеральный IP в URL, и то,
    во что домен резолвится — иначе `evil.com` с A-записью на 127.0.0.1
    обошёл бы проверку.
    """
    try:
        ip = ipaddress.ip_address(host)
        return (ip.is_private or ip.is_loopback or ip.is_link_local
                or ip.is_reserved or ip.is_multicast)
    except ValueError:
        pass
    try:
        infos = socket.getaddrinfo(host, None, proto=socket.IPPROTO_TCP)
    except (socket.gaierror, OSError):
        # не резолвится — не рискуем, пусть падает на самом запросе
        return False
    for info in infos:
        try:
            ip = ipaddress.ip_address(info[4][0])
        except ValueError:
            continue
        if (ip.is_private or ip.is_loopback or ip.is_link_local
                or ip.is_reserved or ip.is_multicast):
            return True
    return False


def check_url(url: str) -> str:
    """Проверить URL перед запросом. Возвращает его же или бросает NetworkDenied.

    Это единственная функция, которой обязан пользоваться downloader.
    Проверять «примерно там же» нельзя — централизация и есть барьер.
    """
    if not url or not isinstance(url, str):
        raise NetworkDenied("пустой URL")
    url = url.strip()
    parsed = urlparse(url)

    if parsed.scheme.lower() not in ALLOWED_SCHEMES:
        raise NetworkDenied(
            f"схема '{parsed.scheme or '(нет)'}' запрещена: разрешён только https"
        )
    if not parsed.hostname:
        raise NetworkDenied(f"в URL нет хоста: {url}")
    if parsed.username or parsed.password:
        # https://user:pass@host/ — классический способ замаскировать хост
        raise NetworkDenied("учётные данные в URL запрещены")

    host = parsed.hostname.lower().rstrip(".")
    if not _host_allowed(host):
        raise NetworkDenied(
            f"хост '{host}' не в списке разрешённых. Разрешены: "
            f"{', '.join(sorted(ALLOWED_HOSTS))}"
        )
    if _is_private_address(host):
        raise NetworkDenied(f"'{host}' ведёт на локальный/приватный адрес")

    port = parsed.port
    if port is not None and port != 443:
        raise NetworkDenied(f"порт {port} запрещён: только 443")

    return url


def check_redirect(from_url: str, to_url: str, seen: int) -> str:
    """Проверить редирект. Без этого первый барьер обходится одним 302.

    Разрешённый хост может отправить куда угодно — включая внутренний адрес.
    Поэтому каждый шаг цепочки проходит ту же проверку, что и исходный URL,
    плюс ограничение на длину цепочки.

    Отличие от check_url: здесь дополнительно разрешены REDIRECT_ONLY_HOSTS
    (объектные хранилища с предподписанными ссылками). Но только если
    ИСТОЧНИК редиректа уже был доверенным — то есть цепочка началась с
    хоста из ALLOWED_HOSTS. Иначе получается «доверенный хост подтверждает
    недоверенный», и барьер теряет смысл.
    """
    if seen >= MAX_REDIRECTS:
        raise NetworkDenied(f"слишком много редиректов (>{MAX_REDIRECTS})")

    # относительный Location — достраиваем от исходного хоста
    if to_url.startswith("/"):
        p = urlparse(from_url)
        to_url = f"https://{p.hostname}{to_url}"

    from_host = urlparse(from_url).hostname or ""
    trusted_source = _host_allowed(from_host)

    try:
        return check_url(to_url)
    except NetworkDenied:
        # не прошёл обычную проверку — возможно, это цель REDIRECT_ONLY
        if trusted_source:
            parsed = urlparse(to_url)
            host = (parsed.hostname or "").lower().rstrip(".")
            if (parsed.scheme.lower() in ALLOWED_SCHEMES
                    and _host_redirect_only(host)
                    and not _is_private_address(host)
                    and parsed.port in (None, 443)
                    and not parsed.username):
                return to_url
        raise


def check_size(declared: int | None, budget: FetchBudget) -> None:
    """Проверить заявленный размер ДО скачивания.

    Content-Length врёт (может отсутствовать, может быть занижен), поэтому
    это ранний фильтр, а не гарантия. Точная проверка — по факту, в downloader.
    """
    if declared is None:
        return
    if declared > MAX_FILE_BYTES:
        raise NetworkDenied(
            f"файл больше лимита: {declared} > {MAX_FILE_BYTES} байт"
        )
    if budget.total_bytes + declared > MAX_TOTAL_BYTES:
        raise NetworkDenied(
            f"файл выведет за лимит сессии: "
            f"{budget.total_bytes + declared} > {MAX_TOTAL_BYTES} байт"
        )
