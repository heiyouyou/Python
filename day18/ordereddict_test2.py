# coding=utf-8

from collections import OrderedDict
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
	def __init__(self,capacity):
		print super(LastUpdatedOrderedDict,self)
		super(LastUpdatedOrderedDict,self).__init__()
		self._capacity = capacity
	def __setitem__(self,key,value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			# last=False时超过容量时进行删除第一个的key,为True时删除最后一个
			last = self.popitem(last=False)
			print 'remove',last
		if containsKey:
			# 删除原来存在的key，目的保持‘先进先出’的顺序
			del self[key]
			print 'set:',(key,value)
		else:
			print 'add:',(key,value)
		OrderedDict.__setitem__(self,key,value)
L = LastUpdatedOrderedDict(3)
L.__setitem__('a',1)
L.__setitem__('b',2)
L.__setitem__('c',3)
print L
print '-------------'
L.__setitem__('b',4)
print L
print '-------------'
L.__setitem__('d',5)
print L