# -*- coding:utf-8 -*-
def my_abs(x):
	# 异常抛出
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x;
a = my_abs(-2)
c = my_abs('cb')
print a #2
print c #'cb'
# 函数默认返回 None
def noreturn(x):
	return
b = noreturn(2)
print b # None
# 空函数
def nop():
	pass
age = 2;
if age>=18:
	pass