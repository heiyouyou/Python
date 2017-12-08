# -*- coding:utf-8 -*-
class Student(object):
	def __init__(self,name):
		self.name = name

	def __call__(self,opts):
		print ('My name is %s %s' % (self.name,opts))
		# print ('My name is %s' % self.name)
s = Student('wzy')
# s() # 实例直接执行方法	
s(89) # 实例直接执行方法

#判断一个对象是否能被调用，能被调用的对象就是一个Callable对象,通过callable()函数，就可以判断一个对象是否是“可调用”对象
print callable(s) # True
print callable(max) # True
print callable([1,2,3]) # True
print callable(None) # False
print callable('string') # False
print callable(str) # True