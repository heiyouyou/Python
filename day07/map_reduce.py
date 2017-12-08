# -*- coding:utf-8 -*-
def fn(x,y):
	return x*10 + y
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

aa = reduce(fn,map(char2num,'13579'))	
print aa,isinstance(aa,int) #13579 True

# 字符串变成整数
def str2int(s):
	def fn(x,y):
	return x*10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn,map(char2num,s))	