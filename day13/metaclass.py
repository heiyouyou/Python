# -*-coding:utf-8 -*-
class ListMetaclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['add'] = lambda self,value:self.append(value)
		return type.__new__(cls,name,bases,attrs)
class MyList(list):
 	__metaclass__ = ListMetaclass
l = MyList()
print  l
l.add(2)
l.add(3)
print  l