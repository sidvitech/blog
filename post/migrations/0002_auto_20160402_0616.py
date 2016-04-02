# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postadd',
            name='choice',
            field=models.CharField(default='private', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postadd',
            name='picture',
            field=models.ImageField(upload_to=b'profile_images', blank=True),
        ),
        migrations.AlterField(
            model_name='postadd',
            name='text',
            field=models.TextField(),
        ),
    ]
