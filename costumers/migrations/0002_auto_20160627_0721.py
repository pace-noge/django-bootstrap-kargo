# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='driver',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]