from django.conf.urls import url

from . import views

app_name = 'student'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^detail/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^results/(?P<question_id>[0-9]+)
    # /$', views.results, name='results'),
    # url(r'^vote/(?P<question_id>[0-9]+)/$', views.vote, name='vote'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/edit-profile$', views.EditProfileView.as_view(),
    #     name='edit-profile'),
    # url(r^/enroll/^$, views.EnrollClassView.as_view(),name='enlist')
]
