# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20160822_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='appt',
            name='my_symbol',
            field=models.CharField(default='&#x263a;', max_length=10),
        ),
        migrations.AlterField(
            model_name='appt',
            name='my_status',
            field=models.CharField(max_length=12),
        ),
    ]
