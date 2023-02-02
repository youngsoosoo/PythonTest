import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a=[list(map(int, input().split())) for i in range(n)]


m, k = map(int, input().split())
b=[list(map(int, input().split())) for i in range(m)]

c = [[0 for i in range(k)] for i in range(n)]

for i in range(n):
	for j in range(k):
		for q in range(m):
			c[i][j] += a[i][q] * b[q][j]

for i in c:
	for j in i:
		print(j, end=' ')
	print()



