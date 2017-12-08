class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	def print_score(self):
		print '%s:%s' %(self.name,self.score)
wzy = Student('wzy',90)
xiao = Student('xiao',89)
wzy.print_score()
xiao.print_score()