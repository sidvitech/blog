# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 07:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0006_auto_20160406_0719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregistration',
            name='image',
        ),
    ]
