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

# Plugins.
# pip install pelican-jupyter
##  https://github.com/danielfrg/pelican-jupyter 
# pip install pelican-liquid-tags
##  https://github.com/pelican-plugins/liquid-tags
##  https://github.com/lqez/pelican-embed-tweet

# Other non-default settings.
MARKUP = ['md',]
PLUGIN_PATHS = ['../plugins']

from pelican.plugins import liquid_tags
PLUGINS = [
        liquid_tags,                # regular ol' liquid tags
        #'filetime_from_git',        # auto-get the publish time from git commit
        'pelican.plugins.embed_tweet'               # embedding tweets
]

LIQUID_TAGS = ["img", "include_code", "gram", "video", "youtube", "notebook"]

# Added given this hotfix: https://github.com/danielfrg/pelican-jupyter/issues/126#issuecomment-745372454
LIQUID_CONFIGS = (("IPYNB_FIX_CSS", "False", ""), 
                  ("IPYNB_SKIP_CSS", "False", ""), 
                  ("IPYNB_EXPORT_TEMPLATE", "base", ""),)

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
AUTHOR_BLOG = 'https://wherearethepancakes.wordpress.com'
AUTHOR_CV = 'https://quinngroup.github.io'
SHOW_ARCHIVES = True
SHOW_FEED = False

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'videos', 'downloads', 'favicon.ico']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
