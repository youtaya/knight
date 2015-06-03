# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joboard', '0005_auto_20150603_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identity_image', models.ImageField(upload_to=b'identity')),
                ('name', models.CharField(max_length=24, blank=True)),
                ('gender', models.CharField(max_length=4)),
                ('birthday', models.CharField(max_length=24)),
                ('experience', models.CharField(max_length=24)),
                ('education', models.CharField(max_length=24)),
                ('phone', models.CharField(max_length=24)),
                ('apply_job', models.CharField(max_length=24)),
                ('expect_salary', models.CharField(max_length=24)),
                ('self_description', models.CharField(max_length=100)),
                ('apply_factory', models.ForeignKey(related_name='factory', to='joboard.Factory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
