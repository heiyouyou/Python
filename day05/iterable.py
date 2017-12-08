from collections import Iterable
a = isinstance('abc',Iterable) #True
b = isinstance([1,2,3],Iterable) #True
c = isinstance((3,4,5),Iterable) #True
d = isinstance(1234,Iterable) #False
e = isinstance({"he":2,"yo":3},Iterable) #True

print a,b,c,d,e