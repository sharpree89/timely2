# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0002_auto_20160819_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_task', models.CharField(max_length=45)),
                ('my_date', models.DateField(blank=True, null=True)),
                ('my_time', models.TimeField(blank=True, null=True)),
                ('my_status', models.TextField(max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userforeignkey', to='login_app.User')),
            ],
        ),
    ]
