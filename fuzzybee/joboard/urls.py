from django.conf.urls import patterns, url
from joboard import views

urlpatterns = patterns('',
    url(r'^$', views.detail, name='detail'),
)
