from django.contrib import admin
from django.conf.urls import include, url, handler403, handler404, handler500
from django.urls import path
from . import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    url(r'^$', views.startpage, name='startpage'),
    url(r'^home/$', views.home, name='home'),
    url(r'^schedule/', include('schedule.urls'), name='schedule'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

handler403 = views.error_403
handler404 = views.error_404
handler500 = views.error_500