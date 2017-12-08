# -*- coding:utf-8 -*-
try:
    print '1try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
finally:
    print '1finally...'
print '1END'

try:
    print '2try...'
    r = 10 / int('a')
    print 'result:', r
except StandardError,e:
	print 'StandardError:', e
except ValueError, e:
    print 'ValueError:', e
finally:
    print '2finally...'
print '2END'

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
		print 'StandardError:',e
	finally:
		print '3finally'
main()