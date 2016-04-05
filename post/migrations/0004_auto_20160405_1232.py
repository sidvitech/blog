# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20160405_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postadd',
            name='postname',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
