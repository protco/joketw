# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 19:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0003_auto_20170918_1914'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='joke',
            options={'ordering': ('created',)},
        ),
    ]