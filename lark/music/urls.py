#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'music.views',
    url(r'^api/music/(?P<sid>\w+)/$', 'music', name='music'),
    url(r'^api/next/(?P<next_number>\d+)/$', 'next_music', name='next'),
    url(r'^api/random/$', 'random_music', name='random'),
)
