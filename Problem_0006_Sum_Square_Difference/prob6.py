#!/usr/bin/python

n=100

a = 0
for i in range(1,n+1):
	a += i
print a*a

b = 0
for i in range(1,n+1):
	b += i*i
print b

print a*a-b