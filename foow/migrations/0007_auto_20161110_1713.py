# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 16:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foow', '0006_auto_20161107_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-pub_date']},
        ),
    ]