import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

v = [0]*(n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

cnt = 0
q=deque([1])
v[1] = 1
while q:
	a = q.popleft()
	for i in graph[a]:
		if not v[i]:
			cnt+=1
			v[i] = 1
			q.append(i)

print(cnt)