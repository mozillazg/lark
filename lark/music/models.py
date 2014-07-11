#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


@python_2_unicode_compatible
class Music(TimeStampedModel):
    title = models.CharField(_('title'), max_length=100)
    author = models.CharField(_('author'), max_length=50)
    cover = models.URLField(_('album cover'))
    douban = models.URLField(_('douban page'), blank=True)
    mp3 = models.URLField(_('mp3 file url'))
    ogg = models.URLField(_('ogg file url'))
    sid = models.CharField(_('SID'), max_length=10, blank=True)

    class Meta:
        verbose_name = _('music')
        verbose_name_plural = _('music')

    def __str__(self):
        return '"{0}" by {1}'.format(self.title, self.author)

    def save(self, *args, **kwargs):
        super(Music, self).save(*args, **kwargs)
        if not self.sid:
            self.sid = self.pk
            self.save(update_fields=('sid',))
