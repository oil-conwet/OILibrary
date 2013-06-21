from django.conf.urls import patterns, url
import settings
import library.views as library

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^$', library.index),

                       # Static Content
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)
