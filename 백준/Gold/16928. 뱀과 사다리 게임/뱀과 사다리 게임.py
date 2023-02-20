import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [0 for i in range(101)]
visited = [0 for i in range(101)]
dx = [1, 2, 3, 4, 5, 6]

for i in range(n+m):
	a, b = map(int, input().split())
	graph[a] = b

q=deque([1])

while q:
	x = q.popleft()
	if graph[x] != 0:
		a = visited[x]
		x = graph[x]
		visited[x] = a
	if x==100:
		print(visited[x])
		break
	for i in dx:
		nx = x + i
		
		if 0 <= nx <= 100 and visited[nx] == 0:
			visited[nx] = visited[x] + 1
			q.append(nx)