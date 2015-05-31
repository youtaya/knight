from django.conf.urls import patterns, url
from resume import views

urlpatterns = patterns('',
    url(r'^applysync$', views.applysync, name='applysync'),
)
