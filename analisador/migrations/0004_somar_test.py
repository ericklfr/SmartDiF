# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analisador', '0003_auto_20170828_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='somar',
            name='test',
            field=models.CharField(default='valor1', max_length=100),
        ),
    ]