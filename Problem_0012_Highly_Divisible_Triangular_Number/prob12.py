#!/usr/bin/python

import math

def isPrime(n):
	if 1 == n:
		return False
	if 2 == n or 3 == n:
		return True
	if n%2 == 0:
		return False
	for i in range(3,int(math.sqrt(n))+1,2):
		if 0 == n%i:
			return False
	return True

def genList(n):
	dic = {}
	leftN = n
	while leftN % 2 == 0:
		leftN /= 2
		if "2" not in dic.keys():
			dic["2"] = 1
		else:
			dic["2"] += 1
	it = 3
	while True:
		if isPrime(it):
			while leftN % it == 0:
				leftN /= it
				if str(it) not in dic.keys():
					dic[str(it)] = 1
				else:
					dic[str(it)] += 1
			if leftN == 1:
				break
		it += 2
	return dic

def calDic(dic):
	product = 1
	for k in dic:
		product *= dic[k]+1
	return product

it = 2
while True:
	n = it*(it+1)/2
	print n,
	tmp = calDic(genList(n))
	print tmp
	if tmp > 500:
		print n
		break
	it += 1
