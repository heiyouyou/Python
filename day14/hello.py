print 1+2

print '2222222'

def p_num():
	global num
	print num
	num = 4
num = 10
p_num()
print num

l = ['apple','banana','wzy']
for item in l:
	print item
	# break #使用break、continue跳出循环，else语句体不会被执行
else:
	print 'ok'