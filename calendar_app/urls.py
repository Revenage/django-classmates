
from django.contrib import admin
from django.conf.urls import include, url, handler403, handler404, handler500
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.calendar, name='calendar'),
    url(r'^api/', views.json_test, name='calendar_api'),
]