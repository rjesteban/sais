# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-28 03:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentScholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('scholarship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Scholarship')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='cash',
            new_name='total',
        ),
        migrations.AddField(
            model_name='enlistedcourse',
            name='is_enrolled',
            field=models.BooleanField(default=False),
        ),
    ]
