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
    mp3 = models.URLField(_('mp3 file url'))
    ogg = models.URLField(_('ogg file url'))

    class Meta:
        verbose_name = _('title')
        verbose_name_plural = _('title')

    def __str__(self):
        return '<{0} by {2}>'.format(self.title, self.author)
