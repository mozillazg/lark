#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import logging
import random

from .decorators import json_view
from .models import Music

logger = logging.getLogger(__name__)


def json_obj(music):
    obj = {
        'title': music.title,
        'author': music.author,
        'cover': music.cover,
        'douban': music.douban,
        'mp3': music.mp3,
        'ogg': music.ogg,
        'sid': music.sid,
    }
    return obj


@json_view
def music(request, sid):
    """通过 sid 获取歌曲信息"""
    logger.debug('music - sid: %s' % sid)
    try:
        music = Music.objects.filter(sid=sid)[0]
    except IndexError:
        music = Music.objects.filter()[0]
    return json_obj(music)


@json_view
def next_music(request, next_number):
    """下一首歌"""
    try:
        music = Music.objects.filter()[int(next_number) + 1]
    except IndexError:
        music = Music.objects.filter()[0]
    logger.debug('music - %s' % music.pk)
    return json_obj(music)


@json_view
def random_music(request):
    """随机歌曲"""
    next_number = random.randint(0, Music.objects.filter().count() - 2)
    return next_music(request, next_number)
