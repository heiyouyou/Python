# coding=utf-8
# 
import os

# 获取当前目录的绝对路径:
print os.path.abspath('.') #必须传递一个参数

# 合并目录的路径达到兼容Linux/Unix/Mac的系统
url = os.path.join('F:\Python\example\day15','testdir')
print url #F:\Python\example\day15\testdir'
# 创建一个目录
# os.mkdir(url)
# 删掉一个目录:
# os.rmdir(url)

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# part-1/part-2

# 而Windows下会返回这样的字符串：
# part-1\part-2

s_path = os.path.split('F:\\Python\\example\\day15\\testdir')
s_path1 = os.path.split('F:\\Python\\example\\day15\\test.py')
print s_path # ('F:\\Python\\example\\day15','testdir')
print s_path1 # ('F:\\Python\\example\\day15','test.py')

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
# 这样可以把一个路径拆分为两部分(元组形式返回)，后一部分总是最后级别的目录或文件名。

# 获取文件的扩展名
print os.path.splitext('F:\\Python\\example\\day15\\test.py')

print os.getcwd() #获取当前工作目录
print os.curdir #h返回当前目录（'.')
print os.path.exists('22.txt') #判断是否存在文件或目录name
print os.path.getsize('log.txt') #获得文件大小，如果name是目录返回1
print os.path.basename('F:\\Python\\example\\day15\\test.py') #返回文件名
print os.path.dirname('F:\\Python\\example\\day15\\test.py') #返回文件路径 
# 以上这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

# os.rename('test.txt','test.py') 
# os.remove('test.py') 