# !/usr/bin/env python
# coding=utf-8

from flask import Flask,jsonify,render_template,request,url_for

app = Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
	print request.args
	# 获取请求参数，默认为0 int类型
	a = request.args.get('a',0,type=int)
	b = request.args.get('b',0,type=int)
	# 格式化成json
	return jsonify(result=a+b)

# 默认路由的请求方式是GET，可以通过methods参数进行配置请求方式，如@app.route('/'，['POST'])
# 可以为同一个映射函数配置多个装饰器
@app.route('/')
@app.route('/<data>')
def index(data=None):
	print request.method
	# 默认回去templates目录下面寻找文件，并且使用关键字参数进行携带参数到模板中
	return render_template('index.html',data=data,pageList = [1,2,3,4,5])

# 使用<.....>括号进行在url中携带参数，格式有：<变量名>、<转换器:变量名>
# 转换器有：
# string	accepts any text without a slash(削减) (the default)
# int	accepts integers
# float	like int but for floating point values
# path	like the default but also accepts slashes(削减)
# any	matches one of the items provided
# uuid	accepts UUID strings
@app.route('/test/<username>/<int:age>')
def test(username,age):
	print type(username),type(age)
	return 'username:%s,age:%d' %(username,age)

with app.test_request_context():
	# 使用函数url_for生成对应路由函数的url
	# print url_for('index')
	# print url_for('index',next='/')
	# print url_for('test',username='youyou',age='23')

	# 静态资源文件的处理
	url_for('static',filename='css/layout.css')
	url_for('static',filename='css/layout.js')

if __name__ == '__main__':
	app.run()