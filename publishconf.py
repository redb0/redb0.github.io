# Production settings: GitHub Actions and local `make publish` / `invoke preview`.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://redb0.github.io"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = None

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""

HOSTING_NAME = "GitHub Pages"
HOSTING_URL = "https://pages.github.com/"
