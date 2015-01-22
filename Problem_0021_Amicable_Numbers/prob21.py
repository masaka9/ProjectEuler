#!/usr/bin/python

import math

def getDivisor(n):	# not for 1
	l = [1]
	for i in range(2,int(math.sqrt(n))+1):
		if n%i == 0:
			l.append(i)
			if i != n/i:
				l.append(n/i)
	return l

l1 = []
l2 = []
for i in range(3,10000):
	if i in l2:
		continue
	a = i
	b = sum(getDivisor(a))
	if sum(getDivisor(b)) == a:
		l1.append((a,b))
		if a != b:
			l2.append(a)
			l2.append(b)
print l1
print l2
print sum(l2)