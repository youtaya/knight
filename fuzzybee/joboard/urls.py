from django.conf.urls import patterns, url
from joboard import views

urlpatterns = patterns('',
    url(r'^(?P<fact_id>[0-9]+)$', views.detail, name='detail'),
)
