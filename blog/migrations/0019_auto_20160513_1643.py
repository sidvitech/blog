# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-13 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20160513_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='/media/user/profile_pictures/no-image.jpg', upload_to='/media/user/profile_pictures/'),
        ),
    ]
