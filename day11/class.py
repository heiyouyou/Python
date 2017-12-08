# -*- coding:utf-8 -*-
# class Ball(object):
# 	def show(self):
# 		print 'I am a ball'

# class Bigball(Ball):
# 	def show(self):
# 		print 'I am a big ball'
# class Smallball(Ball):
# 	def show(self):
# 		print 'I am a small ball'
# class Others(Ball):
# 	def show(self):
# 		print 'I am a others'
# class Basketball(Others,Bigball):
# 	pass
# class Yellowball(Smallball):
# 	pass
# b = Basketball()
# y = Yellowball()
# b.show() #I am a others
# y.show() #I am a small ball

class Grandfa(object):
    def hair(self):
        print 'no hair'

class Father(Grandfa):
    pass

class Mother(Grandfa):
     def hair(self):
        print 'long hair'

class Tom(Father,Mother):
    pass

me = Tom()
me.hair() #long hair

# 新式类的查找方式
# 子类继承多个父类时，如果多个父类之间的继承类属于同一个类，则从左往右查找，再进行返回深入查找
# 如果多个父类之间的继承类不属于同一个类，则从左进行深入查找，再往右深入查找