# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20160625_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(blank=True, to='home.Member'),
        ),
    ]
