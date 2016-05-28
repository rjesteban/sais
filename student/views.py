from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
# from django.core.urlresolvers import reverse
# from django.template import loader
from django.views.generic import DetailView, ListView
from .models import Student
from sais.views import LoginView, LogoutView
from sais.forms import LoginForm
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
