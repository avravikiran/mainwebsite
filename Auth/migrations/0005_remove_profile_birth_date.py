# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 13:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
    ]
