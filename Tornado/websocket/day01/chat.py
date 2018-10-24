# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

import sockjs.tornado

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')




class ChatConnection(sockjs.tornado.SockJSConnection):
	participants = set()

	def on_open(self, info):
		self.broadcast(self.participants, "Someone joined")
		self.participants.add(self)
		print info.ip
		print info.cookies
		print info.arguments
		print info.headers
		print info.path

	def on_message(self, message):
		if message.rfind('test') !=-1:
			self.broadcast(self.participants, message)
		else:
			self.send('disabled user...')

	def on_close(self):
		print 'close...'
		self.participants.remove(self)

		self.broadcast(self.participants, "Someone left.")


if __name__ == '__main__':
	import logging

	logging.getLogger().setLevel(logging.DEBUG)

	ChatRouter = sockjs.tornado.SockJSRouter(ChatConnection, '/chat')

	app = tornado.web.Application(
		[(r'/', IndexHandler)] + ChatRouter.urls,
		{
			'compiled_template_cache':False
		}
	)

	app.listen(8003)

	print 'chat start...'
	tornado.ioloop.IOLoop.instance().start()
