# coding=utf-8
from multiprocessing import Process
import os


def run_proc(name):
	print 'Run child process %s (%s)...' %(name,os.getpid())
if __name__ == '__main__':
	print 'Parent process %s' % os.getpid()
	p1 = Process(target=run_proc,args=('test1',))
	p2 = Process(target=run_proc,args=('test2',))
	print 'Process will start'
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	print 'Process end'

# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。