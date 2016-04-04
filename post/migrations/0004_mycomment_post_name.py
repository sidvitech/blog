# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_remove_mycomment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycomment',
            name='post_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
            preserve_default=False,
        ),
    ]
