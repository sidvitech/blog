# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20160402_0638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postadd',
            old_name='image',
            new_name='picture',
        ),
    ]
