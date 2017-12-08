# coding=utf-8

try:
	import cPickle as pickle
except ImportError:
	import pickle
# 反序列化获取对象内容
f = open('F:\Python\example\day15\log.txt','rb')#创建一个file-like-object对象
f_str = f.read()
# d = pickle.load(f)
d = pickle.loads(f_str)
f.close()
print d