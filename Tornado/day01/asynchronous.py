# -*- coding:utf-8 -*-

from tornado.httpclient import HTTPClient
from tornado.httpclient import AsyncHTTPClient
from tornado import gen

# 同步函数 
def synchronous_fetch(url):
	http_client = HTTPClient()
	response = http_client.fetch(url)
	return response.body

# 异步调用回调传参
def asynchronous_fetch(url,callback):
	http_client = AsyncHTTPClient()
	def handle_response(response):
		callback(response.body)
	http_client.fetch(url,callback=handle_response)

# 异步调用Future
def async_fetch_future(url):
	http_client = AsyncHTTPClient()
	my_future = Future()
	fetch_future = http_client.fetch(url)
	fetch_future.add_done_callback(lambda f:my_future.set_result(f.result()))
	return my_future

# 协程实现的异步
@gen.coroutine
def fetch_coroutine(url):
	http_client = AsyncHTTPClient()
	response = yield http_client.fetch(url)
	raise gen.Return(response.body)


