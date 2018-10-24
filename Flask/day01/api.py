#!/usr/bin/env python
# encoding:utf-8

from flask import Flask, g, request, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource
from passlib.apps import custom_app_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretKey'
api = Api(app)
auth = HTTPBasicAuth()

def hash_password(password):
	return custom_app_context.encrypt(password)

def verify_password(password, e_password):
	return custom_app_context.verify(password, e_password)

def generate_auth_token(id, expiration=600):
	s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
	return s.dumps({'id':id})

def verify_auth_token(token):
	s = Serializer(app.config['SECRET_KEY'])
	try:
		data = s.loads(token)
	except SignatureExpired, e:
		print e
		return None # valid token, but expired
	except BadSignature, e:
		print e
		return None # invalid token
	user = USERS.get(str(data['id']))
	return user

@auth.verify_password
def verify_password(username_or_token, password):
	# username_or_token, password内部分别自动解析请求头中的 Authorization Basic属性的值
	print username_or_token,password
	print request.path
	print request.headers
	print request.data
	if request.path == '/api/login':
		if username_or_token == 'wzy' and password == 'test,./123':
			user = USERS.get('1')
		else:
			return False # 认证通过就返回True，否则就是False
	else:
		user = verify_auth_token(username_or_token)
		print user
		if not user:
			return False
	g.user = user # g为应用全局的上下文对象，可以在应用层调用，不局限于请求上下文
	return True


# 重写认证失败后返回的信息函数
@auth.error_handler
def unauthorized():
	# return make_response(jsonify({'code':0, 'msg':'Unauthorized access'}), 401)
	print type(jsonify({'code':0, 'msg':'Unauthorized access'}))
	return make_response(jsonify({'code':0, 'msg':'Unauthorized access'}), 401)

USERS = {
	'1':{'username':'wzy','password':'test,./123','id':1}
}


TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
# location=json指明传递过来的参数格式是json格式，如果不是将返回not task param...
parser.add_argument('task', required=True, help='not task param...', location='json')

# @app.before_request # 请求拦截器
# def login_require():
# 	print 'before_request...'
# 	print request.path
# 	print request.method
# 	print request.cookies
# 	if request.path in ['/', '/todos']:
# 		return 'not login...' 

# @app.after_request # 响应拦截器
# def responsed(response):
# 	print 'after_request...'
# 	print response.data
# 	print response.status
# 	return response

# @auth.login_required 该认证装饰器内部实际执行了@auth.verify_password装饰器内部的认证函数逻辑，所以需要重写@auth.verify_password该装饰器的逻辑
class Login(Resource):
	@auth.login_required
	def post(self):
		token = generate_auth_token(g.user.get('id'))
		return jsonify(token)


class Todo(Resource):
	decorators = [auth.login_required] #　可以通过decorators属性设置该资源类中的所有请求方法使用某些装饰器
	def get(self, todo_id):
		abort_if_todo_doesnt_exist(todo_id)
		return TODOS[todo_id]

	def delete(self, todo_id):
		abort_if_todo_doesnt_exist(todo_id)
		del TODOS[todo_id]
		return '', 204

	def put(self, todo_id):
		abort_if_todo_doesnt_exist(todo_id)
		args = parser.parse_args()
		task = {'task': args['task']}
		TODOS[todo_id] = task
		return task, 204

class TodoList(Resource):
	decorators = [auth.login_required]
	def get(self):
		return TODOS

	def post(self):
		args = parser.parse_args()
		print args
		todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
		todo_id = 'todo%i' %todo_id
		TODOS[todo_id] = {'task': args['task']}
		return TODOS[todo_id], 201 # RESTful，return语句可以直接返回dict类型

class HelloWorld(Resource):
	decorators = [auth.login_required]
	def get(self):
		return {'hellow': 'world'}




api.add_resource(Login, '/api/login')
api.add_resource(HelloWorld, '/')
api.add_resource(Todo, '/todo/<todo_id>', endpoint='test')
api.add_resource(TodoList, '/todos')

if __name__ == '__main__':
	app.run(debug=True, port=5001)
