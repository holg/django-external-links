# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('external_links.views',
    url(r'^$',
        'external_link',
        name='external_link'),

    #url(r'^admin/', include(admin))
)
