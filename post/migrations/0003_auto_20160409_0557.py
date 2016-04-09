# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20160407_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postadd',
            name='postname',
            field=models.CharField(default=1, unique=True, max_length=200),
            preserve_default=False,
        ),
    ]
