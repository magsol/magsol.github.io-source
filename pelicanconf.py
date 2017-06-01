#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Shannon Quinn'

SITENAME = u'Stochastic Stenography'
SITETITLE = SITENAME
SITESUBTITLE = u'Data science, academia, and donuts'
SITELOGO = u'https://magsol.github.io/images/me.png'
FAVICON = u'https://magsol.github.io/images/favicon.ico'
SITEURL = u'http://127.0.0.1:8000'

# Times and dates.
TIMEZONE = u'America/New_York'
DEFAULT_LANG = u'en'
OG_LOCALE = u'en_US'
DEFAULT_DATE_FORMAT = '%B %d, %Y, at %H:%M:%S. It was %A.'

PATH = 'content/'
THEME = '../themes/Flex/'
STATIC_PATHS = ['downloads', 'images', 'figures', 'code']
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
COPYRIGHT_YEAR = 2017

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = False

# Social widget
SOCIAL = (('envelope-o', 'mailto:magsol@gmail.com'),
          ('twitter', 'https://twitter.com/SpectralFilter'),
          ('github', 'https://github.com/magsol'),
          ('stack-overflow', 'http://stackoverflow.com/users/13604/magsol'),
          ('google', 'https://plus.google.com/+ShannonQuinnBBQ/'),
          ('linkedin', 'http://www.linkedin.com/in/shannonpquinn'))

DEFAULT_PAGINATION = False

# Woo plugins!
PLUGIN_PATHS = ['../plugins/']
PLUGINS = ['liquid_tags.img', 'liquid_tags.youtube', 'liquid_tags.include_code',
  'filetime_from_git', 'embed_tweet']

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
