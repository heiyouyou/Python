# !/usr/bin/env python
# coding=utf-8

def application(environ,start_response):
	method = environ['REQUEST_METHOD']
	path = environ['PATH_INFO']
	print method,path
	# 设置响应头的header信息
	# start_response('200 OK',[('Content-Type','text/html')])
	# 处理中文乱码
	start_response('200 OK',[('Content-Type','text/html;charset=UTF-8')])
	# 返回内容给客户端,environ['PATH_INFO']获取客户端的路径名
	return '<h1>Hello,中国,%s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

# application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
# environ：一个包含所有HTTP请求信息的dict对象。
# start_response：一个发送HTTP响应的函数。