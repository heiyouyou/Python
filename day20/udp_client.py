# !/usr/bin/env python
# coding=utf-8

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in ['Michael','Tracy','Sarah']:
	# 发送数据给客户端
	s.sendto(data,('127.0.0.1',9999))
	# 接受服务端的数据
	print s.recv(1024)
# 关闭客户端连接
s.close()