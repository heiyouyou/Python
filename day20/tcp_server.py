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
		# 接受客户端发来的数据
		data = sock.recv(1024)
		time.sleep(1)
		# 判断发来的数据是否合理
		if data == 'exit' or not data:
			break
		# 返回数据给客户端
		sock.send('Hello,%s' % data)
	# 关闭本次会话
	sock.close()
	print 'Connection from %s:%s closed' % addr

while True:
	# 等待客户端发起连接
	sock,addr = s.accept()
	print sock,addr # sock客户端的socket对象，addr返回元组格式，包含了客户端的地址和端口
	t = threading.Thread(target=tcplink,args=(sock,addr))
	t.start()

# 用TCP协议进行Socket编程在Python中十分简单，对于客户端，要主动连接服务器的IP和指定端口，对于服务器，要首先监听指定端口，然后，对每一个新的连接，创建一个线程或进程来处理。通常，服务器程序会无限运行下去。
# 同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。