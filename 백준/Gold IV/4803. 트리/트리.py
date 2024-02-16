import sys
from collections import deque
input = sys.stdin.readline

def bfs(a):
	result = True
	q = deque([a])
	while q:
		node = q.popleft()
		if visited[node]:
			result = False
		visited[node] = 1
		for i in graph[node]:
			if not visited[i]:
				q.append(i)
	return result

case1 = 0
while True:
	case1 += 1
	n, m = map(int, input().split())
	if n == 0 and m == 0:
		break
	graph = [[] for i in range(n+1)]
	visited = [0 for i in range(n+1)]
	cnt = 0

	for i in range(m):
		a, b = map(int, input().split())
		graph[a].append(b)
		graph[b].append(a)
		
	for i in range(1, n+1):
		if visited == 1:
			continue
		if bfs(i):
			cnt += 1
	
	if cnt == 0:
		print("Case {}: No trees.".format(case1))
	elif cnt == 1:
		print("Case {}: There is one tree.".format(case1))
	else:
		print("Case {}: A forest of {} trees.".format(case1, cnt))