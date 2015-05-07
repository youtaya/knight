# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import joboard.models


class Migration(migrations.Migration):

    dependencies = [
        ('joboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='fact_addr',
            field=joboard.models.PlaceMultiModelField(),
            preserve_default=True,
        ),
    ]
