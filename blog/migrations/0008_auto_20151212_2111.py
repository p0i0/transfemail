# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20151212_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]