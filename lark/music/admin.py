#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin
from django.utils.html import format_html

from .models import Music


class MusicAdmin(admin.ModelAdmin):

    def audio_ogg(self, obj):
        return format_html('''<audio src="%s" controls style="width: 100px;">
                           </audio>''' % obj.ogg)
    audio_ogg.short_description = 'ogg'

    def audio_mp3(self, obj):
        return format_html('''<audio src="%s" controls style="width: 100px;">
                           </audio>''' % obj.mp3)
    audio_mp3.short_description = 'mp3'

    list_display = ('id', 'sid', 'title', 'author', 'audio_ogg', 'audio_mp3',
                    'created', 'modified')
    search_fields = ('title', 'author')
admin.site.register(Music, MusicAdmin)
