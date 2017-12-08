# !/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask import request

# 创建一个应用对象 
app = Flask(__name__)

# 路由配置，采用装饰器的模式进行对URL与对应函数的匹配
@app.route('/',methods=['GET','POST'])
def home():
	print request#request对象对应着不同的url地址
	return '<h1>Home</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
	print request
	return '''<form action="/signin" method="post">
      <p><input name="username"></p>
      <p><input name="password" type="password"></p>
      <p><button type="submit">Sign In</button></p>
      </form>'''
# 注意噢，同一个URL /signin分别有GET和POST两种请求，映射到两个处理函数中
@app.route('/signin',methods=['POST'])
def signin():
	print request
	# 需要从request对象读取表单内容：
	if request.form['username']=='admin' and request.form['password']=='123456':
		return '<h3>Hello,admin</h3>'
	return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
	# 运行服务器应用
	app.run()