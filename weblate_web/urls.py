# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2013 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <http://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weblate_web.views.home', name='home'),
    # url(r'^weblate_web/', include('weblate_web.foo.urls')),

    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^features/$', TemplateView.as_view(template_name="features.html"), name='features'),
    url(r'^download/$', TemplateView.as_view(template_name="download.html"), name='download'),
    url(r'^try/$', TemplateView.as_view(template_name="try.html"), name='try'),
    url(r'^hosting/$', TemplateView.as_view(template_name="hosting.html"), name='hosting'),
    url(r'^contribute/$', TemplateView.as_view(template_name="contribute.html"), name='contribute'),
    url(r'^support/$', TemplateView.as_view(template_name="support.html"), name='support'),

    # Media files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)