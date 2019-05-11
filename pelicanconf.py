#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'table of ele_ments'
# SITENAME = u'ele_mental'
SITENAME = u'. . .e l e _ m e n t a l. . .'
SITEURL = ''

ARTICLE_PATHS = ['posts']
ARTICLE_URL = 'posts/{category}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{category}/{slug}/index.html'

PATH = 'content'

THEME = 'theme'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Resident Advisor', 'https://www.residentadvisor.net'),
         ('+SCALE', 'https://scale.la/'),
         ('Titonton Duvante', 'https://www.titonton.org/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DISPLAY_PAGES_ON_MENU = False

STATIC_PATHS = ['ele_images','favicon.ico']

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
