import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

result = [[-1 for i in range(m)] for j in range(n)]
visited = [[False for i in range(m)] for j in range(n)]

q = deque([])

for i in range(n):
	graph.append(list(map(int, input().split())))
	
	for j in range(m):
		if graph[i][j] == 2:
			result[i][j] = 0
			visited[i][j] = True
			q.append((i, j))
			
		if graph[i][j] == 0:
			result[i][j] = 0


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while q:
	x, y = q.popleft()
	
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 and not visited[nx][ny]:
			result[nx][ny] = result[x][y] + 1
			visited[nx][ny] = True
			q.append((nx, ny))

for i in result:
	for j in i:
		print(j, end=" ")
	print()