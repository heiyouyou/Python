# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie('user')

class MainHandler(BaseHandler):
	# def get(self):
	# 	print self.current_user # 默认会立即调用 self.get_current_user，默认值是None
	# 	if not self.current_user:
	# 		self.redirect('/login')
	# 		return
	# 	name = tornado.escape.xhtml_escape(self.current_user)
	# 	self.write('Hello, '+name)

	@tornado.web.authenticated # 使用装饰器代替了上面的判断逻辑，并且配置项中必须配置login_url
	def get(self):
		name = tornado.escape.xhtml_escape(self.current_user)
		self.write('Hello, '+name)

class LoginHandler(BaseHandler):
	def get(self):
		self.write('<html><body><form action="/login" method="post">'
	       'Name: <input type="text" name="name">'
	       '<input type="submit" value="Sign in">'
	       '</form></body></html>')

	def post(self):
		print self.get_argument('name')
		self.set_secure_cookie('user',self.get_argument('name'))
		self.redirect('/')
setting = {
	"cookie_secret":"__TODO:GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
	'login_url':'/login'
}

app = tornado.web.Application([
		(r'/',MainHandler),
		(r'/login',LoginHandler)
	],**setting)

if __name__ == '__main__':
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()