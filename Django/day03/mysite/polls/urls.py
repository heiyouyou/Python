# !/usr/bin/env python
# coding=utf-8

from django.conf.urls import url
from . import views
# 对不同app的url配置添加命名空间
app_name = 'polls'
urlpatterns = [
	# url(r'^$',views.index,name='index'),
	# url(r'^test$',views.test,name='test'),
	# url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
	# url(r'^specifics/(?P<question_id>[0-9]+)/$',views.detail,name='detail2'),
	# url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
	# url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
	# url(r'^latest\.html|polls/latest\.html$',views.latest,name='latest'),
	# url(r'^test2\.html$',views.test2,name='test2'),
	url(r'^$',views.IndexView.as_view(),name='index'),
	url(r'^test$',views.test,name='test'),
	url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
	url(r'^specifics/(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail2'),
	url(r'^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(),name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
	url(r'^latest\.html|polls/latest\.html$',views.latest,name='latest'),
	url(r'^test2\.html$',views.test2,name='test2'),
	url(r'^ajax$',views.ajax_html,name='ajax'),
	url(r'^data$',views.ajax_data,name='data'),
]