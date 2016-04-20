# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:23:35 2016

@author: appertjt
"""

from django.conf.urls import url
from blog import views

urlpatterns=[url(r'^$', views.index, name='index'),
             url(r'^(?P<post_id>\d+)/$', views.post, name='post')]

