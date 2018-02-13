from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.schedule, name='schedule'),
    url(r'^$', views.ScheduleView.as_view(), name='schedule'),
]