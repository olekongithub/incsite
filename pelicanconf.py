#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Evan Misshula'
SITENAME = u'Queens College Incubator'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Eastern'
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [('Mission','/pages/mission.html'),
             ('Companies','/pages/companies.html'),
             ('Projects','/pages/projects.html'),
             ('Research','/pages/research.html'),
             ('Interns','/pages/interns.html'),
             ('Staff','/pages/staff.html'),
]


LOAD_CONTENT_CACHE = False
THEME = 'Themes/tuxlite_tbs'
DELETE_OUTPUT_DIRECTORY = True
USE_FOLDER_AS_CATEGORY = True

DEFAULT_LANG = u'en'
STATIC_PATHS = [ 'images', 'js','css' ]
IGNORE_FILES = ['.#*', '*~']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Queens Collge', 'http://www.qc.cuny.edu/Pages/home.aspx'),
         ('Queens College CS', 'http://www.cs.qc.cuny.edu/index-5.html'),
         ('Flushing Chamber of Commerce', 'http://flushingchamber.com'),
         )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/emisshula'),
          ('github', 'https://github.com/cisdd'),
         )# ('linkedin','http://www.linkedin.com/pub/evan-misshula/20/5b/810‎'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

