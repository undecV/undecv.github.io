#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime

AUTHOR = 'UndecV'
SITEURL = ''  # 'https://undecv.github.io'
SITENAME = 'キャンディージャー'
SITETITLE = 'キャンディージャー'
SITESUBTITLE = 'undecV\'s Blog \"Candy Jar\"'
SITEDESCRIPTION = 'undecV\'s Blog \"Candy Jar\"'
SITELOGO = SITEURL + '/images/128.png'
FAVICON = SITEURL + '/favicon.ico'
BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

THEME = "./themes/Flex"  # https://github.com/alexandrevicenzi/Flex
PATH = 'content'
# OUTPUT_PATH = "blog/"

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["pelican-yaml-metadata"]

# ===== PATHS =================================================================

STATIC_PATHS = [
    'images',
    'extra/custom.css',
    'extra/favicon.ico',
    # 'extra',
]
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'theme/custom.css'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/CNAME': {'path': 'CNAME'},
#     'extra/LICENSE': {'path': 'LICENSE'},
#     'extra/README': {'path': 'README'},
}
CUSTOM_CSS = "theme/custom.css"

# ===== PAGES =================================================================

ARTICLE_URL = 'posts/{slug}.html'       # 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}.html'   # 'posts/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'          # 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}.html'      # 'pages/{slug}/index.html'

# DISABLE_URL_HASH = True
HOME_HIDE_TAGS = False
# PAGES_SORT_ATTRIBUTE = 'title'
# REL_CANONICAL = True
USE_FOLDER_AS_CATEGORY = False
DEFAULT_PAGINATION = 10

# ===== COPYRIGHT =============================================================

COPYRIGHT_NAME = SITETITLE
COPYRIGHT_YEAR = datetime.now().year
# CC_LICENSE = {
#     "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
#     "version": "4.0",
#     "slug": "by-sa",
#     "icon": True,
#     "language": "en_US",
# }

# ===== I18N ==================================================================

# ARTICLE_HIDE_TRANSLATION = False
# PLUGINS = ["i18n_subsites"]
# JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
# I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = 'zh_TW'
LOCALE = "zh_TW"
OG_LOCALE = "zh_TW"
# DATE_FORMATS = {"en": "%B %d, %Y", }
TIMEZONE = 'Asia/Taipei'

# ===== FEEDS =================================================================

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# ===== MENU ==================================================================

MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

SOCIAL = (
    ('github', 'https://github.com/undecv'),
    ('twitter', 'https://twitter.com/phinhdgxiaohai'),
    ('telegram', 'https://t.me/s/poi0048'),
    ('rss', 'feeds/all.atom.xml'),
    # ('envelope-o',''), ('facebook',''), ('github-alt',''), ('google',''), 
    # ('linkedin',''), ('pinterest',''), ('reddit',''), ('stack-overflow',''), 
    # ('soundcloud',''), ('youtube',''), ('xing','')
)

# LINKS = (
#     ('Pelican', 'http://getpelican.com/'),
#     ('Python.org', 'http://python.org/'),
#     ('Jinja2', 'http://jinja.pocoo.org/'),
#     ('You can modify those links in your config file', '#'),
# )
LINKS_IN_NEW_TAB = True

# ===== DARK MODE =============================================================

THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'monokai'

# ===== PLUGINS ===============================================================

# GITHUB_CORNER_URL = None

# ===== INTEGRATIONS ==========================================================

# ADD_THIS_ID = 'ra-77hh6723hhjd'
# DISQUS_SITENAME = 'yoursite'
# DUOSHUO_SITENAME = 'yoursite'
# GOOGLE_ANALYTICS = 'UA-1234-5678'
# GUAGES= ''
# GOOGLE_TAG_MANAGER = 'GTM-ABCDEF'
# GOOGLE_GLOBAL_SITE_TAG = ''
# STATUSCAKE = 'F'
# PIWIK_SITE_ID = ''
# MATOMO_SITE_ID = ''
# PIWIK_URL = ''
# MATOMO_URL = ''
# ISSO_URL = '//comments.sumnerevans.com'
# ISSO_EMBED_JS_PATH = '/static/javascript/isso-dev.min.js'
# ISSO_OPTIONS = { 'avatar': 'false', 'gravatar': 'true', 
#     'reply-to-self': 'true', 'reply-notifications': 'true', }

# ===== CUSTOMIZE =============================================================

# FRIEND_LINKS = (
#   ('通訊雜記', 'https://wenyuangg.github.io/'),
# )

# ===== DEV OPTIONS ===========================================================

# USE_LESS = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
