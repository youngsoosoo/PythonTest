import sys
from collections import deque
input = sys.stdin.readline

#n은 세로 m은 가로
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for i in range(n)]
visited = [[[0 for i in range(2)] for i in range(m)] for i in range(n)]

q=deque([(0, 0, 1)])
visited[0][0][1] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs():
	while q:
		x, y, w = q.popleft()
		if x == n-1 and y == m-1:
			return visited[x][y][w]

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < n and 0 <= ny < m :
				if graph[nx][ny] == 1 and w == 1:
					visited[nx][ny][0] = visited[x][y][1] + 1
					q.append((nx, ny, 0))
				elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
					visited[nx][ny][w] = visited[x][y][w] + 1
					q.append((nx, ny, w))
	return -1
	

print(bfs())