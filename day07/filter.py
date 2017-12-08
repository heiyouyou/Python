# -*- coding:utf-8 -*-
# 保留奇数
def fn(s):
	return s%2 != 0
aa = filter(fn,[1,2,3,4,5,6])
print aa

# 只保留不是空格的字符串
def not_empty(s):
	return s and isinstance(s,str) and s.strip()#strip()格式化成一个space空格
bb = filter(not_empty,['A','',11,None,[],'22','  ',22,{},'wzy'])
print bb