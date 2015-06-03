# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joboard', '0004_auto_20150522_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='job_position',
            field=models.CharField(max_length=40, choices=[('\u7535\u8bdd\u9500\u552e', '\u7535\u8bdd\u9500\u552e'), ('\u666e\u5de5/\u5b66\u5f92\u5de5', '\u666e\u5de5/\u5b66\u5f92\u5de5'), ('\u670d\u52a1\u5458', '\u670d\u52a1\u5458'), ('\u8425\u4e1a\u5458/\u5e97\u5458', '\u8425\u4e1a\u5458/\u5e97\u5458'), ('\u884c\u653f\u4e13\u5458/\u52a9\u7406', '\u884c\u653f\u4e13\u5458/\u52a9\u7406'), ('\u5bfc\u8d2d', '\u5bfc\u8d2d'), ('\u5ba2\u670d\u4e13\u5458/\u52a9\u7406', '\u5ba2\u670d\u4e13\u5458/\u52a9\u7406'), ('\u6536\u94f6\u5458', '\u6536\u94f6\u5458'), ('\u5176\u4ed6', '\u5176\u4ed6')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='factory',
            name='job_salary',
            field=models.CharField(max_length=10, choices=[('\u9762\u8c08', '\u9762\u8c08'), ('1000\u5143\u4ee5\u4e0b', '1000\u5143\u4ee5\u4e0b'), ('1000\uff0d2000\u5143', '1000\uff0d2000\u5143'), ('2000\uff0d3000\u5143', '2000\uff0d3000\u5143'), ('3000\uff0d5000\u5143', '3000\uff0d5000\u5143'), ('5000\uff0d8000\u5143', '5000\uff0d8000\u5143'), ('8000-12000\u5143', '8000-12000\u5143'), ('12000\uff0d20000\u5143', '12000\uff0d20000\u5143'), ('20000\u4ee5\u4e0a', '20000\u4ee5\u4e0a')]),
            preserve_default=True,
        ),
    ]
