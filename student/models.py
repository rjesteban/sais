# from __future__ import unicode_literals
import datetime

from django.db import models
from django.contrib.auth.models import User
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

    def __str__(self):
        return self.last_name + ', ' + self.first_name


class Student(models.Model):
    student_id = models.IntegerField(unique=True)
    user = models.OneToOneField(User)
    last_name = models.CharField(max_length=100, blank=False)
    first_name = models.CharField(max_length=100, blank=False)
    middle_name = models.CharField(max_length=100, blank=False)
    year = models.IntegerField(blank=False)
    admitted_campus = models.ForeignKey(Campus, blank=False)
    up_mail = models.EmailField(blank=False)
    address = models.CharField(max_length=200)
    birthday = models.DateField(blank=False)
    gender = models.CharField(max_length=7)

    def __str__(self):
        return str(self.student_id)


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
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.code_name + ' ' + str(self.course_no)


class Curriculum(models.Model):
    program = models.OneToOneField(Program, blank=False)
    date_instituted = models.DateTimeField(blank=False)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.program.name + ': ' + str(self.date_instituted.year)


class STSBracket(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    bracket = models.CharField(unique=True, blank=False, max_length=3)
    tuition_subsidy = models.FloatField(unique=True, blank=False)
    beneficiary = models.ManyToManyField(Student)

    def __str__(self):
        return self.bracket


class Scholarship(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    tuition_subsidy = models.IntegerField(blank=False)
    beneficiary = models.ManyToManyField(Student)

    def __str__(self):
        return self.name


class AcademicYear(models.Model):
    semester = models.IntegerField(blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)

    def __str__(self):
        return self.semester + ' sem ' + str(self.start_date.year) + '-' + \
                                             str(self.end_date.year)


class EnrollmentTransaction(models.Model):
    academic_calendar = models.OneToOneField(AcademicYear)
    student = models.OneToOneField(Student)
    cash = models.FloatField(null=False)
    paid = models.BooleanField(blank=False, default=False)

    def __str__self(self):
        return self.id + ': ' + self.student
