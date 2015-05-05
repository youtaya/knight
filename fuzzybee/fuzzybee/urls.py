from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fuzzybee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('joboard.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
