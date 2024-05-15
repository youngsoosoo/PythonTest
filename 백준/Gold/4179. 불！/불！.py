import sys
from collections import deque
input = sys.stdin.readline
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

r, c = map(int, input().split())
graph = []

fire = []
jihoon = []

for i in range(r):
	g = list(input().strip())
	for j in range(c):
		if g[j] == 'J':
			jihoon.append([i, j])
		if g[j] == 'F':
			fire.append([i, j])
	graph.append(g)

q = deque()
q.append([jihoon[0][0], jihoon[0][1], "J"])
graph[jihoon[0][0]][jihoon[0][1]] = 0

if fire:
	for x, y in fire:
		q.append([x, y, "F"])
		graph[x][y] = "#"

def dfs():
	while q:
		x, y, z = q.popleft()
		
		if z == "J" and (x == 0 or y == 0 or x == r-1 or y == c-1):
			if graph[x][y] == "#":
				continue
			return graph[x][y] + 1
		
		for dx, dy in d:
			nx = x + dx
			ny = y + dy
			
			if 0 <= nx < r and 0 <= ny < c:
				if graph[nx][ny] != "#" and z == "F":
					graph[nx][ny] = "#"
					q.append([nx, ny, "F"])
				elif graph[nx][ny] == "." and z == "J" and graph[x][y] != "#":
					graph[nx][ny] = graph[x][y] + 1
					q.append([nx, ny, "J"])

	return "IMPOSSIBLE"

print(dfs())