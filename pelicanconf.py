AUTHOR = 'salonso1602'
SITENAME = 'Portfolio de Intro a Aprendizaje Automático'
SITEURL = '/'

PATH = 'content'

TIMEZONE = 'America/Argentina/Buenos_Aires'

DEFAULT_LANG = 'Spanish'


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

DEFAULT_CATEGORY = 'Home'

PAGE_PATHS = ['pages']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.codehilite': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True