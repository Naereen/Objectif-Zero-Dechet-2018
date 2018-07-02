#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = "Objectif Zéro Déchet"
AUTHOR = "Lilian Besson"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "fr"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM         = None
CATEGORY_FEED_ATOM    = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None

# Blogroll
LINKS = (
    ("Sources (GitHub)", "https://GitHub.com/Naereen/Objectif-Zero-Dechet-2018"),
    ("Idées",            "https://GitHub.com/Naereen/Objectif-Zero-Dechet-2018/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc"),
    ("Mon site",         "https://perso.crans.org/besson/"),
    # ("Pelican",          "http://GetPelican.com/"),
    # ("Python",           "https://Python.org/"),
    ("Famille Zéro Déchet",         "http://www.famillezerodechet.com/"),
)

MENU_LINKS = (
    ("Sources (GitHub)", "https://GitHub.com/Naereen/Objectif-Zero-Dechet-2018"),
    ("Mon site",         "https://perso.crans.org/besson/"),
)

# Social widget
SOCIAL = (
    ("github",           "https://GitHub.com/Naereen"),
    ("bitbucket",        "https://Bitbucket.org/lbesson"),
    ("facebook",         "https://www.Facebook.com/naereencorp.lbesson"),
    ("address-card",     "https://perso.crans.org/besson/callme.html"),
    ("wikipedia-w",      "https://en.wikipedia.org/wiki/User:Naereen"),
    ("envelope",         "mailto:naereen at crans dot org"),
    ("phone",            "tel:+33 6 28 41 22 57"),
    ("rss",              "https://perso.crans.org/besson/zero-dechet/feeds/all.atom.xml"),
)
# Icons : mapping of font-awesome icons to URL
ICONS = SOCIAL

# Articles per page
DEFAULT_PAGINATION = 10

# # Dates of articles from the file modification
# DEFAULT_DATE = "fs"

# http://docs.getpelican.com/en/stable/settings.html?highlight=date#metadata
FILENAME_METADATA = r'.*-(?P<date>\d{2}-\d{2}-\d{4})'

DEFAULT_CATEGORY = "journal"

# Get copied to the output
STATIC_PATHS = [
    "images",
    "content/images",
    "images/favicon.ico",
    "content/images/favicon.ico",
    # "pdfs"
]

# Favicon of the page
FAVICON = "/images/favicon.ico"

# Cf. https://stackoverflow.com/questions/31270373/how-to-add-a-favicon-to-a-pelican-blog#31270471
EXTRA_PATH_METADATA = {
    # "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico":  {"path": "favicon.ico"},
    "extra/LICENSE":      {"path": "LICENSE"},
    "extra/README":       {"path": "README"},
}

# Logo
LOGOPATH = "/images/icon.png"
AVATAR = SITEIMAGE = LOGO = LOGOPATH

# Description and welcome message of the site
# Two emojis in UTF8
DESCRIPTION = u"🇫🇷 📒 Mes expériences et mes progrès, objectif zéro déchet 🍃 pour l'année 2018 !"
WELCOME_MESSAGE = SIDEBAR_DIGEST = SITESUBTITLE = DESCRIPTION

# Improve typography
TYPOGRIFY = True

# SLUGIFY_SOURCE = "title"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Use my fork of the alchemy theme. See https://github.com/Naereen/Objectif-Zero-Dechet-2018/tree/master/themes/alchemy
# THEME = "notmyidea"
THEME = "themes/alchemy"

# Plugins from https://github.com/getpelican/pelican-plugins
PLUGIN_PATHS = [
    "plugins"
]

PLUGINS = [
    # https://github.com/getpelican/pelican-plugins/tree/master/global_license
    "global_license",
    # https://github.com/getpelican/pelican-plugins/tree/master/neighbors
    "neighbors",
    # https://github.com/getpelican/pelican-plugins/tree/master/random_article
    "random_article",
    # https://github.com/getpelican/pelican-plugins/tree/master/section_number
    # "section_number",
    # # https://github.com/getpelican/pelican-plugins/tree/master/simple_footnotes
    "simple_footnotes",
    # # https://github.com/getpelican/pelican-plugins/tree/master/tag_cloud
]

SECTION_NUMBER_MAX = 5

# "global_license" extension, I don't know how it works
LICENSE = "<a href='https://lbesson.MIT-License.org/'>Licence MIT</a>"

# URL for the random page
RANDOM = "random.html"

# # Count of different font sizes in the tag cloud.
# TAG_CLOUD_STEPS = 4
# # Maximum number of tags in the cloud.
# TAG_CLOUD_MAX_ITEMS = 100
# # The tag cloud ordering scheme. Valid values: random, alphabetically, alphabetically-rev, size and size-rev
# TAG_CLOUD_SORTING = 'random'
# # Optional setting : can bring badges, which mean say : display the number of each tags present on all articles.
# TAG_CLOUD_BADGE = True


# Style in case a code block is present
PYGMENTS_STYLE = "monokai"

# https://github.com/getpelican/pelican-plugins/tree/master/headerid
MARKDOWN = {
    "extensions": [
        "markdown.extensions.codehilite",
        "markdown.extensions.extra",
        "markdown.extensions.meta",
        "markdown.extensions.toc",
        "markdown.extensions.smarty",
        "plugins.mdx_unimoji.mdx_unimoji:UnimojiExtension"
    ],
    "extension_configs": {
        "markdown.extensions.codehilite": {
            "css_class": "highlight"
        },
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {},
        "markdown.extensions.smarty": {},
    },
    "output_format": "html5",
}

HEADERID_LINK_CHAR = "¶"

IGNORE_FILES = [
    ".#*",
    "__pycache__",
    "content/template.md",
    "template.md",
    "issues/",
]
