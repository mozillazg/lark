#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import copy
import json

from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.http import HttpResponse
import pytest

from music.admin import MusicAdmin
from music.decorators import json_view
from music.models import Music
from music.views import next_music, json_obj, random_music


@pytest.mark.django_db
class BaseTest(object):

    def setup(self):
        """测试前执行的代码"""
        self.a = dict(title='music_a', author='author_a',
                      cover='http://www.example.com/a.jpg',
                      douban='http://music.douban.com/a',
                      mp3='http://www.example.com/a.mp3',
                      ogg='http://www.example.com/a.ogg',
                      sid='1',
                      )
        self.b = dict(title='music_b', author='author_b',
                      cover='http://www.example.com/b.jpg',
                      douban='http://music.douban.com/b',
                      mp3='http://www.example.com/b.mp3',
                      ogg='http://www.example.com/b.ogg',
                      sid='2',
                      )
        self.c = dict(title='music_c', author='author_c',
                      cover='http://www.example.com/c.jpg',
                      douban='http://music.douban.com/c',
                      mp3='http://www.example.com/c.mp3',
                      ogg='http://www.example.com/c.ogg',
                      sid='4',
                      )
        self.d = dict(title='music_d', author='author_d',
                      cover='http://www.example.com/d.jpg',
                      douban='http://music.douban.com/d',
                      mp3='http://www.example.com/d.mp3',
                      ogg='http://www.example.com/d.ogg',
                      sid='5',
                      )
        self.e = copy.copy(self.d)
        self.e.pop('sid')
        self.m_c = Music.objects.create(**self.c)
        self.m_d = Music.objects.create(**self.d)
        Music(**self.e).save()
        Music.objects.create(**self.a)
        Music.objects.create(**self.b)

        self.username = 'aswxcddvz@!1322214'
        self.password = 'eee21*+daa1@dd/2'
        self.email = 'agc124ds@abded113c.com'
        get_user_model().objects.create_superuser(username=self.username,
                                                  password=self.password,
                                                  email=self.email)
        self.c = dict(title='music_c', author='author_c',
                      cover='http://www.example.com/c.jpg',
                      douban='http://music.douban.com/c',
                      mp3='http://www.example.com/c.mp3',
                      ogg='http://www.example.com/c.ogg',
                      sid='4',
                      )
        self.m_c = Music.objects.create(**self.c)

    def teardown(self):
        """测试后执行的代码"""
        Music.objects.all().delete()


class TestMusic(BaseTest):

    def test_music(self):
        a = Music.objects.get(title=self.a['title'])
        b = Music.objects.get(title=self.b['title'])
        assert a.author == self.a['author']
        assert a.mp3 == self.a['mp3']
        assert b.author == self.b['author']
        assert b.mp3 == self.b['mp3']
        assert self.a['author'] in str(a)


class TestView(BaseTest):

    def test_json_obj(self):
        obj = json_obj(self.m_c)
        assert obj['title'] == self.m_c.title

    def test_music(self, client):
        response = client.get(reverse('music:music', kwargs={'sid': 4}))
        assert json.loads(response.content.decode()) == self.c

    def test_music_sid_error(self, client):
        response = client.get(reverse('music:music', kwargs={'sid': 1000}))
        assert json.loads(response.content.decode())

    def test_next_music(self, rf):
        request = rf.get(reverse('music:next', kwargs={'next_number': 1}))
        response = next_music(request, 1)
        assert response.status_code == 200
        assert json.loads(response.content.decode())

    def test_next_music_index_error(self, rf):
        request = rf.get(reverse('music:next', kwargs={'next_number': 10000}))
        response = next_music(request, 10000)
        assert response.status_code == 200
        assert json.loads(response.content.decode())

    def test_random(self, rf):
        request = rf.get(reverse('music:random'))
        response = random_music(request)
        assert response.status_code == 200
        assert json.loads(response.content.decode())


class TestDeocrator(object):
    def test_json_view(self, rf):
        d1 = {'data': 'hello'}
        view1 = lambda request: d1
        view2 = lambda request: (d1, 400)
        view3 = lambda request: HttpResponse(str(d1))

        response = json_view(view1)(rf.get('/'))
        assert isinstance(response, HttpResponse)
        assert response.status_code == 200
        assert response['Content-Type'] == 'application/json'
        assert json.loads(response.content.decode()) == d1

        response = json_view(view2)(rf.get('/'))
        assert isinstance(response, HttpResponse)
        assert response.status_code == 400
        assert response['Content-Type'] == 'application/json'
        assert json.loads(response.content.decode()) == d1

        response = json_view(view3)(rf.get('/'))
        assert isinstance(response, HttpResponse)
        assert response.status_code == 200
        assert response['Content-Type'] == 'text/html; charset=utf-8'
        assert response.content.decode() == str(d1)


class TestAdmin(BaseTest):

    def test_music_list_url(self, client):
        client.login(username=self.username, password=self.password)
        response = client.get(reverse('admin:music_music_changelist'))
        assert response.status_code == 200

    def test_music_admin_changelist(self, client):
        client.login(username=self.username, password=self.password)
        m = MusicAdmin(Music, admin.site)
        assert self.m_c.ogg in m.audio_ogg(self.m_c)
        assert self.m_c.mp3 in m.audio_mp3(self.m_c)
