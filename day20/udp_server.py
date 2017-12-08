# !/usr/bin/env python
# coding=utf-8

import socket,time
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))

print 'Bind UDP on 9999...'
while True:
	# 接受客户端的数据
	data,addr = s.recvfrom(1024)
	time.sleep(1)
	print 'Received from %s:%s.' % addr
	# 发送数据给客户端
	s.sendto('Hello,%s!' % data,addr)