#!/usr/bin/python

import math

a = 1
while True:
	b = 1000*(a-500)*1.0/(a-1000)
	if b == int(b):
		print a,b,math.sqrt(a*a+b*b),a*b*math.sqrt(a*a+b*b)
		break
	a += 1