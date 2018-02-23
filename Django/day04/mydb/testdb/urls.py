# !/usr/bin/env python
# coding=utf-8

from django.conf.urls import url
from . import views
# 对不同app的url配置添加命名空间
app_name = 'testdb'
urlpatterns = [
	url(r'^test$',views.test,name='test'),
	url(r'^data$',views.data,name='data'),
	url(r'^data/get$',views.get_data,name='get_data'),
	url(r'^test/base$',views.test_base,name='test_base'),
	url(r'^router/.+$',views.test2,name='test2'),
	url(r'^router$',views.router,name='router'),
]