# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 18:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20160625_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 25, 18, 42, 3, 726599, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
