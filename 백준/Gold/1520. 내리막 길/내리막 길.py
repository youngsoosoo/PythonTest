import sys
input = sys.stdin.readline

def recur(x, y):
	
	if x == m - 1 and y == n - 1:
		return 1
	
	if dp[x][y] != -1:
		return dp[x][y]
	
	route = 0
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if 0 <= nx < m and 0 <= ny < n:
			if graph[x][y] > graph[nx][ny]:
				route += recur(nx, ny)
	dp[x][y] = route
	return dp[x][y]


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(m)]

dp = [[-1 for i in range(n)] for j in range(m)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

recur(0, 0)
print(dp[0][0])
