# coding=utf-8

from django.http import HttpResponse,HttpResponseRedirect
from .views import test

# 请求中间件（拦截登录）
class Request_Middleware(object):
	def process_request(self,request):
		print 'process_request...'
		print request.path
		path = request.path
		# print request.COOKIES
		if 'sessionid' in request.COOKIES or path == '/admin/login/':
			return None
		else:
			return HttpResponseRedirect('/admin/login/')

# 视图中间件
class View_Middleware(object):
	def process_view(self,request,view_func,view_args,view_kwargs):
		print 'process_view...'
		return None

# 异常中间件
class Exception_Middleware(object):
	def process_exception(request,exception):
		print 'process_exception...'
		return None

# 响应中间件
class Response_Middleware(object):
	def process_response(request,response):
		print 'process_response...'