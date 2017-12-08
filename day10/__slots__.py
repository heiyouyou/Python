# -*- coding:utf-8 -*-
class Student(object):
	__slots__ = ('name','age')

s = Student()
s.name = 'wzy'
s.age = 23
print dir(s)
# s.score = 99 #报错

# 使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的
# 除非也在子类中也定义__slots__，子类允许定义的属性就是自身的__slots__加上父类的__slots__
class GraduateStudent(Student):
	__slots__ = ('score')
	pass
g = GraduateStudent()
g.name = 'yaya'
g.age = 21	
g.score = 9999
g.height = 9999
print g.name,g.age,g.score ,g.height #9999