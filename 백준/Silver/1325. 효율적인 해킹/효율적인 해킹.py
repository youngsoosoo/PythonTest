import sys
from collections import deque
input = sys.stdin.readline

def bfs(i):
	cnt = 1
	q = deque([i])
	visited = [False for _ in range(n+1)]
	visited[i] = True
	
	while q:
		
		x = q.popleft()
		
		for j in graph[x]:
			if not visited[j]:
				visited[j] = True
				cnt += 1
				q.append(j)
	return cnt

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
	a, b = map(int, input().split())
	graph[b].append(a)

maxcnt = 1
answer = []
	
for i in range(1, n+1):
	
	cnt = bfs(i)
	
	if cnt > maxcnt:
		maxcnt = cnt
		answer.clear()
		answer.append(i)
	elif cnt == maxcnt:
		answer.append(i)
	
print(*answer)