# coding=utf-8
import os,sys

print sys.argv
def search(name, path=os.path.abspath('.')):
    for x in os.listdir(path):
        path_now = os.path.join(path, x)
        if os.path.isfile(path_now) and name in x:
            print path_now
        elif os.path.isdir(path_now):
            search(name, path_now)
name = raw_input('please input name:')
search(name)
print '------------------'
def search1(name,path=os.path.abspath('.')):
	for x in os.walk(path):
		print x
		for y in [s for s in x[2] if name in s]:
			print os.path.join(x[0],y)
search1(name)

def walk_dir(dir,fileinfo,topdown=True):
	for root,dirs,files in os.walk(dir,topdown):
		print root,dirs,files
		for name in files:
			print(os.path.join(name))
			fileinfo.write(' '+os.path.join(root,name)+'\n')
		for name in dirs:
			print(os.path.join(name))
			fileinfo.write(' '+os.path.join(root,name)+'\n')
dir = raw_input('please input the path:')
fileinfo = open('list.txt','w')
walk_dir(dir,fileinfo)