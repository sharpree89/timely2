# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 22:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_auto_20161118_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
    ]
