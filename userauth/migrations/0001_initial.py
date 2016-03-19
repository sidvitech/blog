# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('pwd', models.CharField(max_length=200)),
                ('cfmpwd', models.CharField(max_length=200)),
            ],
        ),
    ]
