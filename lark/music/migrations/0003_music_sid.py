# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20140707_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='sid',
            field=models.CharField(default='', max_length=10, verbose_name='SID', blank=True),
            preserve_default=False,
        ),
    ]
