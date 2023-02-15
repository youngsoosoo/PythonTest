import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
visited_dfs = []
visited_bfs = [v]
fs = [[] for i in range(n+1)]

for i in range(m):
	a, b = map(int, input().split())
	fs[a].append(b)
	fs[b].append(a)


#DFS
def dfs(v):
	visited_dfs.append(v)
	fs[v].sort()
	for i in fs[v]:
		if i not in visited_dfs:
			dfs(i)
#BFS
q=deque([v])
while q:
	a = q.popleft()
	fs[a].sort()
	for i in fs[a]:
		if i not in visited_bfs:
			visited_bfs.append(i)
			q.append(i)

dfs(v)
print(*visited_dfs)
print(*visited_bfs)