# !/usr/bin/env python
# coding=utf-8

# 当文件不存在时，内存自动创建该文件
# f = open('F:/Python/example/day14/test3.txt','w') # 'w'写文本文件，'wb'写二进制文件
# f.write('hello wzy。。。。。。。。。。。。。。。。。world')
# f.close()
# print u'写入结束...'

import codecs
with codecs.open('F:/Python/example/day14/test3.txt','w','utf-8') as f:
	f.write(u'heiyouyou黑黝黝')