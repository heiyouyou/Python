# # -*-coding:utf-8-*-
# def log(func):
# 	def wrapper(*args,**kw):
# 		print 'call %s():' % func.__name__
# 		return func(*args,**kw)
# 	return wrapper
# @log
# def  now():
# 	print '2017-7-23'
# # # 相当于一下形式：
# # # now = log(now) #now指向了一个全新的函数wrapper
# now()
# print now.__name__ #wrapper

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
# @log('excute')
def  now():
	print '2017-7-23'
# 相当于：
now = log('execute')(now)
now()
print now.__name__ #wrapper