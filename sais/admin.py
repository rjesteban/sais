from django.contrib import admin
from .models import *
from student.models import *
# Register your models here.

admin.site.register(Campus)
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(STSBracket)
admin.site.register(Scholarship)
admin.site.register(AcademicYear)
admin.site.register(Transaction)
admin.site.register(Professor)
admin.site.register(EnlistedCourse)
admin.site.register(StudentScholarship)
admin.site.register(CourseOffered)
admin.site.register(CourseSchedule)
admin.site.register(EnrolledCourse)
admin.site.register(Term)
