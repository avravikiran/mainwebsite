# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-26 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.TextField(max_length=15),
        ),
    ]