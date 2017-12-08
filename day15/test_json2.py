# coding=utf-8

import json
class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score
		
s = Student('Bob',20,88)
# print json.dumps(s) #报错
# 错误的原因是Student对象不是一个可序列化为JSON的对象。

# 类序列化成json
def student2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score,
	}

# 使用dumps()的默认参数default进行配置对象转化成dict的函数
s_str = json.dumps(s,default=student2dict)
print s_str

# 将dict反序列化成类的实例
def dict2student(s):
	return Student(s['name'],s['age'],s['score'])

# 通过loads()的默认参数object_hook配置对象转换函数
print json.loads(s_str, object_hook=dict2student)