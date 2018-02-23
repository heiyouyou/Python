# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	# def get(self):
	# 	if not self.get_cookie('mycookie'):
	# 		self.set_cookie('mycookie','this is a test cookie')
	# 		self.write('Your cookie was not set yet!')
	# 	else:
	# 		self.write('Your cookie was set!')

	def get(self):
		if not self.get_secure_cookie("mycookie"):
			self.set_secure_cookie("mycookie",'myvalue')
			self.write("Your cookie was not set yet!")
		else:
			value = self.get_secure_cookie("mycookie")
			self.write("Your cookie's %s was set!" %value)

app = tornado.web.Application([
		(r'/',MainHandler)
	],cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__")

if __name__ == '__main__':
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()
	# 客户端上展示的cookie是经过加密后的值，后端程序通过 get_secure_cookie 获取得到的是未加密的值
	# "2|1:0|10:1519368404|8:mycookie|12:bXl2YWx1ZQ==|6f12771a561e8bf29124a82f61304872459075cdf826e9947efec2959412cadb"