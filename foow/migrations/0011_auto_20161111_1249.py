# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 11:49
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foow', '0010_auto_20161111_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='picture',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media'), upload_to=''),
        ),
    ]
