from django.contrib import admin
from .models import (Campus, Program, Course, Curriculum,
                     Student, STSBracket, Scholarship,
                     AcademicYear, EnrollmentTransaction, Professor)
# from sais.models import *
# Register your models here.

admin.site.register(Campus)
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(Curriculum)
admin.site.register(Student)
admin.site.register(STSBracket)
admin.site.register(Scholarship)
admin.site.register(AcademicYear)
admin.site.register(EnrollmentTransaction)
admin.site.register(Professor)
