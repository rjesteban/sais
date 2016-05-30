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
    url(r'^$', views.IndexView.as_view(), name='menu'),
    url(r'^login$', views.StudentLoginView.as_view(), name='login'),
    url(r'^logout$', views.StudentLogoutView.as_view(), name='logout'),
    url(r'^view-profile$', views.ProfileView.as_view(), name='profile'),
    url(r'^grades$', views.GradesView.as_view(), name='grades'),
    url(r'^courses$', views.ListCoursesView.as_view(), name='enlist'),
    url(r'^enlisted-courses$', views.EnlistedCoursesView.as_view(),
        name='enlisted-courses'),
    url(r'^(?P<pk>\d+)/enlisted-courses$', views.EnlistedCoursesView.as_view(),
        name='remove-enlisted'),
    url(r'^(?P<pk>\d+)/add$', views.ListCoursesView.as_view(), name='enlist'),
    url(r'^(?P<pk>\d+)/grade$', views.GradesTermView.as_view(), name='term'),
    url(r'^(?P<pk>\d+)/sched$', views.ScheduleView.as_view(), name='schedule'),
    url(r'^(?P<pk>\d+)/sched-table$',
        views.ScheduleTabView.as_view(), name='sched-tab'),
    url(r'^(?P<pk>\d+)/enl-schedule$', views.EnlistedScheduleView.as_view(),
        name='enl-schedule'),
    url(r'^(?P<pk>\d+)/enl-sched-tab$',
        views.EnlistedSchedTabView.as_view(), name='enl-sched-tab'),
]
