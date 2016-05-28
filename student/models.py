# from __future__ import unicode_literals
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html_join
from django.contrib import admin
from django.utils import timezone
from sais.models import *

# Create your models here.


class Scholarship(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    tuition_subsidy = models.IntegerField(blank=False)

    def __str__(self):
        return self.name


class Student(models.Model):
    student_id = models.IntegerField(unique=True)
    login_profile = models.OneToOneField(User)
    last_name = models.CharField(max_length=100, blank=False)
    first_name = models.CharField(max_length=100, blank=False)
    middle_name = models.CharField(max_length=100, blank=False)
    admitted_campus = models.ForeignKey(Campus, blank=False)
    up_mail = models.EmailField(blank=False)
    sts_bracket = models.ForeignKey(STSBracket, blank=False)
    address = models.CharField(max_length=200)
    birthday = models.DateField(blank=False)
    gender = models.CharField(max_length=7)

    def __str__(self):
        return str(self.student_id)[0:4] + '-' + str(self.student_id)[4:]
        # return self.scholarships()

    # @property
    # def scholarships(self):
    #    scholarships = self.scholarships_set.objects.all()
    #    list = ''
    #    for scholarship in scholarships:
    #        list += ', ' + str(scholarship)
    #   return list


class Transaction(models.Model):
    academic_calendar = models.OneToOneField(AcademicYear)
    student = models.ForeignKey(Student)
    total = models.FloatField(null=False)
    paid = models.BooleanField(blank=False, default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk) + ': ' + str(self.student)


class EnlistedCourse(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    is_enrolled = models.BooleanField(default=False, blank=False)
    grade = models.FloatField(blank=False, default=0.0)

    def __str__(self):
        return self.course.code_name + ' ' + str(self.course.course_no) +\
               ' ' + str(self.student)


class StudentScholarship(models.Model):
    student = models.ForeignKey(Student)
    scholarship = models.ForeignKey(Scholarship)
    is_active = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return str(self.student) + ': ' + str(self.scholarship)
