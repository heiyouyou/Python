# !/usr/bin/env python
# coding=utf-8

from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
	url(r'^$',views.test,name='test'),
	url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
]