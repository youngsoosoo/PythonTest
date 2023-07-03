import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]

chicken = []
home = []

for i in range(n):
	for j in range(n):
		if graph[i][j] == 1:
			home.append((i, j))
		elif graph[i][j] == 2:
			chicken.append((i, j))

result = sys.maxsize

for c in combinations(chicken, m):
	dis = 0
	for i in home:
		chicken_dis = sys.maxsize
		for j in range(m):
			chicken_dis = min(chicken_dis, abs(i[0] - c[j][0]) + abs(i[1] - c[j][1]))
		dis += chicken_dis
	result = min(result, dis)
	
print(result)