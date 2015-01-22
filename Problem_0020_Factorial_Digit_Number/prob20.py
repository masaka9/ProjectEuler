#!/usr/bin/python

def fact(n):
    ret = 1
    for i in range(1,n+1):
        ret *= i
    return ret

s = str(fact(100))
sum = 0
for i in range(len(s)):
    sum += ord(s[i])-ord('0')
print sum