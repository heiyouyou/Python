# -*-coding:utf-8 -*-
# 升序
def reversed_cmp(x,y):
	if(x>y):
		return -1
	if(x<y):
		return 1
	return 0
# 降序
def reversed_cmp2(x,y):
	if(x>y):
		return 1
	if(x<y):
		return -1
	return 0
a = sorted([23,1,12,6,22,7],reversed_cmp)
aa = sorted([23,1,12,6,22,7],reversed_cmp2)
print a
print aa

# 字符串比较
def cmp_ignore_case(s1,s2):
	u1 = s1.lower()
	u2 = s2.lower()
	if(u1>u2):
		return 1
	if(u1<u2):
		return -1
	return 0
def cmp_str(s1,s2):
	if(s1>s2):
		return 1
	if(s1<s2):
		return -1
	return 0
b = sorted(['bob', 'about', 'Zoo', 'Credit'])
bb = sorted(['bob', 'about', 'Zoo', 'Credit'],cmp_ignore_case)
c = sorted([u'中', u'文', u'而', u'了'],cmp_str)
print b
print bb
print c
cc = [x.encode('utf-8') for x in c ]
print cc