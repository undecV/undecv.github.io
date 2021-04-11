from datetime import datetime

# Flex Custom Settings

AUTHOR = "Foo Bar"
SITEURL = "http://yoursite.com"
SITENAME = "Foo Bar's Blog"

THEME = "Flex"
PATH = "content"
OUTPUT_PATH = "blog/"
TIMEZONE = "America/New_York"
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-yaml-metadata']

STATIC_PATHS = ["images", "extra/ads.txt", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
}

## Feeds

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

## Theme

SITETITLE = "Foo Bar"
SITESUBTITLE = "Web Developer"
SITELOGO = SITEURL + "/images/profile.png"
SITEDESCRIPTION = "Foo Bar's Thoughts and Writings"
BROWSER_COLOR = "#333"
COPYRIGHT_NAME = None
COPYRIGHT_YEAR = datetime.now().year
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}
ROBOTS = "index, follow"
REL_CANONICAL = None
HOME_HIDE_TAGS = True
DISABLE_URL_HASH = None
PAGES_SORT_ATTRIBUTE = None
CUSTOM_CSS = "static/custom.css"
USE_LESS = True
FAVICON = SITEURL + "/images/favicon.ico"
ARTICLE_HIDE_TRANSLATION = None
LINKS_IN_NEW_TAB = None
USE_FOLDER_AS_CATEGORY = False
DEFAULT_PAGINATION = 10

## Flex Menus

MAIN_MENU = True
LINKS = (
    ("Portfolio", "http://alexandrevicenzi.com"),
)
SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/alexandrevicenzi/en"),
    ("github", "https://github.com/alexandrevicenzi"),
    ("twitter", "https://twitter.com/alxvicenzi"),
)
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

## Dark Mode

THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'monokai'

## Integrations

ADD_THIS_ID = "ra-55adbb025d4f7e55"
DISQUS_SITENAME = "flex-pelican"
DUOSHUO_SITENAME = None
GUAGES = None
GOOGLE_ANALYTICS = "UA-1234-5678"
GOOGLE_TAG_MANAGER = "GTM-ABCDEF"
GOOGLE_GLOBAL_SITE_TAG = None
STATUSCAKE = None
PIWIK_SITE_ID = None
PIWIK_URL = None
ISSO_URL = '//comments.sumnerevans.com'
ISSO_EMBED_JS_PATH = '/static/javascript/isso-dev.min.js'
ISSO_OPTIONS = {'avatar': 'false', 'gravatar': 'true', 'reply-to-self': 'true', 'reply-notifications': 'true', }

## Plugins

GITHUB_CORNER_URL = None

## I18N

# Enable i18n plugin.
PLUGINS = ["i18n_subsites"]  # DUMP
# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}
