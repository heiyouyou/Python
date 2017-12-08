# -*- coding:utf-8 -*-
import logging
def foo(s):
	return 10/int(s)
def bar(s):
	return foo(s)*2
def main():
	try:
		print '3try...'
		r = bar('0')
		print r
	except StandardError as e:
		logging.exception(e)
	finally:
		print '3finally'
main()
print 'END'