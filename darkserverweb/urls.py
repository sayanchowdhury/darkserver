# Copyright 2011 Red Hat Inc.
# Author: Kushal Das <kdas@redhat.com>
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.  See http://www.gnu.org/copyleft/gpl.html for
# the full text of the license.
from django.conf.urls.defaults import patterns, include, url
from settings import MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
handler404 = 'buildid.views.view404'
handler500 = 'buildid.views.view500'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'darkserver.views.home', name='home'),
    # url(r'^darkserver/', include('darkserver.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'buildid.views.index'),
    url(r'^buildids/(?P<ids>.+)', 'buildid.views.buildids'),
    #url(r'^buildids/', 'buildid.views.index'),
    url(r'^rpm2buildids/(?P<name>.+)', 'buildid.views.rpm2buildids'),
    #url(r'^rpm2buildids/', 'buildid.views.index'),
    url(r'^package/(?P<name>.+)', 'buildid.views.package'),
    #url(r'^package/', 'buildid.views.index'),
    url(r'^serverversion', 'buildid.views.serverversion'),
    url(r'^dashboard/$', 'buildid.views.web_dashboard'),
)
