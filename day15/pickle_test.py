# coding=utf-8
try:
	import cPickle as pickle
except ImportError:
	import pickle
d = dict(name='Bob',age=20,score=88)
print d
d_str = pickle.dumps(d) #序列化对象
# print d_str 
f = open('F:\Python\example\day15\log.txt','wb')#创建一个file-like-object对象
# f.write(d_str)

pickle.dump(d,f)#序列化的同时将内容进行写入文件
f.close()