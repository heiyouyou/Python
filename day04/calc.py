# -*- coding:utf-8 -*-
# def calc(numbers):
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum

# a = calc([1,2,3])
# print a
# b = calc((1,2,3,5,6))
# print b
c = calc(1,2,3,5,6)
print c
d = calc()
print d

nums = [1,2,3]
e = calc(nums[0],nums[1],nums[2])
ee = calc(*nums)
print e
print ee