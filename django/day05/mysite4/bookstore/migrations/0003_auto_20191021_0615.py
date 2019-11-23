# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-21 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_auto_20191018_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='书名'),
        ),
        migrations.AlterField(
            model_name='bookstore',
            name='title',
            field=models.CharField(max_length=20, verbose_name='书名'),
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
    ]