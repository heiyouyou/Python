# coding=utf-8

import base64

es = base64.b64encode('binary\x00string')
print es
print base64.b64decode(es)

# url safe 编码
print '-------------'
# 有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
urles = base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print urles
print  base64.urlsafe_b64decode(urles)

# 还可以自己定义64个字符的排列顺序，这样就可以自定义Base64编码，不过，通常情况下完全没有必要。
# Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。

print '--------------'
print base64.b64decode('YWJjZA==')
print base64.b64decode('YWJjZA') #报错

# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。