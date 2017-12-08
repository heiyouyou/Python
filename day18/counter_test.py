# coding=utf-8

from collections import Counter

# Counter是一个简单的计数器
c = Counter()
for ch in 'programming':
	print c[ch]
	c[ch] = c[ch] +1

print c
# Counter实际上也是dict的一个子类。
print isinstance(c,dict) #True