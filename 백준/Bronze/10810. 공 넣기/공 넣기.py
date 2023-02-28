import sys
input = sys.stdin.readline

n, m = map(int, input().split())

basket = [0 for i in range(n)]

for a in range(m):
	i, j, k = map(int, input().split())
	for b in range(i-1, j):
		basket[b] = k

print(*basket)
	