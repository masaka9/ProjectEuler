#!/usr/bin/python

import math

n = 600851475143
#n = 13195

def isPrime(n):
	if 1 == n:
		return False
	if 2 == n or 3 == n:
		return True
	for i in range(2,int(math.sqrt(n))+1):
		if 0 == n%i:
			return False
	return True

maxP = 1
leftN = n
while leftN % 2 == 0:
	leftN /= 2
	if maxP < 2:
		maxP = 2

i = 3
while True:
	if isPrime(i):
		while leftN % i == 0:
			leftN /= i
			if maxP < i:
				maxP = i
		if leftN == 1:
			break
	i += 2

print maxP
