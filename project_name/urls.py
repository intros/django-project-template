# -*- coding: utf-8 -*-
from django.conf import settings

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/django-ses/', include('django_ses.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout', 
        {'next_page': '/'}, name="logout"),
    url(r'^account/', include('allauth.urls')),
    url(r'^invitation/', include('invitation.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url('', include('introductions.urls', namespace='introductions')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)
