# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-21 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregister',
            name='event',
            field=models.CharField(max_length=100),
        ),
    ]
