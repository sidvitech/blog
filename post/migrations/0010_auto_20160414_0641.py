# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20160414_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentadd',
            name='postname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='post.PostAdd'),
        ),
    ]
