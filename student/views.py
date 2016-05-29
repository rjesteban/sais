from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
# from django.core.urlresolvers import reverse
# from django.template import loader
from django.views.generic import DetailView, ListView
from .models import Student, Term, EnrolledCourse
from sais.models import CourseOffered
from sais.forms import LoginForm
from sais.views import LoginView, LogoutView
from sais.mixins import LoginRequiredMixin


class StudentLoginView(LoginView):
    template_name = "student/login.html"
    form_class = LoginForm
    success_view_name = 'student:menu'


# Inherits Class Based View "LogoutView"
class StudentLogoutView(LogoutView):
    login_view_name = 'student:login'


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'student/index.html'
    model = Student

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['student'] = self.request.user.student
        return context


class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'student/profile.html'
    model = Student

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['student'] = self.request.user.student
        return context


class GradesView(LoginRequiredMixin, ListView):
    template_name = 'student/grades.html'
    model = Student

    def get_context_data(self, **kwargs):
        context = super(GradesView, self).get_context_data(**kwargs)
        student = self.request.user.student
        context['student'] = student
        context['grades'] = student.enrolled_courses.order_by('course')
        return context


class ListCoursesView(LoginRequiredMixin, ListView):
    template_name = 'student/courses.html'
    model = CourseOffered
    paginate_by = 10
    context_object_name = 'course_list'

    def get_context_data(self, **kwargs):
        context = super(ListCoursesView, self).get_context_data(**kwargs)
        student = self.request.user.student
        context['student'] = student
        courses = CourseOffered.objects.filter(
            academic_year__open_for_enrollment=True)
        context.update({'course_list': courses})
        context['enlisted_courses'] = CourseOffered.objects.filter(
            enlisted__student__pk=student.pk)
        context['enrolled_courses'] = CourseOffered.objects.filter(
            enrolled__student__pk=student.pk)
        return context

#    def get_all_courses(self):
#        return CourseOffered


class GradesTermView(LoginRequiredMixin, DetailView):
    template_name = 'student/term-grade.html'
    model = Term
    context_object_name = 'term'

    def get_context_data(self, **kwargs):
        context = super(GradesTermView, self).get_context_data(**kwargs)
        context['student'] = self.request.user.student
        context['courses'] = EnrolledCourse.objects.filter(
            student__pk=context['student'].pk,
            course__academic_year=context['term'].term)
        return context
