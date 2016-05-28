# from __future__ import unicode_literals
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html_join
from django.contrib import admin
from django.utils import timezone

# Create your models here.


class Campus(models.Model):
    name = models.CharField(max_length=100, blank=False)
    acronym = models.CharField(max_length=10, blank=False)
    address = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class Program(models.Model):
    degree = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank=False)
    campus = models.ForeignKey(Campus)

    def __str__(self):
        return self.degree + ' ' + self.name + ' ' + self.campus.acronym


class Professor(models.Model):
    last_name = models.CharField(max_length=100, blank=False)
    first_name = models.CharField(max_length=100, blank=False)
    middle_name = models.CharField(max_length=100, blank=False)
    login_profile = models.OneToOneField(User)

    def __str__(self):
        return self.last_name + ', ' + self.first_name


class STSBracket(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    bracket = models.CharField(unique=True, blank=False, max_length=3)
    tuition_subsidy = models.FloatField(unique=True, blank=False)

    def __str__(self):
        return self.bracket


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code_name = models.CharField(max_length=30, blank=False, null=False)
    course_no = models.IntegerField(blank=False, null=False)
    block = models.CharField(blank=False, max_length=10)
    professor = models.ForeignKey(Professor, blank=False, null=False)
    prerequisite = models.ForeignKey('self', blank=True, null=True)
    start_hour_time = models.IntegerField(blank=False)
    start_min_time = models.IntegerField(blank=False)
    end_hour_time = models.IntegerField(blank=False)
    end_min_time = models.IntegerField(blank=False)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=False)
    price = models.IntegerField(blank=False)

    def __str__(self):
        return self.code_name + ' ' + str(self.course_no) + ': '\
               + self.program.campus.acronym


class Curriculum(models.Model):
    program = models.OneToOneField(Program, blank=False)
    date_instituted = models.DateTimeField(blank=False)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.program.name + ': ' + str(self.date_instituted.year) +\
               ' ' + self.program.campus.acronym


class AcademicYear(models.Model):
    semester = models.IntegerField(blank=False)
    start_year = models.IntegerField(blank=False)
    end_year = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.semester) + ' sem ' +\
                   str(self.start_year) + '-' + \
                   str(self.end_year)
