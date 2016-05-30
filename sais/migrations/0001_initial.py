# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-29 08:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(choices=[(1, b'First Semester'), (2, b'Second Semester'), (3, b'Third Semester')])),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
            ],
            options={
                'ordering': ['semester', 'start_year', 'end_year'],
            },
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('acronym', models.CharField(max_length=10, unique=True)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('code_name', models.CharField(max_length=30)),
                ('course_no', models.IntegerField()),
                ('units', models.FloatField(default=0.0)),
                ('prerequisite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sais.Course')),
            ],
            options={
                'ordering': ['code_name', 'course_no', 'units'],
            },
        ),
        migrations.CreateModel(
            name='CourseOffered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('slots', models.IntegerField(default=30)),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sais.AcademicYear')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sais.Campus')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sais.Course')),
            ],
            options={
                'ordering': ['academic_year'],
            },
        ),
        migrations.CreateModel(
            name='CourseSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('days', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sais.Campus')),
                ('login_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sais.Campus')),
            ],
        ),
        migrations.CreateModel(
            name='STSBracket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('bracket', models.CharField(max_length=3, unique=True)),
                ('tuition_subsidy', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='courseoffered',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sais.Professor'),
        ),
        migrations.AddField(
            model_name='courseoffered',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sais.CourseSchedule'),
        ),
    ]
