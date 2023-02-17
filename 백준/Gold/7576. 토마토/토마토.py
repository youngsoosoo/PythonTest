import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int ,input().split())
graph = [list(map(int, input().split())) for i in range(m)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

q=deque([])
for i in range(m):
	for j in range(n):
		if graph[i][j] == 1:
			q.append((i, j))

while q:
	x, y = q.popleft()
	
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
			q.append((nx, ny))
			graph[nx][ny] = graph[x][y] + 1


result=0
for i in graph:
	for j in i:
		if j == 0:
			print(-1)
			exit(0)
	result=max(max(i), result)

print(result - 1)