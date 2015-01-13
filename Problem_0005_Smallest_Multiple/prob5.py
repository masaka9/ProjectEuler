#!/usr/bin/python

def gcd(a,b):
	if b>0:
		return gcd(b,a%b)
	else:
		return a

res = 1
for i in range(2,21):
	res = res*i/gcd(res,i)
print res