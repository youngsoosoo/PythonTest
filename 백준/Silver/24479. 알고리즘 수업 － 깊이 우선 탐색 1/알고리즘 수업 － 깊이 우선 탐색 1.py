import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, input().split())

v=[0] * (n+1)
graph=[[] for i in range(n+1)]
cnt=1

for i in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

def dfs(r):
	global cnt
	v[r] = cnt
	graph[r].sort()
	for x in graph[r]:
		if v[x] == 0:
			cnt+=1
			dfs(x)

dfs(r)
for i in range(1, n+1):
	print(v[i])