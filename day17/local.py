# coding=utf-8

import threading

# 全局变量
local_school = threading.local()

def process_student():
	print 'Hello, %s age is %i (in %s)' % (local_school.student,local_school.age,threading.current_thread().name)

def process_thread(name,age):
	local_school.student = name
	local_school.age = age
	process_student()

t1 = threading.Thread(target=process_thread,args=('Alice',23),name='A')
t2 = threading.Thread(target=process_thread,args=('Bob',22),name='B')
t1.start()
t2.start()
t1.join()
t2.join()
# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
# 你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
# 可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。