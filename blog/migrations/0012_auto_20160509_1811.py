# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20160509_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='thumb',
            field=models.ImageField(blank=True, upload_to='/blog/images/'),
        ),
    ]
