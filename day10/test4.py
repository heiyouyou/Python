# -*-coding:utf-8-*-

# class Student(object):
#     __slots__ = ('name', 'age')
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def get_info(self):
#         for item in dir(self):
#             if isinstance(item, (str,int)):
#                 print item

# def print_info(stu):
#     print stu.name, stu.age, stu.score


# bart = Student('Bart', 12)
# lisa = Student('Lisa', 10)
# bart.score = 80
# print_info(bart)
# print bart.score

class Student(object):
    __slots__ = ('name', 'age')
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def get_info(self):
        for item in dir(self):
            if isinstance(item, (str,int)):
                print item

def print_info(stu):
    print stu.name, stu.age, stu.score


bart = Student('Bart', 12)
lisa = Student('Lisa', 10)
# 给类绑定限制外的属性，可以通过实例访问到，对于类变量，实例只能引用，而不能直接重新赋值
Student.score = 80
# Student.score = 81 # 可以改变
# 只读属性，不能通过实例改变类变量的值
# bart.score = 81
# lisa.score = 81
print bart.score,lisa.score #80 80