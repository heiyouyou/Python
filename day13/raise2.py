# -*- coding:utf-8 -*-
def foo(s):
    n = int(s)
    return 10 / n
def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise
def main():
    bar('0')
main()
print 'END'

# try:
# 	10/0
# except ZeroDivisionError:
# 	raise ValueError('input error!')