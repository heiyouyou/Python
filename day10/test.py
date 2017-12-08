# -*-coding:utf-8-*-
# class Student(object):
# 	def __init__(self,name,age,school):
# 		self.__name = name  # private
# 		self.__age = age
# 		self.__school = school
# 	def say(self):
# 		print ' my info : ', self.__name , self.__age, self.__school

# class Hel(Student):
#     def __init__(self,name,age,school):
#         super(Hel,self).__init__(name,age,school)
# h = Hel('wzy',23,'glut')
# h.say();

class Student(object):
	def __init__(self,name,age,school):
		self.__name = name;
		self.__age = age;
		self.__school = school;
	def say(self):
		print 'my info：',self.__name,self.__name,self.__school

	def get(self):
		return self.__name,self.__age,self.__school 

class Hel(Student):
	pass
	def say(self):
		print 'hel info %s %s %s' %super(Hel,self).get()
a = Hel('wzy',23,'glue')
a.say()