class Student(object):
	def __init__(self,name,score):
		# self.name = name
		# self.score = score
		# self._name = name
		# self._score = score
		self.__name = name
		self.__score = score
	def print_score(self):
		# print '%s %s' %(self._name,self._score)
		print '%s %s' %(self.__name,self.__score)
p1 = Student('wzy',88)
p2 = Student('xixi',89)
p1.print_score()
print '--------------'
p1.score = 33
# print p2.__name,p2.__score#不可以访问
# print p2._name,p2._score#可以访问
print p2._Student__name,p2._Student__score#可以访问
p1.print_score()
