#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'EDO Common Engineering'
SITENAME = ''
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Canada/Pacific'

DEFAULT_LANG = 'en'

THEME = '/Users/alexbunardzic/Documents/worksafeblog/pelican-themes/bricks'
THEME = 'c:/_T/bricks'

# Feed generation is usually not desired when developing
FEED_MAX_ITEMS = 50
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('WorkSafeBC', 'https://www.worksafebc.com/en'),
         ('WorkSafeBC IT is hiring','https://www.worksafebc.com/en/about-us/news-events/campaigns/2019/September/connect-to-an-it-career-with-a-difference'),
         ('Careers', 'https://www.worksafebc.com/en/about-us/careers'),
         ('ATOM/RSS Feed', 'https://wsbctechnicalblog.github.io/feeds/posts.atom.xml'),)



# Social widget
SOCIAL = (('WorkSafeBC on Twitter', 'https://twitter.com/WorkSafeBC'),('WorkSafeBC on LinkedIn', 'https://www.linkedin.com/company/worksafebc/'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True