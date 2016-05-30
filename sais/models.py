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
    acronym = models.CharField(max_length=10, blank=False, unique=True)
    address = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class Program(models.Model):
    degree = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank=False)
    campus = models.ForeignKey(Campus, blank=False)

    def __str__(self):
        return self.degree + ' ' + self.name + ' ' + self.campus.acronym


class Professor(models.Model):
    last_name = models.CharField(max_length=100, blank=False)
    first_name = models.CharField(max_length=100, blank=False)
    middle_name = models.CharField(max_length=100, blank=False)
    campus = models.ForeignKey(Campus)
    login_profile = models.OneToOneField(User)

    def __str__(self):
        return self.last_name + ', ' + self.first_name


class STSBracket(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    bracket = models.CharField(unique=True, blank=False, max_length=5)
    tuition_subsidy = models.FloatField(blank=False)

    def __str__(self):
        return self.bracket


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code_name = models.CharField(max_length=30, blank=False, null=False)
    course_no = models.IntegerField(blank=False, null=False)
    units = models.FloatField(blank=False, default=0.0)
    prerequisite = models.ForeignKey('self', blank=True, null=True)

    def __str__(self):
        return self.code_name + ' ' + str(self.course_no)

    class Meta:
        ordering = ['code_name', 'course_no', 'units']


class AcademicYear(models.Model):
    SEMESTER_CHOICES = (
        (1, 'First Semester'),
        (2, 'Second Semester'),
        (3, 'Summer'),
        )
    semester = models.IntegerField(blank=False, choices=SEMESTER_CHOICES)
    start_year = models.IntegerField(blank=False)
    end_year = models.IntegerField(blank=False)
    open_for_enrollment = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.get_semester_display() + ' ' + ' AY ' +\
                   str(self.start_year) + '-' + \
                   str(self.end_year)

    class Meta:
        ordering = ['start_year', 'end_year', 'semester']


class CourseSchedule(models.Model):
    start_time = models.TimeField(blank=False)
    end_time = models.TimeField(blank=False)
    days = models.IntegerField(blank=False)

    @property
    def get_days(self):
        days = bin(self.days)[2:].zfill(6)
        days_list = []
        for i in range(len(days)):
            if days[i] == '1':
                if i == 0:
                    days_list.append('M')
                elif i == 1:
                    days_list.append('T')
                elif i == 2:
                    days_list.append('W')
                elif i == 3:
                    days_list.append('Th')
                elif i == 4:
                    days_list.append('F')
                elif i == 5:
                    days_list.append('S')
        return days_list

    def __str__(self):
        my_list = self.get_days
        return str(self.start_time) + '-' + str(self.end_time) + ' '\
            + '-'.join(my_list)


class CourseOffered(models.Model):
    course = models.ForeignKey(Course)
    block = models.CharField(blank=False, max_length=10)
    academic_year = models.ForeignKey(AcademicYear)
    schedule = models.ForeignKey(CourseSchedule)
    professor = models.ForeignKey(Professor)
    location = models.CharField(max_length=100, blank=False)
    campus = models.ForeignKey(Campus)
    price = models.IntegerField(blank=False)
    slots = models.IntegerField(blank=False, default=30)

    def __str__(self):
        return str(self.course) + ' ' + self.block + ' ' + self.campus.acronym

    class Meta:
        ordering = ['academic_year']
