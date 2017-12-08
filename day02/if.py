#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# age = 3
# if age >= 18:
# 	print 'your age is', age
# 	print 'adult'
# else:
# 	print 'your age is', age
# 	print 'teenager'

age = 20
if age >= 6:
	print 'your age is', age
	print 'teenager'
elif age>=18:
	print 'your age is', age
	print 'adult'
else:
	print 'kid'

# sex = u'男'
# if sex == u'女':
# 	print u'你是：',u'女'
# elif sex == u'男':
# 	print u'你是：',u'男'
# else:
# 	print u'你是：',u'人妖'

#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
# x = ''
# x = 0
x = []
if x:
	print 'True'
else:
	print 'False'