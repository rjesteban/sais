from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
# from django.core.urlresolvers import reverse
# from django.template import loader
from django.views.generic import DetailView, ListView
from .models import Student


class IndexView(ListView):
    template_name = 'student/index.html'
    model = Student
