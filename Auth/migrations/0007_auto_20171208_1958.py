# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0006_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=128),
        ),
    ]
