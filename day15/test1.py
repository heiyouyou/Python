# coding=utf-8

import os
# 获取当前目录下所有的文件和目录
p_l = [x for x in os.listdir('.')]
print p_l
# 获取当前目录下的子目录，不包括深层的目录
p_l1 = [x for x in os.listdir('.') if os.path.isdir(x)]
print p_l1 #['log','test']
# 获取当前目录下的.py文件
p_l2 = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print p_l2