# coding=utf-8
from multiprocessing import Pool
import os,time,random
mm = 4
def long_time_task(name):
	global mm 
	mm = mm + 1
	print 'Run task %s (%s)' % (name,os.getpid())
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print 'Task %s runs %0.2f seconds %i' % (name,(end-start),mm)

if __name__ == '__main__':
	print 'Parent process %s' % os.getpid()
	p = Pool(5)
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	print 'Waiting for all subprocesses done...'
	p.close()
	p.join()
	print 'All subprocesses done'

# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
# Pool的默认大小在电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制，可以进行配置同时执行进程数。