class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print '%s %s' %(self.__name,self.__score)
	def get_name(self):
		return self.__name;
	def get_score(self):
		return self.__score;
	def set_name(self,name):
		self.__name = name
	def set_score(self,score):
		self.__score = score

p1 = Student('wzy',88)
p2 = Student('xixi',89)
print p1.get_name()#wzy
print p1.get_score()#88
print p2.get_name()#xixi
print p2.get_score()#89
p2.set_name('xiaoxiao')
p2.set_score(90)
print p2.get_name()#xiao
print p2.get_score()#90