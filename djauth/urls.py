from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'djauth.views.index', name='index' ),
    url(r'^login/$', 'djauth.views.login', name='login'),
    url(r'^logout/$', 'djauth.views.logout', name='logout'),
    url(r'^dashboard/$', 'djauth.views.dashboard', name='dashboard'),
    url(r'^register/$', 'djauth.views.register', name='register'),

    url(r'^about/$', 'djauth.views.about', name='about'),
    url(r'^about_detail/$', 'djauth.views.about_detail', name='about_detail'),
    url(r'^about_komentar/$', 'djauth.views.about_komentar', name='about_komentar'),

    url(r'^about_admin/$', 'djauth.views.about_admin', name='about_admin'),
    url(r'^about_edit/$', 'djauth.views.about_edit', name='about_edit'),
    url(r'^about_create/$', 'djauth.views.about_create', name='about_create'),


    url(r'^portfolio/$', 'djauth.views.portfolio', name='portfolio'),
    url(r'^upload_gambar/$', 'djauth.views.upload_gambar', name='upload_gambar'),


)

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
) + urlpatterns
