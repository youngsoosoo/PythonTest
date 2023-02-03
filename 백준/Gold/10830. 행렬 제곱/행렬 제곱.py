import sys
input = sys.stdin.readline

n, b = map(int, input().split())
a=[list(map(int, input().split())) for i in range(n)]

def square(a, b):
	if b == 1:
		for i in range(n):
			for j in range(n):
				a[i][j] %= 1000
		return a
	
	c = square(a, b//2)
	if b%2:
		return mul(mul(c, c), a)
	else:
		return mul(c, c)

def mul(u, v):
	c = [[0 for i in range(n)] for i in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				c[i][j] += u[i][k] * v[k][j]
				c[i][j] %= 1000
	return c

c = square(a, b)
for i in c:
	print(*i)