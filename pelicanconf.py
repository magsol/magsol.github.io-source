#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Shannon Quinn'

SITENAME = u'GT at UGA doing SSVD'
SITESUBTITLE = u'Data science, academia, and the occasional donut binge'
SITEURL = 'http://127.0.0.1:8000'

# Times and dates.
TIMEZONE = u'America/New_York'
DEFAULT_LANG = u'en'
OG_LOCALE = u'en_US'
DEFAULT_DATE_FORMAT = 'Posted on %B %d, %Y at %I:%M%p. It was %A.'

PATH = './content'
STATIC_PATHS = ['downloads', 'images', 'figures', 'notebooks']
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
COPYRIGHT_YEAR = 2015

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True


# Blogroll
LINKS = (('Quinn Research Lab', 'https://quinngroup.github.io'),
         ('Faculty Webpage', 'http://cs.uga.edu/~squinn'),
         ('Personal Website', 'http://www.magsol.me'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/SpectralFilter'),
          ('github', 'https://github.com/magsol'),
          ('stack-overflow', 'http://stackoverflow.com/users/13604/magsol'),
          ('google', 'https://plus.google.com/+ShannonQuinnBBQ/'),
          ('linkedin', 'http://www.linkedin.com/in/shannonpquinn'))

DEFAULT_PAGINATION = False

# This header file is automatically generated by the notebook plugin
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Woo plugins!
NOTEBOOK_DIR = 'notebooks'
THEME = 'flex/'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['liquid_tags.notebook']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
