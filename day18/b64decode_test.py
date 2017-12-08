# coding=utf-8

import base64

# 能处理去掉=的base64解码函数
def base64_decode(text):
	length = len(text)
	if length%4==0:
		return base64.b64decode(text)
	else:
		n = 0
		while n<(length%4):
			text = text + '='
			n = n + 1
		return base64.b64decode(text)

print base64_decode('YWJjZA==')
print base64_decode('YWJjZA')

print '-----------'
def safe_b64decode(str):
    safe_str = str + '='*(4 - (len(str) % 4))
    return base64.b64decode(safe_str)
print safe_b64decode('YWJjZA==')
print safe_b64decode('YWJjZA')
		
