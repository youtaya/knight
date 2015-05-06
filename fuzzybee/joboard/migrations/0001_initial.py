# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fact_name', models.CharField(max_length=200)),
                ('fact_addr', models.CharField(max_length=200)),
                ('fact_lat', models.FloatField()),
                ('fact_lng', models.FloatField()),
                ('hire_num', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['fact_name', 'hire_num'],
            },
            bases=(models.Model,),
        ),
    ]
