# def add(x,y):
# 	print x,y
# 	return x+y
# aa = reduce(add,[1,3,5,7,9])
# print aa # 25

def fn(x,y):
	return x*10 + y
bb = reduce(fn,[1,3,5,7,9]) 
print bb #13579