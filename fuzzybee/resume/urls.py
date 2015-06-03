from django.conf.urls import patterns, url
from resume import views

urlpatterns = patterns('',
    url(r'^applysync$', views.applysync, name='applysync'),
    url(r'^applylist$', views.applylist, name='applylist'),
    url(r'^applyid/(?P<fact_id>[0-9]+)$', views.applyid, name='applyid'),
)
