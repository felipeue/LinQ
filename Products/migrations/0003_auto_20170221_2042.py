# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-21 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_rack_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='codigo',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
