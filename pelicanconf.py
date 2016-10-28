#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = """Mark Mc Mahon. This project is maintained by <a href=https://github.com/vasily-v-ryabov>vasily-v-ryabov</a>"""
SITENAME = 'pywinauto'
SITEURL = ''

PATH = 'content'

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    '.gitignore',
    'LICENSE',
    '.nojekyll',  # bypass Jekyll (helps for names with underscores)
]

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'
DEFATUL_DATE = 'fs'

# Show the whole article contents
SUMMARY_MAX_LENGTH = None

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
     ('Documentation', 'https://pywinauto.readthedocs.io/en/latest/'),
     ('Releases', 'https://github.com/pywinauto/pywinauto/releases/'),
     ('Pywinauto ZIP File', 'https://github.com/pywinauto/pywinauto/zipball/master/'),
     ('Pywinauto TAR Ball', 'https://github.com/pywinauto/pywinauto/tarball/master/'),
     ('Automation blog', 'https://guiautomation.blogspot.com/'),
)

# Social widget
SOCIAL = ()  # (('You can add links in your config file', '#'),
#  ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "theme-pelican-bootstrap3"

# Parameters specific for pelican-bottstrap3 theme
BOOTSTRAP_THEME = "flatly"
GITHUB_USER = "pywinauto"
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Disable tags generation
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
