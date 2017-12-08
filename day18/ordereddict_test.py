# coding=utf-8
from collections import OrderedDict

# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict

# d = dict([('a',1),('b',2),('c',3)])
d = dict({'a':1,'b':2,'c':3})
print d
print '---------'
od = OrderedDict([('a',1),('b',2),('c',3)])
print od