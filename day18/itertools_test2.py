# !/usr/bin/env python
# coding=utf-8

import itertools
for c in itertools.chain('ABC','XYZ',[1,2,3,4],('a','b','c')):
	print c
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器


# groupby()把迭代器中相邻的重复元素挑出来放在一起
# for key,group in itertools.groupby('AAABBBbaCCcAAA'):
for key,group in itertools.groupby('AAABBBbaCCcAAA',lambda c:c.upper()):
	print key,list(group)