#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^', include('music.urls', namespace='music')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^%s/' % re.escape(getattr(settings, 'ADMIN_URL', 'admin')),
        include(admin.site.urls)),
)
