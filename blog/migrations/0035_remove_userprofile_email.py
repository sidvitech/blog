# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 12:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_auto_20160517_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
