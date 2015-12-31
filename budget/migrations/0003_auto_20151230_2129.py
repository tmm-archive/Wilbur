# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_auto_20151217_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='description',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.CharField(blank=True, max_length=75),
        ),
    ]