# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0003_blogapp_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentAdd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostAdd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postname', models.CharField(unique=True, max_length=200)),
                ('text', models.TextField()),
                ('picture', models.FileField(null=True, upload_to=b'', blank=True)),
                ('visibility', models.CharField(max_length=200)),
                ('blogname', models.ForeignKey(to='blogapp.Blogapp')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='commentadd',
            name='postname',
            field=models.ForeignKey(blank=True, to='post.PostAdd', null=True),
        ),
    ]
