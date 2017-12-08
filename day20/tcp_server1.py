# !/usr/bin/env python
# coding=utf-8

import socket,threading,time
# 创建服务端的socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 监听端口和地址
s.bind(('127.0.0.1',9999))
# 开启最大连接数5
s.listen(5)
print 'server start....'

# 多线程处理多个客户端的逻辑
def tcplink(sock,addr):
	print 'Accept new connection from %s:%s..' % addr
	# 首次返回数据给客户端，注意是使用客户端的socket对象进行返回数据给客户端
	sock.send('Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data == 'exit' or not data:
			break
		sock.send('Hello,%s' % data)
	sock.close()
	print 'Connection from %s:%s closed' % addr

while True:
	# 等待客户端发起连接
	sock,addr = s.accept()
	print 'Accept new connection from %s:%s..' % addr
	# 首次返回数据给客户端，注意是使用客户端的socket对象进行返回数据给客户端
	sock.send('Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data == 'exit' or not data:
			break
		sock.send('Hello,%s' % data)
	sock.close()
	print 'Connection from %s:%s closed' % addr


