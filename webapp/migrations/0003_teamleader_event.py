# -*- coding: utf-8 -*-=
# Generated by Django 1.11.6 on 2018-01-09 11:36

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_team_teamleader'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamleader',
            name='event',
            field=models.CharField(default='ROBOWARS', max_length=100),
            preserve_default=False,
        ),
    ]
