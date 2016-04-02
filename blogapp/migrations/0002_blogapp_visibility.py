# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogapp',
            name='visibility',
            field=models.CharField(default='private', max_length=200),
            preserve_default=False,
        ),
    ]
