#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import random

from .decorators import json_view
from .models import Music


@json_view()
def next_music(request, next_number):
    """下一首歌"""
    try:
        music = Music.objects.filter()[int(next_number)]
    except IndexError:
        music = Music.objects.filter()[0]
    obj = {
        'status': 0,
        'data': {
            'title': music.title,
            'author': music.author,
            'cover': music.cover,
            'douban': music.douban,
            'mp3': music.mp3,
            'ogg': music.ogg,
        },
    }
    return obj


def random_music(request):
    """随机歌曲"""
    next_number = random.randint(0, Music.objects.filter().count())
    return next_music(request, next_number)
