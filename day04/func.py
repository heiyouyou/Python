# -*- coding:utf-8 -*-
def func(a,b,c=0,*args,**kw):
	print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
func(1,2)
func(1,2,3)
func(1,2,3,*(0,2,3))
func(1,2,3,*(0,2,3),name="wzy")

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
args = (2,3,4,5)
kw = {'age':22}
func(*args,**kw)