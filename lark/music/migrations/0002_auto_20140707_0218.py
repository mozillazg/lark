# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={'verbose_name': 'music', 'verbose_name_plural': 'music'},
        ),
        migrations.AddField(
            model_name='music',
            name='douban',
            field=models.URLField(default='', verbose_name='douban page', blank=True),
            preserve_default=False,
        ),
    ]
