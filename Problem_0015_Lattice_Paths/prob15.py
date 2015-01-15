def c(m, n):
	if m == 0 or m == n:
		return 1
	# n!/((n-m!)m!)
	minn = min(n-m, m)
	ans = 1
	for i in range(minn):
		ans *= n-i
	for i in range(minn):
		ans /= (1+i)
	return ans

print c(20,40)