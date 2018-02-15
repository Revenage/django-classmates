from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    url(r'^$', views.startpage, name='startpage'),
    url(r'^home/$', views.home, name='home'),
    url(r'^schedule/', include('schedule.urls'), name='schedule'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
