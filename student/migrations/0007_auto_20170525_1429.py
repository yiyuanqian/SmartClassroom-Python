# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20170525_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='duty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Duty'),
        ),
    ]
