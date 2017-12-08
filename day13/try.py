# -*- coding:utf-8 -*-
try:
	print 'try...'
	r = 10/0
	print 'result:',r
except ZeroDivisionError as e:
	print 'except:',e
else:
	print 'else...'
finally:#无论有无异常都执行
	print 'finally...'
print 'END'

try:
	print 'try...'
	r = 10/2
	print 'result:',r
except ZeroDivisionError , e:#有异常则执行
	print 'except:',e
else:#没有异常则执行
	print 'no Error'
finally:
	print 'finally...'
print 'END'