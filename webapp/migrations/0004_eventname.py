# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20171021_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
