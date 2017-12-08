# -*- coding:utf-8 -*-
class Fib(object):
	def __init__(self):
		self.a , self.b = 0,1
	def __iter__(self):
		return self
	def next(self):
		self.a,self.b = self.b,self.a+self.b
		if self.a > 1000:
			raise StopIteration()
		return self.a # 返回下一个值
		# 实现__getitem__实例就可以通过下标获取值
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a
		# 判断是否是切片对象 
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			a,b = 1,1
			L = []
			for x in range(stop):
				if x>= start:
					L.append(a)
				a,b = b,a+b
			return L
	def __setitem__(self,n,m):
		pass
	def __delitem__(self,n):
		pass
# 通过下标获取值
f = Fib();
print f[0]
print f[1]
print f[2]
print f[3]
print f[10]
print f[100]


# 切片
# print range(100)[5:10]
print f[5:10]
print f[:10]
print f[0:5]
print f[0:5:2]
