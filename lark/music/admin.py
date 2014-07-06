#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin

from .models import Music


class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created', 'modified')
    search_fields = ('title', 'author')
admin.site.register(Music, MusicAdmin)
