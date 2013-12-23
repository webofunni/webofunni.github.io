#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Unni'
SITENAME = u'Mutexes'
SITEURL = '/blog'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = 'naiq'

MENUITEMS = (('feed', '/feeds/all.atom.xml'),
             ('projects', 'http://github.com/webofunni'),
             ('about', 'www.mutexes.org'))


DEBUG = False

MD_EXTENSIONS = ['codehilite(css_class=codehilite)','extra']

            
