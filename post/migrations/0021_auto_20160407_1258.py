# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_mycomment_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycomment',
            name='user_name',
            field=models.CharField(max_length=20),
        ),
    ]
