# -*-coding:utf-8-*-
class MyObject(object):
	def __init__(self):
		self.x = 0
	def power(self):
		return self.x*self.x
	def __len__(self):
		return 100

obj = MyObject()
print len(obj) # 100
# print dir(obj)
print hasattr(obj,'x') #True
print obj.x # 0
print hasattr(obj,'y') # Flase
print setattr(obj,'y',20) # None
print hasattr(obj,'y') # True
print getattr(obj,'y') # 20
print getattr(obj,'z',30) # 30
print obj.y # 20


print type(int)==type(str)