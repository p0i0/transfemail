# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 21:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_attachfile_filesize'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachfile',
            name='filesize',
        ),
    ]
