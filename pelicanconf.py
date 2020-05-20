#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shannon Quinn'
SITENAME = 'Stochastic Stenography'
SITESUBTITLE = 'Data science, academia, and donuts'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en_US'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_DATE_FORMAT = 'Posted on %B %-d in the year %Y, at %-H:%M%p. It was %A.'
DEFAULT_PAGINATION = 10

# Article URL (seems specific to Flex theme).
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
THEME = './theme/'
LICENSE_URL = 'https://github.com/magsol/magsol.github.io-source/blob/master/LICENSE'
LICENSE = 'MIT'

# Other non-default settings.
MARKUP = ['md']
PLUGIN_PATHS = ['../plugins']
PLUGINS = [
        'summary',                  # auto-summarizing articles
        'ipynb.liquid',             # for embedding notebooks
        'liquid_tags.img',          # embedding images
        'liquid_tags.video',        # embedding videos
        'liquid_tags.include_code', # including code blocks
        'liquid_tags.youtube',      # youtube embeddings
        #'liquid_tags.literal',
        'liquid_tags.gram',         # for embedding instagram posts
        #'filetime_from_git',        # auto-get the publish time from git commit
        'embed_tweet'               # embedding tweets
]
IGNORE_FILES = ['.ipynb_checkpoints']

# For liquid tags extension.
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Constants.
ABOUT_PAGE = '/pages/about.html'
TWITTER_USERNAME = 'SpectralFilter'
GITHUB_USERNAME = 'magsol'
LINKEDIN_USERNAME = 'shannonpquinn'
INSTAGRAM_USERNAME = 'magsolium'
EMAIL_ADDRESS = 'magsol@gmail.com'
STACKOVERFLOW_ADDRESS = 'http://stackoverflow.com/users/13604/magsol'
#AUTHOR_WEBSITE = 'http://cobweb.cs.uga.edu/~squinn'
AUTHOR_BLOG = 'https://wherearethepancakes.wordpress.com'
AUTHOR_CV = 'https://quinngroup.github.io'
SHOW_ARCHIVES = True
SHOW_FEED = False

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
