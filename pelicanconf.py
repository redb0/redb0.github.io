from datetime import date

from pelican.plugins import sitemap, webassets

AUTHOR = "Vladimir Voronov"
SITENAME = "Vladimir Voronov"
SITEURL = ""
SITEROLE = "Python-разработчик"
SITEDESC = f"{SITEROLE}. Backend: FastAPI, gRPC, PostgreSQL"

PATH = "content"

TIMEZONE = "Asia/Krasnoyarsk"

DEFAULT_LANG = "ru"
LOCALE = ["ru_RU.UTF-8", "ru_RU.utf8", "C.UTF-8"]
DATE_FORMATS = {
    "ru": "%-d %B %Y",
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget: (название, url[, имя иконки в includes/social/<name>.svg])
SOCIAL = (
    ("GitHub", "https://github.com/redb0", "github"),
    ("LinkedIn", "https://www.linkedin.com/in/vladimir-voronov-976a0b365/", "linkedin"),
    ("hh", "https://hh.ru/resume/f5d0e0feff085997e40039ed1f4e6376783858", "hh"),
    ("Сетка", "https://set.ki/3Covzkh", "setka"),
    ("Telegram", "https://t.me/vs_voronov", "telegram"),
    ("Канал", "https://t.me/lazy_pythonists", "telegram-channel"),
    ("Email", "mailto:info@vladimir-voronov.ru", "email"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

COPYRIGHT_YEAR = date.today().year
THEME = "themes/third"

STATIC_PATHS = ("extras",)
OG_IMAGE = "og.jpg"
EXTRA_PATH_METADATA = {
    "extras/favicon.ico": {"path": "favicon.ico"},
    "extras/robots.txt": {"path": "robots.txt"},
    "extras/site.webmanifest": {"path": "site.webmanifest"},
    "extras/og.jpg": {"path": OG_IMAGE},
    "extras/cv.pdf": {"path": "cv.pdf"},
    "extras/safe-6-practitioner.png": {"path": "safe-6-practitioner.png"},
    "extras/safe-6-practitioner.pdf": {"path": "safe-6-practitioner.pdf"},
}

PLUGINS = [webassets, sitemap]

# Порядок вывода страниц в навигации
PAGE_ORDER_BY = "order"

# Fallback, если в статье нет Category. У всех текущих статей поле задано явно.
DEFAULT_CATEGORY = "misc"
USE_FOLDER_AS_CATEGORY = False

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": "", "permalink_class": "headerlink"},
    },
    "output_format": "html5",
}

ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = ARTICLE_URL + "index.html"
DRAFT_URL = "drafts/{slug}/"
DRAFT_SAVE_AS = DRAFT_URL + "index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
DRAFT_PAGE_URL = "drafts/pages/{slug}/"
DRAFT_PAGE_SAVE_AS = DRAFT_PAGE_URL + "index.html"
AUTHOR_SAVE_AS = ""
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = CATEGORY_URL + "index.html"
TAG_URL = "tags/{slug}/"
TAG_SAVE_AS = "tags/{slug}/index.html"
ARCHIVES_URL = "archives/"
ARCHIVES_SAVE_AS = ARCHIVES_URL + "index.html"
TAGS_URL = "tags/"
TAGS_SAVE_AS = TAGS_URL + "index.html"

SITEMAP = {
    "format": "xml",
    "changefreqs": {"articles": "weekly", "indexes": "weekly", "pages": "monthly"},
}

# Страницы авторов выключены; категории включены (CATEGORY_SAVE_AS).
DIRECT_TEMPLATES = ["index", "tags", "archives"]
DELETE_OUTPUT_DIRECTORY = True


from feedgenerator import Rss201rev2Feed
from pelican import signals
from pelican.writers import Writer as PelicanWriter


class SummaryAtomWriter(PelicanWriter):
    """Atom без полного HTML статьи — в фиде только summary."""

    def _add_item_to_the_feed(self, feed, item):
        if isinstance(feed, Rss201rev2Feed):
            return super()._add_item_to_the_feed(feed, item)
        orig = item.get_content
        item.get_content = lambda siteurl=None: None
        try:
            return super()._add_item_to_the_feed(feed, item)
        finally:
            item.get_content = orig


def _get_writer(_pelican):
    return SummaryAtomWriter


signals.get_writer.connect(_get_writer)
