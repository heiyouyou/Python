# -*- coding:utf-8 -*-
class FooError(StandardError):
	pass
def foo(s):
	n = int(s)
	if n==0:
		raise FooError('invalid value: %s' % s)
	return 10 / n
print foo(2)
print 'error...'
print foo(0)


