s = str(2**1000)
ans = 0
for i in range(len(s)):
	ans += ord(s[i])-ord('0')
print ans