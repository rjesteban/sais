# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-29 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20160529_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terms', to='student.Student'),
        ),
    ]
