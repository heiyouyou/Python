# !/usr/bin/env python
# coding=utf-8

import itertools

# imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。
for x in itertools.imap(lambda x,y:x*y,[10,20,30],itertools.count(1)):
	print x

print '------------'
# 支持多个序列遍历，但是必须是相同长度
r = map(lambda x,y:x*y,[1,2,3],[4,5,6])
print r
print '------------'
# 不支持遍历无穷序列
# r1 = map(lambda x:x*x,itertools.count(1)) #处于挂起状态
# print r1

# 注意:imap()返回一个迭代对象，而map()返回list。当你调用map()时，已经计算完毕
# imap()实现了“惰性计算”，也就是在需要获得结果的时候才计算。类似imap()这样能够实现惰性计算的函数就可以处理无限序列

r1 = itertools.imap(lambda x:x*x,itertools.count(1))
for n in itertools.takewhile(lambda x:x<=100,r1):
	print n
