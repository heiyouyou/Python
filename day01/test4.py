# -*- coding: utf-8 -*-
# 乱码
print '中文测试'
# 不乱码
print u'中文测试'
# age = raw_input('please enter:')
age = int(raw_input('please enter:'))
# age = input('please enter:')
if(age>=18):
	print 'adult'
else:
	print 'teenager'