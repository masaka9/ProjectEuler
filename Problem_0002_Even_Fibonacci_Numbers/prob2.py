#!/usr/bin/python

a = 0
b = 1
sum = 0
while(True):
	c = a+b
	a = b
	b = c
	if (c > 4000000):
		break
	else:
		if c%2==0:
			sum += c
print sum