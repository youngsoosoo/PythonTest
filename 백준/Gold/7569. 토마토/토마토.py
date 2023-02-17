import sys
from collections import deque
input = sys.stdin.readline

n, m, h = map(int ,input().split())
graph = [[list(map(int, input().split())) for i in range(m)] for i in range(h)]

dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q=deque([])
for i in range(h):
	for j in range(m):
		for k in range(n):
			if graph[i][j][k] == 1:
				q.append((i, j, k))

while q:
	x, y, z = q.popleft()
	
	for i in range(6):
		nx = x + dx[i]
		ny = y + dy[i]
		nz = z + dz[i]
		
		if 0 <= nx < h and 0 <= ny < m and 0 <= nz < n and graph[nx][ny][nz] == 0:
			q.append((nx, ny, nz))
			graph[nx][ny][nz] = graph[x][y][z] + 1


result=0
for i in graph:
	for j in i:
		for k in j:
			if k == 0:
				print(-1)
				exit(0)
		result=max(max(j), result)

print(result - 1)