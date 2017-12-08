# -*- coding:utf-8 -*-
class Student(object):
	def __init__(self,name):
		self.name = name 
	def __getattr__(self,attr):
		if attr == 'score':
			return 99
		elif attr == 'age':
			return lambda n:25*n
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr) 
s = Student('wzy')
print s.name,s.score
print s.age(2)
print s.grade