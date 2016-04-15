# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 12:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0013_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postadd',
            name='choice',
        ),
        migrations.AddField(
            model_name='commentadd',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commentadd',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='commentadd',
            name='postname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.PostAdd'),
        ),
        migrations.AlterField(
            model_name='postadd',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
