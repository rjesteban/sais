# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-29 13:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sais', '0003_auto_20160529_1752'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academicyear',
            options={'ordering': ['start_year', 'end_year', 'semester']},
        ),
    ]