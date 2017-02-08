from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'djauth.views.home', name='home' ),
    url(r'^login/', 'djauth.views.login', name='login'),
)