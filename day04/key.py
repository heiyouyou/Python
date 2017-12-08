# -*- coding:utf-8 -*-
def person(name,age,**kw):
	print 'name:',name,'age:',age,'other:',kw
person('wzy',22) 

person('Adam', 45, gender='M', job='Engineer')
kws = {'city': 'Beijing', 'job': 'Engineer'}
person('wzy',23,**kws)