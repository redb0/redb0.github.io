from datetime import date

from pelican.plugins import sitemap, webassets

AUTHOR = "Vladimir Voronov"
SITENAME = "Vladimir Voronov"
SITEURL = ""
SITEDESC = "Личный сайт Python разработчика"

PATH = "content"

TIMEZONE = "Asia/Krasnoyarsk"

DEFAULT_LANG = "ru"

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

# Social widget
SOCIAL = (
    (
        "GitHub",
        "https://github.com/redb0",
        open("content/extras/social/github.svg").read(),
    ),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

HOSTING_NAME = "localhost"
COPYRIGHT_YEAR = date.today().year
THEME = "themes/third"

STATIC_PATHS = ("extras",)
EXTRA_PATH_METADATA = {
    "extras/favicon.ico": {"path": "favicon.ico"},
}

PLUGINS = [webassets, sitemap]

# Порядок вывода страниц в навигации
PAGE_ORDER_BY = "order"

DEFAULT_CATEGORY = "misc"
USE_FOLDER_AS_CATEGORY = False

MARKDOWN = {
    "extension_configs": {
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
AUTHOR_SAVE_AS = CATEGORY_SAVE_AS = ""
TAG_URL = "tags/{slug}/"
TAG_SAVE_AS = "tags/{slug}/index.html"
ARCHIVES_URL = "archives/"
ARCHIVES_SAVE_AS = ARCHIVES_URL + "index.html"
TAGS_URL = "tags/"
TAGS_SAVE_AS = TAGS_URL + "index.html"

SITEMAP = {
    "format": "xml",
    "changefreqs": {"articles": "weekly", "indexes": "daily", "pages": "monthly"},
}

# Disable "authors" and "categories" pages
DIRECT_TEMPLATES = ["index", "tags", "archives"]
DELETE_OUTPUT_DIRECTORY = True
