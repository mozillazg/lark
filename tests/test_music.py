#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import json

from django.core.urlresolvers import reverse_lazy
import pytest

from music.models import Music
from music.views import next_music


@pytest.mark.django_db
class TestMusic(object):
    def setup(self):
        self.a = dict(title='music_a', author='author_a',
                      cover='http://www.example.com/a.jpg',
                      douban='http://music.douban.com/a',
                      mp3='http://www.example.com/a.mp3',
                      ogg='http://www.example.com/a.ogg'
                      )
        self.b = dict(title='music_b', author='author_b',
                      cover='http://www.example.com/b.jpg',
                      douban='http://music.douban.com/b',
                      mp3='http://www.example.com/b.mp3',
                      ogg='http://www.example.com/b.ogg'
                      )
        Music.objects.create(**self.a)
        Music.objects.create(**self.b)

    def test_music(self):
        a = Music.objects.get(title=self.a['title'])
        b = Music.objects.get(title=self.b['title'])
        assert a.author == self.a['author']
        assert a.mp3 == self.a['mp3']
        assert b.author == self.b['author']
        assert b.mp3 == self.b['mp3']


@pytest.mark.django_db
class TestView(object):
    def setup(self):
        self.c = dict(title='music_c', author='author_c',
                      cover='http://www.example.com/c.jpg',
                      douban='http://music.douban.com/c',
                      mp3='http://www.example.com/c.mp3',
                      ogg='http://www.example.com/c.ogg'
                      )
        self.d = dict(title='music_d', author='author_d',
                      cover='http://www.example.com/d.jpg',
                      douban='http://music.douban.com/d',
                      mp3='http://www.example.com/d.mp3',
                      ogg='http://www.example.com/d.ogg'
                      )
        Music.objects.create(**self.c)
        Music.objects.create(**self.d)

    def test_next_music(self, rf):
        request = rf.get(reverse_lazy('music:next', kwargs={'next_number': 1}))
        response = next_music(request, 1)
        assert response.status_code == 200
        assert json.loads(response.content)['data'] in (self.c, self.d)

    def test_random(self, client):
        response = client.get(reverse_lazy('music:random'))
        assert response.status_code == 200
        assert json.loads(response.content)['data'] in (self.c, self.d)
