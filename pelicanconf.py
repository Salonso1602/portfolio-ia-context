AUTHOR = 'salonso1602'
SITENAME = 'Portfolio de Intro a Aprendizaje Automático'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Argentina/Buenos_Aires'

DEFAULT_LANG = 'es'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('UCI Datasets', 'https://archive.ics.uci.edu/datasets'),
         ('Python.org', 'https://www.python.org/'),
         ('RapidMiner', 'https://rapidminer.com/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/Salonso1602'),
          ('LinkedIn', 'https://www.linkedin.com/in/santiago-rafael-alonso-mendez-374106218/'),)

DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY = '1. Home'

PAGE_PATHS = ['pages']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.codehilite': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

NEWEST_FIRST_ARCHIVES = False
ARTICLE_ORDER_BY = 'date'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False

THEME = "themes\gum"

SITESUBTITLE = 'por Rafael Alonso'

GITHUB_URL = 'https://github.com/Salonso1602'
TWITTER_URL = ''
FACEBOOK_URL = ''
GOOGLEPLUS_URL = ''

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True