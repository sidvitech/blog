# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_blogapp_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostAdd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postname', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('visibility', models.CharField(max_length=200)),
                ('blogname', models.ForeignKey(to='blogapp.Blogapp')),
            ],
        ),
    ]
