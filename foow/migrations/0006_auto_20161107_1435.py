# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-07 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foow', '0005_auto_20161104_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_subtitle',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blog_title',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
