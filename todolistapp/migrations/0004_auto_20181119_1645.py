# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-19 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0003_auto_20181119_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='valid',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='todolisttwo',
            name='created',
            field=models.DateTimeField(),
        ),
    ]