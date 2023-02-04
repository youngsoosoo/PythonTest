import sys
input = sys.stdin.readline
p = 1000000007
n = int(input())

def dfs(a, b):
	if b == 1:
		return a
	if b%2:
		return mul(dfs(a, b-1), a)
	else:
		return dfs(mul(a, a), b//2)
def mul(a, b):
	c = [[0 for i in range(len(b))] for i in range(2)]
	for i in range(2):
		for j in range(len(b[0])):
			for k in range(2):
				c[i][j] += (a[i][k]*b[k][j])
				c[i][j] %= p
	return c

a = [[1, 1], [1, 0]]

start=[[1], [1]]

if n < 3:
	print(1)
else:
	print(mul(dfs(a, n-2), start)[0][0])