#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Wille Marcel'
SITENAME = 'wille.blog.br'
SITESUBTITLE = 'OpenStreetMap, Python, Bikes, Travels, Life...'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# URLs
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = '{slug}-{lang}'
PAGE_URL = 'pages/{slug}'
PAGE_LANG_URL = 'pages/{slug}-{lang}'
CATEGORY_URL = 'category/{slug}'
TAG_URL = 'tag/{slug}'
AUTHOR_URL = 'author/{slug}'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/_wille'),
          ('github', 'https://github.com/willemarcel'),
          ('flickr','https://www.flickr.com/willemarcel/'),
          ('envelope','mailto:wille.yyz@gmail.com'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme'
HEADER_COVER = 'images/pucon2.jpg'
