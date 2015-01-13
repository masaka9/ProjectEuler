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

it = 2
cnt = 0
while True:
	if isPrime(it):
		cnt += 1
		if cnt == 10001:
			print it
			break
	it += 1