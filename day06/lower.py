# -*- coding:utf-8 -*-
L = ['Hello','world',22,'Hei',22,33]
LL = [s.lower() for s in L if isinstance(s,str)]# 只输出字符串 
print LL
L1 = [s.lower() if isinstance(s,str) else s for s in L] # 数字和字符串一起输出
print L1
L2 = [s.lower() for s in L if isinstance(s,str) else s for in L] #list生成式后面不能更else语句 
print L2