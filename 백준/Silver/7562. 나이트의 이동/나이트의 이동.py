import sys
from collections import deque
input = sys.stdin.readline

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

t = int(input())
for i in range(t):
	l = int(input())
	graph = [[0 for i in range(l)] for i in range(l)]
	a, b = map(int, input().split())
	c, d = map(int, input().split())
	q = deque([(a, b)])
	visited = [[0 for i in range(l)] for i in range(l)]
	
	while q:
		n = q.popleft()
		if n == (c, d):
			print(visited[n[0]][n[1]])
			break
		for j in range(8):
			nx = n[0] + dx[j]
			ny = n[1] + dy[j]
			
			if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
				visited[nx][ny] = visited[n[0]][n[1]] + 1
				q.append((nx, ny))