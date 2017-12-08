# -*-coding:utf-8 -*-
class AAA():  
   aaa = 10  
 
# 情形1   
obj1 = AAA()  
obj2 = AAA()   
print obj1.aaa, obj2.aaa, AAA.aaa #10 10 10
 
# 情形2  
obj1.aaa += 2  
print obj1.aaa, obj2.aaa, AAA.aaa #12 10 10
 
# 情形3  
AAA.aaa += 3  
print obj1.aaa, obj2.aaa, AAA.aaa #12 13 13


# 1. Python中属性的获取是按照从下到上的顺序来查找属性；
# 2. Python中的类和实例是两个完全独立的对象；
# 3. Python中的属性设置是针对对象本身进行的；