from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fuzzybee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'joboard.views.index',name='home'),
    url(r'^board/', include('joboard.urls', namespace="board")),
    url(r'^resume/', include('resume.urls', namespace="resume")),
    url(r'^people/', include('people.urls', namespace="people")),
    url(r'^admin/', include(admin.site.urls)),
)
