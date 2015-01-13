#!/usr/bin/python

import math

def gcd(a,b):
	if b>0:
		return gcd(b,a%b)
	else:
		return a

def sumToN(n):
	return n*(n+1)/2

n = 1000
p = 3
q = 5
sumP = sumToN(math.floor((n-1)/p))*p
print(sumP)
sumQ = sumToN(math.floor((n-1)/q))*q
print(sumQ)
r = gcd(p,q)
r = p*q/r
sumR = sumToN(math.floor((n-1)/r))*r
print(sumR)

print(sumP+sumQ-sumR)