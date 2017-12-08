#!/usr/bin/env python
# -*- coding:utf-8 -*-
# sum = 0
# n = 99
# while n>0:
# 	sum = sum + n
# 	n = n -2
# print sum

# .decode('utf-8').encode('gbk') 可以使得控制台中文不会乱码提示输入
# 注意raw_input()接受返回的是字符串类型的值
a = int(raw_input('请输入内容:'.decode('utf-8').encode('gbk')))
if a>20:
	print u'a大于20'
else:
	print u'a小于20'

# while True:
# 	print u'死循环...'