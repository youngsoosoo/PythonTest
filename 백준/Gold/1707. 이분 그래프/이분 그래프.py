import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
	global result
	
	for i in graph[v]:
		if visited[i] == -1:
			if visited[v] == 1:
				visited[i] = 2
			if visited[v] == 2:
				visited[i] = 1
			
			dfs(i)
		else:
			if visited[v] == visited[i]:
				result = False
				return
	
t = int(input())
for _ in range(t):
	v, e = map(int, input().split())
	visited = [-1 for i in range(v+1)]
	graph = [[] for i in range(v+1)]
	for i in range(e):
		start, end = map(int, input().split())
		graph[start].append(end)
		graph[end].append(start)
	
	result = True
	
	for i in range(1, v+1):
		if visited[i] == -1:
			visited[i] = 1
			dfs(i)
			if result==False:
				break
	if result == False:
		print("NO")
	else:
		print("YES")
