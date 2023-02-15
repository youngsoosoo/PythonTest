import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

t = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
	global cnt
	visited[x][y] = True
	if graph[x][y] :
		cnt+=1
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
			
		if 0 <= nx < m and  0 <= ny < n:
			if graph[nx][ny] and not visited[nx][ny] :
				dfs(nx, ny)

for _ in range(t):
	m, n, k = map(int, input().split())
	graph = [[0 for i in range(n)] for i in range(m)]
	visited = [[False for i in range(n)] for i in range(m)]
	result =[]
	for i in range(k):
		x, y = map(int, input().split())
		graph[x][y] = 1
	
	for i in range(m):
		for j in range(n):
			if graph[i][j] and not visited[i][j]:
				cnt=0
				dfs(i, j)
				result.append(cnt)

	print(len(result))