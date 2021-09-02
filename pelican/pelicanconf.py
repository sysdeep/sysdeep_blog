#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'diver'
SITENAME = 'divers'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

# DEFAULT_LANG = 'Russian'
DEFAULT_LANG = 'ru'


#--- theming
THEME = "notmyidea"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
	('tags', '/tags.html'),
	('archives', '/archives.html'),
	('categories', '/categories.html'),
	('authors', '/authors.html'),
	('pelican docs', 'https://docs.getpelican.com/en/stable/index.html'),
)
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True




USE_FOLDER_AS_CATEGORY = False



DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
	("about", "/pages/about.html"),
)