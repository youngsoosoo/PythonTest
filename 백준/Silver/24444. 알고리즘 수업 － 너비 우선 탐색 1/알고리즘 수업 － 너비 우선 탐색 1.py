import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())

v=[0] * (n+1)
graph=[[] for i in range(n+1)]
cnt=2

for i in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)


q=deque([r])
v[r] = 1
while q:
	a = q.popleft()
	graph[a].sort()
	for i in graph[a]:
		if not v[i]:
			v[i] = cnt
			cnt+=1
			q.append(i)

for i in range(1, n+1):
	print(v[i])