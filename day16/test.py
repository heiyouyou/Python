# coding=utf-8
import os

# 以下代码在Windows系统无法执行，fork方法只在Unix中存在
print 'Process (%s) start...' %os.getpid()
pid = os.fork()
if(pid == 0):
	print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:
	print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)