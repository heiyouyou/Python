# -*- coding:utf-8 -*-

# from gevent import monkey; monkey.patch_socket()
# import gevent

# def f(n):
#     for i in range(n):
#         print gevent.getcurrent(), i
#         gevent.sleep(0)

# g1 = gevent.spawn(f, 5)
# g2 = gevent.spawn(f, 5)
# g3 = gevent.spawn(f, 5)
# g1.join()
# g2.join()
# g3.join()

# 当然，实际代码里，我们不会用gevent.sleep()去切换协程，而是在执行到IO操作时，gevent自动切换，代码如下：

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2

def f(url):
	print('GET: %s' % url)
	resp = urllib2.urlopen(url)
	data = resp.read()
	print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
	gevent.spawn(f, 'https://www.python.org/'),
	gevent.spawn(f, 'https://www.yahoo.com/'),
	gevent.spawn(f, 'https://github.com/'),
])