import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(node, weight):
	for n, w in graph[node]:
		if visited[n] == 0:
			visited[n] = weight + w
			dfs(n, weight + w)
	
v = int(input())
graph = [[] for i in range(v+1)]

for i in range(v):
	data = list(map(int, input().split()))[:-1]
	for i in range(1, len(data)//2 + 1):
		graph[data[0]].append([data[i*2-1], data[i*2]])

visited = [0] * (v+1)
visited[1] = 1
dfs(1, 0)

result = visited.index(max(visited))
		
visited = [0] * (v+1)
visited[result] = 1
dfs(result, 0)

print(max(visited))