# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-06 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foow', '0014_album_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='album_header',
            field=models.BooleanField(default=False),
        ),
    ]
