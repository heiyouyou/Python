# coding=utf-8
import re
s1 = 'ABC\\-001'
s2 = r'ABC\-001'
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
print re.match(r'^\d{3}\-\d{3,8}$','010-24324') # 
print re.match(r'^\d{3}\-\d{3,8}$','010 24324') # None

print 'a b 	c'.split(' ')
print re.split(r'\s+','a b 	c')
print re.split(r'\s\,+','a,b, 	c')
print re.split(r'\s*<|\s*\>','<p>heihei<p>')

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# 正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
print m.groups()
print m.group(0)
print m.group(1)
print m.group(2)
# 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
# 注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。

# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
print re.match(r'^(\d+)(0*)$','102300').groups()
# 采用非贪婪匹配
print re.match(r'^(\d+?)(0*)$','102300').groups()



# 在Python中使用正则表达式时，re模块内部会干两件事情：
# 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 用编译后的正则表达式去匹配字符串。

# 预编译正则表达式
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串
print re_telephone.match('001-34324').groups()
print re_telephone.match('001 34324')