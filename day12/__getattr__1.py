# -*- coding:utf-8 -*-
class Chain(object):
	def __init__(self,path=''):
		self._path = path;

	def __getattr__(self,path):
		return Chain('%s/%s' %(self._path,path))
	def __str__(self):
		return self._path

print Chain()
print Chain().status
print Chain().status.user
print Chain().status.user.timeline
print Chain().status.user.timeline.list