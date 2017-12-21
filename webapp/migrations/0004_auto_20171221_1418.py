# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-21 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_eventname_eventid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventname',
            name='eventid',
        ),
        migrations.AddField(
            model_name='eventname',
            name='shortname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
