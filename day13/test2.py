# -*- coding:utf-8 -*-
def fn(self,name='world'):
	print('Hello,%s' % name)
def fn2(self,age=23):
	print('My age is %s' % age)
# 使用type()函数进行创建一个类 
Hello = type('Hello',(object,),dict(hello=fn,age=fn2)) #创建Hello class
h = Hello()
h.hello()
h.age()