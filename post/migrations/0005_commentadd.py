# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20160402_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentAdd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('postname', models.ForeignKey(to='post.PostAdd')),
            ],
        ),
    ]
