from django.conf.urls import patterns, url
from resume import views

urlpatterns = patterns('',
    url(r'^applysync$', views.applysync, name='applysync'),
    url(r'^applylist/(?P<fact_id>[0-9]+)$', views.applylist, name='applylist'),
)
