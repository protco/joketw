# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 20:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0002_auto_20170522_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='completion_level',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email_is_verified',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='personal_info_is_completed',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
    ]
