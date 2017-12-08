# -*-coding:utf-8-*-
class Student(object):
	pass
s = Student()
s.name = 'wzy'
print s.name #wzy

def set_age(self,age):
	self.age = age

from types import MethodType
# 给实例绑定方法，只能该实例调用该方法
s.set_age = MethodType(set_age,s,Student)
s.set_age(23)
print s.age

s2 = Student()
# s2.set_age(22)
# print s2.age

def set_core(self,score):
	self.score = score
# 给类绑定方法，所有该类的实例都可以共享
Student.set_core = MethodType(set_core,None,Student)

s.set_core(99)
print s.score#99
s2.set_core(98)
print s2.score#98