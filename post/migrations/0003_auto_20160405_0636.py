# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_postadd_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postadd',
            old_name='username',
            new_name='user',
        ),
    ]
