from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django.template import loader
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from .models import Student, Term, EnrolledCourse, EnlistedCourse
from sais.models import CourseOffered, AcademicYear
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
        context['term'] = AcademicYear.objects.filter(open_for_enrollment=True)
        return context


class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'student/profile.html'
    model = Student

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['student'] = self.request.user.student
        return context


# class EditProfileView(LoginRequiredMixin, DetailView):
#    template_name = 'student/edit-profile.html'
#    model = Student

#    def get_context_data(self, **kwargs):
#        context = super(ProfileView, self).get_context_data(**kwargs)
#        context['student'] = self.request.user.student

#        return context

#    def post(self, request, *args, **kwargs):
#        return


class GradesView(LoginRequiredMixin, ListView):
    template_name = 'student/grades.html'
    model = Term
    context_object_name = 'terms'

    def get_context_data(self, **kwargs):
        context = super(GradesView, self).get_context_data(**kwargs)
        student = self.request.user.student
        context['student'] = student
        terms = Term.objects.filter(student=student).order_by('term')
        context.update({'terms': terms})
        context['term_list'] = AcademicYear.objects.filter(
            open_for_enrollment=True)
        return context


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


class ListCoursesView(LoginRequiredMixin, ListView):
    template_name = 'student/courses.html'
    model = CourseOffered
    paginate_by = 10
    context_object_name = 'course_list'

    def get_context_data(self, **kwargs):
        context = super(ListCoursesView, self).get_context_data(**kwargs)
        student = self.request.user.student
        context['student'] = student
        course_queried = self.request.GET.get('course')
        course_no_queried = self.request.GET.get('course_no')
        see_all_clicked = self.request.GET.get('seeall')

        course_query = str(course_queried)
        course_no_query = str(course_no_queried)
        courses = []
        if course_query and course_no_query:
            courses = self.get_courses_by_course_name_num(
                student, course_query, course_no_query)

        if see_all_clicked:
            courses = self.get_all_courses(student)

        context.update({'course_list': courses})
        context['enlisted_courses'] = CourseOffered.objects.filter(
            enlisted__student__pk=student.pk)
        context['enrolled_courses'] = CourseOffered.objects.filter(
            enrolled__student__pk=student.pk)
        return context

    def post(self, request, *args, **kwargs):
        post = request.POST
        icourse = CourseOffered.objects.get(pk=post['pk'])
        istudent = request.user.student
        EnlistedCourse.objects.create(course=icourse,
                                      student=istudent)
        return redirect(reverse('student:enlist'))

    def get_courses_by_course_name_num(self, student, name_query, no_query):
        return CourseOffered.objects.filter(
            course__code_name__icontains=name_query,
            course__course_no__icontains=no_query,
            academic_year__open_for_enrollment=True,
            campus=student.admitted_campus)

    def get_all_courses(self, student):
        return CourseOffered.objects.filter(
            academic_year__open_for_enrollment=True,
            campus=student.admitted_campus)


class EnlistedCoursesView(LoginRequiredMixin, ListView):
    template_name = 'student/enlisted-courses.html'
    model = EnlistedCourse
    paginate_by = 10
    context_object_name = 'course_list'

    def get_context_data(self, **kwargs):
        context = super(EnlistedCoursesView, self).get_context_data(**kwargs)
        context['student'] = self.request.user.student
        enlisted = context['student'].enlisted_courses.filter(
            course__academic_year__open_for_enrollment=True)
        context.update({'course_list': enlisted})
        return context

    def post(self, request, *args, **kwargs):
        post = request.POST
        course = EnlistedCourse.objects.get(pk=post['pk'])
        course.delete()
        return redirect(reverse('student:enlisted-courses'))


class ScheduleView(LoginRequiredMixin, DetailView):
    template_name = 'student/schedule.html'
    model = Term
    context_object_name = 'term'

    def get_context_data(self, **kwargs):
        context = super(ScheduleView, self).get_context_data(**kwargs)
        context['student'] = self.request.user.student
        context['courses'] = EnrolledCourse.objects.filter(
            student__pk=context['student'].pk,
            course__academic_year=context['term'].term)
        return context


class ScheduleTabView(LoginRequiredMixin, DetailView):
    template_name = 'student/sched-table.html'
    model = Term
    context_object_name = 'term'

    def get_context_data(self, **kwargs):
        context = super(ScheduleTabView, self).get_context_data(**kwargs)
        context['student'] = self.request.user.student
        context['courses'] = EnrolledCourse.objects.filter(
            student__pk=context['student'].pk,
            course__academic_year=context['term'].term)
        return context


class EnlistedScheduleView(LoginRequiredMixin, DetailView):
    template_name = 'student/schedule-enlisted.html'
    model = AcademicYear
    context_object_name = 'term'

    def get_context_data(self, **kwargs):
        context = super(EnlistedScheduleView, self).get_context_data(**kwargs)
        context['student'] = self.request.user.student
        context['courses'] = EnlistedCourse.objects.filter(
            student__pk=context['student'].pk,
            course__academic_year=context['term'])
        return context


class EnlistedSchedTabView(LoginRequiredMixin, DetailView):
    template_name = 'student/schedule-enlisted-tab.html'
    model = AcademicYear
    context_object_name = 'term'

    def get_context_data(self, **kwargs):
        context = super(EnlistedSchedTabView, self).get_context_data(**kwargs)
        context['student'] = self.request.user.student
        context['courses'] = EnlistedCourse.objects.filter(
            student__pk=context['student'].pk,
            course__academic_year=context['term'])
        return context
