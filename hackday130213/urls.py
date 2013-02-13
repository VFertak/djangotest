from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hackday130213.views.home', name='home'),
    # url(r'^hackday130213/', include('hackday130213.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^swissmap/', include('swissmap.urls')),
    # url(r'^media/(?P.*)$', 'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT }),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
)
if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),)+ urlpatterns