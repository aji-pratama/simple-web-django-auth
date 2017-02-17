from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'djauth.views.home', name='home' ),
    url(r'^login/$', 'djauth.views.login', name='login'),
    url(r'^logout/$', 'djauth.views.logout', name='logout'),
    url(r'^dashboard/$', 'djauth.views.dashboard', name='dashboard'),
    url(r'^register/$', 'djauth.views.register', name='register'),
    url(r'^index/$', 'djauth.views.index', name='index'),
)

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
) + urlpatterns
