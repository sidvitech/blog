# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_auto_20160405_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unlike',
            name='user',
        ),
        migrations.AddField(
            model_name='unlike',
            name='like',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.Like'),
            preserve_default=False,
        ),
    ]
