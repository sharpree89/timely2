# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20160821_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='appt',
            name='my_date',
            field=models.DateField(default='2016-08-21'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appt',
            name='my_time',
            field=models.TimeField(default='14:30:59'),
            preserve_default=False,
        ),
    ]
