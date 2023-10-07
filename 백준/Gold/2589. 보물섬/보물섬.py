import sys
from collections import deque
input = sys.stdin.readline

x, y = map(int, input().split())
graph = [list(input().rstrip()) for i in range(x)]

answer = 0

for i in range(x):
	for j in range(y):
		if graph[i][j] == "L":
			visited = [[0 for _ in range(y)] for _ in range(x)]
			dist = [[0 for _ in range(y)] for _ in range(x)]
			
			q = deque()
			q.append([i, j])
			visited[i][j] = 1
			
			while q:
				ex, ey = q.popleft()
				
				for dx, dy in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
					nx, ny = ex+dx, ey+dy
					
					if 0 <= nx < x and 0 <= ny < y and graph[nx][ny] == "L" and visited[nx][ny] == 0:
						visited[nx][ny] = 1
						dist[nx][ny] = dist[ex][ey] + 1
						answer = max(answer, dist[nx][ny])
						q.append([nx, ny])

print(answer)
	