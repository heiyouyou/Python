#!/usr/bin/env python
# -*- coding:utf-8 -*-

'a test module'

__author__ = 'wzy'
import sys,private
def test():
	args = sys.argv
	if len(args)==1:
		print 'Hello world'
	elif len(args)==2:
		print 'Hello,%s!' % args[1]
	else:
		print 'Many arguments'

print __name__
if __name__ == '__main__':
	test()
	print private.greeting("wzy1")
	print private._private_1("wzy2")
	print private.__private_2("wzy3")