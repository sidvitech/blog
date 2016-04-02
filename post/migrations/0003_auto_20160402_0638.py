# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20160402_0616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postadd',
            old_name='picture',
            new_name='image',
        ),
    ]
