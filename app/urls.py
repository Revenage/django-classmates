"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^schedule/', include('schedule.urls'), name='schedule'),
    # url(r'^login/$', views.log_in, name='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
