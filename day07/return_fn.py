# -*- coding:utf-8 -*-
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
# 当调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
a =  lazy_sum(1,2,3,4,5)
b =  lazy_sum(1,2,3,4,5)
print a
print a()
print b
print b()
