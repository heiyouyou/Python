# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('<a href="%s">link to story 1</a>' % self.reverse_url("story","1"))

class StoryHandler(tornado.web.RequestHandler):
	def initialize(self,db):
		self.db = db

	def get(self,story_id):
		# story_id来自于路由匹配规则中正则部分
		self.write("this is story %s" % story_id)

	# def prepare(self):
	# 	self.set_status(500)
	# 	self.finish("test")


class MyFormHandler(tornado.web.RequestHandler):
	def get(self):
		self.redirect("/",permanent=True)
		# self.write('<html><body><form action="/myform" method="POST">'
  #                  '<input type="text" name="message">'
  #                  '<input type="submit" value="Submit">'
  #                  '</form></body></html>')
	def post(self):
		# 设置响应头编码类型
		self.set_header("Content-Type","text/plain")
		# get_body_argument获取post请求的参数，get_query_argument获取get请求的参数
		self.write("You wrote %s" % self.get_body_argument("message"))

class MyPhotoHandler(tornado.web.RequestHandler):
	def get(self,id):
		self.write("my photos %s" %id)


class AsynchHanlder(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	def get(self):
		http = AsyncHTTPClient()
		http.fetch("http://www.tornadoweb.org/en/stable/guide/structure.html",callback=self.on_response)

	def on_response(self,response):
		if response.error:raise tornado.web.HTTPError(500)
		self.write("success")
		self.finish()

class CoroutineHanlder(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		http = AsyncHTTPClient()
		response = yield http.fetch("http://www.tornadoweb.org/en/stable/guide/structure.html")
		self.write(response.body)



app = tornado.web.Application([
		tornado.web.url(r"/",MainHandler),
		tornado.web.url(r"/story/([0-9]+)",StoryHandler,dict(db='db'),name="story"),#正则部分可以对应到查询参数
		tornado.web.url(r"/form",MyFormHandler),
		tornado.web.url(r"/myform",MyFormHandler),
		(r"/oldpath",tornado.web.RedirectHandler,{"url":"/newpath"}),
		(r"/(.*?)/(.*?)/(.*)", tornado.web.RedirectHandler, {"url": "/{1}/{0}/{2}"}),
		(r"/photos/(.*)",MyPhotoHandler),
		(r"/pictures/(.*)",tornado.web.RedirectHandler,{"url":r"/photos/{0}"}),
		(r"/async",AsynchHanlder),
		(r"/corou",CoroutineHanlder),
	])

if __name__ == '__main__':
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()