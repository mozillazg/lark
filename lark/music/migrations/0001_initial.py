# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='music',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('author', models.CharField(max_length=50, verbose_name='author')),
                ('cover', models.URLField(verbose_name='album cover')),
                ('mp3', models.URLField(verbose_name='mp3 file url')),
                ('ogg', models.URLField(verbose_name='ogg file url')),
            ],
            options={
                'verbose_name': 'title',
                'verbose_name_plural': 'title',
            },
            bases=(models.Model,),
        ),
    ]
