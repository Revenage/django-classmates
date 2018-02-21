from django.conf.urls import include, url
from .views import signup

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^', include('django.contrib.auth.urls')),
]