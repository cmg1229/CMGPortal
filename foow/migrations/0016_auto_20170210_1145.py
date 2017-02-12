# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 10:45
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foow', '0015_picture_album_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='picture',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location=b'C:\\Users\\cmg1229\\Documents\\DjangoProjects\\CMGPortal/media'), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'C:\\Users\\cmg1229\\Documents\\DjangoProjects\\CMGPortal/media'), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='picture',
            name='thumbnail',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'C:\\Users\\cmg1229\\Documents\\DjangoProjects\\CMGPortal/media'), upload_to=b''),
        ),
    ]
