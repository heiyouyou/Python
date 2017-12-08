# !/usr/bin/env python
# coding=utf-8


import socket
# 创建一个socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com.cn',80)) #注意是元组格式
# 发送数据
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
# 每次循环读取1kb新浪服务器发过来的数据
while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = ''.join(buffer)
s.close()
# 按照'\r\n'进行1次分割成两个字符串list
header,html = data.split('\r\n',1)
print header
# 写到文件
with open('sina.html','wb') as f:
	f.write(html)
