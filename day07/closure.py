# -*-coding:utf-8 -*-
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1,f2,f3 = count()
# 返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
print f1() #9
print f2() #9
print f3() #9

# 再创建一个函数，用该函数的参数绑定循环变量当前的值。
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变
`
# def count2():
# 	fs = []
# 	for i in range(1,4):
# 		def f(j):
# 			def g():
# 				return j*j
# 			return g
# 		fs.append(f(i))
# 	return fs
def count2():
    fs = []
    for i in range(1, 4):
        def f(j=i):
            return j*j
        fs.append(f)
    return fs
f11,f22,f33 = count2()
print f11() #1
print f22() #4
print f33() #9