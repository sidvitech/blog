# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_blogapp_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentAdd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PostAdd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postname', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('picture', models.FileField(null=True, upload_to=b'', blank=True)),
                ('visibility', models.CharField(max_length=200)),
                ('blogname', models.ForeignKey(to='blogapp.Blogapp')),
            ],
        ),
        migrations.AddField(
            model_name='commentadd',
            name='postname',
            field=models.ForeignKey(to='post.PostAdd'),
        ),
    ]
