# -*- coding:utf-8 -*-
def foo(s):
	n = int(s)
	assert n!=0,'n is zero' #assert expression [,arguments],表达式为true，没有异常，否则有异常
	return 10/n
def main():
	# foo('0')
	# return foo('2')
	return foo('0')

print main()