# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-20 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('execution', '0002_testsuite_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suitereport',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
