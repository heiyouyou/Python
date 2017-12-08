# !/usr/bin/env python
# coding=utf-8

# f = open('F:/Python/example/day14/test.txt','r')
# try:
# 	s = f.read()
# except IOError,e:
# 	print e
# finally:
# 	print s
# 	f.close()

# 写法一：
# somefile = open(r'F:/Python/example/day14/test.txt')
# try:
#     for line in somefile:
#         print line
#         # ...more code
# finally:
#     somefile.close()

# with语句简写,自动调用了f.close()方法关闭
# with open('F:/Python/example/day14/test.txt','r') as f:
# 	# print f.read() #一次性读完所有数据
# 	# print f.read(22) #一次读22个字节数
# 	# print f.readline() #一次一行内容
# 	# print f.readlines() #一次读取所有内容并按行返回list
# 	for line in f.readlines():
# 		print (line.strip())# strip()把末尾的'\n'删掉


# 读取二进制文件 图片/视频
# f = open('F:/Python/example/day14/2.jpg','rb')
# print f.read()

# codecs模块帮我们在读文件时自动转换编码，直接读出unicode
import codecs

# f = open('F:/Python/example/day14/test2.txt','r')
# 直接读取费ASCII编码的文件，出现乱码
# u = f.read()
# 按照二进制读取
# f = open('F:/Python/example/day14/test2.txt','rb')
# u = f.read().decode('gbk')

with codecs.open('F:/Python/example/day14/test2.txt','r','gbk') as f:
	u = f.read()
	print u
