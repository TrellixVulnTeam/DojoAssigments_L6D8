# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-15 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninja', '0004_auto_20180815_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='some string'),
        ),
    ]