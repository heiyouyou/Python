# coding=utf-8

from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
# 通过对象.属性获取值
print p.x
print p.y
print '----------'
# 通过索引获取值
print p[0]
print p[1]


print isinstance(p,Point) #True
print isinstance(p,tuple) #True

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。


Circle = namedtuple('Circle',['rx','ry','r'])
c = Circle(12,23,2)
print c.rx
print c.ry
print c.r
