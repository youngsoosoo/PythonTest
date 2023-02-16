import sys
from collections import deque
input = sys.stdin.readline

#n은 세로 m은 가로
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for i in range(n)]
visited = [[0 for i in range(m)] for i in range(n)]

q=deque([(0, 0)])
visited[0][0] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while q:
	x, y = q.popleft()
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
			if not visited[nx][ny] or visited[nx][ny] > visited[x][y] + 1:
				q.append((nx, ny))
				visited[nx][ny] = visited[x][y] + 1

print(visited[n-1][m-1])