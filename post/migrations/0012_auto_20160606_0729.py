# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-06 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20160606_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='view',
            field=models.IntegerField(default=True),
        ),
    ]
