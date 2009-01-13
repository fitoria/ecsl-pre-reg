from django.conf.urls.defaults import *
from views import index, show_item

urlpatterns = patterns('',
     (r'^$', 'index'),
     (r'^articulo/(?P<item>\d+)/$', 'show_item'),
)
