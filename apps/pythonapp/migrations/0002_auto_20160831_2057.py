# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokes',
            name='poked',
            field=models.IntegerField(null=True),
        ),
    ]
