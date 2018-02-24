from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.home, name='dashboard'),
    url(r'^home/api$', views.json_test, name='api'),
    url(r'^teachers/$', views.TeacherList.as_view(), name='teachers'),
    url(r'^teachers/create/$', views.TeacherCreate.as_view(), name='teacher_create'),
    url(r'^teachers/(?P<pk>\d+)/update/$', views.TeacherUpdate.as_view(), name='teacher_update'),
    url(r'^teachers/(?P<pk>\d+)/delete/$', views.TeacherDelete.as_view(), name='teacher_delete'),
    url(r'^subjects/$', views.SubjectList.as_view(), name='subjects'),
    url(r'^subjects/create/$', views.SubjectCreate.as_view(), name='subject_create'),
    url(r'^subjects/(?P<pk>\d+)/update/$', views.SubjectUpdate.as_view(), name='subject_update'),
    url(r'^subjects/(?P<pk>\d+)/delete/$', views.SubjectDelete.as_view(), name='subject_delete'),
    url(r'^students/$', views.StudentList.as_view(), name='students'),
    url(r'^students/create/$', views.StudentCreate.as_view(), name='student_create'),
    url(r'^students/(?P<pk>\d+)/update/$', views.StudentUpdate.as_view(), name='student_update'),
    url(r'^students/(?P<pk>\d+)/delete/$', views.StudentDelete.as_view(), name='student_delete'),
    url(r'^grades/$', views.GradeList.as_view(), name='grades'),
    url(r'^grades/create/$', views.GradeCreate.as_view(), name='grade_create'),
    url(r'^grades/(?P<pk>\d+)/update/$', views.GradeUpdate.as_view(), name='grade_update'),
    url(r'^grades/(?P<pk>\d+)/delete/$', views.GradeDelete.as_view(), name='grade_delete'),
]