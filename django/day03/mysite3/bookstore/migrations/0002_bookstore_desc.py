# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-17 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookstore',
            name='desc',
            field=models.CharField(default='', max_length=100, verbose_name='描述'),
        ),
    ]
