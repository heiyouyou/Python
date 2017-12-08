# !/usr/bin/env python
# coding=utf-8

import itertools

f = filter(lambda x:x>=10,[1,2,10,22,11])
print f
# 无限打印
# itertools.ifilter(None,itertools.count(1))
# ifilter()就是filter()的惰性实现
f1 = itertools.ifilter(lambda x:x<20,itertools.count(1))
print f1
for n in f1:
	print n
print '-------------'
f2 = itertools.ifilter(None,itertools.repeat('abc',5))
for n2 in f2:
	print n2