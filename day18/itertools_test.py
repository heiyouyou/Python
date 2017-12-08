# !/usr/bin/env python
# coding=utf-8

import itertools
natuals = itertools.count(1)#从1开始无限迭代生成自然数序列
# for n in natuals:
# 	print n
# count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出

# cs = itertools.cycle('ABC')
cs = itertools.cycle([1,2,3])
# for c in cs:
# 	print c

# cycle()会把传入的一个序列无限重复下去，注意字符串也是一种序列

ns = itertools.repeat('Abc',10)
# for n in ns:
# 	print n
# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数，默认无限次重复

# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来,事实上也不可能在内存中创建无限多个元素。
# 无限序列虽然可以无限迭代下去，但是可以通过takewhile()等函数根据条件判断来截取出一个有限的序列

natuals1 = itertools.count(1)
nsy = itertools.takewhile(lambda x:x<=10,natuals1)
print nsy
for y in nsy:
	print y

