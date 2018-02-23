# -*- coding:utf-8 -*-

import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def set_default_headers(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

	def get(self):
		self.write("Hello,world")

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		items = ['Item1','<span style="color:red;">Item2</span>','Item3']
		self.render('index.html',title="My title",items=items)
		# self.render_string('index.html',title="My title",items=items)

def make_app():
	return tornado.web.Application(handlers=[
		# 处理静态资源路径
		# (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__),'static')}),
		(r"/",MainHandler),
		(r"/index",IndexHandler)
	],template_path=os.path.join(os.path.dirname(__file__),'templates'),debug=True,autoreload=True,compiled_template_cache=False,static_path=os.path.join(os.path.dirname(__file__),'static'))

if __name__ == '__main__':
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()