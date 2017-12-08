# -*- coding:utf-8 -*-
# def enroll(name,gender,age=6,city='Beijing'):
# 	print 'name:',name
# 	print 'gender:',gender
# 	print 'age:',age
# 	print 'city:',city
# enroll('Heiyouyou','M',21)
# enroll('pingping','F',18)
# enroll('Sarah','F',city='hannan') #默认参数不按照顺序使用，需要用对应参数名赋值

def add_end(L=[]):
	L.append("end")
	return L


c = add_end([1,2,'3324'])
d = add_end(['pingping','xixi','wzy'])
print c #[1,2,'3324','end']
print d #['pinpin','xixi','wzy','end']


# 当使用默认参数L时，L在函数定义时，就会被初始化，之后在调用函数
# 这个默认参数L是始终指向可变对象list []的，姑list的值变化，L的值也会变化，就导致以下情况发生
a = add_end();
print a #['end']
b = add_end();
# print b #['end','end']
bb = add_end();
print b #['end','end','end']
print bb #['end','end','end']

# 默认参数设置成不可变的对象
def add_end1(L=None):
	if L is None:
		L = []
	L.append('end')
	return L
aa = add_end1()
cc = add_end1()
print '1',aa
print '2',cc