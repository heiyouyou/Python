# -*- coding:utf-8 -*-
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
# Python内置有capitalize()函数
def format(s):
	lstr = s.lower()
	ustart = lstr[0:1].upper()
	astr = lstr[1:len(lstr)]
	return ustart+astr
aa = map(format,['adam','LISA','barT'])
print aa

# 第一次运算，x表示序列第一个元素，y表示第二个元素。
# 往后的运算x表示运算的结果，y表示下一个元素
def prod(x,y):
	print x,y
	return x*y
bb = reduce(prod,[1,2,3,4,5])
print bb