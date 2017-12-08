# -*-coding:utf-8 -*-
# 在该类中定义三个函数，分别用作赋值、取值和删除变量（此处表达也许不很清晰，请看示例） 
　def getx(self): 
　　return self.__x 
　def setx(self,value): 
　　self.__x=value 
　def delx(self): 
　　del self.__x 
　x = property(getx,setx,delx,'') 
# property函数原型为property(fget=None,fset=None,fdel=None,doc=None)，所以根据自己需要定义相应的函数即可