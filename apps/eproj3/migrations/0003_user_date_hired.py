# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 21:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eproj3', '0002_wish'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_hired',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 27, 14, 44, 43, 301000)),
            preserve_default=False,
        ),
    ]
