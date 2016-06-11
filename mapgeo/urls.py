from django.conf.urls import url, patterns
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.pointmap, name='pointmap'),
]
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)