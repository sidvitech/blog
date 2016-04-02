# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20160401_0618'),
        ('blogapp', '0002_blogapp_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogapp',
            name='category',
            field=models.ForeignKey(default=1, to='category.Category'),
            preserve_default=False,
        ),
    ]
