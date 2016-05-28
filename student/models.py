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
    program = models.ForeignKey(Program)
    sts_bracket = models.ForeignKey(STSBracket, blank=False)
    address = models.CharField(max_length=200)
    birthday = models.DateField(blank=False)
    gender = models.CharField(max_length=7)

    def __str__(self):
        return str(self.student_id)[0:4] + '-' + str(self.student_id)[4:]
        # return self.scholarships()

    @property
    def name(self):
        name = self.first_name + ' ' + self.middle_name + ' ' + self.last_name
        return name

    @property
    def year(self):
        student_year = int(str(self.student_id)[0:4])
        today = datetime.datetime.now()
        difference = today.year - student_year
        if today.month > 7:
            difference += 1
        return difference

    @property
    def scholarships(self):
        scholarships = self.studentscholarship_set.all()
        return scholarships


class Transaction(models.Model):
    TRANSACTION_STATUS = ((1, 'Unpaid'), (2, 'Promised'), (3, 'Paid'))
    academic_calendar = models.OneToOneField(AcademicYear)
    student = models.ForeignKey(Student)
    total = models.FloatField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=TRANSACTION_STATUS, default=1)

    def __str__(self):
        return str(self.pk) + ': ' + str(self.student)


class EnlistedCourse(models.Model):
    GRADE_CHOICES = (
        (1.00, '1.00',),
        (1.25, '1.25',),
        (1.50, '1.50',),
        (1.75, '1.75',),
        (2.00, '2.00',),
        (2.25, '2.25',),
        (2.50, '2.50',),
        (2.75, '2.75',),
        (3.00, '3.00',),
        (4.00, '4.00',),
        (5.00, '5.00',),
        (6.00, 'INC',),
        (7.00, 'No Grade',),
        )
    course = models.ForeignKey(CourseOffered)
    student = models.ForeignKey(Student)
    is_enrolled = models.BooleanField(default=False, blank=False)
    grade = models.FloatField(choices=GRADE_CHOICES, default=7.00)

    def __str__(self):
        return str(self.student) + ' ' +\
               str(self.course.course) + ' ' +\
               str(self.course.block)


class StudentScholarship(models.Model):
    student = models.ForeignKey(Student)
    scholarship = models.ForeignKey(Scholarship)
    is_active = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return str(self.student) + ': ' + str(self.scholarship)
