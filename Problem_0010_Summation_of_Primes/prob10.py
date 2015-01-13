#!/usr/bin/python

import math

def isPrime(n):
	if 1 == n:
		return False
	if 2 == n or 3 == n:
		return True
	for i in range(2,int(math.sqrt(n))+1):
		if 0 == n%i:
			return False
	return True

sum = 2
it = 3
while it < 2000000:
	if isPrime(it):
		sum += it
	it += 2

print sum