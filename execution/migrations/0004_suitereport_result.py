# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-21 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('execution', '0003_auto_20170220_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='suitereport',
            name='result',
            field=models.CharField(default='Passed', max_length=10),
            preserve_default=False,
        ),
    ]
