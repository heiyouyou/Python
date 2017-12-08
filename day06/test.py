# def fib():
# 	a,b=0,1
# 	while 1:
# 		yield b
# 		i = b
# 		b = a+b
# 		a = i
# def gnext(x=0,y=1):
# 	g = fib()
# 	max = y+1
# 	n = 1
# 	l = []
# 	while n<=max:
# 		l.append(g.next())
# 		n = n+1
# 	print l[x:y]

# gnext(2,10)

def fib(max):
    n, a, b = 0, 0, 1
    while(n < max):
        yield b
        a, b = b, a+b
        n += 1

def slfib(fr=0, to=1):
    return [x for x in fib(to) if x not in fib(fr)]
aa = slfib(2,10)
print aa