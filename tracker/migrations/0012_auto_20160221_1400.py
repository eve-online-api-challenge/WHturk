# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_system_color_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='color_code',
            field=models.CharField(max_length=20),
        ),
    ]
