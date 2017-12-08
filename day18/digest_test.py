# !/usr/bin/env python
# -*- coding:utf-8 -*-

import hashlib

# md5算法
# 一次性处理
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

# 数据量大时，分批次处理
md5_1 = hashlib.md5()
md5_1.update('how to use md5 in ')
md5_1.update('python hashlib?')
print md5_1.hexdigest()

print '--------------'

# sha1算法
sha1 = hashlib.sha1()
sha1.update('how to use md5 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()

# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法越慢，而且摘要长度更长。

