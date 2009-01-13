from django.conf.urls.defaults import *
from os import path as os_path
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'ecsl.apps.planet.views.index'),
    (r'^registro/', include('ecsl.apps.registration.urls')),
    (r'^perfiles/', include('ecsl.apps.profiles.urls')),
    (r'^planeta/', include('ecsl.apps.planet.urls')),
    (r'^admin/(.*)', admin.site.root),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^perfiles/avatar/(.*)$', 'django.views.static.serve', 
                {'document_root': os_path.join(settings.MEDIA_ROOT, 'profiles/avatar')}),
            (r'^imagenes/(.*)$', 'django.views.static.serve',
                {'document_root': os_path.join(settings.MEDIA_ROOT, 'img')}),
            (r'^css/(.*)$', 'django.views.static.serve',
                {'document_root': os_path.join(settings.MEDIA_ROOT + '/style')}),
)
