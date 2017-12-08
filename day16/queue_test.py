# coding=utf-8
from multiprocessing import Process,Queue
import os,time,random

# 写数据进程执行
def write(q):
	for value in ['A','B','C']:
		print 'Put %s to queue...' % value
		q.put(value)
		time.sleep(random.random())
# 循环读数据进程执行
def read(q):
	while True:
		print 1
		value = q.get(True)
		print 'Get %s from queue' % value
if __name__ == '__main__':
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	pw.start()
	pr.start()
	pw.join()
	# pr进程里是死循环，无法等待其结束，只能强行终止
	pr.terminate()