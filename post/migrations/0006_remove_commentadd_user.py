# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_commentadd_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentadd',
            name='user',
        ),
    ]
