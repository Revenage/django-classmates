from django.conf.urls import include, url
from .views import signup, account_activation_sent, activate

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>.+)/(?P<token>.+)/$', activate, name='activate'),
    url(r'^', include('django.contrib.auth.urls')),
]