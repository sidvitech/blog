# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_imagecomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagecomment',
            name='image',
        ),
        migrations.RemoveField(
            model_name='imagecomment',
            name='user',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'images/'),
        ),
        migrations.DeleteModel(
            name='ImageComment',
        ),
    ]
