# -*- coding:utf-8 -*-
class Student(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Student object (name:%s)' %self.name
	# def __repr__(self):
	# 	return 'Student object (name:%s)' %self.name
	# 简写方法：
	__repr__ = __str__
print Student('wzy') # 直接打印实例时，默认调用__str__这个方法，不使用print答应实例时，直接在命令窗口打印调用的是__repr__方法
y = Student('youyou')
 