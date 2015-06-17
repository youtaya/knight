from django.conf.urls import patterns, url
from joboard import views

urlpatterns = patterns('',
    url(r'^manager/$', views.manager, name='manager'),
    url(r'^(?P<fact_id>[0-9]+)$', views.detail, name='detail'),
)
