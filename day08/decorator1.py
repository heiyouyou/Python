# -*-coding:utf-8 -*-
# Python内置的functools.wraps，
# 可以不需要编写wrapper.__name__ = func.__name__这样的代码，进行调整函数__name__属性
import functools

def log(text):
    def decorator(func):
    	@functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
@log('excute')
def  now():
	print '2017-7-23'
now()
print now.__name__ #now