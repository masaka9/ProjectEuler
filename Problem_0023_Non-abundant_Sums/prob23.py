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

l = []
for i in range(12, 28124):
	if sum(getDivisor(i)) > i:
		l.append(i)

dic = {}
for i in range(1,28124):
	dic[i] = 1

for item1 in l:
	for item2 in l:
		dic[item1+item2] = 0

ret = 0
for key in dic:
	if dic[key] == 1:
		ret += key
print ret