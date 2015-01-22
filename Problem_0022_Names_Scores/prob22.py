#!/usr/bin/python

def getWorth(s):
	ret = 0
	for i in range(len(s)):
		ret += ord(s[i])-ord('A')+1
	return ret

a = open('p022_names.txt')
listStr = a.readline()
listStr = listStr.replace('\"', '')
l = listStr.split(',')
l = sorted(l)
ret = 0
for i in range(len(l)):
	ret += getWorth(l[i]) * (i+1)
print ret
