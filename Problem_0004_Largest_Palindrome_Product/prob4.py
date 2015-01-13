#!/usr/bin/python

def isPal(n):
	l = []
	while n>10:
		l.append(n%10)
		n = n / 10
	l.append(n)
	for i in range(0, len(l)/2):
		if l[i] != l[len(l)-1-i]:
			return False
	return True

max = 10000
for i in range(999,99,-1):
	for j in range(999,99,-1):
		product = i*j
		if isPal(product):
			if product > max:
				max = product
print max