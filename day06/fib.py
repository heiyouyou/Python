def fib(max):
	n,a,b=0,0,1
	while n<max:
		# print b
		yield b
		# b = a+b
		# a = b
		a,b = b,a+b
		n = n+1
# fib(6)
print fib(6)